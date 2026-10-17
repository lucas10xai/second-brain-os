# GraphRAG và vị trí của nó

`GraphRAG` là phương pháp xây dựng một đồ thị từ kho dữ liệu trước, sau đó trả lời các câu hỏi dựa trên đồ thị đó thay vì dựa trên các phân đoạn văn bản thô (raw chunks). Microsoft Research đã công bố phiên bản nổi tiếng nhất của phương pháp này trong bài báo *"From Local to Global: A Graph RAG Approach to Query-Focused Summarization"*.

Quy trình tổng quát: trích xuất các thực thể và mối quan hệ từ mọi tài liệu, xây dựng đồ thị, phát hiện các cộng đồng (communities) gồm những thực thể kết nối dày đặc với nhau, tóm tắt từng cộng đồng, và trả lời câu hỏi bằng cách dựa trên các bản tóm tắt cộng đồng đó thay vì dựa trên các đoạn văn bản được truy xuất riêng lẻ.

## Tại sao phương pháp này tồn tại

Nó nhắm vào một điểm yếu cụ thể của việc truy xuất theo phân đoạn (chunk retrieval): những câu hỏi về toàn bộ kho dữ liệu nói chung. Câu hỏi kiểu *"Những chủ đề chính ở đây là gì?"* không thể được trả lời bằng cách lấy ra năm phân đoạn có độ tương đồng cao nhất, bởi vì chẳng có phân đoạn đơn lẻ nào chứa câu trả lời cả. Câu trả lời phải được lắp ghép từ tất cả mọi thứ.

Nhóm câu hỏi đó chính xác là những gì mọi người mong muốn ở một `Second Brain`, và cũng chính xác là thứ mà tìm kiếm tương đồng (similarity search) làm tệ nhất.

## Những gì Vault của bạn đã có sẵn

Hãy đọc lại quy trình trên và đối chiếu với một `wiki/` được duy trì tốt: hầu hết các thành phần đó thực chất đã được xây dựng sẵn rồi.

Trích xuất thực thể chính là việc quá trình `Ingest` làm khi nó viết ra các trang thực thể (entity pages). Các mối quan hệ chính là các `Wikilink`, kèm theo kiểu quan hệ nếu bạn có sử dụng liên kết định kiểu. Đồ thị chính là `Vault` của bạn. Thứ duy nhất còn thiếu là tầng cộng đồng: việc tự động phát hiện các cụm (clusters) và viết bản tóm tắt bao quát lên chúng.

Và mảnh ghép còn thiếu đó thực ra đã có một phiên bản thủ công tương đương mà bạn vốn đang viết hàng ngày. Các trang tổng hợp (synthesis pages) chính là các bản tóm tắt cộng đồng, được tạo ra bởi một mô hình đã đọc trực tiếp các tài liệu nguồn thay vì bởi một thuật toán gom cụm các thực thể.

## Có nên chạy GraphRAG hay không

Có lẽ là không, ở quy mô cá nhân, và lý do thẳng thắn nhất là vì kích thước dữ liệu. Phương pháp này chỉ bù đắp được chi phí của nó trên những kho dữ liệu quá lớn không thể biên tập thủ công. Vài nghìn trang đã được biên tập kỹ lưỡng với các liên kết thực sự thì không cần đến thuật toán phát hiện cộng đồng tự động mới tìm ra được chủ đề của chúng; bạn hoàn toàn có thể nhìn thấy các cụm đó ngay trên chế độ xem đồ thị (graph view).

Tuy nhiên, có một trường hợp đáng để dùng nó như một công cụ kiểm toán (audit) hơn là một hệ thống truy xuất. Việc chạy thuật toán phát hiện cộng đồng trên đồ thị đã xuất ra của bạn và so sánh các cụm do thuật toán tìm được với các trang tổng hợp hiện có sẽ cho bạn biết những nơi nào trong `Vault` đang hình thành các chủ đề lớn mà bạn chưa nhận ra. Đó là một bài tập nên làm mỗi quý một lần, chứ không phải là hạ tầng chạy thường trực.

## Các nghiên cứu liên quan đáng đọc

**HippoRAG** áp dụng thuật toán Personalized PageRank trên một `Knowledge graph` để giải quyết các câu hỏi đa bước nhảy (multi-hop questions) — đây là một mô hình tương đồng trực tiếp hơn nhiều với cách một `Agent` lần theo các liên kết tỏa ra từ một trang khởi đầu.

Hãy đọc trực tiếp các bài báo khoa học gốc thay vì chỉ đọc bản tóm tắt của chúng. Cả hai nghiên cứu đều nêu rất cụ thể những điều kiện mà tại đó kết quả của họ có giá trị, và chính những điều kiện đó mới là yếu tố quyết định liệu phương pháp này có áp dụng được vào tình huống của bạn hay không.

## Tiếp theo

[Xuất dữ liệu đồ thị](exporting-your-graph.md)
