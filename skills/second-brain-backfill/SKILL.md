---
name: second-brain-backfill
description: >-
  Nhập một kho lưu trữ lớn vào vault theo từng lô được kiểm soát chặt chẽ:
  sàng lọc những gì đáng nạp, xử lý từ cũ nhất trước, lưu điểm kiểm tra (checkpoint)
  sau mỗi lô, và giữ cho chi phí luôn minh bạch. Sử dụng kỹ năng này bất cứ khi nào
  người dùng muốn nhập hàng năm trời dấu trang (bookmarks), bản xuất dữ liệu từ
  ứng dụng ghi chú khác, thư mục tải về, kho lịch sử trò chuyện, hoặc khi họ nói
  "backfill", "nhập hàng loạt", "xử lý kho lưu trữ của tôi". KHÔNG dùng để nạp một
  hoặc vài nguồn mới đơn lẻ — việc đó thuộc về second-brain-ingest.
---

# Nhập bổ sung một kho lưu trữ (Backfill an archive)

Nhập bổ sung hàng loạt (backfill) là nơi cả chi phí lẫn chất lượng đều rất dễ âm thầm chệch hướng. Nếu làm sai thứ tự thời gian, nó còn làm đảo ngược lịch sử nhận thức của vault, bởi vì các tài liệu nguồn đến sau lẽ ra phải cập nhật những trang do các tài liệu nguồn đến trước tạo nên.

## Quy tắc cốt lõi

Cũ nhất làm trước, mười nguồn mỗi lô, dừng lại chờ phê duyệt giữa các lô.

## Quy trình thực hiện

1. **Sàng lọc trước khi nạp.** Đọc tiêu đề và các đoạn văn đầu tiên. Phân loại thành ba nhóm: đáng nạp vào wiki (`worth-ingesting`), chỉ giữ lại trong `raw/` (`keep-in-raw`), và xóa bỏ (`delete`). Hầu hết các kho lưu trữ cũ có tới một nửa là liên kết chết hoặc những thứ lưu về nhưng chưa bao giờ mở ra đọc.
2. **Sắp xếp theo ngày tháng, cũ nhất trước.** Nếu chạy theo chiều ngược lại, mọi tài liệu cũ được nạp vào sau sẽ xuất hiện như một sự mâu thuẫn đối với một trang vốn đã có sẵn câu trả lời hoàn chỉnh cuối cùng.
3. **Chạy theo lô mười nguồn.** Nạp từng nguồn tuân theo đúng kỹ năng `second-brain-ingest`.
4. **Lưu điểm kiểm tra (Checkpoint):** cập nhật `index.md`, ghi nối tiếp vào `log.md`, tạo git commit có ghi rõ khoảng thứ tự lô trong thông điệp commit, và báo cáo các con số thống kê.
5. **Dừng lại và chờ xác nhận** trước khi chuyển sang lô tiếp theo.
6. **Chạy kiểm lỗi (lint) toàn diện ở cuối quy trình.** Các đợt nhập dữ liệu lớn luôn để lại các trang mồ côi (orphans) và các trang trùng lặp.

## Định dạng đầu ra

```
Batch <n>/<total>: <khoảng thời gian hoặc thứ tự>
Ingested: <n> nguồn -> <n> trang mới, <n> trang cập nhật, <n> liên kết
Skipped: <n> (lý do)
Running total: <n> trên <n>
Next batch: <nội dung lô tiếp theo>
```

## Hiệu chuẩn (Calibration)

Hãy đọc kỹ từng trang mà lô đầu tiên tạo ra, không bỏ sót trang nào. Một lỗi nhỏ bạn để lọt ở lô số một sẽ nhân bản thành lỗi trên bốn trăm trang khi kết thúc, và chi phí sửa lại sau đó sẽ đắt hơn cả lần chạy ban đầu.

Nếu kho lưu trữ có hơn khoảng hai trăm nguồn, hãy đề xuất một bộ lọc trước khi bắt đầu thay vì chỉ báo giá toàn bộ chi phí chạy.
