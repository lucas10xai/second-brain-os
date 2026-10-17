# Các mẫu thiết kế vòng lặp (Patterns)

Năm hình thái `Loop` liên tục xuất hiện đi xuất hiện lại dưới nhiều tên gọi khác nhau. Mỗi hình thái đều phát huy giá trị trên một loại công việc cụ thể, và mỗi hình thái đều có những kiểu lỗi (failure modes) mà những người ủng hộ chúng thường nói giảm nói tránh. Dưới đây là danh sách trình bày đầy đủ cả hai mặt.

## Chạy trong vòng lặp (Run-in-a-loop / Ralph)

Bản gốc tháng 7 năm 2025 của Geoffrey Huntley: `while :; do cat PROMPT.md | claude-code ; done`. Hoàn toàn không có tầng điều phối (orchestration) nào — khi một phiên kết thúc, một phiên khác khởi động lạnh, đọc cùng tệp prompt và cùng kho mã nguồn đó, rồi tiếp tục công việc từ nơi phiên trước dừng lại thông qua các tệp tin trên ổ đĩa. Đây là minh chứng thuần khiết nhất cho thấy ngữ cảnh mới tinh cộng với tệp tin bền vững đánh bại một phiên làm việc kéo dài ngày càng suy thoái, và Anthropic hiện đã đóng gói nó thành plugin `ralph-wiggum` trong kho mã nguồn `Claude Code`.

Các kiểu lỗi được chính tác giả thừa nhận: những đoạn code giữ chỗ (placeholder implementations) chỉ cốt làm hài lòng trình biên dịch chứ không làm được gì khác; thức dậy với một cây mã nguồn không thể build; và nó chỉ hợp với các dự án làm mới từ đầu (greenfield) — chính Huntley cũng nói rằng ông sẽ không chạy Ralph trên một codebase sẵn có. Ralph giúp bạn đi được khoảng 90% chặng đường của phiên bản đầu tiên, với nút dừng bằng cơm của con người là chiếc phanh duy nhất.

## Lập kế hoạch - Thực thi - Xác minh (Plan-execute-verify)

Chia phiên chạy thành các pha: một lượt đầu tạo ra tệp kế hoạch, các lượt tiếp theo thực thi từng bước, và một `Verifier` làm cổng kiểm soát (`Gate`) cho mỗi bước. Rất tốt cho công việc đa bước nơi một prompt đơn lẻ dễ bị trượt khỏi quỹ đạo. Kiểu lỗi: kế hoạch nhanh chóng trở nên lỗi thời khi va chạm với thực tế, và một `Loop` thực thi răm rắp một kế hoạch lỗi thời sẽ nhân lên sai lầm theo cấp số nhân — `Verifier` bắt buộc phải chạy ở từng bước, chứ không phải chỉ chạy một lần vào lúc cuối.

## Cặp Sinh - Phản biện (Generator-critic pairs)

Một `Agent` thực hiện, một lượt chạy tách biệt khác phán xét dựa trên bảng tiêu chí (rubric) hẹp, và các khiếm khuyết sẽ được nạp vào lần thử tiếp theo. Sự tách biệt giữa người làm và người kiểm tra (`Maker`-`Checker`) chính là mấu chốt: kẻ thực thi không được phép tự chấm điểm cho mình. Kiểu lỗi: một bảng tiêu chí mơ hồ sẽ biến `Critic` thành cái máy tạo nhiễu; và khi bộ sinh cùng `Critic` dùng chung một mô hình và chung một ngữ cảnh, chúng sẽ chia sẻ cùng những điểm mù rồi hội tụ về việc tự khen lẫn nhau. Chi tiết xem tại [bộ phản biện và xác minh](critics-and-verification.md); cách ghép nối cụ thể xem tại [Thực hành: Bộ phản biện (`Critic`)](build-critic.md).

## Đấu loại / Chọn tốt nhất trong N (Tournament / best-of-n)

Khởi chạy song song $n$ lần thử — `git worktree` giúp cô lập việc này với chi phí rất rẻ — và để một `Verifier` chọn ra kẻ chiến thắng. Cực kỳ mạnh mẽ khi các lần thử có phương sai lớn và việc xác minh có chi phí rẻ. Kiểu lỗi: chi phí nhân lên $n$ lần bất kể có lần thử nào tốt hay không; và nếu thiếu một bộ chọn thực sự mạnh, bạn sẽ trả tiền gấp $n$ lần cho những đống rác đầy tự tin rồi chọn ra thứ rác tự tin nhất trong số đó. Phép thử bất đối xứng của `Verifier` sẽ quyết định liệu mẫu thiết kế này có đáng tiền hay không.

## Chạy tự động qua đêm kèm báo cáo hộp thư (Overnight unattended runs with mailbox reports)

Các phiên chạy có ngân sách, có chốt chặn một chiều (ratchet), được cô lập trên nhánh riêng, âm thầm làm việc trong lúc bạn ngủ và để lại một bản báo cáo buổi sáng bằng markdown: thứ gì đã cải thiện, thứ gì đã làm dừng `Loop`, thứ gì cần bạn ra quyết định. Đây là trạng thái đích của kỷ luật này, đồng thời là mẫu thiết kế có yêu cầu đầu vào khắt khe nhất — hội tụ mọi phanh hãm từ bài [điều kiện dừng (`Stop condition`)](stop-conditions.md), cộng thêm các thanh ray an toàn biến kịch bản tệ nhất trở nên nhàm chán. Kiểu lỗi: các `Loop` không người giám sát sẽ tạo ra những sai lầm không người giám sát, và khoản nợ đó đổ lên đầu bạn dưới dạng nợ đọc hiểu (comprehension debt) — tốc độ đẩy các thay đổi lên vượt quá khả năng hiểu của bạn về chúng. Lời cảnh báo của Osmani vẫn còn nguyên giá trị: hãy xây dựng `Loop` với tâm thế của một người định tiếp tục làm kỹ sư, chứ không phải chỉ là người bấm nút chạy.

## Lựa chọn giữa các mẫu thiết kế

Hãy bắt đầu với `Loop` đơn giản nhất có một `Verifier` thực thụ: vòng lặp thử lại thuần túy trong bài [Thực hành: Bài kiểm tra mục tiêu](build-goal-test.md). Thêm một `Critic` khi tình trạng "test xanh nhưng code bẩn" trở thành kiểu lỗi phổ biến của bạn. Chỉ tiến tới chạy song song hoặc chạy qua đêm một khi `Loop` đơn lẻ luôn dừng lại một cách rõ ràng, minh bạch trong mọi lần chạy — những mẫu thiết kế cầu kỳ hơn sẽ khuếch đại bất kỳ tính kỷ luật nào bạn đang có, bao gồm cả sự vô kỷ luật.
