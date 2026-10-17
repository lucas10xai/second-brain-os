# Bốn loại trang

Bốn loại trang, mỗi loại đảm nhận một nhiệm vụ riêng. Mọi trang đều khai báo loại của mình trong `Frontmatter`, giúp bạn truy vấn `Vault` theo cấu trúc hình thái thay vì phải đọc toàn bộ nội dung.

## Tài liệu nguồn (Sources)

Mỗi mục được `Ingest` tương ứng với một trang. Trang này ghi lại những gì bài viết, video, bài báo khoa học hoặc cuộc hội thoại đó đã nói.

Ghi nhận các nhận định đúng như bản chất của chúng: nguồn này nói X, kèm theo URL, tác giả và ngày tháng. Nó không đánh giá đúng sai. Nó không trộn lẫn quan điểm của các nguồn khác vào.

Các trang nguồn là dấu vết kiểm toán (audit trail). Khi một trang khái niệm nêu ra điều gì đó đáng ngạc nhiên, các trang nguồn đứng sau nó chính là cách để bạn kiểm tra xem điều đó có thực sự từng được nói đến hay không.

## Thực thể (Entities)

Con người, tổ chức, sản phẩm, công cụ. Nó là gì, tại sao nó xuất hiện trong `Vault` của bạn, và mọi nơi có nhắc đến nó.

Các trang thực thể rất dễ tạo và mang lại giá trị theo một cách không hề hiển nhiên cho đến khi `Vault` của bạn đủ lớn. Chúng trở thành những điểm nối (join points) tự nhiên: ba tài liệu nguồn không liên quan cùng nhắc đến một công ty bỗng nhiên kết nối với nhau thông qua thực thể đó, và mối liên kết ấy thường chính là điều đáng chú ý.

Đừng viết tiểu sử. Một trang thực thể chỉ lưu giữ những gì liên quan đến `Vault` của bạn, không phải những gì Wikipedia lưu giữ.

## Khái niệm (Concepts)

Ý tưởng, phương pháp, framework, lập luận. Đây là những trang mang lại giá trị tích lũy kép (compound).

Một trang khái niệm giải thích ý tưởng bằng ngôn ngữ rõ ràng, dễ hiểu, nêu rõ nó bắt nguồn từ đâu, bằng chứng nào ủng hộ nó, lập luận nào phản bác nó, và điều gì vẫn còn bỏ ngỏ. Khi được viết tốt, một người chưa từng xem bất kỳ tài liệu nguồn nào của bạn — bao gồm cả chính bạn sau một năm nữa — vẫn có thể đọc hiểu trọn vẹn.

Đây là loại trang duy nhất mà `Agent` nên tổng hợp thông tin xuyên suốt nhiều nguồn thay vì chỉ ghi chép lại.

## Tổng hợp (Synthesis)

Các phép so sánh, chủ đề lớn, câu hỏi mở. Một trang tổng hợp chỉ tồn tại khi nó nói lên được điều mà không một nguồn đơn lẻ nào nói tới: hai nguồn mâu thuẫn nhau, ba nguồn cùng mô tả một khuôn mẫu (pattern), hoặc một câu hỏi cứ lặp đi lặp lại qua các tài liệu tưởng chừng không liên quan.

Quy tắc giúp các trang này luôn trung thực: đừng viết một trang tổng hợp chỉ để cho có. Một `Agent` khi được yêu cầu tổng hợp sẽ luôn nặn ra được thứ gì đó, và những chủ đề gượng gạo chính là con đường nhanh nhất làm đầy `wiki/` bằng những lời vô nghĩa đầy vẻ tự tin.

## Khi ranh giới giữa các loại bị mờ đi

Một số thứ hợp lệ ở cả hai loại. Một phương pháp luận được đặt theo tên tác giả của nó vừa là một thực thể (entity), vừa là một khái niệm (concept). Hãy chọn một loại — thường là khái niệm — và gắn cho tên còn lại một `Aliases` trỏ về trang đó.

Một số thứ không thuộc loại nào cả. Một công thức, một đoạn cấu hình (config snippet), một danh sách kiểm tra (checklist). Đó là tài liệu tham khảo (reference material), không phải tri thức, và chúng thuộc về một thư mục dự án hơn là nằm trong `wiki/`.

## Tiếp theo

[Quy tắc liên kết](linking-rules.md)
