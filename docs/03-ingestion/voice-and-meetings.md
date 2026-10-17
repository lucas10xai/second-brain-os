# Ghi chú giọng nói và cuộc họp

Những ý tưởng thực sự đáng giá hiếm khi xuất hiện đúng lúc bạn đang ngồi ngay ngắn trước bàn làm việc. Giọng nói là phương thức thu thập duy nhất hoạt động hiệu quả khi bạn đang đi bộ, lái xe hay đứng xếp hàng — nhưng lại là kênh thông tin mà hầu hết các Vault chưa bao giờ được kết nối tới.

## Thu âm nhanh (Capture)

Bất kỳ ứng dụng ghi âm nào cũng dùng được, miễn là file âm thanh cuối cùng tự động nằm ở một nơi mà Vault có thể chạm tới. Lực cản lớn nhất cần phải triệt tiêu chính là bước chuyển file: nếu việc đưa một đoạn ghi âm từ điện thoại vào Vault đòi hỏi nhiều hơn một thao tác bấm nút, sớm muộn gì bạn cũng sẽ ngừng sử dụng nó.

Thiết lập đơn giản và tin cậy nhất: ghi âm bằng ứng dụng mặc định trên điện thoại, chia sẻ vào một thư mục đám mây, và thiết lập một tác vụ tự động chạy theo lịch để gỡ băng mọi file âm thanh mới thành văn bản lưu vào `raw/`.

Ứng dụng Obsidian trên di động cũng hỗ trợ ghi âm trực tiếp vào thẳng bên trong Vault, giúp loại bỏ hoàn toàn bước chuyển file trung gian nếu bạn đã thiết lập sẵn đồng bộ trên điện thoại.

## Chuyển giọng nói thành văn bản (Transcription)

Mô hình Whisper chạy cục bộ trên máy có chất lượng hoàn toàn đủ tốt cho một đoạn ghi chú giọng nói thu ở khoảng cách cầm tay. Việc xử lý cục bộ ở đây quan trọng hơn nhiều so với các nguồn tài liệu khác, bởi ghi chú giọng nói thường chứa những suy nghĩ cá nhân còn dang dở, và bản ghi âm cuộc họp thì chứa lời nói của nhiều người khác.

Hãy lường trước việc các tên riêng và thuật ngữ kỹ thuật sẽ bị nhận diện sai. Hãy sửa lại chúng ngay tại thời điểm Ingest chứ đừng để sang hôm sau, tranh thủ lúc bạn vẫn còn nhớ rõ mình đã nói gì.

## Ghi chú giọng nói là bản nháp, không phải nguồn tư liệu

Một đoạn ghi chú giọng nói là quá trình bạn đang vừa nghĩ vừa nói thành tiếng, lẫn lộn nhiều câu nói vấp và những ý tưởng bỏ dở giữa chừng. Nếu Ingest nguyên văn bản gỡ băng đó, bạn sẽ nhận về một trang nguồn lủng củng và tối nghĩa.

Thay vào đó, hãy coi bản gỡ băng này là nguyên liệu đầu vào thô cho một ý tưởng duy nhất:

```
This is a voice note, my own thinking out loud. Extract the actual idea, drop
the false starts and repetition, and write it as one short concept page in my
words. If there are two unrelated ideas, make two pages. Keep the recording date.
```

## Cuộc họp

Các cuộc họp thường tạo ra ba thứ rất đáng lưu giữ và vô số lời bàn tán không cần thiết: các quyết định đã chốt, các cam kết công việc kèm tên người phụ trách, và những câu hỏi còn bỏ ngỏ.

```
This is a meeting transcript. Extract decisions made, commitments with who owns
each one, and open questions. Link every person mentioned to their entity page.
Skip discussion that did not lead anywhere.
```

Hãy chuyển các cam kết công việc vào thư mục `Inputs/` của dự án tương ứng thay vì đưa vào tầng `wiki/`. Một lời cam kết giao việc là tác vụ cần làm chứ không phải tri thức lâu dài, và nó sẽ hết hạn chỉ sau một tuần. Bài viết [Cấu trúc hai tầng](../01-concepts/two-layers.md) đã giải thích kỹ vì sao sự tách biệt này lại quan trọng đến vậy.

## Sự đồng thuận và quyền riêng tư của người khác

Việc ghi âm người khác chịu sự điều chỉnh của các quy định pháp lý khác nhau tùy theo từng quốc gia và vùng lãnh thổ — và đây không phải là chuyện thủ tục hình thức. Nhiều nơi quy định bắt buộc phải có sự đồng thuận của tất cả những người tham gia cuộc trò chuyện.

Tách biệt với khía cạnh pháp lý: bản gỡ băng một cuộc họp chứa đựng những lời nói tự nhiên không phòng bị của người khác. Hãy giữ những nội dung đó tránh xa khỏi bất kỳ Vault nào bạn có ý định chia sẻ, đồng thời cân nhắc kỹ xem liệu toàn bộ nội dung cuộc họp có thực sự cần nằm trong tầng tri thức hay không, hay chỉ cần giữ lại đúng ba quyết định đã được trích xuất là đủ.

## Tiếp theo

[Bản tin (Newsletters) và email](newsletters-and-email.md)
