# Các mô hình System One

Hầu hết các sản phẩm AI ngày nay đều được xây dựng dựa trên các mô hình ngôn ngữ lớn (LLM): bạn gửi văn bản vào, mô hình viết văn bản trả lại, nhả từng token một. Cách làm đó vừa chậm vừa đắt đỏ khi tất cả những gì phần mềm của bạn thực sự cần chỉ là một quyết định. "Các mô hình System One" (System One models) là một danh mục hoàn toàn mới — được TypeSafe AI giới thiệu vào ngày 15 tháng 9 năm 2026 thông qua mô hình mang tên Jev — được thiết kế để lấp đúng khoảng trống đó: đưa ra các quyết định định kiểu (typed decisions) cực nhanh thay vì sinh văn bản chậm chạp.


Phần kiến thức tương ứng trong khóa học chính nằm ở [Học phần 3: Các quyết định chi phí thấp](../course-3-gate/cheap-decisions.md) — bàn về mẫu kiến trúc cổng phân luồng (Gate) mà lớp mô hình này thường đảm nhiệm.

## Khung tư duy Kahneman

Tên gọi này mượn từ cuốn sách *Tư duy nhanh và chậm* (*Thinking, Fast and Slow*) của Daniel Kahneman. Hệ thống 1 (System 1) là phán đoán trực giác, diễn ra tức thì; Hệ thống 2 (System 2) là suy luận có chủ đích, diễn ra chậm rãi. Trong khung tham chiếu này, các mô hình LLM chính là những cỗ máy Hệ thống 2: chúng lập luận thành lời bằng văn xuôi. Luận điểm của TypeSafe là một phần rất lớn những việc mà phần mềm yêu cầu mô hình thực hiện — phân loại, định tuyến, chấm điểm, gác cổng — thực chất là công việc của Hệ thống 1, và việc phải trả độ trễ lẫn chi phí của LLM cho những tác vụ đó là một sự lãng phí. Nhà sáng lập của họ, Diogo Almeida (cựu thành viên OpenAI, từng làm việc trên RLHF và ChatGPT), gọi đây là "một lời gọi hàm mang trí tuệ tiên phong: nhận đầu vào là trạng thái phi cấu trúc, trả đầu ra là các quyết định xác suất có định kiểu".

## Những gì Jev thực sự trả về

Jev là mô hình phi tự hồi quy (non-autoregressive): nó hoàn toàn không sinh văn bản. Bạn gửi cho nó một trạng thái `state` (chuỗi ký tự, đối tượng JSON, hoặc mảng văn bản) kèm theo một hoặc nhiều câu hỏi có định kiểu, và nó sẽ trả lời tất cả trong một lượt chạy song song duy nhất. Có ba kiểu nguyên thủy (primitives):

- `Choice` — chọn một phương án trong tối đa 255 lựa chọn được định nghĩa sẵn, kèm theo xác suất cho từng lựa chọn
- `Score` — xếp đầu vào lên một thang đo có thứ tự từ 2 đến 10 mức
- `Noul` — phán đoán có/không được trả về dưới dạng một xác suất nằm giữa 0 và 1

Mọi câu trả lời đều mang một xác suất đã được hiệu chuẩn (calibrated probability). TypeSafe huấn luyện cơ chế này bằng phương pháp họ gọi là RLCD (Reinforcement Learning for Calibrated Decisions — Học tăng cường cho các quyết định được hiệu chuẩn), tối ưu hóa độ tự tin trung thực thay vì cố làm hài lòng người chấm điểm.

## Những lưu ý thẳng thắn

Mô hình này mới ra mắt cách đây ít ngày, và gần như mọi con số hiện có đều do chính nhà cung cấp đưa ra:

- Những tuyên bố tâm điểm — nhanh hơn khoảng 200 lần và rẻ hơn tới 400 lần so với các LLM hàng đầu — đến từ các bài kiểm chuẩn (benchmark) do chính đội ngũ của TypeSafe xây dựng, mà bản thân công ty cũng thừa nhận là nằm ở ngưỡng kịch trần thuận lợi.
- "Không ảo giác" (Zero hallucinations) thực chất có nghĩa là không có đầu ra nào *nằm ngoài lược đồ* (out-of-schema). Jev không thể tự bịa ra một phương án mà bạn không định nghĩa; nhưng nó hoàn toàn vẫn có thể chọn sai phương án.
- Kiến trúc, kích thước mô hình và bộ trọng số đều không được tiết lộ. Chưa có bài báo khoa học nào qua bình duyệt (peer-reviewed). Khả năng duy trì độ hiệu chuẩn khi phân phối dữ liệu dịch chuyển (distribution shift) vẫn chưa được chứng minh, như những người hoài nghi như Anthony Maio đã chỉ ra.

Hãy coi cơ chế kỹ thuật này là có thật, còn các con số phóng đại là thông điệp tiếp thị cho đến khi có các đánh giá độc lập. Để biết những tác vụ nào thực sự phù hợp với nó, hãy xem bài [Jev phù hợp với việc gì](what-jev-is-good-for.md); để dùng thử, hãy xem bài [bắt đầu với Jev](getting-started.md); và để tra cứu nguồn dẫn, hãy xem trang [tài nguyên tham khảo](resources.md).
