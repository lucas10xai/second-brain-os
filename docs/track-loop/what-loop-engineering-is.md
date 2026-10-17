# Kỹ thuật vòng lặp (Loop Engineering) là gì

Kỹ thuật vòng lặp (Loop engineering) là kỷ luật thiết kế hệ thống điều khiển vận hành một `Agent`: phần quyết định sẽ gửi prompt gì, xác minh kết quả ra sao, có thử lại hay không và khi nào thì dừng lại. Bạn ngừng làm những việc đó bằng tay qua từng lượt, mà mã hóa chúng một lần duy nhất. Kỹ thuật viết prompt (Prompt engineering) tối ưu hóa một tin nhắn đơn lẻ. Kỹ thuật vòng lặp tối ưu hóa cả chu trình — ai gọi mô hình tiếp theo, hướng tới mục tiêu nào, được phán quyết bởi bài kiểm tra nào và nằm trong ngân sách bao nhiêu.

## Nguồn gốc của thuật ngữ

Vào ngày 7 tháng 6 năm 2026, Peter Steinberger đã đăng dòng trạng thái đặt tên cho bước chuyển dịch này: "Bạn không nên ngồi viết prompt cho các coding `Agent` nữa. Bạn nên thiết kế các vòng lặp (`Loop`) để tự động gửi prompt cho `Agent` của mình." Bài đăng đạt hàng triệu lượt xem chỉ trong một ngày. Bài tiểu luận "Loop Engineering" của Addy Osmani xuất hiện gần như ngay lập tức sau đó (được O'Reilly Radar đăng lại vào ngày 22 tháng 6), phác họa cấu trúc giải phẫu cho ý tưởng này: tự động hóa (automations), git worktrees, kỹ năng (skills), bộ kết nối (connectors), subagents và trạng thái ngoài (external state) để tiến độ được bảo toàn giữa các lần chạy. Boris Cherny của Anthropic nói thẳng thắn: "Tôi không viết prompt cho Claude nữa. Tôi có các `Loop` đang chạy để gửi prompt cho Claude... Công việc của tôi là viết các `Loop`."

Các thực hành này đã có trước khi cái tên ra đời. Vòng lặp Ralph (Ralph loop) của Geoffrey Huntley có từ tháng 7 năm 2025; Simon Willison đã viết bài "Designing agentic loops" vào tháng 9 năm đó, định nghĩa `Agent` là một thứ "chạy các công cụ trong một vòng lặp để đạt được mục tiêu". Tháng 6 năm 2026 đơn giản là thời điểm kỷ luật này có một nhãn tên chính thức — tính đến khi sổ tay này được viết thì nó mới tròn ba tháng tuổi, vì vậy hãy lường trước việc bộ từ vựng sẽ còn biến động.

## Kỹ thuật viết prompt so với Kỹ thuật vòng lặp

Việc viết prompt thủ công tiêu tốn năng lực phán đoán của bạn qua từng lượt một: bạn đọc đầu ra, quyết định xem nó đã ổn chưa, rồi diễn đạt cú hích tiếp theo. Kỹ thuật vòng lặp chi tiêu năng lực phán đoán đó một lần duy nhất ngay từ đầu vào bốn tạo phẩm (artefacts): một mục tiêu được biểu diễn dưới dạng bài kiểm tra thực thi được, một chính sách thử lại (retry policy) đưa các lỗi ngược trở lại, một ngân sách giới hạn và một quy tắc dừng (`Stop condition`). Sau đó, `Loop` sẽ tự gửi prompt cho `Agent` và bạn chỉ duyệt kết quả đầu ra. Điểm nghẽn dịch chuyển từ việc viết chỉ dẫn sang việc chứng minh kết quả.

## Bốn trụ cột cốt lõi

- **`Context hygiene` (Vệ sinh ngữ cảnh)** — quyết định thứ gì được giữ lại giữa các lượt và các lần thử, cũng như thứ gì bị chủ đích vứt bỏ. Được trình bày chi tiết tại [vệ sinh ngữ cảnh](context-hygiene.md).
- **`Stop condition` (Điều kiện dừng)** — các bài kiểm tra mục tiêu (goal tests), ngân sách, chốt chặn một chiều (ratchets) và phát hiện lặp vô tận (spin detection), bởi vì câu nói "`Agent` bảo rằng đã xong" chỉ là một lời tuyên bố chứ không phải một điều kiện dừng. Được trình bày tại [điều kiện dừng](stop-conditions.md).
- **Một `Critic` thực thụ (Bộ phản biện)** — cơ chế xác minh mà `Agent` không thể tranh cãi, tách biệt hoàn toàn khỏi `Agent` thực hiện công việc. Được trình bày tại [bộ phản biện và xác minh](critics-and-verification.md).
- **Công cụ lũy đẳng (Idempotent tools)** — bất cứ thứ gì `Loop` thử lại sớm muộn cũng sẽ chạy hai lần, vì vậy mọi thao tác ghi mà `Agent` có thể chạm tới phải an toàn khi lặp lại. Một lệnh "tạo hóa đơn" được thử lại không được phép tạo ra hai hóa đơn; hãy thiết kế công cụ sao cho lần gọi thứ hai là một thao tác rỗng (no-op).

## Không đồng nhất với `Harness`

Trang web này đã có một cuốn sổ tay về [`Agent` `Harness`](../track-harness/what-a-harness-is.md) — bộ máy bao quanh mô hình: vòng lặp `while` bên trong, schema công cụ, phân quyền, quản lý cửa sổ ngữ cảnh. Kỹ thuật vòng lặp là kỷ luật điều khiển được đắp lên trên bộ máy đó. `Harness` thực thi một lượt; `Loop` quyết định liệu có nên có lượt tiếp theo hay không, lượt đó nên thử làm gì, ai phán quyết nó và khi nào toàn bộ quá trình kết thúc. Bạn cần cả hai: một `Harness` tốt nhưng thiếu kỷ luật `Loop` là cách cực nhanh để sản xuất ra những sản phẩm chưa được kiểm chứng, còn kỷ luật `Loop` mà không có một `Harness` tử tế thì chẳng có gì đáng tin cậy để điều hướng.
