# Xây dựng đồ thị bằng LLM

Trích xuất chính là toàn bộ cuộc chơi. Một kho lưu trữ đồ thị sẽ lưu giữ trung thành bất cứ thứ gì bạn đưa vào; việc thứ đó là tri thức hay rác nhiễu được quyết định ngay trong đường ống xử lý (pipeline). Trang này trình bày hình hài thực tế của đường ống đó.

## Định hình lược đồ trước khi trích xuất

Trích xuất không ràng buộc sẽ tạo ra một ngăn kéo chứa đồ hỗn tạp: `WORKS_AT`, `WORKS_FOR`, `EMPLOYED_BY` trở thành ba cạnh khác nhau cho cùng một dữ kiện. Hãy quyết định bản thể luận (ontology) trước, dù chỉ là một bộ nhỏ — năm loại thực thể và mười loại quan hệ là đủ bao quát hầu hết kho ngữ liệu cá nhân và bộ nhớ Agent. Mọi công cụ nghiêm túc đều cho phép bạn truyền cấu hình này vào như một ràng buộc: [LLMGraphTransformer](https://reference.langchain.com/python/langchain-neo4j/graph_transformers/llm/LLMGraphTransformer) của LangChain nhận tham số `allowed_nodes` và `allowed_relationships`; [chỉ mục đồ thị thuộc tính](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/) của LlamaIndex có `SchemaLLMPathExtractor` giúp ép kiểu ngay tại thời điểm trích xuất.

Hãy bắt đầu hẹp hơn mức bạn cảm thấy vừa vặn. Mở rộng lược đồ về sau rất rẻ; còn thu gọn một "vườn thú" gồm hàng tá vị ngữ gần giống nhau thì cực kỳ vất vả.

## Lượt chạy trích xuất

Cơ chế vận hành khá ổn định giữa các công cụ: cắt nhỏ tài liệu nguồn (chunking), nhắc (prompt) mô hình xuất ra các bộ ba có định kiểu kèm mô tả ngắn cho từng thực thể, và giữ lại thông tin truy nguyên nguồn gốc (provenance) — bộ ba này đến từ đoạn cắt nào, tài liệu nào, vào ngày nào. Truy nguyên nguồn gốc là thứ giúp bạn trả lời câu hỏi "tại sao đồ thị lại tin vào điều này" và xóa bỏ các cạnh khi một nguồn tin bị rút lại. Các chế độ đầu ra có cấu trúc (structured output) giúp việc phân tích cú pháp luôn đáng tin cậy; lỗi còn sót lại nằm ở tầng ngữ nghĩa chứ không phải cú pháp, vì vậy hãy lấy mẫu và đọc kiểm tra vài chục bộ ba trên mỗi lô (batch) thay vì tin mù quáng vào tỷ lệ chạy thành công.

## Cập nhật tăng dần (Incremental updates)

Đường ống [GraphRAG](graphrag.md) nguyên bản giả định việc lập chỉ mục lại theo lô (batch re-indexing), điều không thể kham nổi về chi phí đối với một kho ngữ liệu thay đổi hàng ngày. Thế hệ công cụ hiện tại được thiết kế ưu tiên cập nhật tăng dần ngay từ đầu. [Graphiti](https://github.com/getzep/graphiti) là thiết kế mạnh nhất ở mảng này: mỗi sự kiện (episode) mới được trích xuất, đối chiếu với đồ thị hiện có, và các cạnh mâu thuẫn không bị xóa đi mà được đánh dấu hết hiệu lực kèm dấu thời gian (timestamp) — đồ thị lưu giữ cả hai trạng thái "đúng cho đến tháng Ba" và "đúng từ tháng Ba trở đi". Đối với bộ nhớ của Agent, tầng thời gian đó chính là ranh giới phân biệt giữa một bộ nhớ thực thụ và một bộ đệm (cache).

## Khử trùng lặp và phân giải thực thể

Cùng một người có thể xuất hiện dưới tên `J. Smith`, `John Smith` và `john bên ops`. Chính sách hợp nhất, xếp theo thứ tự chi phí tăng dần: khớp tên chính xác và chuẩn hóa chuỗi; tính độ tương đồng Embeddings trên phần mô tả thực thể theo ngưỡng; dùng LLM phân xử các cặp ứng viên còn nhập nhằng. Hãy thực hiện các tầng chi phí thấp trước và chỉ gửi phần dư mơ hồ cho mô hình xử lý. Hãy phân giải ngay tại thời điểm ghi — nếu để việc khử trùng lặp thành một tác vụ chạy lô sau đó, mọi truy vấn diễn ra trước đợt chạy lô đều sẽ nhìn thấy một đồ thị bị phân mảnh.

## Giữ vòng lặp nhỏ gọn

Hãy trích xuất thử một trăm tài liệu, nhìn vào đồ thị, sửa lại lược đồ, rồi chạy lại. Những đường ống thất bại thường là những đường ống xử lý toàn bộ kho ngữ liệu trước khi có bất kỳ ai nhìn vào kết quả. Nơi lưu trữ kết quả đầu ra — cơ sở dữ liệu nhúng, tệp tin, hay các Wikilink thuần túy — là chủ đề của phần [kho lưu trữ đồ thị](graph-stores.md), và các bản cài đặt dựng sẵn được khảo sát chi tiết trong phần [công cụ](tools.md).
