When I say "remember X" (or "remeber X"), run: python tools/capture.py "X"

## Cấu trúc theo lĩnh vực

Repo được tổ chức theo lĩnh vực. Phần dùng chung nằm ở gốc, kiến thức của từng lĩnh vực nằm trong thư mục riêng.

```
second-brain/
├── inbox/        # email/tài liệu thô chưa xử lý (dùng chung mọi lĩnh vực)
├── notes/        # note vận hành, do dream ghi
├── log/          # bullet "remember X" trong ngày (tools/capture.py)
├── archive/      # log đã dream xong
├── index.md, hot.md
├── tools/
├── ai/           # lĩnh vực AI
│   ├── sources/<tên-nguồn>/YYYY-MM-DD.md   # tóm tắt từng số newsletter/nguồn
│   ├── knowledge/<khái-niệm>.md            # note khái niệm, chắt lọc từ sources
│   └── applied/                            # (khi cần) áp dụng thực tế
└── invest/       # (sắp có) cùng cấu trúc như ai/
```

Quy ước:
- Mỗi lĩnh vực có `sources/` và `knowledge/` riêng. Không đặt `sources/` hay `knowledge/` ở gốc.
- Note trong `knowledge/` có frontmatter `title, tags, sources, updated`. Trường `sources` và mục Nguồn dùng wikilink đầy đủ đường dẫn tính từ gốc repo, ví dụ `[[ai/sources/the-batch/2026-11-27]]`.
- Mỗi lĩnh vực có skill ingest riêng để chuyển file trong `inbox/` thành `sources/`. Hiện `ai/` **chưa có** skill ingest, đang làm thủ công.
- Skill dream và `tools/capture.py` chỉ làm việc với `notes/`, `log/`, `index.md`, `hot.md` ở gốc, không đụng tới các thư mục lĩnh vực.
