When I say "remember X" (or "remeber X"), run: python tools/capture.py "X"

## Cấu trúc theo lĩnh vực

Repo được tổ chức theo lĩnh vực. Phần dùng chung nằm ở gốc, kiến thức của từng lĩnh vực nằm trong thư mục riêng.

```
second-brain/
├── inbox/        # email/tài liệu thô chưa xử lý, chia theo nguồn (inbox/the-batch/, inbox/tcbs/…); .eml không commit
├── notes/        # note vận hành, do dream ghi
├── log/          # bullet "remember X" trong ngày (tools/capture.py)
├── archive/      # log đã dream xong
├── index.md, hot.md
├── tools/
├── ai/           # lĩnh vực AI
│   ├── sources/<tên-nguồn>/YYYY-MM-DD.md   # tóm tắt từng số newsletter/nguồn
│   ├── knowledge/<khái-niệm>.md            # note khái niệm, chắt lọc từ sources
│   └── applied/                            # (khi cần) áp dụng thực tế
└── invest/       # lĩnh vực đầu tư
    ├── daily/YYYY/MM/YYYY-MM-DD.md         # nhật ký thị trường theo ngày
    ├── tickers/<MÃ>.md                     # mỗi mã một file, ghi dồn
    ├── themes/<chủ-đề>.md                  # chủ đề vĩ mô kéo dài, ghi dồn
    ├── reports/index.md                    # danh sách báo cáo phân tích
    └── data/market-daily.csv               # số liệu thị trường theo ngày
```

Quy ước chung:
- Mỗi lĩnh vực tự tổ chức thư mục theo mục đích của nó, và cấu trúc được mô tả trong mục riêng của lĩnh vực bên dưới. Không đặt thư mục của lĩnh vực nào ở gốc repo.
- Wikilink nội bộ dùng đường dẫn đầy đủ tính từ gốc repo (không có `.md`), vì nhiều file trùng tên theo ngày. Ví dụ `[[ai/sources/the-batch/2026-11-27]]`. Muốn hiển thị gọn thì thêm alias: `[[invest/daily/2026/11/2026-11-27|2026-11-27]]`.
- Mỗi lĩnh vực có skill ingest riêng để chuyển file trong `inbox/<nguồn>/` thành note của lĩnh vực đó. Hiện **chưa có** skill ingest nào, đang làm thủ công.
- Skill dream và `tools/capture.py` chỉ làm việc với `notes/`, `log/`, `index.md`, `hot.md` ở gốc, không đụng tới các thư mục lĩnh vực.

## ai/

- `sources/<tên-nguồn>/YYYY-MM-DD.md`: tóm tắt từng số newsletter/nguồn, nguồn thô nằm ở `inbox/<tên-nguồn>/`.
- `knowledge/<khái-niệm>.md`: frontmatter `title, tags, sources, updated`. Trường `sources` và mục Nguồn link về file trong `sources/` bằng wikilink đầy đủ đường dẫn.

## invest/

Mục đích từng thư mục:
- `daily/YYYY/MM/YYYY-MM-DD.md`: nhật ký từng ngày giao dịch, gồm diễn biến thị trường, tin tức, khuyến nghị TCBS, nhận định và quyết định của mình. Đây là nơi ghi đầu tiên; tickers/ và themes/ trỏ ngược về đây.
- `tickers/<MÃ>.md`: mỗi mã cổ phiếu một file, tên viết hoa (vd `GMD.md`). Theo dõi diễn biến, khuyến nghị và quyết định với mã đó theo thời gian.
- `themes/<kebab-case>.md`: chủ đề vĩ mô kéo dài nhiều ngày/tuần (vd `us-section-301.md`). Theo dõi diễn biến và tác động lên thị trường/mã.
- `reports/index.md`: bảng danh sách báo cáo phân tích (ngày, mã, tiêu đề, nguồn, link PDF), mới nhất ở dưới.
- `data/market-daily.csv`: mỗi ngày giao dịch một dòng theo đúng header `date,vnindex,change_pct,liquidity_bn,foreign_net_bn,usd_vnd`. `date` dạng YYYY-MM-DD; `liquidity_bn` là giá trị **khớp lệnh trên HoSE** (không gồm thoả thuận), tỷ đồng; `foreign_net_bn` là giá trị ròng của khối ngoại trên HoSE, tỷ đồng, **âm khi bán ròng**; `usd_vnd` là **tỷ giá trung tâm do NHNN niêm yết**.

Quy ước:
- **Khuyến nghị luôn ghi rõ nguồn và ngày**, dạng `TCBS: <khuyến nghị> (YYYY-MM-DD)`. Viết **tách khỏi quyết định của mình**: quyết định riêng ghi ở dòng/mục riêng `Quyết định của mình: …`, không trộn chung một câu.
- `tickers/` và `themes/` là **file ghi dồn**: chỉ append theo thời gian, mới nhất ở dưới, không sửa hay xoá dòng cũ. Nhận định đổi thì ghi thêm dòng mới.
- **Mỗi dòng** trong tickers/themes link về daily của ngày đó: `[[invest/daily/YYYY/MM/YYYY-MM-DD|YYYY-MM-DD]]`.
- Email TCBS thô để ở `inbox/tcbs/`, không commit (`.gitignore`: `inbox/**/*.eml`).
