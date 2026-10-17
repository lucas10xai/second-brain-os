# PDF, bài báo khoa học và sách

PDF là định dạng dễ biến thành đống rác văn bản nhất khi đưa vào Vault của bạn. Bố cục hai cột bị trộn lẫn dòng nọ xọ dòng kia, bảng biểu vỡ vụn, chú thích chân trang nhảy vào giữa câu văn, và thế là Agent cứ thế âm thầm xây dựng các trang wiki bên trên mớ hỗn độn đó.

Hãy luôn kiểm tra chất lượng văn bản trích xuất trước khi chạy Ingest. Việc này chỉ mất đúng mười giây nhưng giúp bạn tránh phải ngồi viết lại hàng loạt trang wiki về sau.

## Trích xuất văn bản từ PDF

```bash
# text, layout preserved reasonably well
pdftotext -layout paper.pdf raw/paper.md
```

Đối với những tài liệu có cấu trúc phức tạp, thư viện `pymupdf` mang lại khả năng kiểm soát tốt hơn và có thể tách riêng hình ảnh cũng như bảng biểu. Dù sử dụng công cụ nào, bạn cũng hãy mở file kết quả lên và đọc thử một đoạn văn nằm ở giữa tài liệu. Nếu câu chữ bị đứt gãy không liền mạch, hãy sửa lại khâu trích xuất ngay thay vì hy vọng Agent sẽ tự xoay xở được.

## Tài liệu bản quét (Scanned documents)

Một tài liệu quét thực chất chỉ là một tệp hình ảnh, nên các công cụ trích xuất văn bản thông thường sẽ trả về kết quả trống rỗng. Hãy chạy nhận diện ký tự quang học (OCR) trước bằng công cụ `ocrmypdf` để gắn thêm một lớp văn bản vào file mà không làm thay đổi hình ảnh hiển thị gốc. Hãy lường trước việc OCR sẽ nhận diện sai một số tên riêng và con số, đồng thời coi mọi số liệu lấy từ nguồn tài liệu quét là thông tin cần kiểm chứng lại trước khi đưa vào trang wiki như một sự thật hiển nhiên.

## Bài báo khoa học (Papers)

Các bài báo khoa học cần được xử lý theo cách khác với những bài viết thông thường trên mạng, bởi những thông tin bạn cần tra cứu lại về sau không phân bổ đều khắp bài. Phần tóm tắt (abstract), phương pháp nghiên cứu (method), kết quả (results) và giới hạn nghiên cứu (limitations) là nơi chứa đựng gần như toàn bộ giá trị cốt lõi.

Một câu lệnh chỉ dẫn Ingest hiệu quả cho bài báo khoa học:

```
This is an academic paper. Build the source page around: the question it asks,
the method, the result with its actual numbers, and the limitations the authors
state themselves. Record sample sizes. Do not report a finding without the
condition it holds under.
```

Quy tắc cuối cùng trong đoạn lệnh trên chính là chốt chặn giữ cho hệ thống wiki luôn trung thực. Những kết luận khoa học bị tước bỏ mất điều kiện áp dụng sẽ biến thành những lời khẳng định sai lệch đầy tự tin sau hai năm lưu trữ.

Nếu bạn đọc bài báo khoa học thường xuyên, Zotero là công cụ rất đáng sử dụng. Nó quản lý siêu dữ liệu (metadata) cực tốt và hỗ trợ xuất ra file Markdown gọn gàng để đưa thẳng vào `raw/`.

## Sách

Một cuốn sách nguyên vẹn là quá lớn để Ingest như một nguồn tài liệu đơn lẻ và phần lớn trường hợp cũng không đáng làm vậy. Thứ thực sự đáng đưa vào hệ thống chính là các đoạn tô sáng (highlights) của bạn.

Các đoạn highlight trên Kindle có thể xuất ra từ ứng dụng Kindle hoặc thông qua Readwise — dịch vụ hỗ trợ đồng bộ trực tiếp vào thẳng Obsidian. Dữ liệu highlight sẽ được đưa về dưới dạng danh sách các đoạn trích dẫn, vì vậy hãy Ingest mỗi cuốn sách thành một trang nguồn duy nhất, và để Agent xây dựng các trang khái niệm dựa trên những ý tưởng cốt lõi thay vì chỉ bám vào câu chữ trích dẫn.

Hãy giữ cho các đoạn trích dẫn nguyên văn trên trang wiki thật ngắn gọn và luôn ghi kèm nguồn trích dẫn. Một trang wiki chép lại nguyên xi nửa chương sách vừa vi phạm bản quyền, vừa gây cản trở cho việc truy xuất thông tin sau này.

## Biểu đồ và bảng biểu

Quá trình trích xuất văn bản thuần túy sẽ làm mất cả biểu đồ lẫn bảng biểu. Khi một biểu đồ nắm giữ luận điểm quan trọng của bài viết, hãy chụp ảnh màn hình biểu đồ đó lưu vào `raw/assets/` và đặt liên kết tham chiếu tới nó từ trang nguồn, để nhận định ghi trên trang wiki luôn có bằng chứng trực quan đi kèm.

## Tiếp theo

[Lịch sử trò chuyện AI (Chat exports)](chat-exports.md)
