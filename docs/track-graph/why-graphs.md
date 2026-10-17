# Tại sao cần Knowledge Graph

Bài toán bộ nhớ của một Agent không nằm ở dung lượng lưu trữ. Vấn đề là các dữ kiện khi đến thì có sự kết nối với nhau, nhưng khi lưu lại bị làm phẳng. Một Knowledge graph giữ lại các mối liên kết đó: thực thể là các nút (node), mối quan hệ là các cạnh có định kiểu (typed edge), nhờ đó câu hỏi "X có liên quan gì đến Y" trở thành một bước duyệt đồ thị thay vì một phép phỏng đoán.


Sổ tay này bàn về đồ thị trong vai trò bộ nhớ của Agent nói chung; còn [phần đồ thị](../05-graphs/graph-basics.md) trong cẩm nang bộ não thứ hai sẽ đi sâu vào khía cạnh đặc thù của Vault — dùng Wikilink làm cạnh, liên kết có định kiểu và chế độ xem đồ thị của Obsidian.

## Những gì Vector RAG không làm được

Truy xuất bằng Embeddings trả lời rất tốt một dạng câu hỏi: "tìm cho tôi những đoạn văn nghe giống như thế này". Nhưng nó lại thất bại một cách dễ đoán ở hai dạng câu hỏi khác.

- **Câu hỏi đa bước (multi-hop).** "Khách hàng nào của tôi đang dùng bộ framework mà đồng nghiệp đã cảnh báo?" Không một đoạn cắt (chunk) đơn lẻ nào chứa câu trả lời; đáp án nằm ở phép kết nối (join). Tìm kiếm tương đồng chỉ lấy ra các mảnh rời rạc của mỗi vế và để mặc mô hình tự bịa ra cầu nối.
- **Câu hỏi toàn cục (global).** "Đâu là những chủ đề lặp đi lặp lại trong toàn bộ những gì tôi đã đọc năm nay?" Câu trả lời là một thuộc tính của toàn bộ kho ngữ liệu, chứ không nằm trong năm đoạn văn bất kỳ nào.

Đồ thị xử lý được cả hai, bởi các cạnh chính là những phép kết nối bạn đã tính toán sẵn một lần ngay lúc nạp dữ liệu, và cấu trúc phân cụm của đồ thị chính là tầng chủ đề. [GraphRAG](graphrag.md) là mẫu thiết kế được xây dựng dựa trên chính quan sát này.

## Những gì đồ thị không làm được

Góc nhìn đối trọng thẳng thắn: đồ thị chỉ tốt tương đương với chất lượng của quá trình trích xuất tạo ra nó, mà việc trích xuất lại dễ làm rơi rớt thông tin, tốn kém và đôi khi sai sót. Tìm kiếm Vector không cần lược đồ (schema), chấp nhận mọi đầu vào, và lỗi của nó lộ diện ngay lúc truy vấn thay vì bị chôn chặt từ lúc nạp dữ liệu. Truy hồi mờ (fuzzy recall) — kiểu như "có cái gì đó về định giá, hình như trong một tập podcast" — là lãnh địa của Embeddings, và đồ thị hoàn toàn vô dụng trong trường hợp này.

## Kết hợp lai (Hybrid) hiện là mặc định

Đến năm 2026, cuộc tranh luận này coi như đã ngã ngũ: các hệ thống thực tế cần cả truy hồi mờ lẫn duyệt cấu trúc đa bước đều chạy song song cả hai. Vector tìm ra các điểm khởi đầu; đồ thị mở rộng từ những điểm đó. [LightRAG](https://github.com/HKUDS/LightRAG) và [Graphiti](https://github.com/getzep/graphiti) đều đóng gói cơ chế này làm kiến trúc mặc định chứ không còn là tùy chọn phụ, và các hệ thống bộ nhớ Agent như Zep coi đồ thị là nguồn chân lý (source of truth) với Embeddings đóng vai trò chỉ mục phủ lên trên. Câu hỏi thiết kế giờ đây không còn là chọn đồ thị hay Vector, mà là đồ thị nằm ở đâu và ai là người ghi dữ liệu vào đó — xem thêm tại [kho lưu trữ đồ thị](graph-stores.md).

## Khi nào không nên bận tâm

Hãy bỏ qua đồ thị khi:

- Kho ngữ liệu đủ nhỏ để nhét vừa vào một cửa sổ ngữ cảnh (context window). Hãy đọc trực tiếp luôn.
- Các câu hỏi chỉ là tra cứu một bước (single-hop). Tìm kiếm Vector hoặc thậm chí cấp độ `grep` sẽ thắng về mặt chi phí.
- Không ai duy trì lược đồ (schema). Một đồ thị lỗi thời còn tệ hơn là không có đồ thị, vì nó trả lời đầy tự tin dựa trên những cạnh đã cũ.
- Bạn đã duy trì sẵn một wiki được biên tập kỹ lưỡng với các liên kết có định kiểu. Đó chính là một đồ thị; bạn đã tự tay xây dựng nó, và rất có thể nó tốt hơn đồ thị do LLM trích xuất.

Ngưỡng quyết định đại khái là thế này: chỉ nên đầu tư khi các câu hỏi của bạn cần kết nối dữ kiện xuyên qua nhiều tài liệu thường xuyên hơn là chỉ lấy dữ kiện từ một tài liệu đơn lẻ. Dưới ngưỡng đó, đường ống trích xuất trong phần [xây dựng đồ thị bằng LLM](building-graphs-with-llms.md) chỉ là chi phí bỏ ra mà không mang lại thành quả tương xứng.
