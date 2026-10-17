# Công cụ

Khảo sát toàn cảnh hệ sinh thái, tính đến tháng 9 năm 2026. Lĩnh vực này đã có cuộc thanh lọc và hợp nhất mạnh mẽ trong năm 2025: thế hệ công cụ lập chỉ mục theo lô (batch-indexing) dần lắng xuống, nhường chỗ cho thế hệ công cụ cập nhật tăng dần, hướng tới bộ nhớ dài hạn lên ngôi.

## Các bộ khung bộ nhớ và GraphRAG

- [Graphiti](https://github.com/getzep/graphiti) — Knowledge graph theo thời gian (temporal knowledge graph) dành cho bộ nhớ Agent, do Zep phát triển. Mọi cạnh đều mang một khoảng thời gian hiệu lực, các thông tin mâu thuẫn sẽ đánh dấu hết hiệu lực thay vì ghi đè, và hỗ trợ truy vấn tại một điểm thời gian bất kỳ (point-in-time). Đây là lựa chọn mạnh mẽ nhất cho các Agent chạy dài hạn; đồng thời là lõi đứng sau [nền tảng bộ nhớ](https://www.getzep.com) dạng dịch vụ lưu trữ (hosted) của Zep.
- [Cognee](https://github.com/topoteretes/cognee) — công cụ bộ nhớ tự lưu trữ (self-hosted) kết hợp cả đồ thị và Vector trong cùng một đường ống xử lý, với hệ sinh thái tích hợp ngày càng mở rộng (n8n, các bộ khung Agent) cùng phần lõi bằng Rust đang được hoàn thiện. Dự án hoạt động sôi nổi và được bảo trì tốt.
- [LightRAG](https://github.com/HKUDS/LightRAG) — phiên bản GraphRAG thực dụng: chỉ mục kép kết hợp đồ thị và Vector, cập nhật tăng dần, hỗ trợ nhiều hệ lưu trữ phía sau (Neo4j, PostgreSQL, MongoDB). Xuất phát từ bài báo EMNLP 2025 và vẫn đang được phát triển tích cực.
- [fast-graphrag](https://github.com/circlemind-ai/fast-graphrag) — hướng tiếp cận dựa trên PageRank của Circlemind; bỏ qua bước tạo bản tóm tắt cộng đồng để duyệt đồ thị với chi phí rẻ.
- [microsoft/graphrag](https://github.com/microsoft/graphrag) — phiên bản gốc, hiện đã ở chế độ bảo trì. Hãy đọc để tham khảo, đừng xây dựng hệ thống mới dựa trên nó; xem thêm bối cảnh tại bài [GraphRAG](graphrag.md).

## Tích hợp trong các bộ khung (Framework)

- [LlamaIndex property graph index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/) — lựa chọn tích hợp sẵn hoàn chỉnh nhất trong một bộ khung: cho phép cắm (plug) các bộ trích xuất linh hoạt (ép theo lược đồ hoặc tự do) và các bộ truy xuất chạy trên bất kỳ kho lưu trữ đồ thị thuộc tính nào.
- [LangChain LLMGraphTransformer](https://reference.langchain.com/python/langchain-neo4j/graph_transformers/llm/LLMGraphTransformer) — nhận tài liệu đầu vào, xuất tài liệu đồ thị đầu ra. Lưu ý rằng công cụ này đã được chuyển từ gói `langchain-experimental` sang gói `langchain-neo4j`; các đường dẫn import cũ hiện không còn hoạt động.
- [Neo4j LLM Knowledge Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/) — đường ống xử lý dạng trỏ-và-nhấp (point-and-click) được lưu trữ sẵn, giúp biến tệp PDF, trang web và bản chép lời YouTube thành đồ thị Neo4j. Rất tốt để quan sát thử xem quá trình trích xuất sẽ làm gì với tài liệu của bạn trước khi bắt tay vào viết mã.
- [FalkorDB GraphRAG-SDK](https://github.com/FalkorDB/GraphRAG-SDK) — bộ SDK ưu tiên bản thể luận (ontology-first) chạy trên nền FalkorDB, đã ổn định cho môi trường thực tế (production) và được cập nhật rất nhanh.

## Công cụ trực quan hóa

[Gephi](https://gephi.org) vẫn là "con ngựa thồ" bền bỉ cho việc phân tích ngoại tuyến một đồ thị đã xuất ra tệp — nạp tệp GraphML, chạy thuật toán bố cục (layout) và tô màu phân cụm cộng đồng, bạn sẽ phát hiện ra những cấu trúc tiềm ẩn mà mình chưa từng biết là có tồn tại. Còn trong trường hợp làm việc trực tiếp với cơ sở dữ liệu, bộ công cụ Browser và Bloom đi kèm của Neo4j đã đáp ứng trọn vẹn.

## Bộ công cụ đồ thị trên Obsidian

Chế độ xem đồ thị tích hợp sẵn của Obsidian giống một bức tranh trang trí hơn là một công cụ đo đạc; các plugin mới là thứ thực hiện công việc thực sự. [InfraNodus](https://github.com/noduslabs/infranodus-obsidian-plugin) bổ sung khả năng phân tích mạng lưới bài bản trên toàn bộ Vault — tìm cụm chủ đề, độ trung tâm, các khoảng trống cấu trúc — cộng thêm tính năng dùng AI sinh câu hỏi gợi mở ngay tại những khoảng trống đó. [Extended Graph](https://www.obsidianstats.com/plugins/extended-graph) nâng cấp giao diện gốc với bộ lọc và khả năng tùy chỉnh kiểu dáng theo từng loại thực thể/liên kết. Obsidian Hub hiện duy trì một [danh sách các plugin đồ thị](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.01+Plugins+by+Category/Graph+plugins) luôn được cập nhật mới.

## Cách lựa chọn

Bộ nhớ cho Agent: chọn Graphiti hoặc Cognee. Truy vấn trên kho tài liệu: chọn LightRAG. Đã dùng sẵn LlamaIndex hoặc LangChain: dùng ngay bộ trích xuất nội tại của chúng, ghi dữ liệu vào một hệ lưu trữ trong bài [kho lưu trữ đồ thị](graph-stores.md). Với một Vault đã được biên tập kỹ: các liên kết của bạn chính là đồ thị; chỉ cần cài thêm InfraNodus khi bạn muốn xem số liệu phân tích.
