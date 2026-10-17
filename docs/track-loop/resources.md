# Tài nguyên tham khảo (Resources)

Một lời cảnh báo trước tiên: thuật ngữ "kỹ thuật vòng lặp" (loop engineering) mới được đặt ra vào tháng 6 năm 2026 và mới chỉ ba tháng tuổi tại thời điểm trang này được viết. Những thực hành bên dưới vững chắc hơn nhiều so với cái nhãn tên — chính Steinberger vào giữa tháng 7 cũng đã đặt câu hỏi liệu cuộc thảo luận đã dịch chuyển từ vòng lặp (`Loop`) sang đồ thị (graphs) hay chưa. Hãy đọc để nắm bắt cơ chế vận hành, và đừng quá câu nệ vào từ vựng.

## Nguồn gốc tên gọi

- [Bài đăng của Peter Steinberger](https://x.com/steipete/status/2063697162748260627) — câu nói tạo nên làn sóng vào tháng 6 năm 2026: "Bạn không nên ngồi viết prompt cho các coding `Agent` nữa. Bạn nên thiết kế các vòng lặp (`Loop`) để tự động gửi prompt cho `Agent` của mình."
- [Loop Engineering](https://www.oreilly.com/radar/loop-engineering/) — Bài tiểu luận của Addy Osmani, được đăng lại trên O'Reilly Radar. Giải phẫu chi tiết cấu trúc: tự động hóa, worktrees, kỹ năng (skills), bộ kết nối (connectors), subagents, trạng thái ngoài — cùng những lời cảnh báo thẳng thắn ở phần kết về gánh nặng xác minh và nợ đọc hiểu (comprehension debt).
- [Code review in the age of AI](https://addyosmani.com/blog/code-review-ai/) — Bài viết song hành của Osmani; câu đúc kết "công việc của bạn là xuất xưởng đoạn code mà bạn đã xác nhận là hoạt động đúng" gói gọn toàn bộ cuốn sổ tay này trong một dòng.
- [What is loop engineering?](https://www.ibm.com/think/topics/loop-engineering) — Trang chuyên đề của IBM; hữu ích như một định nghĩa chuẩn mực mang tính tổ chức, phân tích rất sâu về các rủi ro (nợ đọc hiểu, nợ ý định, sự đầu hàng nhận thức).

## Bài báo khoa học

- [Stop Hand-Holding Your Coding Agent](https://arxiv.org/pdf/2607.00038) — Sandeco Macedo. Góc nhìn học thuật: các điều kiện dừng (`Stop condition`), thành phần xác minh (`Verifier`) và phản biện (`Critic`) được xem như hạ tầng vòng lặp hạng nhất.
- [Less Context, Better Agents](https://arxiv.org/pdf/2606.10209) — kỹ thuật ngữ cảnh hiệu quả cho các `Agent` sử dụng công cụ trong tác vụ dài hạn; cung cấp minh chứng định lượng cho việc cắt tỉa ngữ cảnh đã thảo luận trong bài [vệ sinh ngữ cảnh (`Context hygiene`)](context-hygiene.md).

## Tài liệu từ Anthropic

- [Managing context on the Claude Developer Platform](https://claude.com/blog/context-management) — cơ chế chỉnh sửa ngữ cảnh và công cụ bộ nhớ, cùng những con số được trích dẫn trong sổ tay này: cắt giảm 84% token trong bài đánh giá 100 lượt, cải thiện 29% khi chỉ dùng chỉnh sửa ngữ cảnh và 39% khi kết hợp cả hai.
- [Trang tài nguyên](../track-harness/resources.md) của sổ tay `Harness` lưu giữ phần còn lại trong bộ tài liệu kinh điển của Anthropic — xây dựng `Agent` hiệu quả, kỹ thuật ngữ cảnh hiệu quả — những kiến thức mà sổ tay này mặc định bạn đã nắm thay vì nhắc lại.

## Thực hành thực tế

- [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/) — Geoffrey Huntley. Vòng lặp bash đã khởi đầu tất cả, đi kèm những ghi chú về thất bại trung thực đến bất ngờ.
- [Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/) — Simon Willison, tháng 9 năm 2025. Phân tích những tác vụ nào phù hợp để đưa vào `Loop`, cùng tư thế bảo mật cần có khi cho phép một `Loop` tự chạy.

## Các kho mã nguồn đáng đọc

- [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) — các nguyên lý để xây dựng những `Agent` sống sót được trên môi trường production; nhiều yếu tố trong số đó chính là kỷ luật `Loop` dưới một tên gọi khác.
- [anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md) — plugin `ralph-wiggum`: mẫu thiết kế chạy trong vòng lặp (run-in-a-loop) dưới dạng mã nguồn được bảo trì và có thể kiểm tra trực tiếp.
- [vercel-labs/ralph-loop-agent](https://github.com/vercel-labs/ralph-loop-agent) — cùng mẫu thiết kế đó được xây dựng lại trên nền AI SDK, với bước xác minh và lặp được tường minh hóa.

## Bắt đầu tại đây

1. **Viết một bài kiểm tra mục tiêu.** Chọn một tác vụ bạn vẫn thường phải viết prompt thủ công lặp đi lặp lại và biểu diễn trạng thái hoàn thành dưới dạng một script trả về mã thoát 0. Nếu bạn không làm được, theo đúng nguyên lý trong bài [kỹ thuật vòng lặp là gì](what-loop-engineering-is.md), tác vụ đó chưa phải là ứng viên phù hợp cho `Loop`.
2. **Xây dựng vòng lặp thử lại.** Thực hành theo bài [Thực hành: Bài kiểm tra mục tiêu](build-goal-test.md) trên một kho mã nguồn nhỏ đang có các bài test bị lỗi. Chỉ mất một buổi tối.
3. **Thêm thẩm phán, sau đó thêm các thanh ray an toàn.** Bổ sung lượt chạy `Critic`, rồi đến cơ chế ratchet và báo cáo — và chỉ khi nào `Loop` dừng lại một cách rõ ràng, dễ hiểu trong mọi lần chạy thì bạn mới để nó tự làm việc trong lúc mình ngủ.
