# Wiki so với RAG

Lời khuyên mặc định phổ biến mỗi khi bạn muốn đặt câu hỏi trên kho tài liệu cá nhân là hãy tạo Embeddings cho chúng và đưa vào một cơ sở dữ liệu Vector. Cẩm nang này chọn một hướng đi khác hẳn, và lý do nằm ở bản chất cấu trúc dữ liệu chứ không chỉ là sở thích chọn công cụ.

## Hai hướng tiếp cận

**RAG** lưu trữ tài liệu của bạn dưới dạng các đoạn văn bản cắt nhỏ (chunks) kèm theo Vector Embeddings. Khi có câu hỏi, hệ thống tìm ra những đoạn có độ tương đồng cao nhất và mô hình AI sẽ dựa vào đó để trả lời. Không có gì mới được viết ra; kho dữ liệu gốc vẫn giữ nguyên trạng thái ban đầu.

**Một hệ thống Wiki** xử lý tài liệu một lần duy nhất, biến chúng thành các trang được Agent biên soạn và liên kết chặt chẽ với nhau. Các câu hỏi được trả lời bằng cách điều hướng qua mạng lưới các trang đó. Kho dữ liệu được chuyển hóa về chất và liên tục hoàn thiện hơn theo thời gian.

Sự khác biệt cốt lõi nằm ở thời điểm thực hiện công việc xử lý. RAG thực hiện xử lý tại thời điểm truy vấn (query time), lặp lại từ đầu trong mọi lần hỏi. Trong khi đó, hệ thống Wiki thực hiện xử lý một lần ngay tại thời điểm nạp dữ liệu (`Ingest`), và thành quả đó được tái sử dụng mãi về sau.

## Lợi ích mang lại

**Sự thấu hiểu được tích lũy cộng dồn.** Nguồn tài liệu thứ mười về cùng một chủ đề sẽ làm giàu thêm cho trang khái niệm mà chín nguồn trước đó đã xây dựng nên. Còn trong hệ thống RAG, tài liệu thứ mười chỉ đơn thuần tạo ra thêm vài đoạn văn bản rời rạc khác — chất lượng kho tri thức không hề tốt lên khi quy mô mở rộng, nó chỉ phình to hơn mà thôi.

**Các mâu thuẫn được phơi bày rõ ràng.** Hai tài liệu bất đồng quan điểm trong RAG sẽ nằm ở hai đoạn văn bản rời nhau và có thể chẳng bao giờ được truy xuất lên cùng một lúc. Ngược lại, trên một trang wiki, sự bất đồng đó được ghi chép rõ ràng cạnh nhau, có ngày tháng cụ thể và không thể bị bỏ sót.

**Câu trả lời có thể kiểm chứng được.** Trang wiki trích dẫn trực tiếp các nguồn tài liệu mà bạn có thể nhấp vào mở xem ngay. Trong khi các đoạn văn bản truy xuất từ RAG chỉ là những mảnh cắt vụn thiếu đi mạch lập luận kết nối chúng lại với nhau.

**Không tốn hạ tầng phức tạp.** Không cần duy trì chỉ mục Vector, không cần chạy tạo lại Embeddings (re-embedding), và không bao giờ xảy ra tình trạng lệch dữ liệu giữa cơ sở dữ liệu Vector với các file thực tế trên ổ cứng.

## Chi phí đánh đổi

**Khâu Ingest tốn kém hơn.** Việc biên soạn và liên kết các trang tiêu tốn thời gian suy luận của mô hình AI ngay từ đầu, trong khi khâu nạp dữ liệu của RAG gần như không tốn gì.

**Chất lượng phụ thuộc chặt vào quy trình Ingest.** Một bản hợp đồng định dạng trang (page contract) sơ sài sẽ tạo ra một Vault kém chất lượng mà phải một thời gian sau bạn mới nhận ra. Ngược lại, các điểm yếu của RAG bộc lộ ngay tại thời điểm truy vấn nên dễ nhận thấy hơn.

**Độ phủ truy xuất (Recall) phụ thuộc vào liên kết.** Một trang không được ai liên kết tới sẽ trở thành vùng mù mà đồ thị không thể chạm tới được. Trong khi đó, RAG vẫn có thể tìm ra nó nhờ phép đo độ tương đồng ngữ nghĩa.

## Góc nhìn thực tế và công tâm

Sự đánh đổi này hoàn toàn đúng đắn đối với một kho tư liệu cá nhân có chọn lọc gồm vài nghìn trang, nhưng sẽ là sai lầm nếu áp dụng cho một kho dữ liệu gồm hàng triệu tài liệu thô chưa ai từng biên tập.

Nói cách khác, mô hình Wiki là lựa chọn chuẩn xác cho một Second Brain nhưng lại không phù hợp để làm một sản phẩm máy tìm kiếm đại chúng — và hầu hết các lời khuyên về RAG hiện nay đều được viết cho bài toán thứ hai. Hãy xem bài [Bổ sung RAG khi thực sự cần thiết](../07-retrieval/rag-on-top.md) để biết ngưỡng quy mô mà tại đó cán cân đảo chiều, và bài [Đồ thị so với Embeddings](../05-graphs/graph-vs-vectors.md) để hiểu sâu về cơ chế kỹ thuật khi truy xuất.

## Tiếp theo

[Thế nào là một hệ thống vận hành tốt](what-good-looks-like.md)
