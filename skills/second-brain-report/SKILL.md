---
name: second-brain-report
description: >-
  Tạo một bản báo cáo nghiên cứu từ dữ liệu trong vault: đối chiếu phạm vi câu hỏi
  với các trang hiện có, chỉ rõ những khoảng trống thông tin, và viết các phát hiện
  kèm theo trích dẫn, điểm bất đồng và giới hạn của báo cáo. Sử dụng kỹ năng này khi
  người dùng yêu cầu một báo cáo nghiên cứu, một bài tổng hợp chuyên sâu về một chủ đề,
  hoặc muốn hiểu thấu đáo một vấn đề dựa trên những tư liệu họ đã thu thập. KHÔNG dùng
  để trả lời nhanh một câu hỏi từ vault, soạn thảo bài viết theo văn phong cá nhân của
  người dùng, hoặc tóm tắt một tài liệu nguồn đơn lẻ.
---

# Viết báo cáo nghiên cứu (Write a research report)

Một bản báo cáo chỉ trình bày toàn những kết luận tìm được trông có vẻ thuyết phục hơn nhưng thực chất lại ít hữu ích hơn, bởi vì người đọc không thể phân biệt được đâu là phần có nền tảng bằng chứng vững chắc và đâu là phần đang rất mỏng.

## Quy tắc cốt lõi

Định hình phạm vi dựa trên những gì có trong vault trước tiên. Phần lớn giá trị của một báo cáo tốt nằm ở việc biết rõ những gì bạn không cần phải đi tra cứu lại từ đầu.

## Quy trình thực hiện

1. **Kiểm kê những gì hiện có.** Những trang nào đang bao phủ chủ đề này, phần nào còn mỏng, phần nào hoàn toàn chưa có. Câu trả lời cho bước này chính là kế hoạch nghiên cứu.
2. **Báo cáo các khoảng trống trước khi bắt đầu viết,** để người dùng có thể quyết định xem có nên nạp (ingest) thêm tài liệu trước hay không.
3. **Viết từ các trang wiki và trích dẫn rõ trang.** Mọi luận điểm đều phải truy nguyên được về một trang nguồn có gắn URL gốc phía sau.
4. **Ghi nhận sự bất đồng** ở những nơi các tài liệu nguồn mâu thuẫn nhau, kèm theo mốc thời gian và ai nói gì.
5. **Nêu rõ những gì chưa thể xác lập được** và bằng chứng nào sẽ làm thay đổi kết luận hiện tại.
6. **Lưu vào thư mục `output/`** và đề xuất nạp ngược báo cáo này vào lại wiki như một tài liệu nguồn.

## Định dạng đầu ra

```
## Câu hỏi nghiên cứu (Question)
## Những gì vault đã bao phủ (What the vault covers - kèm trích dẫn [[trang]])
## Điểm bất đồng giữa các nguồn (Where sources disagree)
## Những gì chưa thể xác lập (What I could not establish)
## Điều gì sẽ làm thay đổi kết luận này (What would change this)
## Các trang đã đọc (Pages read): <danh sách>
```

## Hiệu chuẩn (Calibration)

Nếu dữ liệu trong vault chỉ mới bao phủ được chưa đầy một nửa câu hỏi, hãy nói rõ điều đó ngay ở phần mở đầu thay vì cố viết ra một bản báo cáo đọc qua tưởng như đã đầy đủ.

Không bao giờ tự lấp đầy khoảng trống bằng kiến thức phổ thông bên ngoài mà không gắn nhãn rõ ràng là nằm ngoài vault. Một bản báo cáo dài mà không thể kiểm chứng được nguồn trích dẫn thì có giá trị thấp hơn nhiều so với một bản báo cáo ngắn nhưng kiểm chứng được từng dòng.
