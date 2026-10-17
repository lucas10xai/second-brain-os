# Tài nguyên về Evals (Eval Resources)

Một danh sách ngắn gọn có chủ đích. Mọi tài liệu ở đây đều xứng đáng với vị trí của nó; còn mọi thứ mà chúng dẫn link tới đều là tùy chọn. Các khái niệm được giảng dạy trong đó ánh xạ trực tiếp vào bài [tại sao cần `Evals`](why-evals.md) cùng phần còn lại của cuốn sổ tay này.

## Các tài liệu kinh điển

- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — Hamel Husain. Bài tiểu luận đã đưa `Evals` trở thành một kỷ luật kỹ thuật: đặt unit test, đánh giá của con người và kiểm thử A/B thành ba cấp độ, cùng lập luận đanh thép về việc phải trực tiếp nhìn vào dữ liệu của mình. Hãy bắt đầu từ đây.
- [AI Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) — Tuyển tập câu trả lời liên tục được cập nhật của Husain và Shreya Shankar cho những câu hỏi mà mọi đội ngũ đều thắc mắc: chấm nhị phân hay thang Likert, cần bao nhiêu nhãn, ai nên là người gán nhãn, tự xây hay đi mua. Cô đọng và hoàn toàn miễn phí.
- [AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals) — khóa học trên Maven đứng đằng sau bản FAQ trên; hàng nghìn kỹ sư và PM đã theo học, các khóa (cohorts) vẫn liên tục mở trong năm 2026. Có thu phí, và là khóa học duy nhất đáng đồng tiền bát gạo trong lĩnh vực này.
- [Who Validates the Validators?](https://arxiv.org/abs/2404.12272) — Shankar và cộng sự. Nền tảng nghiên cứu cho việc căn chỉnh các giám khảo LLM (`LLM-as-judge`) khớp với nhãn của con người; giải thích lý do tại sao các tiêu chí trong bảng rubric lại dịch chuyển dần khi con người chấm ngày càng nhiều đầu ra.
- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Cẩm nang kỹ thuật của Anthropic (tháng 1 năm 2026): lựa chọn tác vụ, chấm điểm quỹ đạo (`Trajectory`) so với chấm điểm kết quả đầu ra, hiệu chuẩn giám khảo, và đưa `Evals` vào CI. Đây là tài liệu gần nhất với một cuốn cẩm nang chính thức cho việc [đánh giá `Agent`](agent-evals.md).
- [Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — Hướng dẫn của OpenAI; bổ sung tốt cho các tài liệu trên và đi cặp với [chuyên mục evals trong cookbook](https://developers.openai.com/cookbook/topic/evals) chứa các ví dụ thực hành chi tiết về giám khảo LLM.

## Các kho mã nguồn đáng đọc

- [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) — hơn 200 bộ đánh giá được hiện thực hóa trên nền framework Inspect của UK AISI. Hãy đọc thử vài bộ chấm điểm (scorers) và bộ giải (solvers) để thấy mã nguồn `Evals` ở cấp độ production trông như thế nào.
- [terminal-bench](https://github.com/laude-institute/terminal-bench) — các tác vụ được kiểm duyệt thủ công chạy trong Docker với bộ chấm điểm thực thi được. Tài liệu tham chiếu sạch sẽ nhất để tự xây dựng các bài đánh giá dựa trên môi trường cho riêng bạn; xem thêm ngữ cảnh tại bài [đánh giá `Agent`](agent-evals.md).

## Bắt đầu tại đây: ba bước

1. **Đọc 30 `Traces`.** Trích xuất ba mươi bản ghi hội thoại thực tế (hoặc sát thực tế) từ sản phẩm của bạn ngay tối nay và viết một câu cho mỗi lỗi gặp phải. Không cần công cụ cầu kỳ, chỉ cần một bảng tính. Đây chính là bước phân tích lỗi, và nó sẽ định hình lại toàn bộ lộ trình sản phẩm (roadmap) của bạn.
2. **Đặt tên cho các lỗi, mã hóa ba lỗi hàng đầu.** Gom cụm các ghi chú của bạn thành một bảng phân loại (taxonomy), sau đó biến ba kiểu lỗi xuất hiện thường xuyên nhất thành các phép kiểm tra — dùng kiểm tra bằng code ở bất cứ nơi nào có thể, và dùng một giám khảo hẹp đã hiệu chuẩn ở những nơi không thể dùng code. Cơ chế chi tiết nằm ở bài [thiết kế bộ đánh giá](designing-evals.md) và [`LLM-as-judge`](llm-as-judge.md).
3. **Đưa bộ đánh giá vào CI và chạy lại hàng tuần.** Kết nối các phép kiểm tra vào đường ống CI/CD của bạn kèm một ngưỡng điểm chặn (`Gate`), sửa kiểu lỗi lớn nhất, rồi quay lại bước 1 với các `Traces` mới. Vòng lặp đó, được lặp đi lặp lại, chính là toàn bộ kỷ luật đánh giá.
