# Claude Code trong vai trò một Harness

Claude Code là bộ `Harness` giàu tính sư phạm nhất để nghiên cứu bởi Anthropic đóng gói cùng một cỗ máy đó dưới hai hình hài: một sản phẩm chạy trên dòng lệnh (terminal), và bộ thư viện [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) bằng Python và TypeScript phơi bày nguyên vẹn vòng lặp (`Loop`), hệ thống phân quyền cùng cơ chế quản lý ngữ cảnh y hệt để bạn tự xây dựng Agent của riêng mình. Hãy đọc trang [cấu trúc giải phẫu của Harness](what-a-harness-is.md) trước; trang này sẽ ánh xạ từng bộ phận lý thuyết sang một tính năng cụ thể trong thực tế.

## CLAUDE.md và bộ nhớ

`CLAUDE.md` là một tệp Markdown thuần túy được đọc ngay khi bắt đầu phiên làm việc — chứa các quy ước của dự án, các câu lệnh đóng gói (build), và nội quy riêng của đội ngũ. Nó được kết hợp theo cấu trúc phân cấp: cấp người dùng, cấp dự án, và cấp thư mục con. Các tệp bộ nhớ tự động (auto-memory) mở rộng khả năng lưu giữ này xuyên suốt nhiều phiên làm việc. Bài học rút ra là: những chỉ dẫn mang tính bền vững thuộc về các tệp tin mà Agent tự đọc vào, chứ không nằm ở những câu lệnh nhắc mà bạn phải gõ đi gõ lại. Xem thêm bài [Context engineering](context-engineering.md) để hiểu tại sao cách làm này vượt trội hơn hẳn việc nhồi nhét mọi thứ vào chung một câu lệnh nhắc.

## Hooks

[Hooks](https://code.claude.com/docs/en/hooks) là các câu lệnh shell được gắn chặt vào các sự kiện trong vòng đời vận hành — `PreToolUse`, `PostToolUse`, `SessionStart`, `PreCompact` cùng hàng chục sự kiện khác tính đến năm 2026. Chúng là cơ chế thực thi mang tính tất định (deterministic enforcement) chứ không phải lời khuyên suông: một hook ở bước `PreToolUse` có thể chặn đứng một câu lệnh nguy hiểm trong mọi lần gọi không trượt phát nào, trong khi một lời dặn trong câu lệnh nhắc chỉ giúp giảm bớt xác suất xảy ra. Quy tắc ngón tay cái: dùng câu lệnh nhắc (prompts) cho những việc cần phán đoán linh hoạt, dùng `Hooks` cho những chính sách bắt buộc phải tuân thủ.

## Subagents

`Subagents` (các Agent con) chạy trong cửa sổ ngữ cảnh riêng biệt của chính chúng, với câu lệnh nhắc hệ thống riêng và các giới hạn công cụ riêng. Agent cha chỉ nhìn thấy bản báo cáo kết quả cuối cùng chứ không bao giờ phải nhận đống rác nhiễu trung gian — nhờ đó biên bản hội thoại điều phối chính luôn sạch sẽ và nhân gấp bội không gian ngữ cảnh khả dụng trên thực tế. Bạn có thể định nghĩa chúng dưới dạng các tệp Markdown đặt trong thư mục `.claude/agents/` hoặc khai báo bằng mã nguồn thông qua SDK.

## Kỹ năng (Skills)

Một kỹ năng (`skill`) là một thư mục chứa tệp `SKILL.md` kèm theo các kịch bản (scripts) và tệp mẫu (templates) tùy chọn. Chỉ có duy nhất dòng mô tả ngắn gọn một dòng là nằm thường trực trong ngữ cảnh; còn phần thân chi tiết chỉ được nạp vào khi thực sự liên quan đến tác vụ đang làm. Đây chính là cơ chế truy xuất chỉ dẫn theo nhu cầu (retrieval-on-demand) — mẫu thiết kế giúp một Agent giàu năng lực không bị chết chìm trong chính cuốn sổ tay hướng dẫn sử dụng của nó. Tài liệu chi tiết: [Agent Skills](https://code.claude.com/docs/en/agent-sdk/skills).

## MCP

Claude Code đóng vai trò là một trình khách MCP (MCP client): các máy chủ bên ngoài có thể đóng góp thêm công cụ song hành cùng bộ công cụ tích hợp sẵn, được cấu hình linh hoạt theo từng dự án hoặc từng người dùng. Đây là tính năng cực kỳ mạnh mẽ nhưng cũng đồng thời là bề mặt tấn công tiêm nhiễm chính — đã được phân tích đầy đủ trong bài [công cụ (Tools) và MCP](tools-and-mcp.md).

## Hệ thống phân quyền (Permissions)

Mọi lệnh gọi công cụ (`Tool use`) đều phải đi qua một tầng kiểm soát quyền hạn: danh sách cho phép (allowlists) trong tệp `settings.json`, lời nhắc hỏi ý kiến trên từng lệnh gọi, chế độ lập kế hoạch `plan` (chỉ-đọc), và thực thi trong môi trường hộp cát (sandbox). Giả định thiết kế cốt lõi ở đây là mô hình thỉnh thoảng kiểu gì cũng sẽ làm điều gì đó ngớ ngẩn, vì vậy chính `Harness` — chứ không phải mô hình — mới là người nắm giữ chân phanh.

## Chạy không giao diện (Headless) và dùng qua SDK

Lệnh `claude -p "prompt"` cho phép chạy một lượt duy nhất (one-shot) bên trong các kịch bản tự động và đường ống CI, trả về đầu ra định dạng JSON. Bộ thư viện Agent SDK còn tiến xa hơn: cung cấp hàm `query()` cho các lệnh gọi đơn giản, một lớp trình khách (client class) hỗ trợ đầy đủ `Hooks` và truyền phát luồng dữ liệu (streaming), cùng khả năng khởi tạo `Subagents` và máy chủ `MCP` ngay bằng mã nguồn. Lúc này bạn không còn viết kịch bản bọc ngoài công cụ dòng lệnh CLI nữa; mà bạn đang nhúng trực tiếp bộ `Harness` vào ứng dụng của mình.

## Đánh giá thẳng thắn

Đây là bộ `Harness` dựng sẵn hoàn chỉnh nhất hiện có vào năm 2026, đồng thời là bộ từ vựng chuẩn mực mà phần còn lại của ngành dùng để đối chiếu — xem thêm tại trang [bức tranh toàn cảnh](harness-landscape.md). Cái giá phải trả: bạn phải kế thừa các quan điểm thiết kế của Anthropic cũng như mức độ "ngốn" token của chúng. Đối với hầu hết những người xây dựng hệ thống, đó là một sự đánh đổi hoàn toàn xứng đáng.
