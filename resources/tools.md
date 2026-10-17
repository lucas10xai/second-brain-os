# Công cụ (Tools)

Mọi công cụ nằm ngoài danh mục plugin của `Obsidian`. Đối với các plugin, hãy xem [plugins.md](plugins.md). Số lượng sao được lấy từ GitHub vào tháng 9 năm 2026.

## Bộ công cụ cốt lõi (The core stack)

| Tool | What it does |
|---|---|
| [Obsidian](https://obsidian.md) | Trình soạn thảo markdown cục bộ. Bản thân `Vault` chỉ là một thư mục thuần túy trên ổ đĩa, đó là lý do các `Agent` làm việc với nó cực kỳ hiệu quả |
| [Obsidian Web Clipper](https://obsidian.md/clipper) | Tiện ích mở rộng trình duyệt chính thức, lưu các bài viết trên web thẳng vào thư mục `raw/`. Sử dụng thư viện Mozilla Readability |
| [Claude Code](https://code.claude.com/docs/en/setup) | `Agent` đảm nhận việc duy trì và biên tập wiki. Yêu cầu tài khoản trả phí |

## Các ngôi nhà thay thế cho một `Vault`

| Tool | Stars | Notes |
|---|---|---|
| [AFFiNE](https://github.com/toeverything/AFFiNE) | 72,292 | Kết hợp tài liệu, bảng trắng (whiteboard) và cơ sở dữ liệu trong một. Nặng nề hơn so với các tệp markdown thuần túy |
| [memos](https://github.com/usememos/memos) | 62,837 | Công cụ ghi chú nhanh tự triển khai (self-hosted), hỗ trợ markdown gốc. Rất hợp làm hộp thư đến cho thư mục `raw/` |
| [Joplin](https://github.com/laurent22/joplin) | 56,264 | Ứng dụng ghi chú chú trọng quyền riêng tư với khả năng đồng bộ trên mọi nền tảng |
| [SiYuan](https://github.com/siyuan-note/siyuan) | 46,225 | Không gian quản trị tri thức tự triển khai, hoạt động dựa trên cấu trúc khối (block-based) |
| [Logseq](https://github.com/logseq/logseq) | 44,818 | Trình soạn thảo dạng dàn ý (outliner), lưu tệp markdown thuần túy, hỗ trợ tham chiếu tới từng khối (block-level) |
| [Outline](https://github.com/outline/outline) | 40,483 | Cơ sở tri thức dành cho đội nhóm. Lựa chọn đúng đắn khi người sử dụng không chỉ có một mình bạn |
| [Trilium](https://github.com/TriliumNext/Trilium) | 37,762 | Cơ sở tri thức cá nhân phân cấp mạnh mẽ, hỗ trợ viết script tự động hóa |
| [Foam](https://github.com/foambubble/foam) | 17,386 | Mang đúng mô hình liên kết wikilink vào bên trong trình soạn thảo VS Code |
| [Anytype](https://github.com/anyproto/anytype-ts) | 8,764 | Ưu tiên lưu trữ cục bộ (local-first), mã hóa đầu cuối, tổ chức dữ liệu hướng đối tượng |
| [Dendron](https://github.com/dendronhq/dendron) | 7,465 | Hệ thống quản trị tri thức cá nhân (PKM) phân cấp chạy trên nền VS Code |

Cần thẳng thắn về sự đánh đổi ở đây: mọi công cụ nằm bên dưới `Obsidian` trong bảng này đều lưu trữ tri thức theo cấu trúc riêng của chúng. Các tệp markdown nằm trong một thư mục thuần túy là định dạng duy nhất mà việc rời bỏ công cụ không khiến bạn tốn bất kỳ chi phí chuyển đổi nào.

## Các ứng dụng tri thức thuần AI (AI-native knowledge apps)

| Tool | Stars | Notes |
|---|---|---|
| [Khoj](https://github.com/khoj-ai/khoj) | 37,186 | Bộ não thứ hai tích hợp AI có thể tự triển khai trên tài liệu của bạn, hỗ trợ tạo `Agent` tùy chỉnh và tự động hóa theo lịch |
| [Quivr](https://github.com/The-Vibe-Company/quivr) | 39,498 | Hệ thống `RAG` định hướng rõ ràng mà bạn có thể nhúng thẳng vào ứng dụng của riêng mình |
| [Reor](https://github.com/reorproject/reor) | 8,563 | Ứng dụng ghi chú AI ưu tiên cục bộ (local-first), tự động liên kết các ghi chú ngay trong lúc bạn viết |

Đây là các sản phẩm đóng gói sẵn, không phải các mẫu thiết kế mở. Chúng làm thay công việc cho bạn, với cái giá phải trả là sự mất đi tính khả chuyển (portability) mà bộ hướng dẫn này lấy làm trọng tâm. Rất đáng để biết qua trước khi bạn kết luận rằng cách tiếp cận dựa trên tệp tin thuần túy là quá vất vả.

## Thu thập và xử lý dữ liệu (Capture and processing)

| Tool | What it does |
|---|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Tải phụ đề và âm thanh từ các nền tảng video |
| [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) | Trích xuất bản ghi lời thoại (transcripts) trực tiếp từ Python |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | Bổ sung lớp văn bản nhận diện được (text layer) cho các tệp PDF dạng ảnh quét |
| [Zotero](https://github.com/zotero/zotero) | Trình quản lý tài liệu tham khảo, 15,184 sao, hỗ trợ luồng xuất dữ liệu sang markdown |
| [Readwise](https://readwise.io) | Đồng bộ các đoạn tô sáng (highlights) từ Kindle và các ứng dụng đọc sau vào thẳng `Obsidian`. Có thu phí |

## Tìm kiếm và đồ thị (Search and graph)

| Tool | What it does |
|---|---|
| [ripgrep](https://github.com/BurntSushi/ripgrep) | Nhanh đến mức hầu hết các `Vault` chẳng bao giờ cần đến một bộ chỉ mục (index) riêng |
| [NetworkX](https://networkx.org) | Thư viện phân tích đồ thị một khi bạn đã xuất được danh sách các cạnh nối (edge list) |
| [Kuzu](https://kuzudb.com) | Cơ sở dữ liệu đồ thị nhúng gọn nhẹ, không cần chạy máy chủ riêng |
| [Neo4j](https://neo4j.com) | Cơ sở dữ liệu đồ thị toàn diện. Quá mức cần thiết trừ phi bạn định xây dựng ứng dụng lớn đắp lên trên |
| [Gephi](https://gephi.org) | Khám phá đồ thị trực quan vượt xa khả năng hiển thị mặc định của `Obsidian` |
| [txtai](https://github.com/neuml/txtai) | 12,931 sao. Tìm kiếm ngữ nghĩa và luồng công việc LLM, phòng khi bạn quyết định mình thực sự cần tới embeddings |

## Xuất bản (Publishing)

| Tool | Stars | Notes |
|---|---|---|
| [Quartz](https://github.com/jackyzha0/quartz) | 13,185 | Biến `Vault` thành trang web tĩnh với đầy đủ liên kết ngược (backlinks), đồ thị cục bộ và thanh tìm kiếm |
