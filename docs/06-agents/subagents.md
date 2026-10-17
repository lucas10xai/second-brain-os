# Subagents và xử lý song song

Các `Subagents` chạy với `Context window` riêng biệt của chính chúng. Đó là toàn bộ ý nghĩa cốt lõi của cơ chế này: một subagent đọc ba mươi trang để trả lời một câu hỏi sẽ không làm đầy `Context window` của phiên làm việc chính bằng cả ba mươi trang đó, mà chỉ trả về duy nhất câu trả lời cuối cùng.

## Khi nào nên phân nhánh song song (Fan out)

**Nghiên cứu xuyên suốt nhiều trang.** Hãy cử một subagent đi đọc toàn bộ một cụm chủ đề (cluster) và quay về với bản tóm tắt. Phiên làm việc chính sẽ giữ nguyên được ngân sách ngữ cảnh cho công việc thực sự đang làm.

**Các tài liệu nguồn độc lập nhau.** Việc `Ingest` mười bài viết không liên quan gì đến nhau có thể chạy song song cực kỳ trơn tru, bởi vì không có bài nào chạm vào cùng một trang `wiki/` của nhau.

**Kiểm chứng chéo (Verification).** Một `Agent` viết bài, một `Agent` khác kiểm tra lại các trang vừa viết đối chiếu với tài liệu nguồn. Ngữ cảnh tách biệt chính là thứ làm cho bước kiểm tra này thực sự có ý nghĩa; còn nếu để cùng một `Agent` tự đọc lại bài do chính nó vừa viết thì hầu như lúc nào nó cũng sẽ gật gù đồng ý với chính mình.

## Khi nào KHÔNG nên chạy song song

**Các tài liệu nguồn có liên quan đến nhau.** Ba bài viết cùng bàn về một chủ đề bắt buộc phải được `Ingest` tuần tự từng bài một. Nếu chạy song song, mỗi subagent sẽ tự tạo ra một trang khái niệm riêng một cách độc lập, và bạn sẽ nhận về hoặc là ba phiên bản khác nhau của cùng một khái niệm, hoặc là hai trong số đó bị ghi đè mất.

**Bất kỳ thao tác nào chạm vào file chỉ mục.** `index.md` và `log.md` là những file đơn lẻ mà mọi lượt chạy đều muốn ghi nối tiếp (append) vào. Việc ghi song song cùng lúc vào hai file này sẽ gây xung đột dữ liệu hoặc âm thầm làm mất các dòng bản ghi.

**Những tác vụ nhỏ.** Việc khởi tạo một subagent tiêu tốn chi phí thiết lập toàn bộ một ngữ cảnh mới. Chỉ để xử lý hai file thì chạy subagent còn chậm hơn là làm trực tiếp luôn trong phiên chính.

## Hợp nhất kết quả từ các luồng song song

Quy tắc giúp tránh hầu hết các xung đột: các `Subagents` chỉ được ghi vào các đường dẫn tách biệt nhau (disjoint paths), còn `Agent` cha (parent) sẽ đảm nhận việc hợp nhất (merge).

Hãy yêu cầu mỗi subagent báo cáo lại những gì nó dự định ghi đối với các file dùng chung thay vì tự ghi trực tiếp vào đó. `Agent` cha sẽ áp dụng toàn bộ các cập nhật cho `index.md` và `log.md` trong một lượt duy nhất, sau khi tất cả các `Subagents` đã hoàn thành và trả kết quả về. Bản thân các file trang nội dung thì hoàn toàn an toàn để ghi song song miễn là không có hai subagent nào được giao xử lý các tài liệu chồng lấp lên nhau.

Hãy luôn tạo commit `Git` trước bất kỳ lượt chạy song song nào. Một khi có sự cố xảy ra trong xử lý song song, nó sẽ làm hỏng hàng loạt file cùng một lúc.

## Chi phí

Xử lý song song không hề làm giảm tổng lượng token tiêu thụ; nó chỉ giúp giảm thời gian chờ đợi thực tế (wall-clock time) và bảo vệ `Context window` của phiên chính. Bốn `Subagents` sẽ tốn chi phí xấp xỉ gấp bốn lần so với một `Agent`.

Sự đánh đổi đó hoàn toàn xứng đáng cho một đợt nạp bổ sung dữ liệu lớn (backfill), nhưng lại là vô nghĩa đối với công việc `Ingest` hàng ngày chỉ có năm bài viết lưu từ web.

## Tiếp theo

[Hooks](hooks.md)
