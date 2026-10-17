# Kỹ năng và Agent (Skills and agents)

Được đếm riêng lẻ từng mục: một kho mã nguồn cung cấp mười sáu kỹ năng sẽ được tính là mười sáu, bởi vì đó là số lượng thực tế bạn cài đặt vào máy. Số liệu được thống kê bằng cách đọc trực tiếp cây thư mục của từng kho mã nguồn vào tháng 9 năm 2026.

## Trong kho lưu trữ này

| Type | Count | Where |
|---|---|---|
| Skills | 18 | [`skills/`](../skills/README.md). Mỗi kỹ năng tương ứng với một quy trình làm việc trong hướng dẫn |
| Commands | 72 | [`commands/`](../commands/README.md). Các điểm vào có phạm vi hẹp dẫn thẳng tới các kỹ năng đó |
| Subagents | 6 | [`agents/`](../agents/README.md). Bốn trong số đó được thiết kế ở chế độ chỉ đọc (read-only) |
| Scripts | 4 | [`scripts/`](../scripts/README.md). Kiểm tra liên kết, thống kê, xuất đồ thị, nhập lịch sử trò chuyện |

Tất cả đều là các tệp `SKILL.md` văn bản thuần túy, vì vậy chúng hoạt động tốt với bất kỳ `Agent` nào hỗ trợ đọc định dạng Agent Skills chuẩn.

## Các bản hiện thực hóa của mô hình này

| Repo | Stars | Ships |
|---|---|---|
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 14,706 | 16 kỹ năng, 3 subagents. `Vault` tự tổ chức đi kèm các cấu hình dựng sẵn theo vai trò |
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 2,174 | 1 kỹ năng bao trọn toàn bộ vòng lặp nạp dữ liệu, biên dịch, truy vấn và kiểm tra lỗi (lint) |
| [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) | 1,856 | 13 kỹ năng, 4 subagents. Một bộ công cụ khởi đầu hoàn chỉnh |
| [coleam00/second-brain-starter](https://github.com/coleam00/second-brain-starter) | 768 | 1 kỹ năng phỏng vấn người dùng và tự động sinh bản kế hoạch xây dựng |
| [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain) | 704 | 4 kỹ năng, có trình cài đặt qua npm, bám rất sát bản gist nguyên mẫu |
| [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | small | 47 câu lệnh chạy xuyên suốt trên Claude, Codex và Gemini |
| [micuintus/llm-wiki](https://github.com/micuintus/llm-wiki) | small | 1 kỹ năng, chủ đích tối giản tuyệt đối, không phụ thuộc thư viện ngoài. Một đối trọng rất đáng tham khảo |

Hai dự án ở cuối bảng được chủ đích giữ cho nhỏ gọn và vẫn rất đáng đọc. Số lượng sao đo lường độ phủ sóng chứ không đo lường chất lượng, và ở góc nhỏ này của hệ sinh thái, nó chủ yếu phản ánh việc ai đã đăng bài giới thiệu về nó.

## Các thư viện kỹ năng tổng quát

Không dành riêng cho bộ não thứ hai, nhưng đây là nơi định nghĩa nên chính định dạng kỹ năng và là nơi lưu giữ những ví dụ được viết mẫu mực nhất.

| Repo | Stars | Ships |
|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 282,827 | 14 kỹ năng. Một framework kỹ năng `Agent` kiêm phương pháp luận phát triển phần mềm |
| [anthropics/skills](https://github.com/anthropics/skills) | 175,035 | 20 kỹ năng, 3 subagents. Kho tham chiếu chính thức cho định dạng Agent Skills |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 33,894 | Danh mục tuyển chọn hơn 1.000 kỹ năng đóng góp từ cộng đồng |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 53,661 | Tập hợp các câu lệnh, hooks, quy trình làm việc và công cụ dành cho `Claude Code` |

## Công cụ dựng đồ thị (Graph builders)

| Repo | Stars | What it does |
|---|---|---|
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 115,697 | Kỹ năng `/graphify` biến bất kỳ thư mục chứa code, tài liệu, PDF và ảnh chụp màn hình nào thành một đồ thị có thể truy vấn được. Mọi cạnh nối đều được gắn nhãn rõ ràng là trích xuất trực tiếp hay suy luận |

Graphify là công cụ đáng thử đầu tiên nếu bạn đã có sẵn một thư mục `raw/` đầy dữ liệu. Nó được xây dựng xoay quanh chính bài toán đó, chạy cục bộ với bộ phân tích cú pháp tất định dành cho mã nguồn, và xuất ra tệp `graph.html` tương tác cùng một `Vault` mở được ngay trong `Obsidian`. Mức tiết kiệm token được công bố là số liệu tự báo cáo và phụ thuộc rất nhiều vào kích thước kho dữ liệu.

## Tự viết kỹ năng của riêng bạn

Ba đặc tính làm nên một kỹ năng đáng để viết ra: bạn thực hiện công việc đó lặp đi lặp lại, bạn có quan điểm rõ ràng về cách thức thực hiện, và những quan điểm đó không đủ hiển nhiên để mô hình có thể tự đoán trúng.

Hãy đọc kho `anthropics/skills` để nắm chuẩn định dạng và đọc một trong các bản hiện thực nhỏ gọn ở trên để xem ví dụ hoàn chỉnh. Chi tiết được trình bày trong bài [kỹ năng và câu lệnh](../docs/06-agents/skills-and-commands.md).
