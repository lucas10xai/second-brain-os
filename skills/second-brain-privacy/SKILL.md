---
name: second-brain-privacy
description: >-
  Kiểm toán vault để tìm những nội dung không nên xuất hiện trong đó: thông tin
  xác thực (credentials), thông tin riêng tư của người khác, tài liệu công việc
  bảo mật, và bất kỳ thứ gì người dùng không muốn bị đồng bộ hoặc sao lưu. Sử dụng
  kỹ năng này khi người dùng hỏi về quyền riêng tư, chuẩn bị chia sẻ hoặc đồng bộ
  vault, vừa mới nhập lịch sử trò chuyện hoặc biên bản cuộc họp, hoặc hỏi có nội
  dung gì nhạy cảm trong ghi chú của họ. KHÔNG dùng để tự ý xóa bất kỳ thứ gì, hoặc
  dùng thay thế cho bước kiểm tra trước khi xuất bản (second-brain-publish).
---

# Kiểm toán quyền riêng tư (Audit privacy)

Một chiếc vault đã trưởng thành là một trong những tài liệu chứa mật độ thông tin cao nhất về một con người, và nó lại nằm trong một thư mục thường xuyên được đồng bộ, commit lên git, sao lưu và đôi khi được chia sẻ. Mỗi bản sao là thêm một nơi mà nội dung đó tồn tại.

## Quy tắc cốt lõi

Tìm kiếm và báo cáo. Không xóa bất kỳ thứ gì nếu không có chỉ dẫn rõ ràng nêu đích danh mục cần xóa.

## Quy trình thực hiện

1. **Quét tìm thông tin xác thực (credentials):** khóa API (API keys), token, mật khẩu, chuỗi kết nối cơ sở dữ liệu (connection strings). Kiểm tra cả thư mục `.obsidian/plugins/`, nơi lưu trữ dữ liệu cấu hình của các plugin.
2. **Tìm thông tin cá nhân của người khác:** bản gỡ băng cuộc họp, tin nhắn cá nhân, những điều được chia sẻ riêng tư (in confidence), chi tiết về sức khỏe hoặc tài chính của một người khác.
3. **Tìm tài liệu công việc bảo mật:** nội dung thuộc diện thỏa thuận bảo mật (NDA) hoặc bị giới hạn bởi quy định của công ty.
4. **Kiểm tra git remote.** Dữ liệu riêng tư nằm trong một kho mã nguồn công khai (public repo) là phiên bản đắt giá nhất của sự cố này.
5. **Báo cáo theo mức độ nghiêm trọng,** chỉ rõ tên file cụ thể và lý do.

## Định dạng đầu ra

```
Critical: <thông tin xác thực, bắt buộc phải gỡ bỏ và đổi khóa mới (rotate)>
High: <thông tin riêng tư của người khác>
Review: <tư liệu người dùng cần tự xem xét và quyết định>
Repo visibility: <public | private> - <nhận định>
```

## Hiệu chuẩn (Calibration)

Không bao giờ trích dẫn nguyên văn chuỗi mật khẩu hay khóa bí mật vào trong bản báo cáo. Chỉ nêu tên file và loại thông tin xác thực.

Việc biên tập che giấu thông tin (redaction) sau khi đã nạp (ingest) là không đáng tin cậy, bởi vì thông tin đó đã kịp lan sang các trang khái niệm và hệ thống liên kết. Khi phát hiện một nội dung không nên có mặt ở đó, hãy chỉ rõ cả những trang liên đới nào cũng sẽ cần được dọn dẹp theo.
