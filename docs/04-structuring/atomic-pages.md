# Mỗi trang một ý tưởng

Mỗi trang chỉ chứa một ý tưởng duy nhất, được giải thích đủ rõ ràng để một người chưa từng xem tài liệu nguồn vẫn có thể hiểu được.

Quy tắc này tồn tại vì cách thức hoạt động của cơ chế truy xuất (retrieval). Khi `Agent` trả lời một câu hỏi, nó sẽ nạp toàn bộ nội dung của các trang liên quan. Một trang ôm đồm bốn chủ đề sẽ kéo theo ba chủ đề không liên quan vào `Context window` mỗi khi được chạm tới. Ngược lại, một trang chỉ bàn về một chủ đề duy nhất sẽ được liên kết chính xác, truy xuất chính xác và cập nhật mà không gây ảnh hưởng dây chuyền.

## Tính nguyên tử (Atomic) ở đây nghĩa là gì

Không phải là ngắn. Một trang khái niệm có thể dài vài trăm từ. Nguyên tử (atomic) có nghĩa là trang đó chỉ có một chủ đề duy nhất và bạn có thể đặt cho nó một tiêu đề chính xác mà không cần dùng đến từ "và".

Nếu tiêu đề cần từ "và", hoặc trang có các tiêu đề phụ (headings) cho những chủ đề không liên quan đến nhau, thì đó thực chất là hai trang.

## Tách nhỏ một tài liệu nguồn

Một bài viết thông thường sẽ tạo ra từ một đến ba khái niệm xứng đáng có trang riêng, cộng với một trang nguồn (source page) ghi lại những gì bản thân bài viết đó đã trình bày.

Bài kiểm tra để xem liệu một nội dung có xứng đáng có trang riêng hay không: nó có thể được giải thích mà không cần tham chiếu ngược lại tài liệu nguồn duy nhất này không? Một ý tưởng chỉ có ý nghĩa dưới dạng "những gì bài viết này lập luận" thì thuộc về bên trong trang nguồn đó. Một ý tưởng sẽ lặp lại qua nhiều tài liệu nguồn khác nhau thì cần trang riêng của nó, vì đó là nơi các tài liệu nguồn khác sẽ liên kết vào.

## Sai lầm ở cả hai thái cực

**Tách quá nhỏ (Over-splitting)** tạo ra mười trang từ một bài viết, mỗi trang chỉ là một đoạn văn được diễn đạt lại, và mỗi trang chỉ liên kết ngược về trang nguồn đó. Đồ thị trông có vẻ dày đặc nhưng thực chất không nói lên điều gì. Đây là lỗi phổ biến hơn khi dùng `Agent`, vì việc tách nhỏ tạo cảm giác như đang làm việc rất kỹ lưỡng.

**Tách quá ít (Under-splitting)** tạo ra các trang nguồn chỉ là bản tóm tắt bài viết và một `wiki/` hoàn toàn không có trang khái niệm nào. Bạn sẽ kết thúc với một kho lưu trữ chỉ để tìm kiếm từ khóa — thứ mà bạn vốn đã có sẵn.

Nếu bạn không chắc chắn, hãy viết ít trang hơn. Việc gộp trang sau này rất rẻ; còn gỡ rối hàng trăm mảnh vụn thì không.

## Độ dài

Một trang khái niệm dưới khoảng tám mươi từ thường là một trang sơ khai (stub) bị viết hỏng chứ không phải là một trang súc tích. Hoặc là tài liệu nguồn không thực sự bàn sâu về nó, hoặc là `Agent` đã bỏ cuộc giữa chừng. Cả hai trường hợp này đều đáng được phát hiện trong một lượt chạy `Lint`.

Một trang dài quá khoảng một nghìn từ thường là hai ý tưởng đã phát triển dính liền vào nhau. Hãy đọc lại và tìm đường ranh giới để tách chúng ra.

## Tiếp theo

[Bốn loại trang](page-types.md)
