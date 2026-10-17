# Tài nguyên tham khảo

Danh sách được tuyển chọn kỹ, không liệt kê tràn lan. Mọi tài liệu tại đây đều đã được kiểm tra vào tháng 9 năm 2026 và hoàn toàn xứng đáng có mặt. Hãy đọc song hành cùng bài [Harness là gì](what-a-harness-is.md) để nắm vững hệ từ vựng cốt lõi.

## Các bài viết nền tảng

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic, tháng 12 năm 2024. Vẫn là bảng phân loại rõ ràng nhất hiện nay: phân biệt rạch ròi giữa luồng công việc cố định (workflows) và `Agent`, cùng lời khuyên mà ai cũng trích dẫn nhưng ít người chịu làm theo — hãy bắt đầu thật đơn giản.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic. Bài viết đặt tên và định hình bộ môn được trình bày trong bài [Context engineering](context-engineering.md).
- [Context engineering for AI agents: lessons from building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) — những vết sẹo xương máu từ môi trường thực tế: bài toán kinh tế của bộ đệm KV-cache, ngữ cảnh chỉ-nối-thêm (append-only context), và kỹ thuật che (masking) công cụ thay vì xóa bỏ chúng khỏi danh sách.
- [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — tài liệu gối đầu giường về thiết kế công cụ, bổ trợ trực tiếp cho bài [công cụ (Tools) và MCP](tools-and-mcp.md).

## Hướng dẫn chuyên sâu và bài nói chuyện

- [How to build an agent](https://ampcode.com/notes/how-to-build-an-agent) — Thorsten Ball. Xây dựng một Agent chỉnh sửa mã nguồn chỉ trong chưa đầy 400 dòng mã Go. Hãy làm theo bài này trước khi áp dụng bất kỳ bộ khung (framework) nào; không có gì xóa bỏ bức màn bí ẩn nhanh hơn cách tự tay gõ từng dòng mã này.
- [12-factor agents](https://github.com/humanlayer/12-factor-agents) — HumanLayer. Mười hai nguyên tắc thiết kế giúp các Agent sống sót vững vàng trên môi trường production: làm chủ câu lệnh nhắc, làm chủ cửa sổ ngữ cảnh, và giữ cho các Agent nhỏ gọn, tập trung.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — Anthropic. Phân tích mẫu kiến trúc điều phối - công nhân (orchestrator-worker), cùng lời thú nhận thẳng thắn rằng hệ thống đa Agent tiêu tốn lượng token nhiều gấp ~15 lần thông thường.
- [Context rot](https://www.trychroma.com/research/context-rot) — Chroma. Bằng chứng thực nghiệm chứng minh hiệu năng của mô hình suy giảm dần khi ngữ cảnh đầu vào phình to, rất lâu trước khi cửa sổ ngữ cảnh chạm ngưỡng giới hạn cứng.
- [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Simon Willison. Khung tư duy bảo mật bắt buộc phải biết đối với mọi Agent có đọc nội dung không đáng tin cậy từ bên ngoài. Trang blog cá nhân được cập nhật liên tục của ông cũng là nguồn bình luận sắc sảo nhất về thế giới Agent nói chung.
- [The 2026-07-28 MCP specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — giải thích chi tiết những thay đổi kiến trúc khi giao thức `MCP` chuyển sang mô hình phi trạng thái (stateless), viết bởi chính đội ngũ phát triển giao thức.

- [Improved token efficiency](https://cursor.com/blog/improved-token-efficiency) — Cursor. Cách một bộ `Harness` thương mại thực tế được ép cân gọn gàng qua sáu bước đi: xóa bỏ hai phần ba câu lệnh nhắc hệ thống khi bản thân mô hình đã thông minh hơn, nạp công cụ theo nhu cầu (giảm ngay 60% lượng token tĩnh dành cho công cụ), đặt các điểm ngắt bộ đệm (cache breakpoints) tường minh, đánh số dòng thưa hơn, và siết chặt kỷ luật sử dụng `Subagents`. Một bài viết hiếm hoi công bố con số đo lường cụ thể cho từng thay đổi; [câu lệnh nhắc tái hiện này](https://x.com/undefinedKi/status/2103219508605555033) giúp bạn áp dụng đúng quy trình kiểm toán đó lên hệ thống của chính mình.

- [Palantir AIP architecture](https://www.palantir.com/docs/foundry/architecture-center/aip-architecture) — ngăn xếp kiến trúc Agent của một nền tảng vận hành bên trong những tổ chức có yêu cầu bảo mật khắt khe bậc nhất, và phần lớn các nguyên tắc đó đều có thể sao chép về áp dụng cho một dự án nhỏ: sử dụng bản thể luận (ontology) gồm các đối tượng có định kiểu và danh sách hành động được cấp phép thay vì cho truy cập dữ liệu thô, đặt một cổng trung gian (gateway) duy nhất chặn trước mọi lệnh gọi mô hình (để che dữ liệu nhạy cảm, lưu bộ đệm, thử lại khi lỗi, kiểm toán lượng token), hoán đổi mô hình linh hoạt đằng sau tệp cấu hình, gói gọn trong ba cơ chế kích hoạt (theo lịch hẹn, theo sự kiện, qua API), đưa bộ đánh giá (evals) vào thẳng chu kỳ phát hành, và truy vết toàn bộ mọi hành động. [Bản phân tích mổ xẻ này](https://x.com/undefinedKi/status/2103883647501652057) ánh xạ từng mảnh ghép trên sang những công cụ tương đương mà bạn có thể tự dựng tại nhà.

## Kho mã nguồn đáng đọc

- [pi](https://github.com/earendil-works/pi) — một bộ `Harness` hoàn chỉnh nhưng đủ nhỏ gọn để bạn thực sự đọc hết được mã nguồn; bao gồm vòng lặp (`Loop`), công cụ (`Tool use`) và cơ chế mở rộng mà không hề có sự rườm rà kiểu cách.
- [smolagents](https://github.com/huggingface/smolagents) — mẫu thiết kế dùng-mã-nguồn-làm-hành-động (code-as-actions) gói gọn trong khoảng ~1.000 dòng mã lõi.
- [OpenHands](https://github.com/OpenHands/OpenHands) — cách thức tổ chức môi trường thực thi đóng hộp (sandboxed runtimes) và luồng sự kiện ở quy mô vận hành thực tế (production).
- [Claude Code docs](https://code.claude.com/docs/en/overview) — không phải là một kho mã nguồn mở, nhưng là cuốn cẩm nang hướng dẫn của bộ `Harness` tham chiếu hàng đầu hiện nay; riêng trang [tài liệu tham chiếu về Hooks](https://code.claude.com/docs/en/hooks) tự thân nó đã là một giáo trình hoàn chỉnh về thiết kế vòng đời vận hành của Agent.

## Bắt đầu từ đây

1. **Tự tay xây dựng vòng lặp trần trụi.** Làm theo bài hướng dẫn của Thorsten Ball bằng ngôn ngữ lập trình bạn yêu thích. Chỉ tốn một buổi chiều; nhưng nó sẽ thay đổi vĩnh viễn cách bạn đọc tài liệu của mọi bộ khung (framework) về sau.
2. **Đọc kỹ hai bài viết.** Bài *Building effective agents*, tiếp nối bằng bài *Effective context engineering*. Kết hợp lại, hai bài viết này giải quyết tới 80% những quyết định đánh đổi mà bạn sẽ phải đối mặt trong thực tế.
3. **Chọn một bộ Harness và gắn thiết bị đo đạc.** Chọn lấy một cái tên từ [bức tranh toàn cảnh](harness-landscape.md), đấu nối vào một tác vụ thực sự, và đọc kỹ biên bản hội thoại thô (raw transcripts) của từng ca chạy lỗi. Biên bản hội thoại chính là giáo trình tốt nhất; mọi khái niệm viết trong cuốn sổ tay này đều hiện nguyên hình ở đó.
