# Bài báo khoa học (Papers)

Các công trình nghiên cứu liên quan trực tiếp đến cách một cơ sở tri thức thực hiện truy xuất và suy luận. Hãy đọc những bài báo này nếu bạn muốn tự mình quyết định xem liệu mình có thực sự cần đến một cơ sở dữ liệu vector hay không.

## GraphRAG

**[From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)**. (arXiv:2404.16130) Edge, Trinh, Cheng, Bradley, Chao, Mody, Truitt, Metropolitansky, Ness, Larson. Microsoft Research. Mã nguồn hiện thực tại [microsoft/graphrag](https://github.com/microsoft/graphrag).

Bài báo đã đặt tên cho phương pháp tiếp cận này. Lập luận của bài báo rất cụ thể và đáng để nắm thật chuẩn xác: `RAG` truyền thống thất bại trước các câu hỏi toàn cục (global questions) về toàn bộ kho dữ liệu — chẳng hạn như các chủ đề chính xuyên suốt là gì — bởi vì đó là một tác vụ tóm tắt chứ không phải tác vụ truy xuất. Đường ống xử lý của họ trích xuất một đồ thị thực thể từ tập tài liệu, sinh trước các bản tóm tắt cho từng cộng đồng gồm các thực thể có liên hệ mật thiết, rồi trả lời các câu hỏi toàn cục dựa trên những bản tóm tắt đó.

Nghiên cứu này đặc biệt liên quan đến bộ não thứ hai bởi vì kiểu lỗi mà nó nhắm tới — những câu hỏi bao quát toàn bộ kho tài liệu — chính xác là điều mọi người mong muốn ở một bộ não thứ hai. Xem bài [`GraphRAG` và vị trí phù hợp của nó](../docs/05-graphs/graphrag.md) để hiểu tại sao bạn có lẽ không cần phải chạy nó ở quy mô cá nhân.

## HippoRAG

**[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)**. (arXiv:2405.14831) Gutiérrez, Shu, Gu, Yasunaga, Su.

Cơ chế truy xuất trên đồ thị tri thức sử dụng thuật toán PageRank cá nhân hóa (personalised PageRank), nhắm tới các câu hỏi suy luận đa bước (multi-hop questions). Đây là công trình công bố gần gũi nhất với hành vi của một `Agent` khi lần theo các liên kết tỏa ra từ một trang khởi đầu, khiến nó trở thành bài báo có tính ứng dụng trực tiếp hơn trong hai bài báo về đồ thị tại đây.

## Lost in the Middle

**[Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)**. (arXiv:2307.03172) Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang. Công bố trên tạp chí TACL.

Cơ sở thực nghiệm giải thích tại sao bạn không nên dán toàn bộ `Vault` của mình vào cửa sổ ngữ cảnh. Hiệu suất của mô hình đạt mức cao nhất khi thông tin liên quan nằm ở phần đầu hoặc phần cuối của đầu vào, và suy giảm nghiêm trọng khi mô hình phải sử dụng thông tin nằm ở khoảng giữa của một ngữ cảnh dài — kể cả đối với các mô hình được thiết kế chuyên biệt cho ngữ cảnh dài.

Đây là lý do tại sao kỹ thuật [tiết lộ tiệm tiến (progressive disclosure)](../docs/07-retrieval/context-budget.md) luôn đánh bại việc nạp tất cả mọi thứ vào cùng lúc, và tại sao một câu trả lời trích dẫn năm trang chọn lọc lại đáng tin cậy hơn một câu trả lời lắp ghép từ bốn trăm trang.

## Cách đọc các bài báo này

Cả ba bài báo đều nêu rất rõ những điều kiện để kết quả của họ có hiệu lực. Chính những điều kiện đó sẽ quyết định liệu phát hiện trong bài báo có áp dụng được sang một `Vault` cá nhân gồm vài nghìn trang đã được biên tập kỹ lưỡng hay không — một bối cảnh rất khác biệt so với các kho dữ liệu thô khổng lồ mà họ dùng để đánh giá.

Hãy đọc kỹ phần giới hạn nghiên cứu (limitations). Đó chính là thói quen tư duy mà toàn bộ cuốn hướng dẫn này cố gắng truyền tải.
