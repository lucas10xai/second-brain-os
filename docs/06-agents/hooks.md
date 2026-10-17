# Hooks

`Hooks` kích hoạt dựa trên sự kiện (events) thay vì dựa trên lịch trình thời gian. Chúng là công cụ hoàn hảo cho những việc bắt buộc phải diễn ra trong mọi lần thực thi — cũng chính xác là nhóm những việc mà nếu chỉ dặn bằng lời trong prompt thì sớm muộn gì `Agent` cũng sẽ có lúc quên.

## Những việc đáng gắn vào Hooks

**Kiểm tra tính hợp lệ trước khi ghi file (Validation before a write).** Kiểm tra xem `Frontmatter` có phân tích cú pháp (parse) thành công không và các trường bắt buộc đã có đủ chưa. Một trang sai định dạng bị bắt lại ngay thời điểm ghi file chỉ là một chuyện nhỏ như con thỏ; nhưng nếu để một tháng sau mới phát hiện ra thì nghĩa là suốt tháng đó trang ấy đã hoàn toàn vô hình trước mọi câu truy vấn.

**Chạy `Lint` sau mỗi lượt thực thi.** Các liên kết đứt gãy (broken links) được phát hiện ngay tại khoảnh khắc chúng vừa sinh ra — cũng chính là lúc vẫn còn đầy đủ ngữ cảnh trong phiên làm việc để sửa chúng một cách chuẩn xác.

**Tạo commit sau một lượt chạy theo lịch.** Loại bỏ hoàn toàn khả năng một lượt chạy đã sửa đổi tới bốn mươi file nhưng lại rời đi mà không để lại một bản commit `Git` nào.

**Thông báo khi có thao tác xóa (Notify on deletion).** Bất kỳ lệnh xóa nào, vào bất cứ lúc nào, đều phải được đẩy thông báo nổi lên. Việc xóa trang hiếm khi xảy ra đến mức một thông báo như vậy hầu như không gây phiền nhiễu gì, nhưng lại cực kỳ quan trọng vào đúng khoảnh khắc nó phát tín hiệu.

## Những việc KHÔNG đáng gắn vào Hooks

Bất cứ tác vụ nào chạy chậm. Một hook kích hoạt trên mỗi lần ghi file và mất hai giây để chạy sẽ biến một lượt `Ingest` bốn mươi trang thành một khoảng chờ đợi dài chín mươi giây — và sớm muộn gì bạn cũng sẽ tắt bỏ nó.

Bất cứ việc gì đòi hỏi sự phán đoán ngữ nghĩa. `Hooks` chỉ dành cho các bước kiểm tra cơ học. Một hook cố gắng phán đoán xem nội dung một trang đã "đủ hay" chưa sẽ mắc sai lầm ở cả hai chiều (chặn nhầm trang tốt và bỏ lọt trang tệ).

## Giữ cho Hooks luôn nhanh và im lặng

Một hook nên hoàn tất trong thời gian chưa đầy một giây và không in ra bất kỳ thông báo nào khi mọi thứ đều hợp lệ (pass). Những hook cứ chạy thành công cũng in log ra màn hình sẽ tập cho bạn thói quen phớt lờ kết quả đầu ra của hook — và điều đó chẳng khác nào việc không có hook nào cả vào đúng ngày có một bước kiểm tra bị lỗi thực sự.

## Hành vi khi xảy ra lỗi (Failure behaviour)

Hãy quyết định thật dứt khoát xem liệu một hook bị lỗi có chặn đứng (block) thao tác đang thực hiện hay không.

Các hook kiểm tra tính hợp lệ (validation hooks) bắt buộc phải chặn: một trang không vượt qua được bước kiểm tra lược đồ (schema validation) thì không được phép ghi xuống đĩa. Ngược lại, các hook gửi thông báo (notification hooks) thì không nên chặn: một thông báo gửi thất bại không phải là lý do chính đáng để vứt bỏ toàn bộ kết quả công việc vừa làm.

Tình huống tệ nhất là một hook có quyền chặn nhưng lại bị lỗi vì một nguyên nhân ngoại cảnh không liên quan và âm thầm làm tê liệt lịch chạy `Ingest` tự động của bạn suốt cả tuần trời. Bất cứ thứ gì được trao quyền chặn thao tác đều phải đơn giản đến mức nó chỉ có thể báo lỗi vì đúng lý do mà nó được sinh ra.

## Tiếp theo

[Skills và Slash commands](skills-and-commands.md)
