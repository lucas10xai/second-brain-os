# Kết nối dữ liệu thời gian thực

Các ghi chú tĩnh mới chỉ là một nửa bộ não. Nửa còn lại nằm ở những thông tin đang biến chuyển liên tục mỗi ngày: lịch làm việc của bạn, hộp thư đến, và các kênh trò chuyện nơi những quyết định thực tế được đưa ra.

Giao thức MCP kết nối những nguồn dữ liệu động đó theo đúng cách mà nó kết nối với Obsidian.

## Kết nối Lịch (Calendar)

```bash
claude mcp add google-workspace uvx workspace-mcp --tools calendar
```

Một cửa sổ đăng nhập OAuth sẽ mở ra trên trình duyệt. Hãy cấp quyền chỉ đọc (read access).

Sau đó, Vault của bạn đã có thể làm việc trực tiếp với dữ liệu lịch:

```
Read my calendar for today, log what I committed to in each meeting into my
tasks project, and flag anything without a clear next step.
```

Email, Slack và Notion cũng được kết nối thông qua các máy chủ MCP tương ứng của chúng, đăng ký bằng quy trình hoàn toàn tương tự.

## Chỉ cấp quyền đọc, tuyệt đối không cấp quyền ghi

Hãy cấp cho mỗi bộ kết nối (connector) phạm vi quyền hạn hẹp nhất đủ để hoàn thành công việc, và luôn ưu tiên chế độ chỉ đọc (read-only) ở bất kỳ nơi nào có tùy chọn này. Second Brain chỉ nên đọc dữ liệu của bạn để tổng hợp thông tin, chứ không được phép xóa dữ liệu hay tự ý gửi tin nhắn, email thay mặt bạn.

## Nguyên tắc quan trọng nhất cần khắc cốt ghi tâm

**Kiểm soát bằng khóa phân quyền (Keys), không phải bằng câu lệnh nhắc (Prompts).**

Việc dặn một Agent rằng "đừng xóa dữ liệu này nhé" chỉ là một lời gợi ý, hoàn toàn không phải là một thiết lập an toàn. Nếu về mặt kỹ thuật, Agent có đủ quyền hạn để xóa một file, dọn sạch một thư mục hay gửi đi một bức thư điện tử, thì sớm muộn gì vào một ngày đẹp trời nào đó, trong một ngữ cảnh mà bạn không lường trước được, nó sẽ thực sự làm điều đó.

Hãy chặn đứng những rủi ro không mong muốn ngay từ tầng cấp quyền hệ thống: sử dụng token chỉ đọc, khóa API giới hạn phạm vi (scoped keys), và tách biệt thông tin xác thực cho từng bộ kết nối. Khi đó, lời dặn trong file `CLAUDE.md` của bạn sẽ đóng vai trò là một chỉ dẫn ưu tiên nằm bên trên một hàng rào kỹ thuật vững chắc, thay vì là chốt chặn mong manh duy nhất ngăn giữa hộp thư của bạn và một lượt chạy lỗi của AI.

Nguyên tắc này cũng áp dụng tương tự cho chính Vault của bạn. Hãy xem bài [Hàng rào bảo vệ (Guardrails)](../06-agents/safety-and-guardrails.md).

## Những nguồn dữ liệu nào thực sự đáng kết nối

Hãy ưu tiên kết nối những nguồn nơi các quyết định và cam kết công việc thực sự diễn ra: đầu tiên là lịch làm việc, tiếp theo là email hoặc ứng dụng trò chuyện mà bạn thực sự dùng chính cho công việc hằng ngày.

Hãy bỏ qua những nguồn sinh ra khối lượng dữ liệu khổng lồ nhưng chứa rất ít tín hiệu giá trị. Một bộ kết nối xả hàng tá thông báo rác vào Vault sẽ làm giảm chất lượng của mọi câu truy vấn trong tương lai, bởi Agent sẽ phải đọc lướt qua toàn bộ đống tạp âm đó.

## Tiếp theo

[Những plugin đáng cài đặt](obsidian-plugins.md)
