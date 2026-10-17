# YouTube và podcast

Video là nguồn thông tin ngốn nhiều thời gian nhất nhưng lại đọng lại trong trí nhớ ít nhất đối với hầu hết mọi người. Một bài thuyết trình hội thảo dài một tiếng đồng hồ thường chẳng để lại dấu vết gì trong đầu bạn chỉ sau một tuần. Bản gỡ băng (Transcripts) giải quyết triệt để vấn đề đó — bởi bản chất Transcript chỉ là văn bản thuần túy, đúng thứ mà Vault của bạn xử lý tốt nhất.

## Trích xuất bản gỡ băng (Transcript)

Hầu hết các video đều có sẵn phụ đề, hoặc do hệ thống tự động tạo hoặc do người đăng tải lên. Có hai cách trích xuất đáng tin cậy nhất:

```bash
# yt-dlp: subtitles only, no video download
yt-dlp --write-auto-sub --skip-download --sub-format vtt --sub-lang en URL
```

```python
# youtube-transcript-api, if you want it in a script
from youtube_transcript_api import YouTubeTranscriptApi
lines = YouTubeTranscriptApi.get_transcript("VIDEO_ID")
```

Hãy lưu kết quả thu được vào thư mục `raw/` kèm theo phần Frontmatter ghi rõ tiêu đề video, tên kênh và đường dẫn URL. Nếu thiếu URL, bản gỡ băng sẽ chỉ là một bức tường chữ vô danh và Agent không thể trích dẫn nguồn chính xác được.

## Giữ lại các dấu mốc thời gian (Timestamps)

Các bản gỡ băng tự động thường được xuất ra dưới dạng những câu ngắn cắt vụn kèm dấu thời gian dày đặc. Hãy lọc bỏ các thẻ định dạng thừa, nhưng giữ lại các mốc thời gian thô cách nhau mỗi vài phút.

Lý do nằm ở khâu truy xuất kiểm chứng sau này: khi trang wiki ghi nhận một luận điểm được nêu ở phút thứ 34 của bài nói chuyện, bạn có thể mở video tua đến đúng chỗ đó kiểm tra chỉ trong mười giây. Nếu không có mốc thời gian, việc kiểm chứng đồng nghĩa với việc phải ngồi xem lại cả video — và chắc chắn bạn sẽ bỏ qua không kiểm tra nữa.

## Làm sạch văn bản trước khi Ingest

Phụ đề tự động thường không có dấu câu, không phân biệt người nói và viết sai chính tả hàng loạt thuật ngữ chuyên ngành. Hãy yêu cầu Agent chạy một lượt làm sạch văn bản trước tiên:

```
Read raw/talk-transcript.md. Add punctuation and paragraph breaks, label
speakers where they change, and fix obvious mistranscriptions of technical
terms. Do not summarise, do not cut anything, and flag anything you could not
make sense of.
```

Đừng đốt cháy giai đoạn mà nạp thẳng bản phụ đề thô chưa qua xử lý vào hệ thống. Các trang khái niệm được tạo ra từ văn bản không dấu câu có chất lượng tệ hơn hẳn, bởi mô hình AI phải tiêu tốn năng lực chú ý (attention) vào việc đoán ranh giới câu thay vì tập trung phân tích các luận điểm chuyên môn.

## Xử lý video thời lượng dài

Một tập podcast dài ba tiếng đồng hồ không phải là một nguồn tài liệu đơn lẻ. Hãy chia nhỏ nó theo từng chủ đề trước khi đưa vào Ingest — có thể dựa theo các mốc chương (chapter markers) nếu người đăng video có gắn sẵn, hoặc yêu cầu Agent đọc bản gỡ băng và đề xuất các điểm ngắt đoạn hợp lý.

Nếu nạp nguyên cả khối, một cuộc phỏng vấn dài sẽ chỉ đẻ ra một trang nguồn phình to nặng nề cùng hai ba trang khái niệm chung chung mờ nhạt. Ngược lại, nếu chia nhỏ ra, nó sẽ kết tinh thành bốn ý tưởng sắc bén thực sự nằm bên trong cuộc trò chuyện đó.

## Podcast và các nguồn chỉ có âm thanh

Các chương trình podcast hiếm khi đính kèm sẵn bản gỡ băng. Các phương án xử lý, xếp theo thứ tự công sức tăng dần: kiểm tra phần ghi chú tập phát sóng (show notes) vì hiện nay khá nhiều kênh đã đăng kèm văn bản tại đây; chạy mô hình nhận diện giọng nói Whisper cục bộ trên máy; hoặc sử dụng dịch vụ gỡ băng trả phí.

Việc thiết lập Whisper chạy cục bộ rất đáng công sức nếu bạn có thói quen nghe podcast hằng ngày. Toàn bộ file âm thanh không bao giờ rời khỏi máy tính của bạn — một yếu tố đặc biệt quan trọng đối với các bản ghi âm cuộc họp nội bộ hơn cả podcast.

## Những nội dung nào thực sự đáng gỡ băng

Các bài diễn thuyết chuyên sâu, bài giảng, các cuộc phỏng vấn với những người làm nghề thực chiến, hoặc bất kỳ nội dung nào đưa ra những nhận định, số liệu cụ thể mà sau này bạn sẽ cần tra cứu lại.

Đừng gỡ băng những video hướng dẫn cầm tay chỉ việc (tutorials) mà bạn chỉ xem một lần để làm theo cho xong việc, hay những video mà nếu chuyển thành bài viết chữ thì bạn cũng chẳng buồn đọc lại. Video thường tạo cảm giác giá trị cao trong lúc xem chỉ vì nó tiêu tốn của bạn cả một tiếng đồng hồ — nhưng cảm giác đó không phải là tín hiệu phản ánh chất lượng thực sự của nội dung.

## Tiếp theo

[PDF, bài báo khoa học và sách](pdfs-and-books.md)
