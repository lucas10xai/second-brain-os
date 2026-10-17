# Những lỗi ai cũng gặp phải

## Vault bị đình trệ sau hai tuần

Nguyên nhân gần như luôn nằm ở khâu thu thập (capture), chứ không phải do bản thân hệ thống. Việc lưu một bài viết mất tới ba cú nhấp chuột thay vì một, hoặc điện thoại của bạn không có đường truyền dữ liệu vào Vault, thế là tài liệu mới ngừng chảy về và chẳng còn gì để xử lý nữa.

Hãy sửa lại luồng thu thập dữ liệu, đừng sửa Vault. Xem thêm chương [Thu thập và nạp dữ liệu (Ingestion)](../03-ingestion/README.md).

Nguyên nhân còn lại là kỳ vọng thu về thành quả quá sớm. Khi mới chỉ có ba mươi trang thì chưa có gì nhiều để mà kết nối cả. Xem thêm [hình mẫu một Vault tốt](../01-concepts/what-good-looks-like.md) để nắm được lộ trình thời gian thực tế.

## Các trang chỉ là bản tóm tắt của các bản tóm tắt

Các trang nguồn tóm tắt lại bài viết gốc, rồi các trang khái niệm lại tóm tắt các trang nguồn đó. Qua mỗi tầng như vậy thông tin lại rơi rụng bớt, trong khi tầng dưới cùng mới là thứ được đọc.

Nguyên nhân là do quy ước trang (page contract) có chứa từ "tóm tắt" (summarise) ở đâu đó. Các trang khái niệm phải giải thích một ý tưởng bằng ngôn từ rõ ràng, theo cách hiểu của bạn, và có khả năng đứng độc lập. Hãy viết lại quy ước trong `CLAUDE.md` rồi chạy Ingest lại một vài tài liệu nguồn để kiểm tra.

## Agent viết đè lên những nội dung bạn tự viết tay

Điều này cực kỳ gây ức chế nhưng hoàn toàn có thể phòng tránh được. Hãy đánh dấu các trang do bạn tự viết tay trong phần Frontmatter:

```yaml
maintained_by: human
```

Và bổ sung quy tắc vào `CLAUDE.md`: tuyệt đối không bao giờ viết lại một trang có gắn nhãn `maintained_by: human`, chỉ được phép nối thêm các liên kết ở cuối trang và gắn cờ báo cáo các vấn đề cho chủ sở hữu.

## Chất lượng Ingest giảm dần khi Vault lớn lên

Đây là hiện tượng có thật, và nguyên nhân thường nằm ở ngữ cảnh. Khi Ingest vào một Vault đã có ba trăm trang, lẽ ra Agent phải kiểm tra xem những trang nào đã tồn tại trước, và nếu nó bỏ qua bước đó, nó sẽ cứ thế tạo ra các trang mới tinh thay vì cập nhật vào các trang sẵn có.

Hãy kiểm tra để đảm bảo quy trình Ingest luôn đọc `index.md` trước khi đặt bút viết. Chỉ riêng một bước đó thôi là đủ để giữ cho chất lượng ổn định khi Vault ngày một phình to.

## Mọi thứ đều liên kết với mọi thứ

Một vài trang trung tâm (hub pages) tích tụ mọi liên kết đổ về, khiến cho Knowledge graph mất hết khả năng biểu đạt thông tin. Hãy tách nhỏ các trang trung tâm đó thành những ý tưởng cụ thể mà các trang khác thực sự muốn nhắm tới. Xem thêm [quy tắc liên kết](../04-structuring/linking-rules.md).

## Bạn ngừng mở Vault ra xem

Sự thất bại thực tế nhất. Thường là do luồng thu thập đã gãy từ nhiều tháng trước khiến Vault rơi vào trạng thái đóng băng, hoặc do bản báo cáo rà soát định kỳ quá dài dòng khiến bạn ngại đọc.

Cả hai vấn đề này đều sửa được. Không vấn đề nào là lý do chính đáng để đập đi xây lại từ đầu bằng một công cụ khác — đó là phản xạ bản năng nhưng lúc nào cũng chỉ làm bạn tốn thêm một tháng trời vô ích.

## Tiếp theo

[Agent viết ra nội dung rác](agent-writes-garbage.md)
