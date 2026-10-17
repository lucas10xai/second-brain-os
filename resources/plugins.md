# Các plugin Obsidian (Obsidian plugins)

Được xếp hạng theo số lượt cài đặt từ chính thống kê cộng đồng của `Obsidian`, tháng 9 năm 2026. Danh mục chính thức hiện có hơn 7.400 plugin; dưới đây là những plugin thực sự quan trọng đối với một `Vault` do `Agent` duy trì.

## `Agent` chạy ngay bên trong `Obsidian`

Một hướng tiếp cận mà phần [thiết lập ban đầu](../docs/02-setup/claude-code-setup.md) của hướng dẫn này từng bỏ qua: thay vì chạy `Agent` trong cửa sổ dòng lệnh (terminal) trỏ vào thư mục `Vault`, bạn có thể chạy nó ngay bên trong giao diện `Obsidian`.

| Plugin | Installs | What it does |
|---|---|---|
| [Claudian](https://github.com/yishentu/claudian) | 2,035,966 | Nhúng `Claude Code`, Codex và các `Agent` cục bộ khác làm cộng tác viên ngay trong `Vault` |
| [Copilot](https://github.com/logancyang/obsidian-copilot) | 1,832,464 | Chạy `Claude Code`, Codex và OpenCode ngay bên trong `Vault` của bạn |
| [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) | 1,189,513 | Mô hình embedding cục bộ giúp gợi ý các ghi chú liên quan ngay khi bạn đang viết. Không cần API key |
| [Local REST API with MCP](https://github.com/coddingtonbear/obsidian-local-rest-api) | 712,443 | Cung cấp quyền truy cập `Vault` qua local API bảo mật, nay đã tích hợp sẵn máy chủ MCP |
| [Agent Client](https://github.com/rait-09/obsidian-agent-client) | 261,371 | Trò chuyện với `Claude Code`, Codex và Gemini CLI thông qua giao thức Agent Client Protocol |
| [Smart Composer](https://github.com/glowingjade/obsidian-smart-composer) | 171,863 | Trò chuyện AI kèm ngữ cảnh ghi chú và áp dụng chỉnh sửa chỉ với một cú nhấp chuột |

## Cấu trúc và truy vấn

| Plugin | Installs | What it does |
|---|---|---|
| [Templater](https://github.com/SilentVoid13/Templater) | 5,527,936 | Tạo khuôn mẫu (templates) động. Phục vụ cho những trang bạn tự viết bằng tay |
| [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | 4,918,446 | Ngôn ngữ truy vấn trên dữ liệu frontmatter. Giúp trả lời câu hỏi "những trang nào có thuộc tính P" |
| [Metadata Menu](https://github.com/mdelobelle/metadatamenu) | 330,430 | Quản lý các trường frontmatter ở quy mô lớn. Rất hữu ích một khi [schema](../docs/04-structuring/frontmatter-schema.md) của bạn đã cố định |
| [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links) | 210,926 | Định kiểu hiển thị liên kết dựa theo frontmatter của trang đích, giúp nhận biết loại trang ngay trên dòng văn bản |

## Đồ thị (Graph)

| Plugin | Installs | What it does |
|---|---|---|
| [ExcaliBrain](https://github.com/zsviczian/excalibrain) | 336,025 | Bản đồ tư duy có cấu trúc, suy diễn năm loại quan hệ từ các liên kết, trường Dataview và thẻ (tags) |
| [Juggl](https://github.com/HEmile/juggl) | 135,614 | Đồ thị Cytoscape.js tương tác với các cạnh được phân loại và chế độ không gian làm việc có thể lưu lại |
| [Graph Analysis](https://github.com/SkepticMystic/graph-analysis) | community plugin | Chạy các thuật toán đồ thị và độ đo tương đồng trên toàn `Vault`, làm lộ diện các mối liên hệ chưa được gắn link |
| [Breadcrumbs](https://github.com/michaelpporter/breadcrumbs) | community plugin | Liên kết phân loại kèm hiển thị dạng cây, ma trận, hỗ trợ xuất ra Mermaid và Canvas |
| [3D Graph](https://github.com/AlexW00/obsidian-3d-graph) | community plugin | Hiển thị `Vault` dưới dạng đồ thị lực 3D. Giúp nhìn rõ cấu trúc phân cụm mà đồ thị 2D rối rắm thường che khuất |

## Bảo trì (Maintenance)

| Plugin | Installs | What it does |
|---|---|---|
| [Git](https://github.com/Vinzent03/obsidian-git) | 3,110,571 | Commit và đồng bộ `Vault` ngay từ bên trong `Obsidian`. Xem bài [quản lý phiên bản với Git](../docs/09-maintenance/versioning-with-git.md) |
| [Omnisearch](https://github.com/scambier/obsidian-omnisearch) | 1,837,484 | Tìm kiếm toàn văn (full-text search) mạnh mẽ hơn, bao gồm cả tìm kiếm nội dung bên trong tệp PDF |
| [Importer](https://github.com/obsidianmd/obsidian-importer) | 1,638,001 | Công cụ nhập dữ liệu chính thức từ Notion, Evernote, Roam, Bear, Apple Notes. Bước đầu tiên cho bất kỳ ai thực hiện [nạp dữ liệu hàng loạt](../docs/03-ingestion/bulk-backfill.md) |
| [Linter](https://github.com/platers/obsidian-linter) | 1,044,521 | Định dạng ghi chú theo các quy tắc nhất quán. Hãy cấu hình thật cẩn thận vì nó sẽ ghi đè trực tiếp vào tệp tin |
| [Find orphaned files and broken links](https://github.com/Vinzent03/find-unlinked-files) | 224,687 | Thực hiện chính xác những gì bước [kiểm tra sức khỏe và lint](../docs/09-maintenance/lint-and-health.md) làm, ngay trong `Obsidian` |

## Thu thập và học tập (Capture and study)

| Plugin | Installs | What it does |
|---|---|---|
| [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) | 7,795,993 | Plugin có số lượt cài đặt cao nhất trong toàn danh mục. Vẽ sơ đồ lưu trữ trực tiếp dưới dạng tệp tin trong `Vault` |
| [QuickAdd](https://github.com/chhoumann/quickadd) | 2,082,182 | Thu thập nhanh chỉ với một phím tắt vào thư mục và khuôn mẫu đã chọn trước |
| [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 592,497 | Tạo thẻ ghi nhớ (flashcards) từ chính ghi chú của bạn. Xem bài [tự học từ `Vault` của bạn](../docs/08-outputs/teaching-yourself.md) |
| [Zotero Integration](https://github.com/obsidian-community/obsidian-zotero-integration) | 550,881 | Đồng bộ trích dẫn, danh mục tài liệu tham khảo và ghi chú trên PDF từ Zotero |
| [ReadItLater](https://github.com/DominikPieper/obsidian-ReadItLater) | 134,982 | Lưu nội dung trực tuyến vào `Vault` theo khuôn mẫu định sẵn |
| [Webpage HTML Export](https://github.com/KosmosisDire/obsidian-webpage-export) | 152,194 | Xuất các ghi chú, bảng vẽ canvas hoặc toàn bộ `Vault` thành trang web tĩnh HTML |

## Lời cảnh báo về số lượng plugin

Mỗi plugin đều là một đoạn mã có quyền ghi vào ghi chú của bạn, chạy song song với một `Agent` cũng đang ghi vào chính những tệp tin đó. Hai thực thể cùng tự động viết lại tệp tin theo lịch trình riêng sớm muộn gì cũng sẽ xung đột với nhau.

Hãy chỉ cài đặt những gì giải quyết đúng vấn đề bạn đang thực sự gặp phải. Một `Vault` trống rỗng nhưng cài sẵn mười lăm plugin chính là biểu hiện kinh điển của sự trì hoãn.
