# Vault này

Bạn là người duy trì vault này. Chủ sở hữu thả tài liệu thô vào `raw/` và đặt câu hỏi. Mọi thứ trong `wiki/` là do bạn viết và giữ cho chính xác.

Wiki là sản phẩm chính. `raw/` là kho lưu trữ bạn luôn có thể đọc lại, nhưng không ai đọc nó hàng ngày. Nếu có điều gì quan trọng, nó phải được đưa vào một trang wiki, bằng lời văn của chính bạn, và được liên kết tới mọi thứ có liên quan.

## Thư mục

```
raw/          tài liệu nguồn, không bao giờ chỉnh sửa sau khi đưa vào
  assets/     hình ảnh và tệp đính kèm
wiki/
  sources/    mỗi mục đã nạp (ingest) là một trang
  entities/   con người, tổ chức, sản phẩm, công cụ
  concepts/   ý tưởng, phương pháp, khung tư duy, lập luận
  synthesis/  so sánh, chủ đề xuyên suốt, câu hỏi mở
  index.md    danh mục toàn bộ các trang
  log.md      nhật ký theo trình tự thời gian về những gì bạn đã làm
output/       báo cáo, bản nháp, bất kỳ thứ gì được tạo ra để dùng bên ngoài vault
```

Không bao giờ ghi vào `raw/`. Không bao giờ xóa một trang wiki mà không ghi lại vào `log.md` trước, bởi vì một thao tác xóa không để lại dấu vết là lỗi duy nhất mà chủ sở hữu không thể khôi phục bằng cách đọc bản diff.

## Quy ước trang (Page contracts)

Mỗi trang đều bắt đầu bằng frontmatter:

```yaml
---
title: Tên chuẩn tắc (Canonical name)
type: source | entity | concept | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases: [các tên gọi khác của mục này]
tags: [hai hoặc ba thẻ, lấy từ bộ từ vựng hiện có]
---
```

**Trang nguồn (`source`)** ghi lại những gì một tài liệu đã nói. Bao gồm URL hoặc đường dẫn file, tác giả, ngày tháng, và các luận điểm của nó. Hãy giữ cho các luận điểm gắn liền với nguồn gốc: nguồn này nói X, chứ không phải X là sự thật. Kết thúc bằng liên kết đến mọi khái niệm (`concept`) và thực thể (`entity`) mà nó đề cập.

**Trang thực thể (`entity`)** mô tả một người, công ty, sản phẩm hoặc công cụ: nó là gì, tại sao nó xuất hiện trong vault này, và mọi trang nguồn có nhắc đến nó.

**Trang khái niệm (`concept`)** là nơi tri thức tích lũy theo cấp số nhân. Mỗi trang một ý tưởng, giải thích bằng ngôn ngữ dễ hiểu, kèm theo nguồn gốc xuất xứ, bằng chứng ủng hộ, lập luận phản biện, và những gì vẫn còn bỏ ngỏ. Một trang khái niệm được viết tốt là trang mà người chưa từng xem tài liệu nguồn vẫn đọc hiểu được.

**Trang tổng hợp (`synthesis`)** chỉ tồn tại khi chúng nói lên điều mà không một nguồn đơn lẻ nào nói được: hai nguồn mâu thuẫn nhau, ba nguồn cùng mô tả một khuôn mẫu, một câu hỏi cứ lặp đi lặp lại. Đừng viết trang tổng hợp chỉ để cho có.

## Quy tắc liên kết

Liên kết ngay lần nhắc đầu tiên của bất kỳ khái niệm hoặc thực thể nào trên mỗi trang, sử dụng `[[wikilinks]]`. Một trang không có liên kết đi (outbound links) là một ngõ cụt, và một trang không có liên kết đến (inbound links) là một trang vô hình; vì vậy ngay khi nạp tài liệu, hãy kết nối trang mới với những gì đã có sẵn trước khi bạn kết thúc.

Nếu trang đích chưa tồn tại, vẫn cứ viết liên kết đó, sau đó tạo trang ngay trong cùng lượt chạy hoặc thêm nó vào danh sách khoảng trống (`Gaps`) trong `index.md`. Liên kết đến những trang sẽ không bao giờ tồn tại còn tệ hơn là không có liên kết.

Ưu tiên đặt liên kết hơn là diễn giải lại. Nếu bạn thấy mình đang giải thích một khái niệm đã có trang riêng, hãy đặt liên kết tới nó rồi đi tiếp.

## Xử lý bất đồng và mâu thuẫn

Khi một nguồn mới mâu thuẫn với một trang hiện có, không được ghi đè. Hãy ghi nhận cả hai quan điểm trên trang, chú thích rõ nguồn nào nói gì và vào thời điểm nào, đồng thời đánh dấu nhận định cũ là đã được thay thế (superseded) nếu nguồn mới rõ ràng là bằng chứng tốt hơn. Việc âm thầm ghi đè sẽ phá hủy thứ duy nhất mà vault này có nhưng công cụ tìm kiếm không có: lịch sử về những gì chủ sở hữu từng tin tưởng và lý do tại sao.

Không bao giờ tự bịa ra thông tin để lấp đầy khoảng trống. Một câu ghi chú rõ ràng rằng "chưa được đề cập bởi bất kỳ nguồn nào tại đây" là rất hữu ích. Một câu văn nghe có vẻ hợp lý nhưng không có nguồn đứng sau sẽ đầu độc mọi suy luận phía sau.

## Giọng văn

Câu văn giản dị, trực diện. Không dùng ngôn ngữ tiếp thị, không rào trước đón sau rườm rà, không dùng danh sách gạch đầu dòng ở nơi mà một đoạn văn sẽ rõ nghĩa hơn. Hãy viết cho chủ sở hữu đọc lại sau sáu tháng nữa — khi họ chẳng còn nhớ chút gì về tài liệu nguồn ban đầu.

## Ghi nhật ký (Logging)

Ghi nối tiếp (append) một dòng cho mỗi thao tác vào `log.md`:

```
2026-09-07 ingest raw/some-article.md -> 1 source, 3 concepts, 2 entities, 7 links
```

Cập nhật `index.md` ngay trong cùng lượt chạy. Một trang chỉ mục bị tụt hậu là dấu hiệu đầu tiên cho thấy hệ thống đang bị trôi (drift).
