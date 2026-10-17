# Câu hỏi thường gặp (FAQ)

**Tôi có bắt buộc phải dùng MCP không?**

Không. Khi khởi động Claude Code ngay bên trong thư mục Vault, nó có thể đọc và ghi các file trực tiếp. MCP chỉ bổ sung khả năng chạm tới Vault từ những phiên làm việc không chạy bên trong thư mục đó — điều này chủ yếu hữu ích cho các tác vụ chạy tự động theo lịch trình. Xem thêm [MCP cho Obsidian](../02-setup/mcp-obsidian.md).

**Hệ thống này có hoạt động với các Agent khác ngoài Claude Code không?**

Có. Bản chất Vault là các file markdown và các Skills là những file `SKILL.md` — một định dạng mà nhiều Agent hiện nay đều đọc được. Bất kỳ công cụ nào có khả năng đọc và ghi file trong một thư mục đều có thể duy trì Vault; bạn chỉ cần đổi tên file chỉ dẫn `CLAUDE.md` sao cho phù hợp với công cụ đó.

**Chi phí vận hành hệ thống này là bao nhiêu?**

Phụ thuộc hoàn toàn vào khối lượng tài liệu. Việc Ingest vài bài viết mỗi ngày tốn chi phí rất nhỏ. Nhưng một đợt nạp bù dữ liệu (backfill) một lần cho cả nghìn tài liệu nguồn thì không hề rẻ — đó là lý do trang hướng dẫn [nạp bù hàng loạt](../03-ingestion/bulk-backfill.md) nhấn mạnh việc chia thành từng lô nhỏ với chi phí được hiển thị rõ ràng.

**Tôi có thể dùng mô hình chạy cục bộ (local model) không?**

Để Ingest các tài liệu nhạy cảm thì hoàn toàn được, nhưng chất lượng sẽ thấp hơn. Các mô hình cục bộ thường yếu hơn ở những quyết định đòi hỏi sự phán đoán tinh tế vốn rất quan trọng trong hệ thống này: chẳng hạn như ý tưởng nào xứng đáng có một trang riêng, hay khi nào hai tài liệu nguồn thực sự mâu thuẫn với nhau. Một cách phân chia hợp lý là dùng mô hình cục bộ cho tài liệu riêng tư và dùng mô hình hàng đầu (frontier model) cho mọi thứ còn lại.

**Tôi có bắt buộc phải dùng Obsidian không?**

Không. Vault thực chất chỉ là một thư mục chứa các file markdown. Obsidian là một trình xem rất tốt cho Knowledge graph và sở hữu công cụ Web Clipper — đó là lý do thực tế mạnh mẽ nhất để chọn nó. Ngoài ra, Logseq, Foam, hoặc một trình soạn thảo văn bản thuần túy đều làm việc tốt.

**Nếu tôi đã có sẵn một kho ghi chú khổng lồ trong Notion hoặc Evernote thì sao?**

Hãy dùng plugin [Importer](https://github.com/obsidianmd/obsidian-importer) chính thức của Obsidian; công cụ này xử lý được dữ liệu từ Notion, Evernote, Roam, Bear và Apple Notes. Sau đó, hãy coi kết quả thu được như những nguyên liệu thô: chạy nạp bù (backfill) từ những ghi chú cũ nhất trước. Hãy chuẩn bị tinh thần là dữ liệu xuất ra sẽ khá lộn xộn. Hãy làm sạch khâu trích xuất trước khi Ingest thay vì hy vọng Agent sẽ tự xoay xở được.

**Hệ thống này khác gì so với tính năng bộ nhớ (Memory) tích hợp sẵn trong các ứng dụng trò chuyện AI?**

Tính năng bộ nhớ chỉ ghi nhớ các sự kiện rời rạc về cá nhân bạn qua các phiên trò chuyện và thuộc quyền sở hữu của công cụ đó. Còn đây là một kho tàng tri thức do chính bạn sở hữu dưới dạng các file độc lập, tồn tại lâu hơn bất kỳ công cụ nào, và bạn có thể tự mình đọc, chỉnh sửa cũng như xuất bản tùy ý.

**Liệu Agent có tự bịa ra thông tin không?**

Có thể, và đó chính là lý do mọi quy tắc trong chương [Cấu trúc hóa (Structuring)](../04-structuring/README.md) đều xoay quanh việc quy kết nguồn gốc (attribution): các nhận định phải được ghi nhận đúng là nhận định, có đính kèm tài liệu nguồn, và những khoảng trống thông tin phải được nêu rõ thay vì tự suy diễn lấp đầy. Một trang đưa ra con số cụ thể mà không có trang nguồn nào đứng sau chính là dấu hiệu cảnh báo bạn cần để mắt tới.

**Chế độ xem đồ thị (Graph view) có thực sự hữu ích hay chỉ để ngắm cho đẹp?**

Đồ thị tổng thể (global view) chủ yếu là để ngắm cho đẹp. Nhưng đồ thị cục bộ (local graph) lại thực sự hữu ích trong vai trò một bài kiểm tra chất lượng nhanh chỉ mất năm giây cho bất kỳ trang nào. Xem thêm [cách đọc chế độ xem đồ thị](../05-graphs/obsidian-graph-view.md).

**Mất bao lâu thì hệ thống này bắt đầu mang lại giá trị xứng đáng?**

Từ tuần thứ hai đến tuần thứ tư để thấy những thành quả thực tế đầu tiên, và khoảng tháng thứ sáu để đạt tới trạng thái mà mọi người vẫn mô tả là toàn bộ ý nghĩa của việc xây dựng Second Brain.

---

Còn điều gì chưa được giải đáp ở đây? Hãy mở một issue nhé.
