# Agent viết ra nội dung rác

Những trang về mặt kỹ thuật thì đúng chủ đề đấy, nhưng đọc vào lại chẳng có chút giá trị nào.

## Chẩn đoán tài liệu nguồn trước tiên

Trước khi sửa đổi các chỉ dẫn, hãy kiểm tra dữ liệu đầu vào. Hãy mở file tương ứng trong `raw/` và đọc thử nó.

Một nửa số trang chất lượng kém mà người dùng đổ lỗi cho Agent thực chất bắt nguồn từ khâu trích xuất văn bản tồi: một file PDF bị trộn lẫn các cột văn bản vào nhau, một bản Transcripts phụ đề tự động không hề có dấu câu, hay một trang lưu qua Web Clipper chỉ chụp được mỗi khung thông báo cookie thay vì nội dung bài viết.

Agent không thể viết ra một trang tốt từ một đoạn văn bản bị băm nát, và nó cũng sẽ không báo cho bạn biết là nó đang phải vật lộn với dữ liệu hỏng đâu. Xem thêm hướng dẫn xử lý [PDF và sách](../03-ingestion/pdfs-and-books.md) cùng [Transcripts từ YouTube](../03-ingestion/youtube-transcripts.md).

## Sau đó kiểm tra CLAUDE.md

Nếu tài liệu nguồn đã sạch sẽ, vấn đề nằm ở quy ước trang (page contract).

Những nguyên nhân cụ thể tạo ra các trang viết mơ hồ, chung chung gồm: không định nghĩa rõ mỗi loại trang cần chứa những gì, xuất hiện từ "tóm tắt" (summarise) ở bất kỳ đâu trong chỉ dẫn, không yêu cầu viết cho một người đọc chưa từng xem tài liệu gốc, và không bắt buộc phải gắn liên kết.

Hãy viết lại quy ước trang với cấu trúc được quy định rõ ràng từng phần. Xem thêm [các loại trang](../04-structuring/page-types.md).

## Thêm một ví dụ mẫu, thay vì thêm một quy tắc mới

Đây là cách khắc phục có đòn bẩy cao nhất nhưng lại ít được sử dụng nhất. Hãy đưa nguyên văn một trang khái niệm mẫu mực vào trong `CLAUDE.md` để làm đích nhắm chuẩn.

Các quy tắc chỉ mô tả kết quả đầu ra một cách trừu tượng, và mỗi quy tắc mới thêm vào lại va chạm với các quy tắc cũ. Một ví dụ cụ thể sẽ truyền tải trực tiếp hình mẫu mong muốn — và đó cũng chính là thứ một người bình thường sẽ hỏi xin nếu bạn yêu cầu họ viết theo một văn phong nhất định.

## Hỏi xem Agent đã dựa vào đâu để viết

```
Bạn đã viết trang [[page]]. Bạn đã sử dụng những phần nào trong tài liệu nguồn, và đã bỏ qua những phần nào?
```

Câu trả lời thường chỉ ra ngay nguyên nhân cốt lõi: hoặc là nó chỉ đọc được một mảnh nhỏ của tài liệu, hoặc nó không phân biệt được đâu là nhận định của tác giả gốc so với thông tin trích dẫn lại, hoặc các chỉ dẫn đã kéo nó về hướng viết tóm tắt chung chung.

## Hoàn tác và chạy lại

Sửa lại quy ước trang, hoàn tác các trang viết hỏng, rồi chạy Ingest lại từ đầu.

```bash
git checkout HEAD~1 -- wiki/
```

Đừng tự tay ngồi vá lại từng trang hỏng. Nếu quy ước trang đã sai, thì mọi trang sinh ra từ lượt chạy đó đều mắc chung một khuyết điểm, và việc sửa thủ công ba trang bạn tình cờ thấy sẽ bỏ sót toàn bộ phần còn lại.

## Tiếp theo

[Liên kết gãy và các trang mồ côi](broken-links.md)
