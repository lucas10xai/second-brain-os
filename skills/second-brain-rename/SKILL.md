---
name: second-brain-rename
description: >-
  Đổi tên một trang wiki một cách an toàn: cập nhật tên file, sửa toàn bộ các
  wikilink trỏ đến (inbound wikilinks), thêm tên cũ vào danh sách tên gọi khác
  (aliases), và ghi vào nhật ký (log). Sử dụng kỹ năng này bất cứ khi nào một trang
  cần đổi sang tiêu đề chuẩn tắc (canonical title) khác, khi người dùng nói "đổi tên
  X thành Y", yêu cầu sửa tiêu đề thiếu nhất quán, hoặc sau khi chạy lint phát hiện
  vấn đề về đặt tên. KHÔNG dùng để gộp hai trang, di chuyển trang giữa các thư mục mà
  không đổi tên, hoặc đổi tên các file nằm ngoài wiki.
---

# Đổi tên một trang (Rename a page)

Việc agent tự ý đổi tên file trực tiếp là nguyên nhân phổ biến số một gây ra tình trạng gãy liên kết hàng loạt trong một chiếc vault do agent quản lý. Khi bạn đổi tên bên trong ứng dụng Obsidian, ứng dụng sẽ tự động cập nhật các liên kết; nhưng khi ghi/đổi tên file trực tiếp trên ổ đĩa thì không.

## Quy tắc cốt lõi

Đổi tên là một tổ hợp gồm bốn thao tác, không phải một. Phải thực hiện trọn vẹn cả bốn, hoặc không làm gì cả.

## Quy trình thực hiện

1. **Kiểm tra tên mới** đối chiếu với các trang và `aliases` hiện có. Một cái tên mới trùng với một `alias` sẵn có sẽ tạo ra sự nhập nhằng mà đồ thị không thể tự phân giải được.
2. **Đổi tên file** và cập nhật trường `title` trong phần frontmatter.
3. **Thêm tiêu đề cũ vào danh sách `aliases`.** Bước này giúp các tham chiếu từ bên ngoài, trí nhớ của người dùng, và bất kỳ liên kết nào vô tình bị sót vẫn tiếp tục hoạt động.
4. **Cập nhật toàn bộ các liên kết đến (inbound links).** Tìm kiếm trên toàn bộ vault, bao gồm cả `index.md`.
5. **Ghi nhật ký vào `log.md`:** tên cũ, tên mới, số lượng liên kết đã cập nhật.
6. **Xác minh lại** bằng công cụ kiểm tra liên kết (`link_check.py`).

## Định dạng đầu ra

```
Renamed: [[tên cũ]] -> [[tên mới]]
Inbound links updated: <n> liên kết trên <n> trang
Alias added: <tên cũ>
Remaining references: <none | danh sách còn sót>
```

## Hiệu chuẩn (Calibration)

Đừng đổi tên chỉ để chiều theo một sở thích trình bày câu chữ nhỏ nhặt trên một trang đang có rất nhiều liên kết trỏ đến. Chi phí xáo trộn là thật còn lợi ích thu về chỉ mang tính hình thức.

Nếu tên chuẩn xác thực sự còn mơ hồ, hãy hỏi ý kiến người dùng thay vì tự chọn bừa. Việc phải đổi tên lần thứ hai gây xáo trộn còn lớn hơn lần đầu.
