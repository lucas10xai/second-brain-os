# Thiết kế bộ đánh giá (Designing Evals)

Một bộ `Evals` chỉ tốt tương xứng với các ca kiểm thử (test cases) của nó. Con đường đi từ nhận xét mơ hồ "con bot của chúng ta thỉnh thoảng lại làm sai" đến một bộ đánh giá mà bạn tin tưởng phải đi qua các kiểu lỗi (failure modes): gọi tên những gì trục trặc, sau đó xây dựng các ca kiểm thử nhằm kích hoạt chính lỗi đó. Trang này giả định bạn đã thực hiện bước phân tích lỗi được mô tả trong bài [tại sao cần `Evals`](why-evals.md).

## Bộ dữ liệu chuẩn (`Golden set`)

Một `Golden set` là một tập hợp cố định các đầu vào đi kèm kỳ vọng đầu ra chuẩn xác đã biết, được tinh tuyển bởi một con người thực sự hiểu sản phẩm. Các nguyên tắc thực tiễn:

- Lấy nguồn từ `Traces` trên môi trường production trước, tự nghĩ ra sau. Đầu vào thực tế luôn kỳ quặc hơn bất cứ thứ gì bạn có thể tự ngồi viết.
- Mỗi kiểu lỗi đã được đặt tên phải có ít nhất một vài ca kiểm thử từng kích hoạt nó trong lịch sử.
- Đưa vào cả những ca thành công nhàm chán (happy path), nếu không bạn sẽ tối ưu quá mức (over-fit) cho các ca bệnh lý và làm hỏng mất luồng chạy chuẩn.
- Quản lý phiên bản trong git ngay cạnh mã nguồn. Một `Golden set` mà không ai có thể xem diff là một `Golden set` không ai tin tưởng.

## Dữ liệu tổng hợp (Synthetic data)

Khi lưu lượng truy cập còn mỏng — giai đoạn trước khi ra mắt, hoặc đối với các luồng hiếm gặp nhưng tối quan trọng — hãy sinh tự động các ca kiểm thử. Sử dụng LLM để biến thiên theo các chiều (dimensions) mà bạn chủ đích lựa chọn: chân dung người dùng (persona), cách diễn đạt, độ dài, ngôn ngữ, ý định đối kháng (adversarial intent). Hai lời nhắc cẩn trọng:

- Đầu vào tổng hợp thì ổn; nhưng *nhãn* tổng hợp lại mang tính luẩn quẩn. Một mô hình chấm điểm một mô hình khác trên dữ liệu do chính nó bịa ra chẳng chứng minh được nhiều điều. Hãy để con người kiểm tra xác suất lại các nhãn.
- Hãy sinh dữ liệu dọc theo một khung cấu trúc (schema) các chiều cụ thể, đừng ra lệnh kiểu "hãy cho tôi 100 ví dụ đa dạng" — cách đó chỉ tạo ra 100 biến thể của cùng ba ý tưởng lặp đi lặp lại.

## Chấm điểm theo thang bậc so với Nhị phân

Hãy ưu tiên đánh giá nhị phân (Binary). Đạt/trượt (Pass/fail) buộc bạn phải định nghĩa rõ tiêu chuẩn tối thiểu, và những bất đồng giữa người với người sẽ lộ diện ngay lập tức. Thang điểm "chất lượng" từ 1–5 phần lớn chỉ đo tâm trạng của người chấm; hai người gán nhãn sẽ vui vẻ cho cùng một đầu ra điểm 3 và điểm 4 mà chẳng rút ra được bài học gì. Nếu một tiêu chí thực sự có nhiều mức độ, hãy phân rã nó thành nhiều phép kiểm tra nhị phân (có trích dẫn nguồn: có/không; trích dẫn đúng nguồn: có/không) thay vì một con số vô hướng mờ nhạt. Điều này càng quan trọng gấp đôi khi người chấm là một [`LLM-as-judge`](llm-as-judge.md).

## Đánh giá từng bước so với Đầu-cuối (Per-step vs end-to-end)

Đối với các lệnh gọi mô hình đơn lẻ, câu hỏi này không phát sinh. Nhưng đối với `Agent`, bạn cần cả hai:

- **Đầu-cuối (End-to-end)**: tác vụ có được hoàn thành hay không? Đây là con số có ý nghĩa với người dùng.
- **Từng bước (Per-step)**: mỗi lệnh gọi công cụ có hợp lý không, bước truy xuất có trả về đúng tài liệu không, kế hoạch vạch ra có giải quyết đúng yêu cầu không? Những kiểm tra này giúp khoanh vùng vị trí lỗi khi bài kiểm tra đầu-cuối thất bại.

Đánh giá đầu-cuối cho bạn biết *rằng* hệ thống đã hỏng; đánh giá từng bước cho bạn biết nó hỏng *ở đâu*. Chi tiết được trình bày trong bài [đánh giá `Agent`](agent-evals.md).

## Kích thước mẫu có ý nghĩa thống kê

Các bộ đánh giá nhỏ thường nói dối. Với 20 ca kiểm thử, một cú nhảy từ 70% lên 80% chỉ tương đương với hai ví dụ — hoàn toàn là nhiễu (noise). Hướng dẫn ước lượng sơ bộ:

- 20–50 ca: đủ để khởi động bánh đà, nhưng chưa đủ để so sánh các prompt với nhau.
- 100–200 ca cho mỗi kiểu lỗi mà bạn quan tâm: mức chênh lệch khoảng ~10 điểm phần trăm bắt đầu mang ý nghĩa thực sự.
- Chạy các hệ thống ngẫu nhiên (stochastic) nhiều lần trên mỗi ca kiểm thử; báo cáo độ phân tán (spread) chứ đừng chỉ báo cáo một lần chạy ăn may.

Khi còn nghi ngờ, hãy tính khoảng tin cậy (confidence interval) trước khi ăn mừng. Nếu khoảng tin cậy trải dài qua cả vùng "cải thiện" lẫn vùng "suy thoái", hãy thu thập thêm ca kiểm thử thay vì vội vã xuất xưởng.
