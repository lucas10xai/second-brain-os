# Bản tin (Newsletters) và email

Bản tin định kỳ (newsletters) là nguồn dữ liệu dễ tự động hóa nhất nhưng cũng là thứ dễ bị nạp quá đà (over-ingest) nhất. Hãy tự động hóa khâu thu thập về kho thô, nhưng phải thật khắt khe khi quyết định nội dung nào xứng đáng có một trang wiki riêng — bởi một luồng dữ liệu tự động nạp không kiểm soát sẽ vui vẻ lấp đầy Vault của bạn bằng hàng trăm trang rác mỗi tháng mà bạn chẳng hề yêu cầu.

## Tạo một địa chỉ email chuyên dụng

Hãy tạo một địa chỉ email chỉ tồn tại với mục đích duy nhất là phục vụ cho Vault, rồi chuyển toàn bộ các gói đăng ký nhận bản tin của bạn sang địa chỉ đó. Chỉ một bước đơn giản này sẽ giúp tách bạch hoàn toàn những tư liệu bạn muốn lưu giữ khỏi mớ hỗn độn trong hộp thư cá nhân, đồng thời đảm bảo các quy trình tự động hóa không bao giờ chạm vào email làm việc thật của bạn.

Từ địa chỉ chuyên dụng đó, hãy thiết lập chuyển tiếp tự động (forward) vào thư mục `raw/` bằng bất kỳ công cụ tự động hóa nào bạn quen dùng. Mọi quy tắc có khả năng ghi nội dung ra thành file đều đáp ứng tốt công việc này.

## Khử trùng lặp thông tin

Các bản tin tổng hợp thường xuyên lặp lại nội dung của nhau. Cùng một sự kiện ra mắt sản phẩm có thể xuất hiện trên bốn bản tin khác nhau trong cùng một tuần, mỗi nơi đều nêu bấy nhiêu thông tin cơ bản và chỉ đổi khác đi câu mở đầu.

Nếu cứ thế đưa thẳng vào Ingest, bạn sẽ nhận về bốn trang nguồn cùng nói về một thứ và một trang khái niệm trích dẫn cả bốn nguồn đó như thể chúng là các bằng chứng độc lập củng cố cho nhau. Việc các bản tin dẫn lại cùng một nguồn tin không phải là sự xác nhận độc lập, và một hệ thống wiki đánh đồng hai điều đó sẽ thổi phồng mức độ tin cậy của thông tin lên quá mức thực tế.

Hãy chỉ dẫn rõ ràng cho quy trình Ingest:

```
These are newsletters. Several will cover the same item. Group them by topic
first, write one source page per actual item citing every newsletter that
mentioned it, and note where they disagree. Do not treat repetition across
newsletters as confirmation.
```

## Nội dung nào thực sự xứng đáng có một trang riêng

Bản chất của hầu hết các bản tin là một danh sách liên kết kèm theo vài dòng bình luận ngắn. Phần bình luận đó hiếm khi đủ sâu sắc để tạo thành một trang khái niệm; thứ nằm phía sau đường dẫn liên kết đôi khi mới là thứ đáng giá.

Cách làm hiệu quả nhất là để Agent đọc lướt qua toàn bộ các bản tin trong tuần rồi lập cho bạn một danh sách rút gọn:

```
Read this week's newsletters in raw/newsletters/. List anything worth reading in
full, with one line on why. Ingest nothing yet.
```

Sau đó, bạn chỉ cần mở và lưu (clip) hai hoặc ba nguồn tài liệu gốc thực sự chất lượng rồi chạy Ingest cho đúng những tài liệu gốc đó. Như vậy, bản tin đã hoàn thành xuất sắc vai trò bộ lọc sơ cấp, còn Vault của bạn thì lưu giữ được nguồn tư liệu gốc chuẩn xác thay vì một bản tóm tắt tam sao thất bản.

## Email trao đổi thông thường

Phần lớn email hàng ngày không nên có mặt trong một Second Brain. Các chuỗi thư bàn về lịch hẹn, hóa đơn thanh toán, hay trao đổi hậu cần qua lại: không có thứ nào trong đó là tri thức, tất cả chỉ là rác dung lượng.

Những thứ duy nhất đáng để Ingest: các chuỗi email nơi một quyết định quan trọng được chốt lại hoặc một vấn đề chuyên môn được giải thích thấu đáo. Hãy đưa chúng vào hệ thống bằng cách chủ động bấm chuyển tiếp (forward) từng chuỗi thư một sang địa chỉ email thu thập chuyên dụng.

Tuyệt đối không bao giờ đấu nối tự động toàn bộ hộp thư đến của bạn xả thẳng vào `raw/` theo lịch định kỳ. Làm vậy sẽ nạp bừa bãi mọi thông tin về tất cả những người từng trao đổi thư từ với bạn — mà phần lớn trong số đó là dữ liệu riêng tư của họ chứ không phải của bạn.

## Tiếp theo

[Nạp bù dữ liệu tồn đọng nhiều năm (Bulk backfill)](bulk-backfill.md)
