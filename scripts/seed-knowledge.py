#!/usr/bin/env python3
"""
Seed the OpenFang semantic memory with CoachAI ecosystem knowledge.

Reads knowledge/*.md files, chunks them by section, and inserts into
the openfang.db SQLite memory store so C-Suite agents can recall
relevant knowledge during RAG-powered conversations.

Usage:
    python scripts/seed-knowledge.py [--db PATH] [--agent-name NAME] [--dry-run]

Defaults:
    --db        ~/.openfang/openfang.db
    --agent-name  openchief-ceo  (also seeds cfo, cmo, cto)
"""

import argparse
import json
import os
import re
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path


def chunk_markdown(text: str, max_chunk_size: int = 1500) -> list[dict]:
    """Split markdown into semantic chunks by headings."""
    chunks = []
    current_section = ""
    current_content = []

    for line in text.split("\n"):
        # Detect heading
        heading_match = re.match(r"^(#{1,3})\s+(.+)", line)
        if heading_match:
            # Save previous chunk
            if current_content:
                content = "\n".join(current_content).strip()
                if content and len(content) > 20:
                    chunks.append({
                        "section": current_section,
                        "content": content,
                    })
            current_section = heading_match.group(2).strip()
            current_content = [line]
        else:
            current_content.append(line)

    # Final chunk
    if current_content:
        content = "\n".join(current_content).strip()
        if content and len(content) > 20:
            chunks.append({
                "section": current_section,
                "content": content,
            })

    # Split oversized chunks
    result = []
    for chunk in chunks:
        content = chunk["content"]
        if len(content) > max_chunk_size:
            # Split on double newlines
            parts = content.split("\n\n")
            buffer = ""
            for part in parts:
                if len(buffer) + len(part) > max_chunk_size and buffer:
                    result.append({
                        "section": chunk["section"],
                        "content": buffer.strip(),
                    })
                    buffer = part
                else:
                    buffer = buffer + "\n\n" + part if buffer else part
            if buffer.strip():
                result.append({
                    "section": chunk["section"],
                    "content": buffer.strip(),
                })
        else:
            result.append(chunk)

    return result


def get_agent_ids(conn: sqlite3.Connection, agent_names: list[str]) -> dict[str, str]:
    """Look up agent UUIDs from the agents table."""
    result = {}
    cursor = conn.execute(
        "SELECT id, name FROM agents WHERE name IN ({})".format(
            ",".join("?" for _ in agent_names)
        ),
        agent_names,
    )
    for row in cursor:
        result[row[1]] = row[0]
    return result


def seed_memories(
    conn: sqlite3.Connection,
    agent_id: str,
    agent_name: str,
    chunks: list[dict],
    dry_run: bool = False,
):
    """Insert knowledge chunks into the memories table."""
    now = datetime.now(timezone.utc).isoformat()
    inserted = 0
    skipped = 0

    for chunk in chunks:
        content = chunk["content"]
        section = chunk["section"]

        # Check for duplicates (same agent + same content)
        existing = conn.execute(
            "SELECT id FROM memories WHERE agent_id = ? AND content = ? AND deleted = 0",
            (agent_id, content),
        ).fetchone()

        if existing:
            skipped += 1
            continue

        mem_id = str(uuid.uuid4())
        source = json.dumps("System")
        metadata = json.dumps({
            "section": section,
            "source_file": "coachai-ecosystem.md",
            "seeded": True,
            "importance": 8,
        })

        if dry_run:
            print(f"  [DRY RUN] Would insert: {section[:60]}... ({len(content)} chars)")
            inserted += 1
            continue

        conn.execute(
            """INSERT INTO memories
               (id, agent_id, content, source, scope, confidence, metadata,
                created_at, accessed_at, access_count, deleted, embedding)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                mem_id,
                agent_id,
                content,
                source,
                "knowledge",
                1.0,
                metadata,
                now,
                now,
                0,
                0,
                None,  # Embedding will be computed at recall time by the driver
            ),
        )
        inserted += 1

    if not dry_run:
        conn.commit()

    print(f"  {agent_name}: {inserted} inserted, {skipped} skipped (duplicates)")
    return inserted


def main():
    parser = argparse.ArgumentParser(description="Seed OpenFang memory with CoachAI knowledge")
    parser.add_argument(
        "--db",
        default=os.path.expanduser("~/.openfang/openfang.db"),
        help="Path to openfang.db",
    )
    parser.add_argument(
        "--knowledge-dir",
        default=os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge"),
        help="Path to knowledge/ directory",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show what would be inserted")
    args = parser.parse_args()

    # Read knowledge files
    knowledge_dir = Path(args.knowledge_dir)
    if not knowledge_dir.exists():
        print(f"ERROR: Knowledge directory not found: {knowledge_dir}")
        return 1

    md_files = sorted(knowledge_dir.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {knowledge_dir}")
        return 1

    print(f"Knowledge directory: {knowledge_dir}")
    print(f"Found {len(md_files)} knowledge file(s)")

    # Chunk all knowledge files
    all_chunks = []
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        chunks = chunk_markdown(text)
        print(f"  {md_file.name}: {len(chunks)} chunks")
        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")

    # Connect to database
    db_path = Path(args.db)
    if not db_path.exists():
        print(f"\nWARNING: Database not found at {db_path}")
        print("Start the OpenFang daemon first to create the database.")
        print("Then re-run this script to seed knowledge.")
        if args.dry_run:
            print("\n[DRY RUN] Would insert chunks for each C-Suite agent:")
            for chunk in all_chunks:
                print(f"  - {chunk['section'][:60]}... ({len(chunk['content'])} chars)")
        return 0

    conn = sqlite3.connect(str(db_path))

    # Find C-Suite agent IDs
    csuite_names = ["openchief-ceo", "openchief-cfo", "openchief-cmo", "openchief-cto"]
    agent_ids = get_agent_ids(conn, csuite_names)

    if not agent_ids:
        print("\nNo C-Suite agents found in database.")
        print("Spawn the agents first, then re-run this script.")
        print(f"Searched for: {', '.join(csuite_names)}")

        # Seed with a placeholder agent ID so knowledge is available when agents spawn
        print("\nSeeding with shared scope (agent_id='openchief-shared')...")
        shared_id = "openchief-shared"
        total = seed_memories(conn, shared_id, "openchief-shared", all_chunks, args.dry_run)
        print(f"\nDone. {total} chunks seeded to shared namespace.")
        print("When C-Suite agents are spawned, they'll recall from shared memory.")
    else:
        print(f"\nFound {len(agent_ids)} C-Suite agent(s): {', '.join(agent_ids.keys())}")
        print("Seeding knowledge to each agent...\n")

        total = 0
        for name, agent_id in agent_ids.items():
            count = seed_memories(conn, agent_id, name, all_chunks, args.dry_run)
            total += count

        print(f"\nDone. {total} total chunks seeded across {len(agent_ids)} agents.")

    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
