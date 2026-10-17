---
name: second-brain-ingest
description: >-
  Biến tài liệu nguồn thô trong vault bộ não thứ hai thành các trang wiki được
  liên kết chặt chẽ: đọc tài liệu nguồn, tách thành các khái niệm (concepts) và
  thực thể (entities), viết mới hoặc cập nhật trang, kết nối chúng với các trang
  hiện có, và ghi lại lượt chạy vào nhật ký (log). Sử dụng kỹ năng này bất cứ khi
  nào người dùng thả một file vào raw/, dán một bài viết, bản gỡ băng (transcript)
  hoặc PDF và yêu cầu thêm vào vault, nói "nạp tài liệu này" ("ingest this"),
  "thêm vào bộ não thứ hai", "xử lý thư mục raw", hoặc yêu cầu xử lý nốt các nguồn
  đang chờ, ngay cả khi họ không gọi đích danh lệnh ingest. KHÔNG dùng để trả lời
  câu hỏi từ dữ liệu đã có trong vault, để kiểm lỗi (lint) hay sửa chữa cấu trúc
  trang, hoặc để biên tập các ghi chú do chính người dùng tự tay viết.
---

# Nạp một tài liệu nguồn (Ingest a source)

Một lượt nạp tài liệu mà chỉ viết ra một trang tóm tắt sẽ tạo nên một chiếc vault ngày càng phình to nhưng không hề thông minh hơn. Toàn bộ giá trị nằm ở nửa sau của công việc: kết nối tư liệu mới với những gì đã có sẵn. Một trang được đưa vào mà không có liên kết nào sẽ trở nên vô hình chỉ sau một tuần.

## Quy tắc cốt lõi

Chưa được liên kết nghĩa là chưa hoàn tất nạp (ingest). Mọi lượt chạy đều phải kết thúc với việc các trang mới được kết nối hai chiều với các trang hiện có.

## Quy trình thực hiện

1. **Đọc toàn bộ tài liệu nguồn** trước khi đặt bút viết bất kỳ thứ gì. Việc đọc một phần sẽ tạo ra những trang chỉ được xây dựng từ phần mở đầu — vốn là nơi tài liệu nguồn ít tính cụ thể nhất.
2. **Kiểm tra những gì đã tồn tại.** Tìm kiếm trong wiki các thực thể và khái niệm chính. Nạp tài liệu vào một vault trống rỗng và nạp vào một vault đã có 300 trang là hai công việc hoàn toàn khác nhau: ở trường hợp thứ hai, phần lớn công việc của bạn là cập nhật các trang sẵn có chứ không phải tạo trang mới.
3. **Viết trang nguồn (`source page`)** trong `wiki/sources/`. Ghi nhận các luận điểm đúng dưới dạng luận điểm của nguồn đó, kèm theo thông tin nguồn rõ ràng.
4. **Trích xuất các khái niệm (`concepts`) và thực thể (`entities`).** Mỗi ý tưởng một trang. Nếu trang khái niệm đã tồn tại, hãy bổ sung những gì nguồn mới này đóng góp và cập nhật trường `updated:`. Nếu nó mâu thuẫn với nội dung đang có, hãy ghi nhận cả hai quan điểm thay vì ghi đè.
5. **Liên kết theo cả hai chiều.** Trang nguồn liên kết tới mọi khái niệm và thực thể mà nó chạm tới; và mỗi trang đó lại liên kết ngược về trang nguồn. Tạo các trang đích còn thiếu, hoặc liệt kê chúng vào mục `Gaps` (Khoảng trống) trong `index.md`.
6. **Cập nhật `index.md` và ghi nối tiếp vào `log.md`** ngay trong cùng lượt chạy, bởi vì một trang chỉ mục bị tụt hậu chính là điểm khởi đầu khiến vault bị trôi (drift).
7. **Báo cáo** những gì đã thay đổi.

## Định dạng đầu ra

Kết thúc mọi lượt chạy bằng đúng cấu trúc sau:

```
Ingested: <tên nguồn>
New pages: <n> (danh sách)
Updated pages: <n> (danh sách)
Links added: <n>
Contradictions found: <none | mô tả>
Gaps created: <danh sách các trang được liên kết tới nhưng chưa tồn tại>
```

## Hiệu chuẩn (Calibration)

Trích xuất quá đà (over-extraction) là lỗi phổ biến nhất: đẻ ra mười trang khái niệm mỏng dính từ một bài viết duy nhất, mỗi trang chỉ là một đoạn văn viết lại. Một tài liệu nguồn thông thường chỉ mang lại từ một đến ba khái niệm thực sự xứng đáng có trang riêng. Nếu một khái niệm ứng viên không thể giải thích độc lập mà cứ phải chiếu ngược về đúng một nguồn này mới hiểu được, thì nó thuộc về bên trong trang nguồn đó chứ không phải một trang riêng.

Trích xuất quá ít (under-extraction) biểu hiện dưới dạng các trang nguồn ôm đồm ba ý tưởng tách biệt nhau và chẳng liên kết tới đâu cả. Nếu một trang cần tới các tiêu đề mục cho những chủ đề không liên quan đến nhau, hãy tách nó ra.

## Ví dụ

Đầu vào: người dùng thả file `raw/karpathy-llm-wiki.md` (một bản gist lưu về) vào một chiếc vault vốn đã có sẵn trang `[[Obsidian]]` và `[[Claude Code]]`.

Đầu ra: một trang nguồn; một trang khái niệm mới `[[LLM wiki]]` giải thích khuôn mẫu này bằng ngôn ngữ giản dị; một trang thực thể `[[Andrej Karpathy]]`; cập nhật hai trang `[[Obsidian]]` và `[[Claude Code]]` để ghi nhận vai trò của chúng trong khuôn mẫu này; một liên kết từ trang khái niệm sẵn có `[[Personal knowledge management]]` trỏ tới trang mới; cập nhật `index.md` và `log.md`; báo cáo hiển thị 3 trang mới, 3 trang cập nhật, 11 liên kết.
