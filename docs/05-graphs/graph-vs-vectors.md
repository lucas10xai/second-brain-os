# Đồ thị và Embeddings

Lời khuyên phổ biến nhất khi bạn muốn đặt câu hỏi trên tập tài liệu của chính mình là tạo `Embeddings` cho chúng và truy xuất theo độ tương đồng (similarity). Hướng dẫn này không làm theo cách đó, và lý do đằng sau rất đáng để hiểu tường tận thay vì chỉ tin theo một cách mù quáng.

## Thế mạnh của từng phương pháp

**`Embeddings`** tìm ra những đoạn văn bản có ý nghĩa tương tự với câu truy vấn của bạn, kể cả khi cách dùng từ hoàn toàn khác biệt. Chúng rất mạnh về độ phủ (recall), không đòi hỏi cấu trúc từ trước, và hoạt động tốt trên một đống tài liệu hỗn độn mà bạn chưa từng sắp xếp.

**Đồ thị (Graph)** tìm ra những thứ được kết nối tường minh với nhau, theo một hướng mà bạn có thể lần theo được, kèm theo lý do rõ ràng nếu các liên kết được định kiểu. Nó rất mạnh đối với các câu hỏi đa bước nhảy (multi-hop questions) và trong việc giải thích *tại sao* hai thứ lại liên quan đến nhau.

## Nơi độ tương đồng (Similarity) thất bại

Điểm yếu của nó rất cụ thể: tìm kiếm theo độ tương đồng sẽ truy xuất ra các phân đoạn (chunks) giống với câu hỏi, trong khi câu trả lời cho một câu hỏi hay thường lại chẳng hề giống với câu hỏi đó chút nào.

Hãy thử hỏi điều gì kết nối hai ý tưởng với nhau: những đoạn văn thiết lập mối liên kết đó có thể chẳng chia sẻ chung bất kỳ từ vựng nào với cả hai ý tưởng kia. Hãy thử hỏi bạn đã thay đổi quan điểm về vấn đề gì: sẽ chẳng có phân đoạn văn bản nào tương đồng với câu hỏi đó cả, bởi vì câu trả lời nằm ở mối quan hệ giữa hai trang được viết cách nhau một năm trời.

Ngoài ra còn có bài toán xếp hạng (ranking). Hai mươi phân đoạn trả lời nửa vời sẽ chèn ép và đẩy văng một trang duy nhất trả lời trọn vẹn câu hỏi, bởi vì độ tương đồng `Vector` hoàn toàn không có khái niệm về tính hoàn chỉnh.

## Nơi đồ thị thất bại

Độ phủ (Recall). Nếu một trang chưa bao giờ được liên kết, đồ thị không thể nào chạm tới nó, và các quy tắc liên kết lại chính là thứ âm thầm xuống cấp khi quá trình `Ingest` trở nên cẩu thả.

Đồ thị cũng không thể tìm ra thứ mà bạn chỉ nhớ mang máng nhưng không thể gọi tên. Đó là bài toán tìm kiếm (search), và tìm kiếm toàn văn (full-text search) trên một `Vault` vài nghìn trang cho kết quả tức thì — đó là lý do trên thực tế `ripgrep` đã giải quyết gọn hầu hết nhu cầu này.

## Tại sao một Vault cá nhân nên nghiêng về đồ thị

Có ba lý do đặc thù ở quy mô này.

Kho dữ liệu (corpus) của bạn nhỏ. Vài nghìn trang không phải là một bài toán truy xuất quy mô lớn, nó chỉ là một thư mục trên máy tính. Hạ tầng mà `Embeddings` đòi hỏi chỉ thực sự sinh lời ở quy mô hàng triệu tài liệu, và dưới ngưỡng đó thì chi phí duy trì lớn hơn nhiều so với lợi ích mang lại.

Kho dữ liệu của bạn vốn đã được phân đoạn (chunked) sẵn rồi. Các trang nguyên tử (atomic pages) chính là những đơn vị ngữ nghĩa được viết ra bởi một thực thể thực sự hiểu chúng. Việc cắt nhỏ chúng một lần nữa thành các phân đoạn có kích thước cố định (fixed-size chunks) sẽ phá hủy toàn bộ cấu trúc mà bạn đã dày công tạo dựng.

Các câu hỏi của bạn mang tính quan hệ (relational). Tôi biết gì về X, điều gì kết nối X và Y, điều gì phản bác lại Z. Đó bản chất đều là các truy vấn đồ thị.

## Mô hình lai (Hybrid), khi bạn thực sự cần đến

Sự kết hợp hợp lý nhất: dùng tìm kiếm toàn văn hoặc `Embeddings` để tìm các điểm khởi đầu (entry points), sau đó dùng đồ thị để mở rộng ra xung quanh từ các điểm đó.

Bằng cách đó, độ phủ (recall) đến từ công cụ tìm kiếm còn cấu trúc đến từ đồ thị — mỗi bên làm đúng phần việc sở trường của mình. Xem thêm [bổ sung RAG khi bạn thực sự cần](../07-retrieval/rag-on-top.md) để biết ngưỡng quy mô nào thì việc đầu tư công sức bảo trì hệ thống này bắt đầu trở nên xứng đáng.

## Tiếp theo

[GraphRAG và vị trí của nó](graphrag.md)
