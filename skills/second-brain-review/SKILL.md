---
name: second-brain-review
description: >-
  Tạo bản tổng kết định kỳ cho vault bộ não thứ hai: những gì đã được thêm vào,
  những chủ đề nào đang phát triển mạnh, điều gì đang mâu thuẫn với điều gì, những
  câu hỏi nào vẫn còn bỏ ngỏ, và tài liệu nào đáng đọc tiếp theo. Sử dụng kỹ năng
  này bất cứ khi nào người dùng yêu cầu tổng kết tuần hoặc tháng, hỏi vault của họ
  có gì thay đổi, gần đây họ đang tìm hiểu về những gì, hoặc họ nên xem gì tiếp theo,
  cũng như khi tác vụ tổng kết theo lịch định kỳ được kích hoạt. KHÔNG dùng để kiểm
  lỗi cấu trúc (lint), nạp tài liệu nguồn, hoặc trả lời một câu hỏi tra cứu sự kiện cụ thể.
---

# Tổng kết định kỳ Vault (Review the vault)

Các hệ thống thu thập thông tin thường thất bại ở đúng thời điểm mọi thứ chỉ có chiều đi vào mà không có chiều đi ra. Bản tổng kết định kỳ chính là mắt xích khép kín vòng lặp đó: nó biến một tuần nạp tài liệu thành thứ mà chủ sở hữu thực sự đọc và hành động theo, đồng thời làm cho chiếc vault trở nên sống động thay vì chỉ là một nhà kho lưu trữ chết.

## Quy tắc cốt lõi

Bản tổng kết báo cáo về tri thức trong vault, chứ không phải báo cáo về hoạt động của agent. Không ai cần biết đã có bao nhiêu lệnh gọi công cụ được thực thi; điều họ cần biết là giờ đây họ đã hiểu thêm được những gì.

## Quy trình thực hiện

1. **Đối chiếu sự thay đổi trong kỳ (Diff the period).** Tìm các trang mới và trang được cập nhật kể từ lần tổng kết trước, dựa vào `log.md` và ngày tháng trong frontmatter.
2. **Tìm các cụm chủ đề đang lớn lên.** Những khái niệm nào thu hút thêm nhiều liên kết nhất. Đó chính là nơi sự chú ý thực sự của chủ sở hữu đã đổ dồn vào — thường khác với những gì họ tự hình dung.
3. **Làm nổi bật các điểm mâu thuẫn** đã được ghi nhận trong kỳ nhưng vẫn chưa được giải quyết.
4. **Liệt kê các câu hỏi mở** từ các trang khái niệm (`concept`) và trang tổng hợp (`synthesis`).
5. **Tìm những điểm bị bỏ bê.** Các trang được liên kết tới rất nhiều lần nhưng nội dung lại sơ sài, hoặc các khoảng trống (`Gaps`) trong `index.md` cứ liên tục được nhắc tới.
6. **Khuyến nghị ba việc nên đọc hoặc viết tiếp theo**, mỗi việc gắn liền với một trang cụ thể.

## Định dạng đầu ra

```
## Tuần lễ từ ngày <date>

Added: <n> trang, <n> nguồn đã nạp

### Sự chú ý của bạn đã tập trung vào đâu
<hai hoặc ba câu nhận định về các cụm chủ đề phát triển mạnh nhất>

### Chưa ngã ngũ (Unresolved)
<các mâu thuẫn và câu hỏi mở, kèm liên kết tới từng trang>

### Những điểm còn mỏng (Thin spots)
<các trang được tham chiếu nhiều hơn mức độ sâu nội dung hiện có của chúng>

### Tiếp theo (Next)
1. <hành động cụ thể gắn với một trang>
2.
3.
```

## Hiệu chuẩn (Calibration)

Những bản tổng kết liệt kê tất tần tật mọi thứ sẽ chỉ được đọc lướt qua rồi bị phớt lờ. Hãy giữ độ dài dưới một trang. Chỉ đưa ra đúng ba khuyến nghị, không phải mười. Nếu cả một tuần qua không có gì đáng báo cáo, hãy nói gọn điều đó trong một dòng thay vì cố nặn ra những nhận định sáo rỗng.
