# Graph Report - second-brain  (2026-11-27)

## Corpus Check
- 3 files · ~36,195 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 448 nodes · 856 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.87)
- Token cost: 62,418 input · 0 output

## Community Hubs (Navigation)
- Market Late Oct (Oil & Gas)
- Dream Script Internals (1)
- TCBS Analysis Reports Index
- AI Agents & Cyber Research
- Macro & Policy (Early Nov)
- Dream Script Internals (5)
- Market 23-28 Oct, Retail & Banks
- Model Routing & Dream Workflow
- Chemicals & Fertilizer
- Section 301 & 26/11 Sell-off
- FPT, EIB & PVD
- Repo Root

## God Nodes (most connected - your core abstractions)
1. `TCBS Analysis Reports Index` - 63 edges
2. `Theme: Vietnam Macro` - 21 edges
3. `Theme: Seaports and Shipping Sector` - 20 edges
4. `VHM – Vinhomes` - 19 edges
5. `Theme: Chemicals, Fertilizer and Rubber Sector` - 19 edges
6. `Theme: Residential Real Estate Sector` - 18 edges
7. `Theme: Market-wide Earnings (quarterly)` - 17 edges
8. `Daily 2026-11-06` - 16 edges
9. `Daily 2026-11-12` - 16 edges
10. `Daily 2026-11-23` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Planner-Executor Model Routing` --conceptually_related_to--> `Dreamer Agent`  [INFERRED]
  ai/knowledge/planner-executor.md → .claude/agents/dreamer.md
- `Use Graph for Cross-Domain Questions` --references--> `US Section 301 tariffs on Vietnam (overcapacity)`  [INFERRED]
  CLAUDE.md → invest/themes/us-section-301.md
- `Antigravity Orchestrator` --semantically_similar_to--> `Antigravity Orchestrator`  [INFERRED] [semantically similar]
  ai/knowledge/planner-executor.md → ai/sources/the-batch/2026-11-27.md
- `VHM 90.9% of Sector Profit` --semantically_similar_to--> `Earnings Growth Concentration (ex-VIC/VHM only +22.4%)`  [INFERRED] [semantically similar]
  invest/themes/nganh-bat-dong-san.md → invest/themes/ket-qua-kinh-doanh-thi-truong.md
- `Token Tax (Tokenizer Language Bias)` --semantically_similar_to--> `Token Tax (The Batch section 3)`  [INFERRED] [semantically similar]
  ai/knowledge/token-tax.md → ai/sources/the-batch/2026-11-27.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AI Cyber Capabilities Trend (cheaper, stronger vuln finding)** — ai_sources_the_batch_2026_10_02_glm_5_3_cyber_capability, ai_sources_the_batch_2026_11_27_gemini_4_carbon, ai_sources_the_batch_2026_11_13_gpt_6_cyber, ai_sources_the_batch_2026_10_30_agent_escape_incident [EXTRACTED 1.00]
- **Local LLM Inference Stack** — ai_sources_the_batch_2026_11_27_llama_cpp, ai_sources_the_batch_2026_11_27_gguf, ai_sources_the_batch_2026_11_27_quantization, ai_sources_the_batch_2026_11_27_ollama, ai_sources_the_batch_2026_11_27_lm_studio [EXTRACTED 1.00]
- **MSCI Frontier Markets Q4/2026 rebalance (NLG, PNJ add; PC1 remove)** — invest_tickers_nlg_msci_frontier_markets_addition, invest_tickers_pnj_msci_frontier_markets_addition, invest_tickers_pc1_msci_frontier_markets_removal [EXTRACTED 1.00]
- **Planner-Executor Implementations Across Vendors** — ai_knowledge_planner_executor_antigravity_orchestrator, ai_knowledge_planner_executor_claude_code_advisor, ai_knowledge_planner_executor_codex_subagents, ai_knowledge_planner_executor_sakana_fugu [EXTRACTED 1.00]
- **Sectors assessed by TCBS under Section 301 tariff** — invest_themes_us_section_301_textile_garment, invest_themes_us_section_301_seafood, invest_themes_us_section_301_wood_furniture, invest_themes_us_section_301_rubber_tyres, invest_themes_us_section_301_electronics, invest_themes_us_section_301_ports [EXTRACTED 1.00]
- **2026-11-26 TCBS coverage without Buy/Sell/Hold call** — invest_tickers_acv, invest_tickers_vnm [EXTRACTED 1.00]
- **TCBS e-commerce vs listed retail chains report (2026-10-23)** — invest_tickers_msn_tcbs_attractive_opportunity, invest_tickers_mwg_tcbs_attractive_opportunity, invest_themes_thuong_mai_dien_tu_ban_le_thuong_mai_dien_tu_ban_le [EXTRACTED 1.00]
- **Cái Mép deep-sea port capacity race** — invest_daily_2026_11_2026_11_09_cai_mep_ha_container_port, invest_tickers_gmd_gemalink, invest_tickers_gmd_gemalink_2a, invest_daily_2026_11_2026_11_25_port_shipping_q3_report [INFERRED 0.75]
- **Agent Safety Controls (sandbox, monitor, approval, harness)** — ai_sources_the_batch_2026_10_30_agent_sandboxing_least_privilege, ai_sources_the_batch_2026_10_30_reasoning_monitor, ai_sources_the_batch_2026_11_13_human_approval_gate, ai_sources_the_batch_2026_11_13_openworker_harness_sdk, ai_sources_the_batch_2026_11_13_agent_harness [INFERRED 0.85]
- **Graph Freshness Mechanism** — claude_graphify_code_update_rule, claude_graphify_stop_hook_auto_update, claude_hooks_graphify_stale, claude_note_wins_rule [INFERRED 0.85]
- **Invest Note-Writing Conventions** — claude_tcbs_recommendation_convention, claude_append_only_convention, claude_daily_backlink_convention, claude_full_path_wikilink_convention [INFERRED 0.85]
- **PNJ liquidity and governance stress (Nov 2026)** — invest_tickers_pnj_t_120_buyback_policy, invest_tickers_pnj_diamond_inventory, invest_tickers_pnj_independent_directors_resignation [INFERRED 0.85]
- **TCBS Q3/2026 Earnings Season Sector Reports** — invest_themes_ket_qua_kinh_doanh_thi_truong_ket_qua_kinh_doanh_thi_truong, invest_themes_nganh_bat_dong_san_nganh_bat_dong_san, invest_themes_nganh_chung_khoan_nganh_chung_khoan, invest_themes_nganh_hoa_chat_nganh_hoa_chat, invest_themes_nganh_cang_bien_nganh_cang_bien [INFERRED 0.85]
- **TCBS chemical sector Q3/2026 stock ratings** — invest_daily_2026_11_2026_11_25_chemical_sector_q3_report, invest_tickers_dpr_positive_chem_rating, invest_tickers_dpm_neutral_chem_rating, invest_tickers_ddv_negative_chem_rating [INFERRED 0.95]
- **Dream Consolidation Pipeline (capture -> log -> dream -> notes/index/hot -> archive)** — tools_capture, _claude_agents_dreamer_dreamer_agent, claude_skills_dream_scripts_read_today, claude_skills_dream_scripts_dream, index_notes_index, hot_hot_md [INFERRED 0.95]
- **MSCI Frontier Markets Q4/2026 index exclusions** — invest_daily_2026_11_2026_11_12_msci_fm_q4_2026_review, invest_tickers_dig_msci_fm_exclusion, invest_tickers_fts_msci_fm_exclusion [INFERRED 0.95]

## Communities (12 total, 1 thin omitted)

### Community 0 - "Market Late Oct (Oil & Gas)"
Cohesion: 0.06
Nodes (63): Daily 2026-10-27: VN-Index 1,761.87 (-0.10%), Fed Meeting 27-28 Oct 2026, TCBS: Wait to Buy FMC (2026-10-27), OCB Q3/2026 Pre-tax Profit >1,653 bn, Daily 2026-10-30: VN-Index 1,741.62 (-0.80%), TCBS: Wait to Buy PVS (2026-10-30), VHM Q3/2026 Net Profit 23,021 bn (+419%), Cái Mép Hạ container port (Vingroup-led consortium) (+55 more)

### Community 1 - "Dream Script Internals (1)"
Cohesion: 0.07
Nodes (28): main(), rel(), action_problems(), append_line(), apply_action(), apply_actions(), bullet(), check_plan() (+20 more)

### Community 2 - "TCBS Analysis Reports Index"
Cohesion: 0.06
Nodes (56): Daily 2026-11-10, HVN-ANA Holdings joint venture framework, TCBS: Mua KDH @15,900 (2026-11-10), MOIT 2027 power supply requirement (+10%/yr demand), Vietnam-Japan agreements (Ô Môn 3 JICA loan, nuclear MoU), VinaCapital buys 12.5M KDH shares (6.2% to 7.2%), BESS generation price framework 2026 (max 3,209.98 VND/kWh), Daily 2026-11-12 (+48 more)

### Community 3 - "AI Agents & Cyber Research"
Cohesion: 0.07
Nodes (32): Antigravity Orchestrator, Claude Code Advisor, Codex Subagents, Sakana Fugu, AREX Research Agent, DeepSeek-V4.1-Flash, Gemini 3.8 Live, GLM-5.3 Open-weights Cyber Capability (+24 more)

### Community 4 - "Macro & Policy (Early Nov)"
Cohesion: 0.06
Nodes (47): 10-month Trade Turnover ~1,010.6 bn USD, CPI Oct +5.09% YoY Release, TCBS: Wait to Buy SSI (2026-11-03), NHNN directive to cut deposit and lending rates, Daily 2026-11-05, Draft decree replacing ND 83/2014 on petroleum pricing, Slow NSTW disbursement for national target programs (8.73%), TCBS: Nắm giữ PVT (2026-11-05) (+39 more)

### Community 5 - "Dream Script Internals (5)"
Cohesion: 0.08
Nodes (21): Planner-Executor Model Routing, ai/ Domain, ai/knowledge (Concept Notes), ai/sources (Per-Issue Newsletter Summaries), archive/ (Dreamed Logs), 20 Dangling Edges Limitation, Per-Domain Ingest Skill (Not Yet Built), graphify Knowledge Graph (graphify-out/) (+13 more)

### Community 6 - "Market 23-28 Oct, Retail & Banks"
Cohesion: 0.07
Nodes (41): Daily 2026-10-23: VN-Index 1,774.15 (+0.77%), KDH 13,500 bn VietinBank Loan for BT Projects, VN-Index Reclaims MA50, TCBS: Hold VPB (2026-10-23), Daily 2026-10-28: VN-Index 1,766.65 (+0.27%), MWG Q3/2026 Net Profit >3,500 bn, Plan to Cut Retail Power Price and Fuel Excise Tax (11/2026-03/2027), TCBS: Wait to Buy SCS (2026-10-28) (+33 more)

### Community 7 - "Model Routing & Dream Workflow"
Cohesion: 0.07
Nodes (28): Dreamer Agent, Dream Skill, Ahia et al. (2023), CLEAR (Coalition for Language Equity in AI Research), FLORES-200, Petrov et al. (NeurIPS 2023), AI Engineering Skills Map, GGUF Format (+20 more)

### Community 8 - "Chemicals & Fertilizer"
Cohesion: 0.11
Nodes (29): Daily 2026-10-26: VN-Index 1,763.55 (-0.60%), TCBS: Wait to Buy DDV (2026-10-26), SBV Extra Credit Quota for 35 Key Projects, VIC 230bn Won International Bond at 8%, Daily 2026-11-03: VN-Index 1,699.62 (-0.65%), DPR 14% Cash Dividend and 1:1 Bonus Share, Amended Electricity Law Discussion, VN-Index Loses 1,700 (+21 more)

### Community 9 - "Section 301 & 26/11 Sell-off"
Cohesion: 0.18
Nodes (14): TCBS (Techcom Securities), VN-Index -3.42% sell-off (1,629.68), Electronics sector (neutral, mostly exempt, FDI), Seaports sector, Proposed Section 301 tariff up to 35% on Vietnam, Reciprocal Trade Agreement (tariff to 20%), Competitors at 18% (Bangladesh, Cambodia, Indonesia, Malaysia, Thailand), Rubber & tyres sector (GVR, PHR, DRC) (+6 more)

### Community 10 - "FPT, EIB & PVD"
Cohesion: 0.27
Nodes (11): Daily 2026-11-04, HFIC divestment of 8.48M EIB shares, FPT chip testing and packaging plant (Yên Phong II-C), TCBS: Chờ mua PVD (2026-11-04), EIB, HFIC divests entire 8.48M EIB stake, FPT chip testing & packaging plant (300M chips/yr), Persistent foreign net selling of FPT (+3 more)

## Ambiguous Edges - Review These
- `No prod deploys on Monday` → `Pefima data syncs every Monday`  [AMBIGUOUS]
  notes/pefima-sync.md · relation: conceptually_related_to

## Knowledge Gaps
- **95 isolated node(s):** `Calls to Slow AI (Pacing the frontier)`, `Gemini 4 Argon MuJoCo Simulation from Images`, `AI Search vs Traditional Search Ads War`, `LLM Editing Neural Network Weights`, `QĐ 2409/QĐ-NHNN banking modernization plan to 2030` (+90 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 113 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TCBS Analysis Reports Index` connect `Market Late Oct (Oil & Gas)` to `TCBS Analysis Reports Index`, `Macro & Policy (Early Nov)`, `Market 23-28 Oct, Retail & Banks`, `Chemicals & Fertilizer`, `FPT, EIB & PVD`?**
  _High betweenness centrality (0.549) - this node is a cross-community bridge._
- **What connects `Calls to Slow AI (Pacing the frontier)`, `Gemini 4 Argon MuJoCo Simulation from Images`, `AI Search vs Traditional Search Ads War` to the rest of the system?**
  _95 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Late Oct (Oil & Gas)` be split into smaller, more focused modules?**
  _Cohesion score 0.057859703020993344 - nodes in this community are weakly interconnected._
- **Why does `US Section 301 tariffs on Vietnam (overcapacity)` connect `Market Late Oct (Oil & Gas)` to `Chemicals & Fertilizer`, `Dream Script Internals (5)`?**
  _High betweenness centrality (0.490) - this node is a cross-community bridge._
- **Should `Dream Script Internals (1)` be split into smaller, more focused modules?**
  _Cohesion score 0.06753246753246753 - nodes in this community are weakly interconnected._
- **Should `TCBS Analysis Reports Index` be split into smaller, more focused modules?**
  _Cohesion score 0.05909090909090909 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `No prod deploys on Monday` and `Pefima data syncs every Monday`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._