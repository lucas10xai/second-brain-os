---
name: second-brain-lint
description: >-
  Kiểm toán vault bộ não thứ hai để tìm các lỗi cấu trúc và sửa chữa chúng:
  wikilink bị gãy, trang mồ côi (orphan pages), trang sơ khai rỗng (empty stubs),
  frontmatter sai quy chuẩn (schema), các trang gần như trùng lặp, và các mục chỉ
  mục bị lệch. Sử dụng kỹ năng này bất cứ khi nào người dùng yêu cầu kiểm lỗi (lint),
  dọn dẹp, kiểm toán hoặc kiểm tra sức khỏe của vault, nói rằng các trang trông lộn
  xộn hoặc liên kết bị hỏng, sau một đợt nhập dữ liệu hàng loạt lớn, hoặc khi đến
  lịch bảo trì định kỳ. KHÔNG dùng để nạp tài liệu nguồn mới, trả lời câu hỏi từ
  vault, hoặc viết lại nội dung những trang có cấu trúc tốt nhưng hành văn chưa hay.
---

# Kiểm lỗi cấu trúc Vault (Lint the vault)

Sự mục ruỗng về cấu trúc diễn ra rất âm thầm. Không có thông báo lỗi, không có gì bị sập, chiếc vault chỉ từ từ mất đi khả năng trả lời câu hỏi một cách hiệu quả bởi vì một phần ba số trang của nó đã không còn đường dẫn tới. Kiểm lỗi (linting) là cách duy nhất phát hiện ra tình trạng này trước khi chủ sở hữu nhận ra.

## Quy tắc cốt lõi

Báo cáo trước khi sửa chữa. Tự động khắc phục các lỗi cơ học, nhưng không bao giờ xóa hoặc gộp một trang mà không liệt kê ra trước và nhận được sự đồng ý rõ ràng, bởi vì rất có thể chủ sở hữu đã tự tay viết trang đó.

## Quy trình thực hiện

1. **Kiểm kê (Inventory).** Đếm số lượng trang theo từng loại (`type`). Xây dựng đồ thị liên kết bằng cách phân tích mọi cú pháp `[[wikilink]]`.
2. **Liên kết gãy (Broken links).** Các liên kết trỏ tới những trang không tồn tại. Hãy phân biệt rõ hai trường hợp: lỗi chính tả hoặc đổi tên trang — trường hợp này bạn tự động sửa; và một khoảng trống kiến thức thực sự (gap) — trường hợp này bạn đưa vào mục `Gaps` trong `index.md`.
3. **Trang mồ côi (Orphans).** Những trang không có bất kỳ liên kết đến (inbound links) nào. Với mỗi trang, hãy tìm nơi phù hợp để đặt liên kết trỏ tới nó, hoặc gắn cờ nó làm ứng viên cần xem xét xóa.
4. **Trang sơ khai (Stubs).** Những trang ngắn dưới khoảng 40 từ và không có liên kết nào. Thường là hậu quả của một lượt nạp (ingest) bị lỗi. Hãy gắn cờ để nạp lại từ tài liệu gốc trong `raw/`.
5. **Quy chuẩn dữ liệu (Schema).** Thiếu hoặc sai định dạng frontmatter, sai giá trị `type`, thiếu ngày tháng, hoặc dùng các thẻ (`tags`) nằm ngoài bộ từ vựng hiện có.
6. **Trang gần như trùng lặp (Near-duplicates).** Những trang có tiêu đề hoặc tên gọi khác (`aliases`) rất giống nhau. Chỉ đề xuất gộp trang; không tự ý thực hiện khi chưa được yêu cầu.
7. **Lệch chỉ mục (Index drift).** Các trang có trong thư mục nhưng thiếu trong `index.md`, hoặc các mục trong `index.md` trỏ tới trang không còn tồn tại.
8. **Sửa chữa**, sau đó ghi nối tiếp lượt chạy vào `log.md`.

## Định dạng đầu ra

```
Vault: <n> trang (<n> sources, <n> concepts, <n> entities, <n> synthesis)
Link graph: <n> liên kết, trung bình <n> liên kết/trang, <n> trang mồ côi

Fixed automatically:
- <danh sách các lỗi cơ học đã tự động sửa>

Needs a decision:
- <danh sách các mục cần quyết định, kèm hành động khuyến nghị cho từng mục>

Health: orphan rate <n>%, broken link rate <n>%, stub rate <n>%
```

## Hiệu chuẩn (Calibration)

Một trình kiểm lỗi quá hung hăng tự ý gộp trang theo phán đoán riêng sẽ phá hỏng công sức tích lũy. Ngược lại, một trình kiểm lỗi quá rụt rè chỉ biết liệt kê sẽ tạo ra một danh sách dài mà chẳng ai buồn động tay vào. Ranh giới phân chia ở trên chính là điểm cân bằng hữu ích: tự động sửa các lỗi cơ học, và đề xuất xin ý kiến cho các quyết định mang tính ngữ nghĩa.

Không chạy kiểm lỗi toàn diện sau mỗi lần nạp đơn lẻ. Chỉ chạy hàng tuần, hoặc sau khi nhập hàng loạt trên hai mươi nguồn tài liệu.
