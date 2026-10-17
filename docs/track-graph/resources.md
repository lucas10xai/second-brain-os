# Tài nguyên tham khảo

Danh sách tuyển chọn kỹ lưỡng, không chạy theo số lượng dàn trải. Mọi liên kết tại đây đều đã được kiểm tra còn hoạt động vào tháng 9 năm 2026.

## Bài báo khoa học

- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — bài báo gốc về GraphRAG của Microsoft. Hãy đọc nó để hiểu cách đặt vấn đề cũng như phương pháp giải quyết; trang [GraphRAG](graphrag.md) trong sổ tay này là bản tóm tắt ngắn gọn.
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for LLMs](https://arxiv.org/abs/2405.14831) — kết hợp Knowledge graph với thuật toán PageRank cá nhân hóa cho bài toán truy xuất đa bước (multi-hop), công bố tại NeurIPS 2024. Đây là mô hình toán học chính quy gần gũi nhất với hành vi một Agent lần theo các liên kết tỏa ra từ một trang ghi chú.
- [From RAG to Memory: Non-Parametric Continual Learning for LLMs](https://arxiv.org/abs/2502.14802) — HippoRAG 2. Đưa ra lập luận thuyết phục rằng bộ nhớ đồ thị có thể đánh bại Vector RAG mà không hề bị hụt hơi ở các truy vấn tra cứu đơn giản.
- [LightRAG: Simple and Fast Retrieval-Augmented Generation](https://arxiv.org/abs/2410.05779) — thiết kế hai tầng kết hợp đồ thị và Vector mà hầu hết các hệ thống năm 2026 đều âm thầm học hỏi.
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) — bài báo thiết kế đứng sau Graphiti; tài liệu giải thích rõ ràng và sâu sắc nhất về lý do tại sao bộ nhớ của Agent cần gắn yếu tố thời gian lên các cạnh.
- [When to Use Graphs in RAG](https://arxiv.org/abs/2506.05690) — một phân tích đối chiếu tỉnh táo chỉ ra đâu là nơi truy xuất đồ thị thực sự giúp ích và đâu là nơi nó chỉ gây cồng kềnh lãng phí. Đây là liều thuốc cân bằng cần đọc sau loạt bài báo đầy hào hứng phía trên.

## Hướng dẫn và khóa học

- [Knowledge Graphs for RAG](https://www.deeplearning.ai/courses/knowledge-graphs-rag) — khóa học ngắn của DeepLearning.AI phối hợp cùng Neo4j. Thời lượng vài giờ, thực hành trực tiếp, có bao gồm ngôn ngữ truy vấn Cypher.
- [Neo4j GraphAcademy: knowledge graphs and GraphRAG](https://graphacademy.neo4j.com/knowledge-graph-rag/) — miễn phí, chuyên sâu hơn, tự học theo tốc độ cá nhân.
- [Building Knowledge Graphs with LLM Graph Transformer](https://medium.com/data-science/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59) — bài hướng dẫn chi tiết của Tomaz Bratanic về trích xuất có ràng buộc lược đồ; bài viết thực hành hữu ích nhất về chủ đề này.
- [Implementing "from local to global" GraphRAG with Neo4j and LangChain](https://neo4j.com/blog/developer/global-graphrag-neo4j-langchain/) — tái hiện lại toàn bộ đường ống xử lý từng bước một, giúp bạn nhìn thấy rõ ràng các chi phí phát sinh trong thực tế.
- [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) — bài viết của Microsoft Research về kỹ thuật trì hoãn chi phí lập chỉ mục sang thời điểm truy vấn.

## Kho mã nguồn đáng đọc

Hãy đọc [Graphiti](https://github.com/getzep/graphiti) để học cách xử lý cạnh theo thời gian và phân giải thực thể một cách bài bản; đọc [LightRAG](https://github.com/HKUDS/LightRAG) để nắm một đường ống xử lý đầu-cuối (end-to-end) gọn gàng mà bạn có thể hình dung trọn vẹn trong đầu; và đọc [microsoft/graphrag](https://github.com/microsoft/graphrag) như một bản cài đặt tham chiếu đã đóng băng. Khảo sát các công cụ đang hoạt động nằm tại trang [công cụ](tools.md).

## Bắt đầu từ đây

1. Đọc bài [tại sao cần Knowledge Graph](why-graphs.md) và áp dụng bài kiểm tra ngưỡng quyết định vào chính kho ngữ liệu cùng các câu hỏi thực tế của bạn. Nếu nhu cầu của bạn nằm dưới ngưỡng đó, hãy dừng lại; các liên kết wiki hiện tại của bạn vốn đã là đồ thị rồi.
2. Học khóa ngắn hạn của DeepLearning.AI, sau đó chạy thử LightRAG trên khoảng một trăm tài liệu của chính bạn và đọc kỹ các bộ ba được trích xuất ra. Không gì dạy bạn hiểu về các kiểu lỗi của quá trình trích xuất nhanh hơn cách này.
3. Đọc bài báo của Zep, sau đó chủ động chọn kho lưu trữ phù hợp dựa theo bài [kho lưu trữ đồ thị](graph-stores.md) — ưu tiên tệp tin trước, chỉ dựng máy chủ khi việc có nhiều tiến trình ghi đồng thời bắt buộc bạn phải làm vậy.
