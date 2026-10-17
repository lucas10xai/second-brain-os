# Context Engineering (Kỹ thuật ngữ cảnh)

Kỹ thuật câu lệnh nhắc (prompt engineering) đặt câu hỏi "tôi nên dùng những từ ngữ nào?". Còn `Context engineering` (kỹ thuật ngữ cảnh) đặt câu hỏi "mô hình đang nhìn thấy những gì ngay tại thời điểm này, và tại sao?". Đối với các Agent, câu hỏi thứ hai chiếm vị trí thống trị: mọi kết quả trả về từ công cụ, mọi tệp tin được đọc và mọi lượt hội thoại cũ đều phải cạnh tranh nhau để giành chỗ trong một cửa sổ ngữ cảnh hữu hạn, và `Harness` chính là người biên tập cửa sổ đó. Bài viết [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) của Anthropic là tuyên ngôn kinh điển định hình bộ môn này.

## Ngân sách ngữ cảnh (The budget)

Hãy coi cửa sổ ngữ cảnh là một khoản ngân sách có hạn, chứ không phải một cái thùng rác. Cơ chế chú ý (attention) bị suy giảm chất lượng trước cả khi cửa sổ ngữ cảnh chạm ngưỡng đầy — nghiên cứu về hiện tượng [thối rữa ngữ cảnh (context rot)](https://www.trychroma.com/research/context-rot) của Chroma đã chứng minh hiệu năng mô hình trượt dốc khi đầu vào dài ra, rất lâu trước khi chạm tới bất kỳ giới hạn cứng nào. Quy tắc thực tiễn là: chỉ giữ lại tập hợp nhỏ nhất các token mang tín hiệu cao (high-signal tokens) đủ để mô hình hành động. Bất cứ thứ gì bạn nhét thêm vào đều làm loãng mọi thứ đang có sẵn ở đó.

## Thứ gì được đưa vào, và vào lúc nào

- **Luôn luôn có mặt**: câu lệnh nhắc hệ thống (system prompt), lược đồ công cụ (tool schemas), các tệp bộ nhớ như `CLAUDE.md`. Hãy giữ cho chúng gọn gàng và cố định — các tiền tố (prefixes) ổn định còn giúp giữ ấm bộ đệm KV-cache, yếu tố mà đội ngũ Manus [đã đo lường được là tạo ra chênh lệch chi phí gấp 10 lần](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus).
- **Nạp theo nhu cầu (On demand)**: nội dung tệp tin, kết quả tìm kiếm, phần thân của các kỹ năng (skills), tài liệu hướng dẫn. Hãy trang bị cho Agent các công cụ truy xuất và để nó tự kéo về những gì nó cần, thay vì nạp sẵn mọi thứ mà bạn đoán có thể nó sẽ cần.
- **Không bao giờ đưa vào**: toàn bộ kho mã nguồn, toàn bộ phản hồi API thô, hay mười biến thể khác nhau của cùng một chỉ dẫn.

## Nén ngữ cảnh (Compaction)

Các phiên làm việc kéo dài sẽ vượt quá bất kỳ cửa sổ ngữ cảnh nào. Quá trình nén (compaction) sẽ tóm tắt lại biên bản hội thoại (transcript) — các quyết định đã chốt, các luồng việc còn dang dở, đường dẫn các tệp tin — rồi khởi tạo lại không gian mới từ bản tóm tắt đó. Về mặt thiết kế, quá trình này chấp nhận mất mát thông tin (lossy); một Harness tốt sẽ nén mạnh tay quanh các kết quả trả về từ công cụ (vốn cồng kềnh và hiếm khi cần đọc lại nguyên văn) trong khi bảo toàn nguyên vẹn ý định ban đầu. [Claude Code](claude-code-as-harness.md) thực hiện việc này hoàn toàn tự động và cung cấp thêm các `Hooks` tại sự kiện `PreCompact` để bạn kiểm soát khi cần.

## Các tệp bộ nhớ (Memory files)

Những trạng thái bắt buộc phải sống sót qua các đợt nén ngữ cảnh và qua nhiều phiên làm việc khác nhau thuộc về bên ngoài cửa sổ ngữ cảnh, nằm trong các tệp văn bản thuần túy mà Agent có thể đọc và ghi: một tệp nháp (scratchpad), một tệp `MEMORY.md`, hay một danh sách việc cần làm (todo list). Hệ thống tệp tin chính là bộ nhớ dài hạn của Agent; còn cửa sổ ngữ cảnh chỉ là bộ nhớ làm việc (working memory). Những độc giả của phương pháp bộ não thứ hai (second-brain) hẳn sẽ nhận ra ngay mẫu thiết kế quen thuộc này.

## Đầu ra có cấu trúc (Structured outputs)

Khi mã nguồn ở tầng hạ nguồn (downstream) cần tiêu thụ câu trả lời của Agent, hãy yêu cầu một lược đồ chặt chẽ — định dạng JSON với các trường được định kiểu, và ép buộc trực tiếp qua API bất cứ khi nào có thể. Văn bản tự do là dành cho con người đọc; còn cấu trúc là dành cho các đường ống tự động (pipelines). Cách này cũng rèn kỷ luật cho chính mô hình: một trường bắt buộc (`required`) trong lược đồ là một câu hỏi mà nó không thể lảng tránh.

## Các kiểu lỗi thường gặp (Failure modes)

- **Đầu độc ngữ cảnh (Context poisoning)**: một "dữ kiện" do mô hình tự ảo giác ra lọt vào biên bản hội thoại và bị coi là sự thật hiển nhiên trong suốt phần còn lại của phiên làm việc.
- **Xao nhãng (Distraction)**: các chỉ dẫn nằm sâu bên dưới bị lép vế trước những nhiễu loạn mới phát sinh gần đây; Agent quên mất mục tiêu chính giữa một rừng kết quả trả về từ công cụ.
- **Xung đột (Clash)**: các chỉ dẫn mâu thuẫn nhau giữa câu lệnh nhắc hệ thống, tệp bộ nhớ và yêu cầu của người dùng, khiến mô hình tự phân xử một cách tùy tiện.
- **Phình đại (Bloat)**: một kết quả trả về từ công cụ dài tới 40.000 token mà chẳng ai đọc, nhưng lại phải trả tiền lặp đi lặp lại ở mọi lượt gọi tiếp theo.

Hầu hết các phàn nàn kiểu "sao tự nhiên mô hình ngu đi thế" đều rơi vào một trong bốn trường hợp này. Hãy chẩn đoán lỗi bằng cách đọc trực tiếp biên bản hội thoại thực tế — một Harness tốt phải cho phép bạn xem tận mắt biên bản đó.

## Vị trí của các công cụ

Lược đồ công cụ và kết quả trả về từ công cụ là đối tượng ngốn nhiều ngữ cảnh nhất trong hầu hết các Agent, điều đó biến việc thiết kế công cụ trở thành một quyết định cốt tử của `Context engineering` — đây cũng chính là chủ đề của bài [công cụ (Tools) và MCP](tools-and-mcp.md).
