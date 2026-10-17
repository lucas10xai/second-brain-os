# Chạy Claude Code bên trong Vault

Claude Code đóng vai trò là nửa đọc và ghi dữ liệu của hệ thống. Có hai cách chính để chạy nó, và sự lựa chọn chỉ ảnh hưởng đến nơi bạn gõ lệnh chứ không làm thay đổi kết quả thực thi.

## Phương án A: Dùng ứng dụng máy tính (Desktop app)

Tải ứng dụng Claude Desktop từ địa chỉ [claude.com/download](https://claude.com/download) và đăng nhập. Bên trong ứng dụng có thẻ **Code**, thực chất chính là Claude Code nhưng có giao diện đồ họa không cần dùng đến terminal. Nếu bạn chưa từng làm việc với giao diện dòng lệnh, hãy bắt đầu từ đây.

## Phương án B: Dùng cửa sổ dòng lệnh (Terminal)

Cài đặt Claude Code và chạy lệnh `claude` ngay bên trong thư mục Vault của bạn:

```bash
cd ~/brain
claude
```

Khi được khởi động theo cách này, Agent sẽ đọc và ghi trực tiếp vào Vault thông qua hệ thống tệp tin (filesystem) của máy tính mà không cần đến bất kỳ plugin hay máy chủ MCP nào. Đây là cách thiết lập đơn giản nhất có thể và đã hoàn toàn đủ dùng cho mọi tác vụ trong các chương thu thập dữ liệu (Ingestion), cấu trúc hóa và truy xuất của cẩm nang này.

Hướng dẫn cài đặt chi tiết cho từng hệ điều hành nằm trong [tài liệu thiết lập chính thức](https://code.claude.com/docs/en/setup).

## Phương án C: Nhúng trực tiếp bên trong Obsidian

Các plugin cộng đồng hiện nay đã cho phép nhúng thẳng Agent vào bên trong trình soạn thảo, và được sử dụng rất rộng rãi: [Claudian](https://github.com/yishentu/claudian) đã vượt mốc hai triệu lượt cài đặt và [Copilot](https://github.com/logancyang/obsidian-copilot) cũng bám sát ngay phía sau. Cả hai đều cho phép chạy Claude Code, Codex hoặc một Agent cục bộ ngay trong một khung cửa sổ nằm cạnh ghi chú của bạn.

Bạn nên biết đến tùy chọn này vì nó loại bỏ hoàn toàn việc phải chuyển đổi qua lại giữa các cửa sổ ứng dụng. Tuy nhiên, cũng cần hết sức cẩn trọng với nó vì cùng một lý do mà cẩm nang này khuyên bạn nên chạy quy trình Ingest theo lịch định kỳ: việc có sẵn một Agent ngay trong trình soạn thảo rất dễ khiến bạn tiện tay yêu cầu những chỉnh sửa ngẫu hứng không bao giờ được ghi nhận vào `log.md` — và một Vault không có nhật ký đầy đủ là một Vault bạn không thể kiểm toán được.

Cách phân chia hợp lý nhất là dùng plugin trong Obsidian để trò chuyện và nháp văn bản, còn mọi thao tác ghi các trang wiki chính thức thì thực hiện qua terminal hoặc tác vụ tự động theo lịch.

## Yêu cầu về gói tài khoản

Claude Code yêu cầu tài khoản trả phí: gói Pro, Max, Team, Enterprise, hoặc tài khoản Console tính phí theo lượng token sử dụng. Theo tài liệu thiết lập của chính Anthropic, gói Claude.ai miễn phí không bao gồm quyền truy cập Claude Code. Nếu thẻ Code yêu cầu bạn nâng cấp tài khoản thì đó chính là lý do.

## Thao tác file trực tiếp (Filesystem) hay qua MCP

Cả hai cách đều hoạt động tốt. Sự khác biệt khá hẹp nhưng rất đáng nắm rõ trước khi bạn lựa chọn:

| Tiêu chí | Hệ thống tệp tin (Filesystem) | Giao thức MCP |
|---|---|---|
| Thiết lập | không cần gì thêm, chỉ cần `cd` vào thư mục Vault | cần cài đặt plugin cộng thêm một câu lệnh cấu hình |
| Yêu cầu mở sẵn Obsidian | không bắt buộc | bắt buộc, vì plugin phải chạy để cung cấp API |
| Phạm vi truy cập | gói gọn trong thư mục nơi bạn khởi chạy lệnh | toàn bộ Vault, truy cập được từ bất kỳ phiên làm việc nào |
| Khả năng gặp lỗi | hầu như không có | plugin bị tắt, ứng dụng đang đóng, hoặc lệch cổng (port) kết nối |

Hãy bắt đầu bằng cách thao tác trực tiếp trên hệ thống tệp tin. Chỉ chuyển sang dùng [MCP](mcp-obsidian.md) khi bạn muốn Agent chạm được vào Vault từ những phiên làm việc không khởi chạy bên trong thư mục đó — điều chủ yếu phát sinh khi bạn bắt đầu thiết lập các tác vụ chạy tự động theo lịch.

## Lần chạy đầu tiên

Hãy yêu cầu Agent đọc hiểu cấu trúc trước khi giao cho nó bất kỳ nhiệm vụ nào khác:

```
Read CLAUDE.md and wiki/index.md, then tell me what this vault currently
contains and what is missing.
```

Câu trả lời nhận được sẽ cho bạn biết ngay lập tức liệu Agent đã hiểu đúng các chỉ dẫn hay chưa. Nếu nó bắt đầu tự bịa ra một cấu trúc thư mục mà bạn không hề yêu cầu, nghĩa là file `CLAUDE.md` của bạn đang quá mơ hồ. Hãy xem bài [Viết file CLAUDE.md của bạn](claude-md.md).

## Quyền hạn truy cập (Permissions)

Agent sẽ hỏi xin phép trước khi chỉnh sửa các file. Hãy cấp cho nó quyền ghi vào bên trong thư mục Vault và không cấp thêm bất kỳ quyền nào khác ở ngoài. Tuyệt đối không cấp quyền chạy lệnh hệ thống (shell access) tràn lan trên một thư mục chứa những dữ liệu quan trọng không thể để mất, và hãy đọc kỹ bài [Hàng rào bảo vệ (Guardrails)](../06-agents/safety-and-guardrails.md) trước khi bạn thiết lập bất kỳ quy trình tự động hóa chạy theo lịch nào.

## Tiếp theo

[Giao thức MCP cho Obsidian](mcp-obsidian.md)
