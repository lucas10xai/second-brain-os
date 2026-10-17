# GraphRAG

GraphRAG là phương pháp sinh văn bản tăng cường truy xuất (RAG), trong đó chỉ mục là một đồ thị được xây dựng từ kho ngữ liệu, thay vì một đống các đoạn văn bản (chunk) được nhúng bằng Embeddings. Phiên bản kinh điển là bài báo năm 2024 của Microsoft Research mang tên [From Local to Global](https://arxiv.org/abs/2404.16130), nhắm thẳng vào loại câu hỏi mà Vector RAG trả lời tệ nhất: những truy vấn về toàn bộ kho ngữ liệu như một chỉnh thể.

## Mẫu thiết kế cốt lõi

Bốn giai đoạn, tất cả đều diễn ra tại thời điểm lập chỉ mục (indexing):

1. **Trích xuất thực thể.** Một mô hình LLM đọc từng đoạn cắt (chunk) và xuất ra các thực thể cùng mối quan hệ, thường dưới dạng bộ ba `(chủ ngữ, vị ngữ, tân ngữ)` kèm theo mô tả.
2. **Xây dựng đồ thị.** Các bộ ba được gộp vào một đồ thị; các thực thể trùng lặp sẽ được phân giải và hợp nhất.
3. **Phát hiện cộng đồng (community detection).** Một thuật toán phân cụm (thuật toán Leiden trong bản gốc) tìm ra các vùng lân cận có mật độ kết nối dày đặc.
4. **Tóm tắt cộng đồng.** LLM viết báo cáo tổng hợp cho từng cộng đồng theo cấu trúc phân cấp, nhờ đó kho ngữ liệu có sẵn các bản tóm tắt ở nhiều mức độ thu phóng khác nhau.

Các truy vấn cục bộ (local queries) sẽ bước dọc theo đồ thị từ những thực thể khớp lệnh. Các truy vấn toàn cục (global queries) sẽ ánh xạ (map) qua các bản tóm tắt cộng đồng rồi rút gọn (reduce) thành một câu trả lời duy nhất — đó là lý do câu hỏi "đâu là các chủ đề chính" cuối cùng cũng hoạt động hiệu quả.

## Microsoft GraphRAG và các thế hệ kế nhiệm

Kho mã nguồn [microsoft/graphrag](https://github.com/microsoft/graphrag) hiện đã chuyển sang chế độ bảo trì: chỉ sửa lỗi và vá lỗ hổng CVE, không thêm tính năng mới. Hãy xem nó như một bản cài đặt tham chiếu để đọc hiểu, chứ không phải bộ khung (framework) để áp dụng vào dự án.

Những bước tiến thú vị đã dịch chuyển sang các hậu duệ tiết kiệm chi phí hơn. [LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) trì hoãn gần như toàn bộ công việc của LLM sang thời điểm truy vấn — không tóm tắt trước — với chi phí lập chỉ mục được công bố chỉ bằng 0,1% so với bản gốc, dù nó được tích hợp vào các sản phẩm Azure của Microsoft thay vì thư viện mã nguồn mở. Trong thế giới mã nguồn mở, [LightRAG](https://github.com/HKUDS/LightRAG) (bài báo tại EMNLP 2025, vẫn đang được phát triển tích cực) duy trì chỉ mục kép kết hợp đồ thị và Vector với khả năng cập nhật tăng dần (incremental updates), còn [fast-graphrag](https://github.com/circlemind-ai/fast-graphrag) thay thế phần tóm tắt cộng đồng bằng duyệt đồ thị qua PageRank. Hầu hết các hệ thống triển khai mới trong năm 2026 đều chọn một trong số này; trang [công cụ](tools.md) sẽ khảo sát chi tiết toàn cảnh lĩnh vực.

## Chi phí và sự đánh đổi

Đường ống nguyên bản đắt đỏ theo một cách rất đặc thù: mọi đoạn văn bản đều phải đi qua LLM lúc nạp dữ liệu, sau đó mọi cộng đồng lại được tóm tắt, rồi tiếp tục tóm tắt lại theo từng bậc phân cấp lên trên. Việc lập chỉ mục cho một kho ngữ liệu vừa phải cũng tốn một khoản tiền thật, và lập chỉ mục lại sau khi chỉnh sửa lại tốn ngần ấy tiền một lần nữa. Đó là thứ "thuế" mà các hậu duệ sinh ra để né tránh — thông qua tính toán lười (lazy evaluation), cập nhật tăng dần, hoặc bỏ qua hoàn toàn bước tóm tắt.

Sự đánh đổi âm thầm hơn nằm ở độ trung thực. Quá trình trích xuất ép phẳng các sắc thái tinh tế thành những bộ ba khô khan; một lời rào đón, một mốc thời gian giới hạn hay thông tin quy thuộc nguồn đều có thể biến mất. Bản tóm tắt cộng đồng suy cho cùng vẫn là bản tóm tắt — chúng kế thừa mọi kiểu lỗi của việc yêu cầu một mô hình nén đoạn văn bản mà bản thân nó không thực sự hiểu. GraphRAG trả lời được các câu hỏi toàn cục mà Vector RAG bó tay, nhưng câu trả lời của nó lại cách nguồn dữ liệu gốc của bạn thêm một tầng sinh văn bản bằng mô hình nữa.

## Khi nào nó đáng đồng tiền bát gạo

Những kho ngữ liệu lớn, chưa được biên tập, đi kèm nhu cầu thực sự về các câu hỏi đa bước và tổng hợp chủ đề — hãy xem [tại sao cần Knowledge Graph](why-graphs.md) để biết bài kiểm tra ngưỡng quyết định. Đối với một Vault cá nhân đã được chăm chút kỹ, chính tay bạn đã làm công việc trích xuất rồi; thứ còn lại hữu ích là hình hài của đường ống xử lý, được trình bày chi tiết trong [xây dựng đồ thị bằng LLM](building-graphs-with-llms.md).
