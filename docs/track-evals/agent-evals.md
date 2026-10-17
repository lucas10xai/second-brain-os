# Đánh giá Agent (Agent Evals)

Một lần sinh phản hồi đơn lẻ là một hàm số; còn một `Agent` là cả một tiến trình. Nó lập kế hoạch, gọi công cụ, đọc kết quả và tự phục hồi (hoặc không) sau những sai lầm của chính mình. Chỉ đánh giá câu trả lời cuối cùng chẳng khác nào nhận xét cả một ván cờ chỉ qua nước đi cuối. Trang này phát triển tiếp từ bài [thiết kế bộ đánh giá](designing-evals.md).

## Quỹ đạo thực thi (`Trajectory`), không chỉ là kết quả đầu ra

Hãy ghi log toàn bộ `Trajectory`: mọi lượt gọi mô hình, lệnh gọi công cụ, kết quả trả về từ công cụ và các lần thử lại. Sau đó đánh giá ở hai cấp độ:

- **Kết quả (Outcome)**: tác vụ đã hoàn thành chưa, và trạng thái cuối cùng có chính xác không? Tốt nhất nên kiểm tra trực tiếp trên *môi trường* (tệp tin đã tồn tại, dòng dữ liệu đã được chèn vào bảng, bộ test đã vượt qua), chứ không dựa vào lời tuyên bố hoàn thành của `Agent`. Các `Agent` luôn tuyên bố chiến thắng một cách cực kỳ lưu loát.
- **Quỹ đạo (`Trajectory`)**: con đường đi đến kết quả có hợp lý không? Hãy đếm số bước, phát hiện các vòng lặp quẩn, gắn cờ những lỗi công cụ bị âm thầm phớt lờ. Hai `Agent` có cùng tỷ lệ thành công hoàn toàn không ngang bằng nhau nếu một bên mất tới 40 lượt và đốt gấp 20 lần lượng token.

## Tính chính xác của lệnh gọi công cụ (Tool-call correctness)

Những phép kiểm tra mang tính cơ học nhất nhưng mang lại hiệu suất phát hiện lỗi cao nhất:

- Chọn đúng công cụ cho ý định tương ứng.
- Các đối số (arguments) hợp lệ và được trích xuất chính xác từ ngữ cảnh (ID, ngày tháng, bộ lọc — đây là nơi các `Agent` thường âm thầm làm sai).
- Tuân thủ các ràng buộc về thứ tự (`search` trước khi `answer`, `read` trước khi `write`).
- Xử lý lỗi: chủ động bơm một lỗi công cụ vào giữa `Trajectory` và kiểm tra xem `Agent` có thử lại hoặc báo cáo lỗi hay không, thay vì tự ảo giác ra kết quả.

Đây là các phép kiểm tra bằng code (code assertions) chạy trực tiếp trên bản ghi `Traces`, không phải lệnh gọi giám khảo LLM. Hãy để dành [`LLM-as-judge`](llm-as-judge.md) cho những câu hỏi kiểu "kế hoạch vạch ra có hợp lý hay không".

## Đánh giá dựa trên môi trường (Environment-based evals)

Tiêu chuẩn vàng: cung cấp cho `Agent` một môi trường cô lập (một Docker container, một cơ sở dữ liệu đã nạp sẵn dữ liệu mẫu, một mock API) và chấm điểm *trạng thái* của môi trường sau khi chạy xong bằng các bài kiểm tra thực thi được. Thiết lập tất định, dọn dẹp bằng chương trình, không có sự mơ hồ của người chấm. Cách này tốn nhiều công sức xây dựng hơn so với một `Golden set` gồm các bản ghi hội thoại tĩnh, nhưng hoàn toàn xứng đáng cho bất kỳ tác vụ nào làm thay đổi trạng thái hệ thống.

## Các bộ benchmark `Harness`, phiên bản 2026

Các bộ benchmark công khai dùng để so sánh các mô hình và `Harness` với nhau, chứ không phải để đo lường sản phẩm của bạn — nhưng chúng cho thấy một hệ thống đánh giá dựa trên môi trường tốt sẽ trông như thế nào:

- Họ [SWE-bench](https://www.swebench.com/) — các issue thực tế trên GitHub, được chấm điểm bằng chính bộ test của kho mã nguồn đó; SWE-bench Verified (500 bài đã được con người kiểm duyệt) vẫn là con số tiêu điểm cho các coding `Agent`, với các mô hình tiên phong hiện đã đạt mức 80–90% và cả họ benchmark này đang đẻ thêm nhiều biến thể khó hơn khi tập gốc dần bão hòa.
- [Terminal-Bench](https://www.tbench.ai/) — phiên bản 2.0 gồm 89 tác vụ dòng lệnh được kiểm duyệt thủ công chạy trong các Docker container thực, chấm điểm bằng các bài test thực thi được. Đây là khuôn mẫu sạch sẽ nhất để bạn học hỏi.
- [GAIA](https://arxiv.org/abs/2311.12983) — các tác vụ trợ lý tổng quát đòi hỏi duyệt web, dùng công cụ và suy luận đa bước.
- [tau2-bench](https://github.com/sierra-research/tau2-bench) — tương tác giữa công cụ - `Agent` - *người dùng* với một khách hàng mô phỏng; đo lường hội thoại dưới các ràng buộc chính sách.
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) — hơn 200 bản hiện thực hóa của các bộ đánh giá trên quy tụ dưới một framework duy nhất.

## Tích hợp vào CI

`Evals` thuộc về đường ống CI/CD, không phải nằm trong một tệp notebook:

- Chạy bộ kiểm thử khói (smoke suite) nhỏ gọn (chỉ gồm các kiểm tra tất định) trên mỗi PR; chạy toàn bộ bộ đánh giá vào ban đêm (nightly) và trước mỗi đợt phát hành.
- Đặt cổng chặn (`Gate`) cho thao tác gộp nhánh (merge) dựa trên một ngưỡng điểm; chạy $N$ lần thử cho mỗi ca và xét ngưỡng trên giá trị trung bình.
- Ghim cố định phiên bản mô hình trong CI, và coi việc nâng cấp phiên bản mô hình là một thay đổi bắt buộc phải vượt qua bộ đánh giá giống như bất kỳ thay đổi mã nguồn nào khác.

Các công cụ giúp quá trình này bớt vất vả hơn được khảo sát chi tiết tại bài [công cụ đánh giá](tooling.md).
