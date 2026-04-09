# OpenChief C-Suite Agent Specifications

## Overview

OpenChief runs 5 AI executive agents powered by **Qwen 3.6 235B** via OpenRouter. Each agent specializes in a business domain and has the full CoachAI ecosystem knowledge base loaded via RAG.

All agents share memory scope `openchief.*` and can delegate to each other via `agent_send`.

## Agent Registry

| Agent | ID | Role | Temperature | Status |
|-------|-----|------|-------------|--------|
| openchief-ceo | `319fbac1` | Chief Executive Officer | 0.4 | Active |
| openchief-coo | `be5dc934` | Chief Operating Officer | 0.4 | Active |
| openchief-cfo | `42cc843e` | Chief Financial Officer | 0.3 | Active |
| openchief-cmo | `9455b374` | Chief Marketing Officer | 0.6 | Active |
| openchief-cto | `5f0c2653` | Chief Technology Officer | 0.3 | Active |

## Agent Specifications

### CEO — Chief Executive Officer
- **Domain:** Strategy, business planning, vision, Founders Club, partnerships
- **Conversion focus:** Founders Club ($10K-$100K) → CAMP Alpha ($20/mo) → Sponsors → Enrollment
- **Delegates to:** CFO (finance), CMO (marketing), CTO (tech)
- **Tools:** file_read/write, memory_store/recall, web_fetch, agent_send/list
- **Template:** `agents/openchief-ceo/agent.toml`

### COO — Chief Operating Officer
- **Domain:** Operations, fleet management, Zo engine, onboarding, workflow automation
- **Operational scope:** 14-agent fleet, 5-layer architecture, 9 cron jobs, QUEUE.md dispatch
- **Manages:** Zo workstations (19 agents/station), service health, incident response
- **Tools:** file_read/write, memory_store/recall, web_fetch, shell_exec, agent_send/list
- **Template:** `agents/openchief-coo/agent.toml`

### CFO — Chief Financial Officer
- **Domain:** Finance, investment analysis, tokenomics, ROI, compliance
- **Products:** Founders Club tiers, CAMP Alpha pricing, USDca protocol economics, GBB FX
- **Disclaimers:** Always includes risk disclosures and "consult a licensed financial advisor"
- **Tools:** file_read/write, memory_store/recall, web_fetch, agent_send/list
- **Template:** `agents/openchief-cfo/agent.toml`

### CMO — Chief Marketing Officer
- **Domain:** Marketing, campaigns, content strategy, sponsor acquisition, enrollment growth
- **Funnel ownership:** Free OpenChief → CAMP Alpha, Content → Tech Camps, B2B → Sponsors
- **Content engine:** Penthouse Papi (4 hands: Strategist, Producer, Coordinator, Analyst)
- **Tools:** file_read/write, memory_store/recall, web_fetch, agent_send/list
- **Template:** `agents/openchief-cmo/agent.toml`

### CTO — Chief Technology Officer
- **Domain:** AI architecture, blockchain, RWA, DeFi, security, tech curriculum
- **Stack:** OpenFang (Rust, 14 crates), Qwen 3.6, RAG pipeline, multi-chain (Base/Solana/ETH)
- **Security:** 3-layer (ACL + injection scanning + secret redaction)
- **Tools:** file_read/write, memory_store/recall, web_fetch, shell_exec, agent_send/list
- **Template:** `agents/openchief-cto/agent.toml`

## LLM Configuration

All C-Suite agents use:
- **Provider:** OpenRouter
- **Model:** `qwen/qwen3-235b-a22b` (Qwen 3.6, 235B parameters)
- **API Key Env:** `OPENROUTER_API_KEY`
- **No fallback models** — Qwen 3.6 only

## Knowledge Base

- **Source:** `knowledge/coachai-ecosystem.md`
- **Seeding:** `scripts/seed-knowledge.py` (SQLite) or `scripts/seed-msg.json` (API)
- **Storage:** Semantic memory (per-agent) + KV store (key: `coachai_knowledge_base`)
- **Embedding:** Ollama `nomic-embed-text` (768 dimensions, local)
- **Recall:** Top 5 memories injected into system prompt via cosine similarity

## Spawning Agents

### Via template (daemon must have templates installed):
```bash
curl -X POST http://127.0.0.1:4200/api/agents \
  -H "Content-Type: application/json" \
  -d '{"template": "openchief-ceo"}'
```

### Via inline manifest:
```bash
node -e "
const fs = require('fs');
const toml = fs.readFileSync('agents/openchief-ceo/agent.toml', 'utf8');
process.stdout.write(JSON.stringify({manifest_toml: toml}));
" | curl -X POST http://127.0.0.1:4200/api/agents \
    -H "Content-Type: application/json" -d @-
```

### Restart a crashed agent:
```bash
curl -X POST http://127.0.0.1:4200/api/agents/{id}/restart \
  -H "Content-Type: application/json"
```

## Revenue Priority

Agents are trained to prioritize conversion in this order:
1. Founders Club ($10K-$100K per investor)
2. CAMP Alpha subscriptions ($20/mo + data bundles)
3. Sponsor marketplace fees
4. Tech Camp enrollment
5. RWA tokenization fees
6. DeFi protocol fees
