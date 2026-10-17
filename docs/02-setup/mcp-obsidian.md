# Giao thức MCP cho Obsidian

MCP là giao thức chuẩn giúp Claude giao tiếp với các ứng dụng khác. Đối với một Vault, MCP mở ra một cánh cửa kết nối thẳng vào ứng dụng Obsidian thay vì chỉ thao tác trên thư mục bên dưới ổ cứng — nghĩa là Agent có thể làm việc với Vault từ bất kỳ phiên trò chuyện nào, chứ không chỉ giới hạn ở những phiên được khởi chạy bên trong thư mục đó.

Bạn không cần thiết lập phần này ngay từ đầu. Chỉ bổ sung nó khi bạn muốn chạy các tác vụ tự động theo lịch, hoặc khi bạn làm việc từ ứng dụng Claude Desktop thay vì mở terminal bên trong thư mục Vault.

## Hai lộ trình kết nối

Plugin [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) hiện đã tích hợp sẵn một máy chủ MCP tại đường dẫn `/mcp/`, vì vậy việc cài thêm một máy chủ trung gian riêng biệt không còn là điều bắt buộc nữa. Hãy kiểm tra file README của plugin đó trước tiên: nếu máy chủ tích hợp sẵn đã đáp ứng đủ nhu cầu của bạn, hãy chuyển thẳng sang bước đăng ký nó với ứng dụng khách (client) và bỏ qua bước 2 bên dưới.

Lộ trình sử dụng công cụ bên thứ ba được mô tả tại đây — chạy `mcp-obsidian` thông qua REST API của plugin — vẫn là phương án có tài liệu hướng dẫn phổ biến nhất hiện nay. Cả hai lộ trình đều mang lại kết quả cuối cùng như nhau.

## Bước 1: Bật plugin trong Obsidian

Trong Obsidian: mở **Settings** (biểu tượng bánh răng ở góc dưới bên trái) → **Community plugins** → **Turn on community plugins** → **Browse** → tìm kiếm từ khóa `Local REST API` → bấm **Install** → bấm **Enable**.

Mở phần cài đặt của plugin vừa cài. Tại đây bạn sẽ thấy mục **API Key**, là một chuỗi dài gồm các chữ cái và chữ số. Hãy sao chép chuỗi đó.

Obsidian hiển thị khóa này kèm theo từ `Bearer` ở phía trước. Từ `Bearer` đó không phải là một phần của khóa. Hãy chỉ sao chép phần chuỗi ký tự nằm phía sau nó. Đây chính là nguyên nhân phổ biến số một khiến kết nối thất bại ngay trong lần thử đầu tiên.

## Bước 2: Đăng ký máy chủ MCP

Trong thẻ Code hoặc cửa sổ terminal, hãy chạy câu lệnh sau với khóa API của bạn thay thế vào vị trí `PASTE-YOUR-KEY-HERE`:

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-obsidian"],
  "env": {
    "OBSIDIAN_API_KEY": "PASTE-YOUR-KEY-HERE",
    "OBSIDIAN_HOST": "127.0.0.1",
    "OBSIDIAN_PORT": "27124"
  }
}'
```

Lệnh `uvx` giúp tải và chạy máy chủ ngay mà không cần cài đặt cố định vào hệ thống. Nếu máy báo không tìm thấy lệnh này, hãy cài đặt bộ công cụ `uv` trước.

## Bước 3: Kiểm tra kết nối

```
List every file in my Obsidian vault.
```

Nếu Agent đọc và liệt kê đúng các ghi chú của bạn, kết nối đã hoạt động thành công.

## Khi kết nối không hoạt động

- **Obsidian đang đóng.** Plugin cung cấp API từ bên trong ứng dụng, vì vậy kết nối chỉ tồn tại khi Obsidian đang được mở.
- **Dính chữ `Bearer` trong khóa API.** Hãy xóa bỏ từ đó đi.
- **Sai cổng kết nối (port).** Hãy đối chiếu số cổng hiển thị trong phần cài đặt plugin với giá trị khai báo trong cấu hình của bạn. Giá trị mặc định là `27124`.
- **Plugin bị vô hiệu hóa.** Các plugin cộng đồng đôi khi bị tự động tắt đi khi chế độ hạn chế (Restricted mode) được bật lại sau một đợt cập nhật ứng dụng.

## Bạn có thực sự cần đến MCP không

Một nhánh phát triển (fork) được duy trì khá tích cực của `mcp-obsidian` từng được đưa vào trạng thái lưu trữ (archived) với lý do rất thẳng thắn: việc định tuyến vòng qua một plugin REST làm tăng thêm độ phức tạp không cần thiết trong khi bản chất Vault chỉ là các file Markdown nằm sẵn trên ổ đĩa. Đó cũng chính là lập luận mà cẩm nang này đưa ra khi khuyên bạn bắt đầu bằng cách thao tác trực tiếp trên hệ thống tệp tin — và điều này rất đáng để cân nhắc nghiêm túc: MCP chỉ thực sự phát huy giá trị khi bạn cần truy cập vào Vault từ những phiên làm việc không chạy bên trong thư mục đó, chứ không phải sớm hơn.

## Lưu ý bảo mật

Thiết lập này mở ra một máy chủ HTTP cục bộ cùng một khóa truy cập cho phép toàn quyền đọc và ghi đối với toàn bộ ghi chú của bạn. Hãy luôn giữ địa chỉ máy chủ ở `127.0.0.1`, tuyệt đối không mở cổng này ra mạng ngoài, và hãy bảo mật khóa API cẩn thận như một mật khẩu quan trọng. Nếu bạn vô tình dán lộ khóa này ở bất kỳ nơi công cộng nào, hãy lập tức tạo lại khóa mới (rotate) trong phần cài đặt của plugin.

## Tiếp theo

[Viết file CLAUDE.md của bạn](claude-md.md)
