# Vệ sinh ngữ cảnh (Context Hygiene)

Sổ tay về `Harness` đã trình bày kỹ năng [kỹ thuật ngữ cảnh (context engineering)](../track-harness/context-engineering.md): những gì mô hình nhìn thấy trong một phiên làm việc, được tinh tuyển qua từng lượt. `Context hygiene` (vệ sinh ngữ cảnh) là phiên bản ở cấp độ `Loop` của cùng kỷ luật đó: thứ gì sống sót qua các lượt và giữa các lần thử, và — quan trọng không kém — thứ gì bị chủ đích tiêu hủy. `Harness` quản lý một cửa sổ ngữ cảnh; `Loop` quản lý cả một vòng đời.

## Chỉnh sửa ngữ cảnh trong các phiên chạy dài

Các `Loop` chạy dài hạn thường chết vì kiệt quệ ngữ cảnh trước khi chết vì bất kỳ nguyên nhân nào khác. Công trình quản lý ngữ cảnh của Anthropic tấn công trực diện vào vấn đề này: cơ chế chỉnh sửa ngữ cảnh (context editing) tự động dọn sạch các lệnh gọi công cụ và kết quả cũ kỹ khi cửa sổ tiến gần đến giới hạn, giữ cho mạch hội thoại không bị đứt gãy. Trong bài đánh giá tìm kiếm web kéo dài 100 lượt của họ, chỉnh sửa ngữ cảnh đã giúp các `Agent` hoàn thành những quy trình làm việc mà nếu không có nó sẽ thất bại hoàn toàn, đồng thời cắt giảm 84% lượng token tiêu thụ. Trên các bài benchmark đa bước, chỉ riêng việc chỉnh sửa ngữ cảnh đã cải thiện hiệu suất thêm 29% so với mức cơ sở; khi kết hợp với công cụ bộ nhớ (memory tool), con số này lên tới 39%. Bài học này có giá trị tổng quát vượt ra ngoài phạm vi một nhà cung cấp: đầu ra cũ của công cụ là thứ ít giá trị nhất nhưng lại chiếm diện tích lớn nhất trong cửa sổ ngữ cảnh, và một `Loop` không bao giờ cắt tỉa chúng đang phải trả tiền thuê chỗ cho rác.

## Tệp tin là bộ nhớ của `Loop`

Trạng thái cần phải sống sót nên nằm hoàn toàn bên ngoài cửa sổ ngữ cảnh, trong các tệp văn bản thuần túy mà `Agent` đọc và ghi: một tệp `plan.md`, một tệp `TODO.md` với các ô đánh dấu, một tệp chốt chặn (ratchet file) ghi lại điểm số tốt nhất tính đến hiện tại. Mô hình sẽ quên giữa các lần chạy; nhưng kho lưu trữ (repository) thì luôn nhớ. Đây chính là thành phần "trạng thái ngoài" (external state) của Osmani và là bí quyết thầm lặng đằng sau mọi mẫu thiết kế chạy tự động — [vòng lặp chạy qua đêm](build-overnight.md) thực chất chỉ là một tệp ratchet và một tệp báo cáo được bọc bởi một vòng lặp `while` xung quanh. Độc giả của phương pháp bộ não thứ hai (second-brain) sẽ nhận ra ngay nước đi này: bộ nhớ làm việc là phù du, vì vậy bất cứ thứ gì quan trọng đều phải được ghi chép xuống.

## Ngữ cảnh mới tinh cho mỗi lần thử

Một kỷ luật nghe có vẻ ngược đời, được cộng đồng làm vòng lặp Ralph rút ra sau nhiều vấp váp: giữa các lần thử, hãy vứt bỏ toàn bộ lịch sử hội thoại (transcript). Lịch sử hội thoại của một lần thử thất bại phần lớn chỉ là bản ghi của sự hỗn loạn — những giả thuyết sai lầm, những cuộc tìm kiếm vào ngõ cụt, những lời xin lỗi — và việc mang nó sang lần thử tiếp theo sẽ đầu độc phiên mới, khiến mô hình coi sự hỗn loạn đó như những sự thật đã được xác lập. Vòng lặp nguyên bản của Geoffrey Huntley chủ đích khởi động lại `Agent` từ trạng thái lạnh (cold start) ở mỗi vòng lặp; cùng những tệp tin đó được đưa vào ngữ cảnh ở mỗi lượt, nhờ vậy tệp prompt và kho mã nguồn là bộ nhớ duy nhất, giúp mỗi lần thử đều nhận được một cửa sổ sạch sẽ cộng với mục tiêu.

Thứ được phép bắc cầu qua khoảng trống giữa các lần thử là một bản chưng cất cô đọng, chứ không phải lịch sử: đầu ra của bài test bị lỗi, danh sách khiếm khuyết từ `Critic`, trạng thái hiện tại của danh sách việc cần làm (todo). Đó chính xác là thứ mà bài [thực hành bài kiểm tra mục tiêu](build-goal-test.md) đưa ngược trở lại — luồng lỗi chuẩn (`stderr`) của script mục tiêu, ngoài ra không còn gì khác.

## Thứ gì cần mang theo, thứ gì cần đốt bỏ

- **Mang theo (Carry)**: mục tiêu, tệp todo, đầu ra mới nhất của `Verifier`, phán quyết của `Critic`, điểm số ratchet.
- **Đốt bỏ (Burn)**: lịch sử hội thoại thăm dò, đầu ra công cụ cồng kềnh, những lời bình luận lan man của `Agent` trong lúc chạy, bất cứ điều gì nó tự nhận xét về việc mọi thứ đang tiến triển tốt đẹp ra sao.

Phép thử cho từng mục rất thẳng thắn: liệu một `Agent` mới tinh, có năng lực có hành động tốt hơn khi đặt thông tin này trước mặt nó hay không? Đầu ra của `Verifier` vượt qua phép thử đó. Còn bản log dài 40.000 token ghi lại cảnh lần thử trước thất bại thì không. `Context hygiene` là việc đưa ra quyết định thay cho lần thử tiếp theo, đó là lý do tại sao nó thuộc về `Loop` chứ không thuộc về mô hình.
