# Tại sao cần Evals (Why Evals)

`Evals` chính là các bài kiểm thử (tests) của sản phẩm AI. Một thay đổi trong prompt giúp sửa được một lời phàn nàn nhưng lại âm thầm làm hỏng ba thứ khác; nếu không có đo lường, bạn sẽ chỉ phát hiện ra điều đó từ chính người dùng. Các đội ngũ xuất xưởng những tính năng LLM đáng tin cậy luôn coi việc đánh giá là một kỷ luật kỹ thuật, chứ không phải màn kiểm tra theo cảm tính (vibe check) trước buổi demo.

## Cảm tính so với Đo lường

Phát triển dựa trên cảm tính trông như thế này: tinh chỉnh lại prompt, dán vào ba ví dụ mà bạn sực nhớ ra, gật gù hài lòng rồi đẩy lên production. Cách này dùng được cho một dự án cuối tuần. Nhưng nó sẽ sụp đổ ngay khoảnh khắc bạn có lưu lượng truy cập thực tế, bởi vì bạn đang lấy mẫu từ trí nhớ của chính mình thay vì từ đầu vào thực của người dùng.

Đo lường thì nhàm chán và cụ thể:

- một tập hợp đầu vào cố định đại diện cho nhu cầu sử dụng thực tế
- một cách tự động để chấm điểm từng đầu ra
- một con số thay đổi mỗi khi bạn chỉnh sửa điều gì đó

Con số đó chính là thứ cho phép bạn dõng dạc tuyên bố "mô hình mới hoàn toàn xứng đáng để chuyển đổi" hoặc "chỉnh sửa prompt này đã làm chất lượng truy xuất kém đi".

## Bánh đà đánh giá (The eval flywheel)

Vòng lặp này, được giảng dạy bởi Hamel Husain và Shreya Shankar cũng như được đồng vọng lại trong [hướng dẫn đánh giá `Agent` của Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), bao gồm các bước:

1. **Phân tích lỗi (Error analysis).** Đọc các `Traces` thực tế. Không phải nhìn vào bảng biểu dashboard — mà là đọc từng bản ghi hội thoại thực sự, ba mươi hoặc một trăm bản. Viết một ghi chú ngắn cho mỗi lỗi bạn nhìn thấy.
2. **Phân loại lỗi (Taxonomy).** Gom cụm các ghi chú đó thành những kiểu lỗi (failure modes) được đặt tên cụ thể: "ảo giác ra mã đơn hàng", "bỏ qua bộ lọc ngày tháng", "xin lỗi thay vì hành động".
3. **Thước đo (Metrics).** Biến mỗi kiểu lỗi thường gặp thành một bài kiểm tra — một phép kiểm tra chuỗi (string assertion), một bài test bằng code, hoặc một [`LLM-as-judge`](llm-as-judge.md) với bảng tiêu chí (rubric) hẹp.
4. **Lặp lại (Iterate).** Sửa kiểu lỗi lớn nhất, chạy lại bộ đánh giá, quan sát các con số, rồi quay lại bước 1 với các `Traces` mới.

Bánh đà này quan trọng hơn bất kỳ thước đo đơn lẻ nào. Những điểm số chung chung như "độ hữu ích từ 1–10" chẳng cho bạn biết điều gì cả; ngược lại, một thước đo ra đời từ chính bảng phân loại lỗi của bạn sẽ chỉ đích danh thứ cần phải sửa. Cách biến các kiểu lỗi thành những ca kiểm thử (test cases) cụ thể được trình bày trong bài [thiết kế bộ đánh giá](designing-evals.md).

## Tại sao các đội ngũ thường bỏ qua, và cái giá phải trả

Những lời biện minh phổ biến, tất cả đều dễ hiểu và tất cả đều đắt giá:

- "Đầu ra mang tính chủ quan, không thể kiểm thử được." Bạn hoàn toàn làm được. Một tổng thể chủ quan luôn có thể phân rã thành các phần khách quan.
- "Chúng tôi sẽ bổ sung `Evals` sau khi ra mắt." Sau khi ra mắt, bạn sẽ phải gỡ lỗi ngay trên môi trường production với những người dùng đang nổi giận làm người chấm điểm.
- "Ngồi đọc dữ liệu là việc tay chân nhàm chán." Đọc `Traces` là giờ làm việc mang lại đòn bẩy cao nhất mà một kỹ sư AI bỏ ra. Không ai giao phó unit test của mình cho sự hy vọng cả.

Hóa đơn sẽ tìm đến dưới dạng trò đập chuột lỗi hồi quy (regression whack-a-mole): mỗi bản sửa lỗi là một canh bạc, việc nâng cấp mô hình trở thành nỗi kinh hoàng, và tốc độ phát triển tụt dốc đúng vào lúc sản phẩm bắt đầu trở nên quan trọng. Những đội ngũ có sẵn `Evals` nâng cấp mô hình ngay trong tuần mô hình mới ra mắt, bởi vì bộ đánh giá cho họ biết ngay thứ gì vừa bị hỏng.

Hãy bắt đầu nhỏ thôi. Hai mươi lỗi thực tế, một bảng phân loại lỗi, một thước đo. Bánh đà sẽ lo phần còn lại. Khi sản phẩm của bạn là một `Agent` thay vì một lệnh gọi mô hình đơn lẻ, hãy xem bài [đánh giá `Agent`](agent-evals.md) để biết thêm các cơ chế bổ sung.
