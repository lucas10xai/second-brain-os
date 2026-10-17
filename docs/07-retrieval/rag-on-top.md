# Bổ sung RAG khi cần thiết

Hướng dẫn này phản đối việc dùng cơ sở dữ liệu Vector cho một Vault cá nhân. Tuy nhiên, lập luận đó có một ngưỡng giới hạn nhất định, và chúng ta nên chỉ rõ ngưỡng đó thay vì coi nó như một giáo điều bất biến.

## Khi nào RAG bắt đầu đáng giá

Khi hội tụ đủ khoảng ba điều kiện sau:

**Quy mô vượt quá vài nghìn trang,** khi việc đọc trang chỉ mục cộng với lần theo các liên kết không còn vừa vặn với ngân sách ngữ cảnh (Context budget) nữa.

**Câu hỏi được diễn đạt bằng từ ngữ mà các trang của bạn không dùng.** Nếu bạn thường xuyên không tìm thấy những thứ mình biết chắc là có trong Vault, đó là bài toán về độ phủ truy xuất (recall) — và đây chính là thứ mà Embeddings giải quyết.

**Một kho tài liệu không do chính bạn tuyển chọn.** Một Vault nuốt trọn mười nghìn tài liệu mà không có con người quyết định xem đâu là phần quan trọng sẽ không có cấu trúc đáng tin cậy để điều hướng, nên tìm kiếm theo độ tương đồng (similarity) là lựa chọn duy nhất còn lại.

Hầu hết các Vault cá nhân không bao giờ chạm tới cả ba điều kiện này. Vault của tôi cũng vậy, và tôi sẽ không gánh thêm chi phí bảo trì nếu chỉ mới chạm hai trên ba điều kiện.

## Nên tạo Embeddings cho thứ gì

Đừng tạo Embeddings cho các tài liệu nguồn thô trong `raw/`. Hãy tạo Embeddings cho các trang trong `wiki/`.

Bản thân các trang đó đã là những đơn vị ngữ nghĩa hoàn chỉnh, được viết bởi một chủ thể hiểu rõ nội dung, mỗi trang xoay quanh một ý tưởng. Đó chính là đích đến mà kỹ thuật chia nhỏ văn bản (chunking) cố gắng xấp xỉ nhưng hiếm khi đạt được. Việc cắt nhỏ chúng một lần nữa thành các cửa sổ kích thước cố định sẽ phá hủy cấu trúc mà bạn đã dày công tạo dựng.

Hãy gộp chung tiêu đề trang, Aliases và phần nội dung khi tạo Embeddings. Trong một Vault được biên tập kỹ, tiêu đề mang rất nhiều tín hiệu quan trọng vì chính bạn là người đã chọn chúng.

## Kết hợp lai (Hybrid), không phải thay thế

Cách bố trí hiệu quả nhất vẫn giữ Knowledge graph ở vị trí cầm trịch:

1. Embeddings tìm ra các trang điểm khởi đầu (entry-point pages), bao gồm cả những trang có cách dùng từ khác với câu hỏi.
2. Knowledge graph mở rộng từ các điểm khởi đầu đó thông qua hệ thống liên kết.
3. Agent đọc tập hợp các trang đã mở rộng và trả lời kèm trích dẫn.

Embeddings cung cấp độ phủ (recall), còn Knowledge graph cung cấp cấu trúc và lý do vì sao hai trang lại liên quan với nhau. Dùng độ tương đồng cho toàn bộ quy trình sẽ vứt bỏ các liên kết — vốn là phần tốn nhiều công sức nhất trong Vault của bạn.

## Giữ cho chỉ mục luôn mới

Đây là gánh nặng bảo trì mà chẳng mấy ai tính đến. Mỗi lần Ingest đều làm thay đổi các trang, và một chỉ mục Embeddings cũ kỹ sẽ trả về những trang có nội dung thực tế đã thay đổi từ lâu.

Hãy tạo lại Embeddings cho các trang bị thay đổi ngay trong lượt chạy Ingest, chứ đừng tách thành một lịch trình riêng. Một chỉ mục bị trễ một tuần sẽ âm thầm sai lệch theo cách tạo ra những câu trả lời nghe có vẻ hợp lý nhưng thực chất là sai.

Nếu việc đó nghe có vẻ tốn công bảo trì hơn giá trị mang lại, thì đó chính là nhận định hoàn toàn chính xác đối với hầu hết các Vault, và cũng là lý do thực tế khiến mục này được viết ngắn gọn như vậy.

## Những cách đơn giản hơn nên thử trước

Trước khi lắp thêm hạ tầng, hãy kiểm tra xem vấn đề có thực sự nằm ở độ phủ truy xuất hay không.

Thiếu Aliases là nguyên nhân phổ biến nhất dẫn đến tình trạng "tôi không tìm thấy nó". Một chỉ mục tồi cũng vậy. Hoặc một quy trình Ingest đã ngừng gắn liên kết đúng cách từ hai tháng trước, để lại một đống trang mồ côi ngày càng phình to mà không phương pháp truy xuất nào chạm tới được.

Hãy chạy `scripts/link_check.py` và đọc lại trang chỉ mục của bạn trước khi kết luận rằng mình cần đến Vector.

## Tiếp theo

[Ngân sách ngữ cảnh (Context budget)](context-budget.md)
