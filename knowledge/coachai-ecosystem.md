# CoachAI CAMP Ecosystem — Complete Knowledge Base

## Company Identity

**OpenChief** is an AI-powered C-Suite of business experts that serves as the front door to the CoachAI CAMP ecosystem. Users interact with OpenChief for free — getting CEO, CFO, CMO, and CTO-level business guidance powered by Qwen 3.6 with RAG intelligence.

**CoachAI Tech Camps** (helpmecoach.ai) is the parent education company building the future of AI-powered tech education, real-world asset tokenization, and decentralized finance.

**Mission:** Create generational wealth through technology education and blockchain innovation.

---

## Products & Services

### 1. OpenChief — Free AI C-Suite

OpenChief is the primary user-facing product. It provides free business guidance through four AI executives:

- **CEO** — Strategy, business planning, vision, partnership development, Founders Club presentations
- **CFO** — Financial analysis, investment guidance, tokenomics, ROI modeling, budget planning
- **CMO** — Marketing strategy, campaigns, content creation, sponsor acquisition, enrollment growth
- **CTO** — Technical architecture, blockchain guidance, AI/ML advisory, security, integration support

**Pricing:** Free to use, no sign-up required.
**Upgrade Path:** CAMP Alpha subscription for full-power AI agents and tools.
**Technology:** Qwen 3.6 (open-weight LLM) with Retrieval-Augmented Generation trained on the CAMP ecosystem knowledge base.

### 2. CAMP Alpha — Premium AI Subscription

CAMP Alpha is the premium subscription tier providing advanced AI tools for builders and entrepreneurs.

**Features:**
- Advanced AI agent access with custom automation
- Design tools and content creation
- Priority support and dedicated agent capacity
- Custom agent training on user's business data
- Unlimited C-Suite consultations

**Pricing Tiers:**
- Starter: $29/month
- Professional: $99/month
- Business: $249/month
- Enterprise: $499/month

**Payment:** Stripe integration via Supabase Edge Functions.
**Conversion Path:** Free OpenChief chat demonstrates value → user upgrades for unlimited access.

### 3. CAMP Marketplace — Talent & AI Agent Exchange

A two-sided marketplace connecting Sponsors (businesses) with Campers (Tech Camp graduates).

**For Sponsors (Businesses):**
- Access to vetted AI agent teams and trained developers
- On-chain accountability with blockchain-verified deliverables
- Transparent KPIs and SLAs
- Tokenized co-ownership of agent output and IP
- Enterprise integration options

**For Campers (Talent):**
- Project opportunities from real businesses
- Revenue sharing through tokenized co-ownership
- Portfolio building with verified on-chain track records
- Mentorship and continued education

**Revenue Model:** Marketplace fees on sponsor-camper matches, commission on tokenized revenue sharing.

### 4. CAMP RWA Agent — Real-World Asset Tokenization

A platform for tokenizing real-world assets — primarily real estate — on the blockchain.

**Capabilities:**
- Custom NFT marketplace development for real estate
- Property fractionalization and tokenized ownership
- Multi-chain deployment: Base, Solana, Ethereum
- LayerZero protocol for cross-chain interoperability
- GoldBackBond 70% appraised value protection
- Enterprise integration: Bloomberg terminal, institutional APIs
- KYC/AML compliance automation

**Target Clients:** Real estate investors, property developers, institutional clients, family offices.
**Revenue Model:** Tokenization service fees, marketplace transaction fees, enterprise licensing.

### 5. CAMP DeFi — USDca Stablecoin Protocol

A multi-collateral stablecoin protocol built on Ethena-based architecture.

**USDca Token:**
- Backed by 5 assets: WBTC, USDC, USDT, ETH, WSOL
- Delta-neutral hedging strategies for price stability
- AI Lab agent continuously optimizes collateral ratios
- Target yield range: 18-20% (past performance does not guarantee future results)
- Deployed across 24 blockchain networks via LayerZero
- Total supply target: 100M USDca tokens

**Protection:**
- $100M GoldBackBond protection fund
- Coverage for smart contract risk, oracle failures, and market volatility

**Revenue Model:** Minting fees, yield optimization fees, cross-chain bridge fees.

**Disclaimers:** All yields are projections, not guarantees. Investments carry risk. Consult a licensed financial advisor.

### 6. Founders Club — Equity Investment Program

Three-tier investment program offering equity ownership in the CoachAI ecosystem.

**Silver Founder — $9,997:**
- Equity ownership in AI tech platform
- Quarterly strategic briefings
- Early access to CAMP developments
- Community forum participation
- Tax benefits through 501(c)(3) structure
- VIP launch event access ($2,500 value)
- Exclusive founder merchandise ($500 value)

**Gold Founder — $49,997:**
- Enhanced equity ownership position
- Governance board seat with voting rights
- Monthly founder consultations
- Priority investment opportunities
- Direct founder access and mentorship
- Private founder retreat ($5,000 value)
- 1-on-1 strategy sessions ($3,000 value)
- Tech camp preview access ($2,000 value)

**Platinum Founder — $99,997:**
- Maximum equity ownership tier
- Executive advisory board position
- Weekly founder strategy meetings
- Co-investment opportunities
- Named facility recognition (buildings/facilities)
- Legacy founder status (permanent)

**Revenue Model:** Direct equity investment capital.

### 7. CoachAI Tech Camps — Education Program

6-month intensive tech boot camps training the next generation of AI engineers, blockchain developers, and tech entrepreneurs.

**Curriculum Areas:**
- AI Engineering: LLM integration, RAG pipelines, agent development, prompt engineering
- Blockchain Development: Solidity, Rust (Solana), smart contract security, DeFi protocols
- Full-Stack Development: React, Node.js, Python, TypeScript, cloud infrastructure
- DevOps & Security: CI/CD, container orchestration, security auditing, monitoring

**Differentiator:** Graduates enter the CAMP Marketplace talent pool with verified skills and immediate access to project opportunities from sponsors.

**Revenue Model:** Tuition fees, corporate training packages, enterprise talent pipeline contracts.

### 8. GoldBackBond (GBB) — Protection Framework

Enterprise-grade security and protection service for the CAMP ecosystem.

**Services:**
- 70% appraised value protection for tokenized real-world assets
- $100M protection fund for DeFi protocol coverage
- Smart contract audit and risk assessment
- Enterprise-grade KYC/AML compliance
- Insurance-like coverage for oracle failures and market volatility

---

## Technology Architecture

### AI Stack
- **Primary LLM:** Qwen 3.6 235B via OpenRouter (open-weight, auditable)
- **Agent OS:** OpenFang — Rust-based Agent Operating System (14 crates)
- **RAG Pipeline:** Semantic memory with vector embeddings, cosine similarity search
- **Embedding Model:** all-MiniLM-L6-v2 (384 dimensions)
- **Knowledge Graph:** Entity-relation store with confidence scoring
- **Memory Backend:** SQLite (local) or PostgreSQL + pgvector (production)

### Blockchain Stack
- **Primary Chains:** Base, Solana, Ethereum
- **Cross-chain:** LayerZero protocol (24 networks)
- **Smart Contracts:** ERC-20 (USDca), ERC-721/1155 (RWA NFTs), DAO governance
- **Stablecoin:** Ethena-based multi-collateral architecture

### Platform Stack
- **Frontend:** React + TypeScript + Vite + Tailwind CSS
- **Backend:** Supabase (PostgreSQL, Auth, Edge Functions)
- **Payments:** Stripe via Supabase Edge Functions
- **Agent API:** OpenFang REST API (port 4200) with A2A protocol
- **Dashboard:** Alpine.js SPA served from OpenFang

### Security
- 3-layer security: Channel ACL, prompt injection scanning, outbound secret redaction
- End-to-end encryption on agent communications
- Hardened systemd services (ProtectSystem=strict)

---

## Business Units

| Unit | Status | Focus |
|------|--------|-------|
| Cashflow Trustee Ops | Provisioning | Trust setup, compliance |
| Goldbackbond Sales | Active | Lead conversion, revenue |
| GBB FX Sales | Active | Trade volume, growth |
| CoachAI Tech Camps | Active | Enrollment, completion rates |
| OpenChief Growth | Active | Agent uptime, fleet health |

---

## Revenue Funnels (Priority Order)

1. **Founders Club** — Highest value ($10K-$100K per investor)
2. **CAMP Alpha Subscriptions** — Recurring monthly ($29-$499/mo)
3. **Sponsor Marketplace Fees** — B2B revenue per match
4. **Tech Camp Enrollment** — Tuition per student
5. **RWA Tokenization Fees** — Per-asset service charges
6. **DeFi Protocol Fees** — Minting, yield optimization, bridges

---

## Key URLs

- **helpmecoach.ai** — CoachAI Tech Camps main site
- **openchief.ai** — OpenChief AI mission control
- **openchief.zo.computer** — Zo workstation operations (5 agents live)

---

## Competitive Advantages

1. **Open-weight AI** — Qwen 3.6 is fully transparent and auditable, unlike proprietary models
2. **RAG-grounded accuracy** — Answers sourced from real ecosystem data, not hallucinations
3. **No vendor lock-in** — Full control over AI infrastructure and data
4. **Integrated ecosystem** — Education → Talent → Marketplace → Finance → Investment pipeline
5. **On-chain accountability** — Blockchain-verified deliverables and transparent KPIs
6. **Multi-chain reach** — 24 networks via LayerZero for maximum accessibility
7. **GoldBackBond protection** — Enterprise-grade risk coverage across all products
