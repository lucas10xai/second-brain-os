# Điều kiện dừng (Stop Conditions)

Bài toán thiết kế khó nhất trong một `Loop` không phải là làm cho `Agent` chạy, mà là làm cho nó dừng lại. Một `Agent` sẽ vui vẻ báo cáo thành công mà nó chưa thực sự đạt được, và một `Loop` không có lối thoát chính là một hóa đơn không có trần chi phí. Mọi `Loop` nghiêm túc đều mang theo nhiều phanh hãm độc lập, chỉ cần một trong số chúng kích hoạt là phiên chạy sẽ kết thúc.

## Bài kiểm tra mục tiêu (Goal tests)

Điểm dừng chính yếu là một định nghĩa hoàn thành có thể thực thi được: một script trả về mã thoát 0 (exit 0) khi công việc đạt yêu cầu — bộ test vượt qua, linter sạch lỗi, bản build biên dịch thành công. Nếu mục tiêu không thể viết thành một script, bạn không có một tác vụ có thể đưa vào `Loop`; bạn đang có một phiên làm việc tương tác, và điều đó hoàn toàn bình thường, nhưng đừng tự huyễn hoặc mình. Mục tiêu "cải thiện code" không bao giờ có thể kết thúc. Còn "tất cả các bài test trong `tests/` đều đạt và `ruff check .` không báo lỗi gì" thì có thể. [Trang thực hành bài kiểm tra mục tiêu](build-goal-test.md) chuyển hóa nguyên lý này thành bốn mươi dòng lệnh bash.

Hãy lưu ý thứ vắng mặt ở đây: ý kiến chủ quan của chính `Agent`. Câu nói "`Agent` bảo rằng đã xong" không bao giờ là một `Stop condition` — đó chính là lời tuyên bố mà bài kiểm tra mục tiêu sinh ra để kiểm chứng, một luận điểm được đào sâu thêm trong bài [bộ phản biện và xác minh](critics-and-verification.md).

## Ngân sách (Budgets)

Các bài kiểm tra mục tiêu làm nhiệm vụ dừng những phiên chạy thành công. Ngân sách dừng tất cả những trường hợp còn lại, và bạn sẽ cần ít nhất ba loại ngân sách vì chúng thất bại theo những cách khác nhau:

- **Số vòng lặp (Iterations)** — mức trần cứng cho số lần thử. Hãy bắt đầu nhỏ; năm lần thử sẽ giải quyết được hầu hết các vấn đề khả thi, và những bài toán mà hai mươi lần thử giải được nhưng năm lần thử bó tay là cực kỳ hiếm.
- **Token hoặc chi phí tiền bạc** — mức trần chi tiêu cho mỗi phiên chạy. Các CLI không giao diện (headless CLIs) đều báo cáo chi phí cho mỗi lần gọi (`--output-format json` bao gồm trường `total_cost_usd` trong `Claude Code`), nhờ đó script bọc ngoài (wrapper) có thể cộng dồn và thoát khi chạm ngưỡng.
- **Thời gian thực (Wallclock)** — giới hạn thời gian chờ (timeout) cho toàn bộ phiên chạy và cho từng lần thử. Một `Agent` bị kẹt khi chờ một câu lệnh treo sẽ đốt hàng giờ đồng hồ chứ không phải đốt token.

Ngân sách là khoản bảo hiểm giá rẻ; sai lầm duy nhất là đặt chúng quá hào phóng "để cho nó có không gian xoay sở". Ngân sách hào phóng sẽ biến lỗi phần mềm thành hóa đơn thanh toán.

## Chốt chặn một chiều (Ratchets)

Một ngân sách vẫn cho phép mười vòng lặp suy thoái từ từ. Nhưng chốt chặn một chiều (ratchet) thì không: nó đòi hỏi mỗi vòng lặp phải vượt qua trạng thái tốt nhất trước đó trên một thang điểm đo lường được — số bài test vượt qua, số hạng mục được đánh dấu hoàn thành, số lỗi còn lại — nếu không `Loop` sẽ khôi phục (reset) lần thử đó và dừng hẳn. Tiến độ phải có tính đơn điệu tăng; đi ngang đồng nghĩa với thất bại. Đây là xương sống của các phiên chạy không người giám sát, được xây dựng cụ thể trong bài [vòng lặp chạy qua đêm](build-overnight.md).

## Phát hiện lặp tại chỗ (Detecting spin)

Một số thất bại diễn ra rất ồn ào. Nhưng sự lặp tại chỗ (spin) lại diễn ra âm thầm: `Agent` lặp đi lặp lại cùng một truy vấn tìm kiếm, tạo ra một bản diff rỗng, hoặc đâm đầu vào cùng một bài test lỗi với cùng một thông báo qua hết lần thử này đến lần thử khác. Hãy phát hiện điều này bằng cách tạo dấu vân tay (fingerprint) cho trạng thái giữa các vòng lặp — tập hợp tên các bài test bị lỗi, mã băm (hash) của bản diff, các lệnh gọi công cụ cuối cùng đã phát ra. Hai dấu vân tay giống hệt nhau liên tiếp có nghĩa là `Loop` không hề hội tụ, và thử thêm cũng chỉ đốt sạch ngân sách. Hãy dừng sớm và nêu rõ lý do.

## Bàn giao lại cho con người

Mọi lối thoát không phải là trạng thái xanh của bài kiểm tra mục tiêu (goal-test-green) đều phải kết thúc bằng một bản báo cáo gửi cho con người: những gì đã được thử, cây thư mục làm việc (working tree) đang ở trạng thái nào, phanh hãm nào đã kích hoạt và bằng chứng tốt nhất của `Loop` giải thích lý do tại sao. Cơ chế leo thang (escalation) là một tính năng. Một `Loop` thất bại một cách rõ ràng, dễ hiểu ở lần thử thứ ba có giá trị hơn nhiều so với một `Loop` vùng vẫy vô vọng đến lần thử thứ năm mươi, bởi vì bản báo cáo giúp bạn biết nên sửa bài kiểm tra mục tiêu, nâng ngân sách hay tự tay tiếp quản lại tác vụ. [Trang các mẫu thiết kế](patterns.md) sẽ chỉ ra cách các biến thể chạy tự động chuẩn hóa điều này thành bản báo cáo buổi sáng.
