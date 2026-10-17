---
name: second-brain-project
description: >-
  Thiết lập hoặc cập nhật một dự án bên trong vault: quy trình thư mục bốn giai đoạn,
  file CLAUDE.md khoanh vùng riêng cho dự án với một mục tiêu duy nhất, và các liên
  kết tới những trang khái niệm mà dự án phụ thuộc vào. Sử dụng kỹ năng này khi người
  dùng bắt đầu một công việc mới kéo dài theo thời gian, nói "tạo một dự án", "thiết lập
  thư mục cho X", hoặc yêu cầu xác định mục tiêu và cấu trúc cho công việc đang triển khai.
  KHÔNG dùng cho các tác vụ làm một lần rồi xong, các trang wiki tìm hiểu về một chủ đề,
  hoặc để thu hẹp phạm vi của một dự án sẵn có khi đang làm việc bên trong nó.
---

# Thiết lập một dự án (Set up a project)

Tầng tri thức (knowledge layer) trả lời câu hỏi bạn biết những gì. Tầng dự án (project layer) trả lời câu hỏi tuần này bạn đang làm gì. Việc trộn lẫn hai tầng này sẽ làm đầy wiki bằng những danh sách công việc đã chết và chôn vùi các file đang làm việc dở dang dưới hàng núi ghi chú khái niệm.

## Quy tắc cốt lõi

Mỗi dự án một mục tiêu duy nhất, được phát biểu rõ trong file `CLAUDE.md` của riêng dự án đó. Một dự án có ba mục tiêu thực chất là ba dự án khác nhau.

## Quy trình thực hiện

1. **Phỏng vấn ngắn nếu cần.** Dự án này tạo ra sản phẩm gì, dành cho ai, hạn chót là khi nào, và vai trò của agent là gì. Những câu trả lời mơ hồ sẽ tạo ra một file chỉ dẫn làm hỏng mọi phiên làm việc về sau.
2. **Tạo bộ thư mục bốn giai đoạn:** `Inputs/`, `Process/`, `Outputs/`, `Feedback/`.
3. **Viết file `CLAUDE.md` của dự án:** dự án này là gì, mục tiêu duy nhất kèm mốc thời gian, vai trò của bạn, quy tắc làm việc, và trạng thái hiện tại. Hãy nêu rõ cả những việc agent không được làm tại đây.
4. **Liên kết với tầng tri thức.** Tìm các trang khái niệm (`concept`) mà dự án phụ thuộc vào và tham chiếu chúng từ file dự án. Chỉ sao chép vào `Inputs/` một vài trang thực sự cốt lõi nhất.
5. **Đăng ký dự án** vào danh sách dự án trong file `CLAUDE.md` ở thư mục gốc của vault.

## Định dạng đầu ra

```
Project: <tên dự án>
Goal: <một kết quả đầu ra đo lường được kèm mốc thời gian>
Folders created: Inputs, Process, Outputs, Feedback
Concept pages linked: <danh sách>
Agent role: <một dòng mô tả>
```

## Hiệu chuẩn (Calibration)

`Feedback/` là thư mục mọi người thường bỏ qua nhưng lại chính là nơi giúp hệ thống ngày càng tốt lên. Nếu người dùng hoàn toàn không hình dung được sẽ bỏ gì vào thư mục đó, hãy nêu rõ vấn đề này ra: điều đó thường có nghĩa là mục tiêu của dự án vẫn chưa thể đo lường được.

Đừng tạo một dự án cho công việc chỉ làm trong tuần này là xong. Đó là một tác vụ đơn lẻ (task).
