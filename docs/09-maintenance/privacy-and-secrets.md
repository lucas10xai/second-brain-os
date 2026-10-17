# Quyền riêng tư và thông tin nhạy cảm

Một Second Brain khi đã trưởng thành là một trong những tài liệu chứa nhiều tín hiệu rõ nét nhất về một con người. Mọi thứ bạn đọc, làm việc, trăn trở và đặt câu hỏi đều được kết nối và lập chỉ mục tại đây.

Đó chính là mục đích của hệ thống, và cũng là lý do bạn phải hết sức có chủ đích về những gì được đưa vào và nơi lưu trữ chúng.

## Quyết định ngay ở khâu thu thập, đừng đợi đến sau này

Việc biên tập xóa bỏ thông tin nhạy cảm sau khi đã Ingest là không khả thi. Đến lúc bạn nhận ra một thông tin nào đó không nên xuất hiện ở đây, nó đã kịp lan truyền sang các trang khái niệm, các liên kết và các trang tổng hợp, và việc gỡ bỏ đồng nghĩa với việc phải truy tìm toàn bộ những nơi đó.

Hãy quyết định trước khi file được đưa vào `raw/`. Xem thêm [bản xuất lịch sử trò chuyện](../03-ingestion/chat-exports.md) — đây là nơi vấn đề này gây hậu quả nặng nề nhất, bởi lịch sử trò chuyện chứa nhiều thông tin nhạy cảm hơn bất kỳ nguồn nào khác và lại thường được nhập vào hàng loạt.

## Những thứ không thuộc về nơi này

**Thông tin xác thực (Credentials) dưới mọi hình thức.** Không phải vì sợ Agent làm rò rỉ chúng, mà vì Vault được đồng bộ, commit lên Git, sao lưu và đôi khi được chia sẻ. Mỗi bản sao là thêm một nơi mà khóa bảo mật đó tồn tại.

**Thông tin riêng tư của người khác.** Bản ghi lời thoại cuộc họp (meeting transcripts), tin nhắn cá nhân, hay bất kỳ điều gì được tâm sự riêng với bạn. Ghi chú của bạn không phải là nơi thích hợp để lưu giữ bí mật của người khác, và họ cũng chưa từng đồng ý cho phép thông tin đó được Ingest.

**Tài liệu bạn có nghĩa vụ bảo mật theo hợp đồng.** Công việc của khách hàng thuộc diện thỏa thuận bảo mật (NDA) mà lại nằm trong một Vault đồng bộ lên tài khoản đám mây cá nhân là một rủi ro lộ lọt dữ liệu thực sự.

## Tách hẳn thành các Vault riêng thay vì cố lọc cẩn thận

Nếu bạn có những nhóm tài liệu tuyệt đối không được phép trộn lẫn với nhau, hãy dùng một Vault riêng biệt thay vì dựa vào thẻ (tags) hay thư mục bên trong cùng một Vault.

Một Vault dùng chung có chứa phân khu riêng tư sẽ phụ thuộc vào việc mọi câu truy vấn, mọi lần trích xuất và mọi bước xuất bản đều phải tuân thủ nghiêm ngặt ranh giới đó. Hai Vault tách biệt thì không thể rò rỉ dữ liệu sang nhau, và cái giá duy nhất phải trả chỉ là việc chọn mở đúng Vault khi làm việc.

## Dùng mô hình cục bộ (Local models) cho tài liệu nhạy cảm

Nếu một nhóm tài liệu tuyệt đối không được phép rời khỏi máy tính của bạn, hãy dùng một mô hình chạy cục bộ để xử lý khâu Ingest cho Vault đó. Chất lượng sẽ thấp hơn so với các mô hình hàng đầu (frontier models), và đó là sự đánh đổi tất yếu.

Sự đánh đổi này hoàn toàn xứng đáng đối với tài liệu y tế, pháp lý hoặc tài chính. Nhưng thường là không đáng đối với các bài viết về phần mềm thông thường.

## Xuất bản

Chỉ áp dụng cơ chế chủ động chọn (explicit opt-in). Xem thêm [xuất bản và trích xuất](../08-outputs/publishing-and-export.md).

## Trước khi chia sẻ một Vault

Hãy tìm kiếm toàn bộ Vault để rà soát các khóa bảo mật (keys), kiểm tra kỹ Frontmatter xem có chứa thông tin định danh cá nhân hay không, và đọc lại file nhật ký (`log.md`) để biết những gì đã được Ingest từ nguồn nào. Một khi đã chia sẻ ra ngoài là không thể thu hồi, và cấu trúc Knowledge graph sẽ giúp người đọc dễ dàng ghép nối các mảnh thông tin thành một bức tranh toàn cảnh mà bạn không hề có ý định tiết lộ.

## Tiếp theo

[Mở rộng quy mô vượt ngưỡng một nghìn trang](scaling.md)
