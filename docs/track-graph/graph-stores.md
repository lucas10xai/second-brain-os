# Kho lưu trữ đồ thị

Nơi đồ thị cư trú ít quan trọng hơn mọi người tưởng, nhưng lại quan trọng hơn những gì các nhà cung cấp thừa nhận. Thứ tự ưu tiên thực tế ở quy mô cá nhân và Agent đi từ văn bản thuần (plain text) trở lên, chứ không phải từ cơ sở dữ liệu đi xuống.

## Wikilink chính là đồ thị

Một thư mục chứa các tệp Markdown, nơi các liên kết `[[Trang]]` đóng vai trò là cạnh, bản thân nó đã là một Knowledge graph. Đó là mẫu thiết kế làm nền tảng cho toàn bộ trang web này: thực thể là các trang, mối quan hệ là các liên kết — có định kiểu đàng hoàng nếu bạn làm theo [liên kết có định kiểu](../05-graphs/typed-links.md) — và kho lưu trữ chính là hệ thống tệp tin (filesystem). Một Agent truy vấn nó bằng `grep` và lần theo liên kết; còn bạn truy vấn nó trong Obsidian. Không máy chủ, không trình điều khiển (driver), không kịch bản di trú dữ liệu (migration), và đồ thị hoàn toàn có thể đọc hiểu trực tiếp bởi chính người sở hữu nó. Ở quy mô vài nghìn nút, đây không phải là một sự thỏa hiệp tạm bợ. Đây là lựa chọn đúng đắn.

## Lưu trữ NetworkX trong tệp tin

Khi bạn cần đến các thuật toán — PageRank, phát hiện cộng đồng, đo độ trung tâm (centrality) — hãy nạp đồ thị vào [NetworkX](https://networkx.org) và lưu trữ bền vững dưới định dạng GraphML hoặc JSON ngay cạnh các ghi chú của bạn. Chạy Python trên bộ nhớ trong (in-memory), không cần hạ tầng, hoạt động trơn tru tới quy mô hàng chục nghìn nút. Khá nhiều bản cài đặt [GraphRAG](graphrag.md) sử dụng chính phương thức này làm backend mặc định, điều đó đủ cho bạn thấy quy mô thực tế mà họ kỳ vọng là ở mức nào.

## Cơ sở dữ liệu nhúng, và bài học từ Kuzu

Kuzu từng là lựa chọn cơ sở dữ liệu nhúng hiển nhiên — được ví như DuckDB dành cho đồ thị, hỗ trợ Cypher, gói gọn trong một tệp duy nhất. Thế rồi Kùzu Inc. được Apple mua lại và [kho mã nguồn](https://github.com/kuzudb/kuzu) bị đưa vào lưu trữ (archive) vào tháng 10 năm 2025 với phiên bản cuối cùng là 0.11.3. Nó vẫn chạy được, các bản nhánh (fork) từ cộng đồng vẫn tồn tại, nhưng câu chuyện này là minh chứng rõ ràng nhất cho việc ưu tiên các tầng lưu trữ phía trên: giấy phép MIT đã cứu sống mã nguồn, nhưng nếu dùng tệp văn bản thuần túy thì ngay từ đầu đã chẳng cần ai phải cứu. [Bức tranh hậu Kuzu](https://gdotv.com/blog/kuzu-legacy-embedded-graph-database-landscape/) hiện vẫn đang trong quá trình tự định hình lại.

## Máy chủ chuyên dụng: Neo4j và FalkorDB

[Neo4j](https://neo4j.com) là cái tên kỳ cựu thống lĩnh thị trường: ngôn ngữ truy vấn Cypher, hệ sinh thái lớn nhất, tích hợp hạng nhất trong mọi bộ khung (framework), và có gói miễn phí đủ dùng cho nhu cầu cá nhân. Cái giá phải trả nằm ở khâu vận hành — nó là một máy chủ (server), và giờ bạn phải nuôi một máy chủ. [FalkorDB](https://www.falkordb.com/) là giải pháp thay thế nhẹ nhàng hơn, một cơ sở dữ liệu đồ thị dạng mô-đun Redis nhắm thẳng vào các tác vụ GraphRAG, đi kèm bộ SDK riêng đang được phát triển rất tích cực. Đây là lựa chọn hợp lý khi một đội ngũ Agent dùng chung một đồ thị và độ trễ truy vấn là yếu tố quan trọng.

## Giải pháp nào khớp với nhu cầu nào

- Một người dùng, kho ngữ liệu được biên tập kỹ: dùng Wikilink. Bạn đang đọc chính bản chứng minh khái niệm (proof of concept) của cách này.
- Kho ngữ liệu cá nhân cộng thêm các thuật toán đồ thị: dùng NetworkX chạy trên danh sách liên kết được xuất ra.
- Bộ nhớ cho một Agent đơn lẻ: dùng bất cứ thứ gì mà thư viện bộ nhớ của bạn chọn làm mặc định — [Graphiti](https://github.com/getzep/graphiti) cần Neo4j hoặc FalkorDB, các thư viện khác thường gói sẵn NetworkX. Xem thêm tại [công cụ](tools.md).
- Đa Agent, dùng chung dữ liệu, ghi đồng thời: cần một máy chủ thực thụ, và lúc này bạn chính thức phải vận hành một hệ quản trị cơ sở dữ liệu.

Hãy chọn kho lưu trữ sau khi đường ống trích xuất đã hoạt động ổn định, đừng chọn trước. Một đồ thị nằm trong tệp tin có thể chuyển sang Neo4j chỉ trong một buổi chiều; còn chiều di cư ngược lại chính là cách mà các dự án nhận ra đồ thị của họ chưa bao giờ đáng giá đến mức phải dựng cả một máy chủ. Logic xác định ngưỡng chuyển đổi nằm ở bài [tại sao cần Knowledge Graph](why-graphs.md).
