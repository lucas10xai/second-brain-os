# Quy tắc liên kết

Liên kết (links) là toàn bộ giá trị của cấu trúc. Không có chúng, bạn chỉ có một thư mục chứa các file với tên gọi đẹp đẽ — thứ thực chất chỉ là một chỉ mục tìm kiếm (search index), mà chỉ mục tìm kiếm thì đã tồn tại sẵn rồi.

## Quy tắc cốt lõi

Liên kết ở lần nhắc đến đầu tiên của bất kỳ khái niệm hoặc thực thể nào, trên mọi trang.

Chỉ vậy thôi. Khi được áp dụng nhất quán, quy tắc này tự động hình thành nên đồ thị mà không cần một lượt chạy liên kết riêng biệt hay bất kỳ nghi thức bảo trì nào.

## Liên kết, đừng diễn giải lại

Nếu bạn đang giải thích một thứ vốn đã có trang riêng, hãy đặt liên kết tới nó và đi tiếp.

Đây là cách giữ cho tri thức nằm ở một nơi duy nhất. Khi lời giải thích của một khái niệm nằm rải rác trên bốn trang với bốn phiên bản hơi khác nhau, việc cập nhật nó đồng nghĩa với việc phải tìm ra cả bốn trang — và bạn sẽ không làm thế đâu. Khi được liên kết, nó chỉ tồn tại ở một nơi và được cải thiện tại một nơi duy nhất.

## Liên kết hai chiều

Một trang mới sẽ liên kết ra ngoài tới những gì nó tham chiếu. Và những trang được nó tham chiếu cũng phải liên kết ngược lại.

Liên kết một chiều tạo ra những trang có tham chiếu tới `Vault` nhưng `Vault` không bao giờ chạm tới được chúng. Chúng có tồn tại, nội dung hoàn toàn đúng, nhưng không có gì tìm thấy chúng. `Obsidian` có hiển thị các `Backlinks` chưa được liên kết (unlinked backlinks) giúp bạn phát hiện ra điều này, nhưng `Agent` nên tự khép kín vòng lặp liên kết ngay lúc `Ingest` thay vì để phần việc đó lại cho bạn.

## Những liên kết tới trang chưa tồn tại

Cứ viết liên kết đó ra, sau đó hoặc là tạo trang đích ngay trong cùng lượt chạy, hoặc ghi nhận nó vào mục Gaps (Khoảng trống) trong `index.md`.

Các khoảng trống là thông tin hữu ích. Một trang được ba tài liệu nguồn cùng liên kết tới nhưng lại chưa tồn tại chính xác là thứ cần được viết tiếp theo, hoặc chính xác là chủ đề bạn cần tìm đọc thêm.

Điều không thể chấp nhận là một khoảng trống vĩnh viễn. Những liên kết trỏ tới các trang sẽ không bao giờ tồn tại làm cho đồ thị tự nói dối về độ bao phủ của chính nó.

## Bao nhiêu liên kết là vừa

Không có con số mục tiêu cố định, nhưng hình thái phân bổ rất quan trọng. Một trang không có liên kết đi ra (outbound links) là một ngõ cụt. Một trang có tới bốn mươi liên kết thường là một danh sách đang giả dạng làm một trang nội dung.

Hãy theo dõi mức trung bình trên toàn `Vault` thay vì săm soi từng trang đơn lẻ. Nếu trung bình dưới khoảng hai liên kết mỗi trang, đồ thị chưa đủ kết nối để trả lời bất kỳ điều gì vượt qua phạm vi của từng trang riêng lẻ. Hãy theo dõi chỉ số này bằng `scripts/vault_stats.py`.

## Các trang trung tâm (Hub pages)

Một số trang tích lũy liên kết cho đến khi mọi thứ đều đi qua chúng. Một khái niệm chung chung mà mọi tài liệu nguồn đều chạm tới sẽ trở thành một điểm nút trung tâm (hub), và một khi nó trở thành hub, đồ thị xung quanh nó không còn mang lại thông tin hữu ích nữa: mọi thứ đều chỉ cách nhau hai bước nhảy (hops).

Cách khắc phục là tách hub đó thành các ý tưởng cụ thể mà mọi người thực sự đang liên kết tới. Nếu bốn mươi trang cùng liên kết tới một khái niệm rộng lớn, thực chất chúng đang liên kết tới bốn khía cạnh khác nhau của khái niệm đó.

## Liên kết trang trí (Decorative links)

Một liên kết là một khẳng định rằng hai trang có mối liên hệ đáng để lần theo. Những liên kết được thêm vào chỉ vì một từ tình cờ xuất hiện là nhiễu (noise), và khi có quá nhiều nhiễu như vậy, đồ thị sẽ trở nên vô dụng y hệt như một đồ thị trống rỗng.

Bài kiểm tra rất đơn giản: bạn có bấm vào liên kết này khi đang nghiên cứu chủ đề đó không? Nếu không, hãy xóa nó đi.

## Tiếp theo

[Lược đồ Frontmatter](frontmatter-schema.md)
