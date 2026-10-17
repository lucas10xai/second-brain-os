# Dùng LLM làm giám khảo (LLM as Judge)

Một số phép kiểm tra có thể viết bằng code: khớp chính xác (exact match), biểu thức chính quy (regex), JSON schema, hay "câu lệnh SQL có chạy được không". Mọi thứ còn lại — giọng điệu, độ trung thực với tài liệu nguồn (faithfulness), liệu câu trả lời có thực sự giải quyết đúng câu hỏi hay không — đều cần một người chấm có khả năng đọc hiểu. Người chấm đó thường là một mô hình LLM khác. Rất hữu ích, chi phí rẻ, nhưng hoàn toàn không đáng tin cậy cho đến khi được hiệu chuẩn (calibrated).

## Viết prompt cho giám khảo

Prompt dành cho giám khảo là một bản mô tả công việc cụ thể, không phải một lời ước nguyện:

- Mỗi giám khảo chỉ trả lời một câu hỏi. "Khẳng định này có được hỗ trợ bởi ngữ cảnh đã cung cấp hay không: có/không" luôn tốt hơn nhiều so với "hãy chấm điểm chất lượng tổng thể".
- Đầu ra nhị phân đi kèm yêu cầu *viết lập luận giải thích trước khi đưa ra phán quyết*. Phần lập luận chính là dấu vết gỡ lỗi của bạn; những giám khảo đưa ra phán quyết trước thường chỉ tìm cách hợp thức hóa kết luận của mình.
- Đưa vào 2–4 ví dụ mẫu đã giải sẵn cho cả trường hợp đạt và trượt, đặc biệt là những trường hợp nằm ở ranh giới mong manh.
- Cung cấp cho giám khảo đúng ngữ cảnh mà sản phẩm đã nhận được. Một giám khảo chấm điểm câu trả lời `RAG` mà không có các tài liệu đã truy xuất thì chỉ đang đoán mò.

Hãy giữ cho bảng tiêu chí (rubric) trong prompt thật cụ thể: trích dẫn thẳng bảng phân loại lỗi từ bước phân tích lỗi của bạn (xem [thiết kế bộ đánh giá](designing-evals.md)), tuyệt đối không dùng các tính từ mơ hồ như "hữu ích" hay "chất lượng cao".

## Hiệu chuẩn theo nhãn của con người (Calibration against human labels)

Một giám khảo chưa được hiệu chuẩn chỉ là một trình sinh số ngẫu nhiên đầy vẻ tự tin. Quy trình hiệu chuẩn, lấy trực tiếp từ [hướng dẫn về giám khảo](https://hamel.dev/blog/posts/llm-judge/) của Hamel Husain, gồm các bước:

1. Một chuyên gia nghiệp vụ (domain expert) gán nhãn đạt/trượt cho 50–100 đầu ra kèm theo lý do ngắn gọn.
2. Chạy giám khảo LLM trên cùng tập dữ liệu đó; đo lường mức độ đồng thuận (hãy báo cáo độ đồng thuận trên từng lớp đạt/trượt thay vì độ chính xác thô — một giám khảo lúc nào cũng phán "đạt" vẫn sẽ đạt điểm chính xác 90% trên một tập dữ liệu phần lớn là tốt).
3. Đọc từng trường hợp bất đồng. Sửa lại bảng tiêu chí, hoặc phát hiện ra chính nhãn của bạn thiếu nhất quán — cả hai trường hợp đều xảy ra thường xuyên.
4. Lặp lại cho đến khi mức độ đồng thuận trở nên ổn định nhàm chán, sau đó kiểm tra lại định kỳ hàng quý và bất cứ khi nào bạn thay đổi mô hình làm giám khảo.

Bài báo [Who Validates the Validators?](https://arxiv.org/abs/2404.12272) của Shreya Shankar là công trình nghiên cứu chuyên sâu về vòng lặp này.

## Các kiểu thiên kiến (bias) đã biết

Đã được ghi nhận từ [bài báo MT-Bench](https://arxiv.org/abs/2306.05685) và vẫn còn nguyên tính thời sự vào năm 2026:

- **Thiên kiến vị trí (Position bias).** Trong các phép so sánh theo cặp, giám khảo thường thiên vị câu trả lời đầu tiên (đôi khi là câu thứ hai). Hãy đảo thứ tự hai câu và lấy trung bình, nếu không phép so sánh sẽ hoàn toàn vô nghĩa.
- **Thiên kiến chuộng dài dòng (Verbosity bias).** Các câu trả lời dài hơn thường được chấm điểm cao hơn dù độ chính xác như nhau. Hãy giới hạn độ dài hoặc ra chỉ dẫn rõ ràng chống lại thiên kiến này, sau đó kiểm chứng lại.
- **Thiên kiến tự ưu ái (Self-preference).** Các mô hình thường chấm điểm cao hơn cho đầu ra từ những mô hình cùng họ với mình. Hãy dùng một mô hình khác họ với mô hình đang bị chấm bất cứ khi nào khả thi.
- **Tính xu nịnh theo ý định tuyên bố (Sycophancy toward stated intent).** Nếu đưa mục tiêu tự nhận của người dùng vào, giám khảo sẽ chấm điểm sự nỗ lực thay vì kết quả thực tế.

## Khi giám khảo nói dối

Giám khảo âm thầm thất bại trước: toán học và số học, các sự kiện chuyên ngành hẹp, những vi phạm chỉ dẫn tinh vi, và bất cứ điều gì mà chính mô hình giám khảo cũng sẽ làm sai. Nếu một phép kiểm tra *có thể* viết bằng code, hãy biến nó thành code. Chỉ dành giám khảo LLM cho những phán đoán thực sự mang tính ngôn ngữ, duy trì việc để con người kiểm toán định kỳ một mẫu phán quyết của nó mãi mãi, và đừng bao giờ để điểm số của giám khảo làm cổng chặn (`Gate`) cho một bản phát hành mà các kiểm tra từng bước (per-step checks) đang bác bỏ — xem bài [đánh giá `Agent`](agent-evals.md) để hiểu cách kết hợp cả hai.
