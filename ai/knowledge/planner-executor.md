---
title: Planner–Executor (model routing cho agent)
tags: [agents, model-routing, cost-optimization, coding-agents]
sources:
  - "[[ai/sources/the-batch/2026-11-27]]"
updated: 2026-11-27
---

# Planner–Executor (model routing cho agent)

## Tóm tắt
Pattern chia một task agentic cho hai model. **Model mạnh, đắt** (planner) đọc context và viết plan. **Model nhanh, rẻ** (executor) thực thi: sửa code, build, test, đối chiếu với plan. Khi executor gặp khó, nó trả quyền lại cho planner để viết lại plan. Mục tiêu là đạt gần chất lượng của model mạnh với chi phí và thời gian thấp hơn.

## Chi tiết / số liệu
- Vòng lặp: planner khảo sát (không sửa gì), viết plan, executor làm theo. Executor escalate khi gặp tín hiệu lỗi, ví dụ một check fail 2 lần hoặc interface chạy khác dự kiến. Planner sửa plan theo feedback rồi giao lại.
- Google Antigravity Orchestrator, dùng Gemini 4 Carbon làm planner và Hydrogen làm executor, trên Terminal-Bench:
  - Tỉ lệ thành công **gần bằng Carbon chạy một mình**
  - **Nhanh hơn 19%**, **tốn ít hơn 24%** quota token
- **Cảnh báo:** đơn giá rẻ không có nghĩa là tổng token ít. Hydrogen-xhigh sinh 304M output token trên AA Intelligence Index, Carbon chỉ 205M. Cần đo chi phí theo task, đừng chỉ nhìn giá trên mỗi token.
- Tham khảo giá: Hydrogen $1.50/$7.50 và Neon $3/$15 cho mỗi 1M token input/output.

## Ví dụ / biến thể
| Hệ thống | Cách chia việc |
|---|---|
| **Antigravity Orchestrator** (Google) | Một agent, **một context window**, chỉ đổi model phía sau giữa planner và executor |
| **Claude Code advisor** (Anthropic) | Model rẻ làm việc, hỏi model mạnh ở thời điểm then chốt (trước khi chốt plan, khi bị kẹt) |
| **Codex subagents** (OpenAI) | Gán model khác nhau cho từng subagent, chỉ giao việc khi được yêu cầu |
| **Sakana Fugu** | Có một model điều phối riêng, gọi model của Google/OpenAI/Anthropic ở từng bước |

Kết luận của The Batch: model tốt nhất cho một task coding có thể là **hai model trở lên phối hợp**.

## Áp dụng cho mình
- Với việc lặp lại trong second-brain (lọc newsletter vào `sources/`, chạy dream), thử dùng model mạnh để lên plan hoặc duyệt, còn bước điền nội dung thì giao model rẻ hơn (Sonnet/Haiku), hoặc bật advisor trong Claude Code.
- Workflow hiện tại (plan mode, mình duyệt, rồi mới thực thi) đã là một dạng planner–executor có con người làm "planner check".
- Khi so chi phí, ghi lại **tổng token và thời gian mỗi task**, không chỉ đơn giá.

## Nguồn
- [[ai/sources/the-batch/2026-11-27]] (mục 1: Gemini 4 Hydrogen & Neon + Antigravity Orchestrator)
- [Antigravity docs: models](https://antigravity.google/docs/models) · [Claude Code advisor](https://code.claude.com/docs/en/advisor) · [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) · [Sakana Fugu](https://www.deeplearning.ai/the-batch/fugu-blends-models-task-by-task)
