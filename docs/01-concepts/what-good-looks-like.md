# Thế nào là một hệ thống vận hành tốt

Những tiêu chí đánh giá cụ thể giúp bạn biết chắc chắn liệu hệ thống của mình có đang hoạt động hiệu quả hay không thay vì chỉ phỏng đoán cảm tính.

## Bài kiểm tra thực tế

Hãy thử hỏi hệ thống về một nội dung nào đó bạn chỉ còn nhớ mang máng là mình từng đọc cách đây vài tháng, nhưng không tài nào nhớ nổi tên gọi chính xác của nó.

Nếu hệ thống trả về đúng ý tưởng đó, chỉ rõ các nguồn tài liệu gốc, kèm theo hai khái niệm liên quan mà bạn đã quên bẵng đi — nghĩa là nó đang vận hành tốt. Ngược lại, nếu nó không tìm thấy gì, hoặc chỉ trả về một đoạn giải thích chung chung mà bất kỳ mô hình AI nào cũng có thể tự bịa ra, nghĩa là hệ thống chưa đạt yêu cầu.

## Các dấu hiệu của một Vault khỏe mạnh

**Bạn tìm kiếm trong Vault trước khi lên mạng tìm kiếm.** Đây là tín hiệu mạnh mẽ nhất, và thói quen này sẽ tự động hình thành một khi mật độ liên kết trong Vault của bạn đã đủ dày.

**Câu trả lời luôn trích dẫn các trang bạn có thể mở xem ngay,** và nội dung trong các trang đó khớp chính xác với những gì câu trả lời trình bày.

**Đồ thị xuất hiện những cụm chủ đề (clusters) mà bạn không hề chủ đích lên kế hoạch trước.** Đây là bằng chứng cho thấy hệ thống đang phản ánh trung thực những gì bạn thực sự dành sự chú ý, chứ không phải những danh mục cứng nhắc bạn áp đặt cho nó từ đầu.

**Các nguồn tài liệu mới chủ yếu cập nhật vào những trang hiện có** thay vì liên tục đẻ ra trang mới. Điều đó chứng tỏ Vault đã nắm bắt được bộ khung các khái niệm cốt lõi và đang đi vào chiều sâu thay vì chỉ lan rộng bề ngang.

**Đôi khi hệ thống phản biện lại chính bạn,** bởi vì trong kho tư liệu của bạn có lưu giữ lập luận của cả hai phía về cùng một vấn đề.

## Các dấu hiệu cảnh báo sự cố

**Tỷ lệ trang mồ côi (orphan rate) tăng dần.** Quy trình Ingest đã ngừng tạo liên kết giữa các trang. Hãy xem bài [Các chỉ số đồ thị](../05-graphs/metrics.md).

**Các trang đọc lên giống như những bản tóm tắt đơn thuần** hơn là văn bản giải thích bản chất vấn đề. Hợp đồng định dạng trang (page contract) trong file `CLAUDE.md` cần được siết chặt lại.

**Các trang khái niệm nằm im hàng tháng trời không được cập nhật dù nguồn tài liệu mới vẫn nạp vào đều đặn.** Tư liệu mới đang bị đẩy sang các trang mới tinh thay vì bồi đắp vào những trang sẵn có, dẫn đến tình trạng có tới bốn trang khác nhau cùng viết về một thứ.

**Bạn ngừng mở Vault ra xem.** Đây là dấu hiệu thẳng thắn nhất. Nguyên nhân thường là do khâu thu thập (capture) bị rườm rà đứt gãy, chứ không phải bản thân ý tưởng Second Brain thất bại.

## Lộ trình phát triển thực tế theo thời gian

**Tuần đầu tiên.** Thiết lập hệ thống, nạp mười đến hai mươi nguồn tài liệu. Cảm giác lúc này chẳng khác mấy một thư mục chứa file nhưng lại tốn thêm nhiều bước thao tác. Điều này hoàn toàn bình thường và đây cũng chính là giai đoạn hầu hết mọi người bỏ cuộc.

**Tuần thứ hai đến tuần thứ tư.** Đạt mốc năm mươi đến một trăm nguồn tài liệu. Khoảnh khắc đầu tiên bạn chứng kiến Vault tự động kết nối hai bài viết bạn đọc cách nhau cả mấy tuần lễ. Đây là lúc hệ thống bắt đầu trả lại giá trị xứng đáng với công sức thiết lập ban đầu.

**Tháng thứ ba.** Quy mô đạt vài trăm trang. Hệ thống trả lời các câu hỏi nhanh hơn nhiều so với việc bạn tự lục tìm đọc lại, đồng thời làm trồi lên những kiến thức bạn từng lưu nhưng đã quên sạch.

**Tháng thứ sáu.** Hệ thống nắm rõ những tri thức mà chính bạn cũng không còn nhớ là mình đã từng học qua. Đó chính là trạng thái "trái ngọt" mà ai cũng nhắc tới — nó hoàn toàn có thật, và nó đòi hỏi sáu tháng đều đặn nạp tư liệu cho hệ thống.

## Tiếp theo

[Thiết lập](../02-setup/README.md).
