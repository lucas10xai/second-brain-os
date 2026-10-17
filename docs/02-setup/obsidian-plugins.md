# Những plugin đáng cài đặt

Obsidian vẫn hoạt động hoàn toàn tốt ngay cả khi không cài bất kỳ plugin nào dưới đây. Bạn chỉ nên cài thêm từng công cụ khi thực sự chạm trán đúng bài toán mà công cụ đó giải quyết.

## Local REST API

Chỉ bắt buộc phải có nếu bạn đi theo [lộ trình kết nối MCP](mcp-obsidian.md). Plugin này cung cấp quyền truy cập vào Vault của bạn thông qua một HTTP API cục bộ để Agent có thể giao tiếp với Vault từ bất kỳ phiên làm việc nào miễn là ứng dụng Obsidian đang mở.

## Dataview

Cho phép chạy các câu truy vấn trực tiếp trên dữ liệu Frontmatter và hiển thị kết quả ngay bên trong một trang ghi chú. Rất đáng cài một khi bạn đã có số lượng trang đủ nhiều và muốn tạo các bảng theo dõi tổng quan (dashboards):

````
```dataview
TABLE updated, tags
FROM "wiki/concepts"
WHERE updated < date(today) - dur(90 days)
SORT updated ASC
```
````

Đoạn truy vấn trên liệt kê toàn bộ các trang khái niệm chưa được ai đụng tới trong suốt ba tháng qua — đây chính là câu truy vấn rà soát hữu ích nhất trong toàn bộ Vault.

## Templater

Cung cấp hệ thống biểu mẫu (templates) có hỗ trợ biến động và ngày tháng tự động, dùng cho các khuôn mẫu trang nằm trong thư mục [`vault-template/templates/`](../../vault-template/templates/). Công cụ này rất tiện lợi cho những ghi chú bạn tự tay gõ. Riêng Agent thì không cần đến Templater vì nó tự ghi trực tiếp dữ liệu Frontmatter vào file.

## Những plugin đáng bổ sung về sau

- **[Git](https://github.com/Vinzent03/obsidian-git)**, plugin có lượt cài đặt cao thứ ba trên toàn hệ thống danh mục. Hỗ trợ tạo commit ngay bên trong giao diện Obsidian, kết hợp rất ăn ý với quy trình [quản lý phiên bản bằng Git](../09-maintenance/versioning-with-git.md).
- **[Importer](https://github.com/obsidianmd/obsidian-importer)**, plugin chính chủ của Obsidian, giúp kéo dữ liệu từ Notion, Evernote, Roam, Bear và Apple Notes về. Đây là bước đầu tiên cần dùng nếu bạn đang muốn di cư một kho ghi chú cũ sang hệ thống mới.
- **[Find orphaned files and broken links](https://github.com/Vinzent03/find-unlinked-files)**, thực hiện đúng các phép kiểm tra như quy trình [Lint](../09-maintenance/lint-and-health.md) nhưng hiển thị trực tiếp ngay trong ứng dụng.
- **[Omnisearch](https://github.com/scambier/obsidian-omnisearch)** giúp nâng cấp khả năng tìm kiếm toàn văn (full-text search), bao gồm cả việc tìm kiếm nội dung nằm bên trong các file PDF.

Xem danh sách xếp hạng đầy đủ kèm số lượt cài đặt tại: [resources/plugins.md](../../resources/plugins.md).

## Những thứ cần tránh xa

Hãy tránh các plugin tự động ghi lại file chạy ngầm phía sau. Bất kỳ công cụ nào tự động định dạng lại văn bản, tự động sắp xếp lại thứ tự các trường trong Frontmatter, hoặc tự động đổi tên file theo lịch trình đều sẽ xung đột trực diện với Agent — và bạn sẽ phải mất đứt một buổi tối chỉ để truy tìm xem thủ phạm nào trong hai bên đã làm hỏng định dạng của một trang wiki.

Ngoài ra, hãy tránh cài đặt các plugin vẽ đồ thị nặng nề hoặc tạo trang tổng quan màu mè cho đến khi bạn thực sự có đủ tư liệu đáng để nhìn ngắm. Một chiếc Vault trống rỗng nhưng cài sẵn mười lăm plugin chính là biểu hiện kinh điển của sự trì hoãn chứ không phải là một hệ thống làm việc thực thụ.

## Tiếp theo

[Git, đồng bộ hóa và sao lưu](git-and-sync.md)
