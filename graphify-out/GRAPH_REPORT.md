# Graph Report - second-brain  (2026-11-27)

## Corpus Check
- Corpus is ~8,793 words - fits in a single context window. You may not need a graph.

## Summary
- 154 nodes · 243 edges · 14 communities (10 shown, 4 thin omitted)
- Extraction: 89% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 25 edges (avg confidence: 0.9)
- Token cost: 152,982 input · 0 output

## Community Hubs (Navigation)
- TCBS Daily & Tickers
- The Batch AI Concepts
- Planner-Executor & Gemini
- Ops Notes & Logs
- Section 301 Sector Impact
- Dream Script Core
- Doc Workspace Model
- Plan Validation & Moves
- Bullet Matching & Index
- Capture Tool
- Action Application
- Errors & File Reading
- Hot.md Trimming
- Repo Root

## God Nodes (most connected - your core abstractions)
1. `dream()` - 15 edges
2. `Proposed Section 301 tariff up to 35% on Vietnam` - 11 edges
3. `Planner-Executor Model Routing` - 10 edges
4. `The Batch 2026-11-27` - 10 edges
5. `Daily 2026-11-26 (TCBS Cơ hội đầu tư)` - 10 edges
6. `Báo cáo phân tích (reports index)` - 9 edges
7. `Doc` - 8 edges
8. `Token Tax (Tokenizer Language Bias)` - 8 edges
9. `bullet()` - 7 edges
10. `GMD: Gemadept Corporation (HOSE)` - 7 edges

## Surprising Connections (you probably didn't know these)
- `ai/ Domain` --conceptually_related_to--> `Planner-Executor Model Routing`  [INFERRED]
  CLAUDE.md → ai/knowledge/planner-executor.md
- `Dreamer Agent` --references--> `hot.md Recent Bullets`  [EXTRACTED]
  .claude/agents/dreamer.md → hot.md
- `Dreamer Agent` --references--> `Notes Index (index.md)`  [EXTRACTED]
  .claude/agents/dreamer.md → index.md
- `Planner-Executor Model Routing` --conceptually_related_to--> `Dreamer Agent`  [INFERRED]
  ai/knowledge/planner-executor.md → .claude/agents/dreamer.md
- `Domain-Based Repo Structure` --references--> `Dream Skill`  [EXTRACTED]
  CLAUDE.md → .claude/skills/dream/SKILL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Dream Consolidation Pipeline (capture -> log -> dream -> notes/index/hot -> archive)** — tools_capture, _claude_agents_dreamer_dreamer_agent, claude_skills_dream_scripts_read_today, claude_skills_dream_scripts_dream, index_notes_index, hot_hot_md [INFERRED 0.95]
- **Planner-Executor Implementations Across Vendors** — ai_knowledge_planner_executor_antigravity_orchestrator, ai_knowledge_planner_executor_claude_code_advisor, ai_knowledge_planner_executor_codex_subagents, ai_knowledge_planner_executor_sakana_fugu [EXTRACTED 1.00]
- **Local LLM Inference Stack** — ai_sources_the_batch_2026_11_27_llama_cpp, ai_sources_the_batch_2026_11_27_gguf, ai_sources_the_batch_2026_11_27_quantization, ai_sources_the_batch_2026_11_27_ollama, ai_sources_the_batch_2026_11_27_lm_studio [EXTRACTED 1.00]
- **Sectors assessed by TCBS under Section 301 tariff** — invest_themes_us_section_301_textile_garment, invest_themes_us_section_301_seafood, invest_themes_us_section_301_wood_furniture, invest_themes_us_section_301_rubber_tyres, invest_themes_us_section_301_electronics, invest_themes_us_section_301_ports [EXTRACTED 1.00]
- **2026-11-26 TCBS coverage without Buy/Sell/Hold call** — invest_tickers_acv, invest_tickers_vnm, invest_tickers_msn [EXTRACTED 1.00]

## Communities (14 total, 4 thin omitted)

### Community 0 - "TCBS Daily & Tickers"
Cohesion: 0.12
Nodes (27): Daily 2026-11-26 (TCBS Cơ hội đầu tư), Foreign investors net selling (7th session), TCB (Techcombank), TCBS (Techcom Securities), VIC (Vingroup), VN-Index -3.42% sell-off (1,629.68), VN-Index technicals (below MA50, support ~1,600), Báo cáo phân tích (reports index) (+19 more)

### Community 1 - "The Batch AI Concepts"
Cohesion: 0.09
Nodes (19): Ahia et al. (2023), CLEAR (Coalition for Language Equity in AI Research), FLORES-200, Petrov et al. (NeurIPS 2023), AI Engineering Skills Map, GGUF Format, LatentMAS, llama.cpp 1.0 (+11 more)

### Community 2 - "Planner-Executor & Gemini"
Cohesion: 0.17
Nodes (12): Dreamer Agent, Dream Skill, Antigravity Orchestrator, Claude Code Advisor, Codex Subagents, Sakana Fugu, Antigravity Orchestrator, Gemini 4 Carbon (+4 more)

### Community 3 - "Ops Notes & Logs"
Cohesion: 0.19
Nodes (10): Proposals for knowledge/, Log: deploys will go out Tuesday 9am, Log: check monitor every morning, Log: pefima data sync every Monday, Log: not deploy prod on Monday, hot.md Recent Bullets, Notes Index (index.md), Deploys Note (+2 more)

### Community 4 - "Section 301 Sector Impact"
Cohesion: 0.21
Nodes (12): Electronics sector (neutral, mostly exempt, FDI), Seaports sector, Proposed Section 301 tariff up to 35% on Vietnam, Reciprocal Trade Agreement (tariff to 20%), Competitors at 18% (Bangladesh, Cambodia, Indonesia, Malaysia, Thailand), Rubber & tyres sector (GVR, PHR, DRC), Seafood sector (VHC), Section 232 exclusions (steel, aluminium, autos, wood, semiconductors) (+4 more)

### Community 5 - "Dream Script Core"
Cohesion: 0.31
Nodes (4): commit(), iso_day(), main(), repo_root()

### Community 7 - "Plan Validation & Moves"
Cohesion: 0.22
Nodes (5): check_plan(), dream(), files_under(), plan_moves(), print_diff()

### Community 8 - "Bullet Matching & Index"
Cohesion: 0.29
Nodes (6): bullet(), find_line(), is_struck(), rebuild_index(), squash(), summarize()

### Community 10 - "Action Application"
Cohesion: 0.29
Nodes (4): action_problems(), append_line(), apply_action(), apply_actions()

### Community 11 - "Errors & File Reading"
Cohesion: 0.50
Nodes (3): DreamError, log_bullets(), read_text()

## Ambiguous Edges - Review These
- `No prod deploys on Monday` → `Pefima data syncs every Monday`  [AMBIGUOUS]
  notes/pefima-sync.md · relation: conceptually_related_to

## Knowledge Gaps
- **28 isolated node(s):** `Per-Domain Ingest Skill (not yet built)`, `market-daily.csv Schema`, `second-brain`, `Claude Code Advisor`, `Codex Subagents` (+23 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 46 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Planner-Executor Model Routing` connect `Planner-Executor & Gemini` to `The Batch AI Concepts`, `Ops Notes & Logs`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Planner-Executor Model Routing` (e.g. with `Dreamer Agent` and `Proposals for knowledge/`) actually correct?**
  _`Planner-Executor Model Routing` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Per-Domain Ingest Skill (not yet built)`, `market-daily.csv Schema`, `second-brain` to the rest of the system?**
  _28 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `TCBS Daily & Tickers` be split into smaller, more focused modules?**
  _Cohesion score 0.11965811965811966 - nodes in this community are weakly interconnected._
- **Why does `Dream Skill` connect `Planner-Executor & Gemini` to `The Batch AI Concepts`, `Dream Script Core`, `Capture Tool`?**
  _High betweenness centrality (0.123) - this node is a cross-community bridge._
- **Should `The Batch AI Concepts` be split into smaller, more focused modules?**
  _Cohesion score 0.08666666666666667 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `No prod deploys on Monday` and `Pefima data syncs every Monday`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._