# Xuất bản và trích xuất

Một vài phần trong Vault của bạn rất đáng để chia sẻ cho người khác xem. Nhưng phần lớn thì không, và cơ chế phân tách rạch ròi hai phần đó rất đáng để thiết lập trước khi bạn xuất bản bất cứ thứ gì.

## Quyết định nội dung nào được công khai

Cách tiếp cận đơn giản và đáng tin cậy nhất là cơ chế chủ động chọn (explicit opt-in): thêm một trường `publish: true` vào Frontmatter, và bất kỳ trang nào không có trường này sẽ không bao giờ lọt ra ngoài.

Cơ chế loại trừ (opt-out) là hướng ngược lại và đó là một sai lầm. Với cơ chế loại trừ, chỉ cần quên gắn cờ một lần là nội dung riêng tư sẽ bị công khai ngay lập tức, và hậu quả này diễn ra âm thầm nhưng vĩnh viễn vì các công cụ tìm kiếm đã kịp lập chỉ mục trang đó rồi.

## Các lựa chọn tạo trang web tĩnh (Static site)

Obsidian Publish là giải pháp chính thức và tốn ít công sức nhất. Quartz và Obsidian Digital Garden là hai lựa chọn mã nguồn mở phổ biến; cả hai đều dựng trang web tĩnh từ một Vault và đều hiểu được Wikilink lẫn Backlinks — điều này cực kỳ quan trọng vì một trang wiki được xuất bản mà đầy liên kết gãy thì còn tệ hơn cả một trang blog thông thường.

Dù bạn chọn công cụ nào, hãy kiểm tra xem điều gì sẽ xảy ra với một liên kết trỏ tới trang chưa được xuất bản. Nó nên tự động chuyển về dạng văn bản thuần túy thay vì dẫn người đọc tới một trang lỗi 404.

## Xuất bản một phần Vault một cách an toàn

Mô hình hoạt động hiệu quả: thiết lập một bước dựng (build step) chỉ sao chép những trang có `publish: true` sang một thư mục riêng, viết lại các liên kết trỏ tới những trang chưa xuất bản thành văn bản thuần túy, rồi mới dựng trang web từ bản sao đó.

Đừng bao giờ trỏ thẳng công cụ xuất bản vào Vault đang hoạt động của bạn. Chỉ một mẫu cấu hình (include pattern) bị sai lệch cũng đủ làm lộ toàn bộ dữ liệu, và một khi nội dung đã bị các trình thu thập dữ liệu (crawler) quét qua thì không còn cách nào thu hồi lại được nữa.

## Việc xuất bản ảnh hưởng thế nào đến cách bạn viết

Một trang wiki công khai sẽ làm thay đổi cách bạn viết ghi chú, và không hẳn theo chiều hướng tốt lên. Bạn bắt đầu viết cho khán giả đọc: rào đón nhiều hơn, giải thích dài dòng hơn, và giữ lại không dám viết ra những suy nghĩ còn đang phôi thai.

Mà những suy nghĩ đang phôi thai lại chính là lý do tồn tại của một Vault cá nhân. Nếu bạn muốn xuất bản, hãy cân nhắc giữ Vault riêng tư làm nơi làm việc chính và chỉ xuất bản một tập hợp con được chọn lọc có chủ đích, thay vì công khai toàn bộ rồi vô thức tự kiểm duyệt và làm trơn tru hóa mọi ghi chú của mình.

## Các định dạng trích xuất khác

Trích xuất ra PDF và HTML cho một báo cáo đơn lẻ, chuyển trực tiếp từ markdown bằng `pandoc`. Cách này hoàn toàn ổn khi cần chia sẻ một tài liệu riêng biệt.

Đừng trích xuất toàn bộ Vault sang bất kỳ định dạng nào mà bạn không thể tái tạo lại được. Các file markdown mới chính là tài sản cốt lõi.

## Tiếp theo

[Tự học từ chính Vault của bạn](teaching-yourself.md)
