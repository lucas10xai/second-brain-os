# Vault phình ra quá lớn

## Triệu chứng

Các câu trả lời ngày càng chậm chạp và mơ hồ hơn. Agent đọc tới hai mươi trang nhưng chỉ trả về những nhận xét chung chung. Chế độ xem đồ thị trông như một cuộn len rối bù. Bạn không còn nhớ nổi một chủ đề đã được ghi chép hay chưa, và việc lục tìm trong Vault còn mất nhiều thời gian hơn cả việc lên mạng tìm kiếm lại từ đầu.

## Những thứ thường không phải là nguyên nhân

Dung lượng ổ đĩa, tốc độ tìm kiếm, hay bản thân phần mềm Obsidian. Tất cả những thứ đó đều mở rộng quy mô rất tốt.

Nguyên nhân thực sự nằm ở kinh tế học truy xuất (retrieval economy). Trang chỉ mục đã dài đến mức chỉ riêng việc đọc nó thôi cũng tiêu tốn một lượng ngữ cảnh đáng kể, khiến Agent hoặc là bỏ qua luôn trang chỉ mục, hoặc là đốt hết ngân sách ngữ cảnh ngay tại đó thay vì dành cho việc đọc các trang nội dung.

## Trước hết, hãy kiểm tra xem vấn đề là do quy mô hay do sự mục ruỗng cấu trúc

Hãy chạy công cụ đo lường [các chỉ số](../05-graphs/metrics.md). Một Vault có tỷ lệ trang mồ côi lên tới hai mươi phần trăm không hề gặp vấn đề về quy mô, mà đang gặp vấn đề về gắn kết liên kết — và việc tách nhỏ Vault sẽ chẳng giúp ích được gì.

Một Vault thực sự lớn nhưng khỏe mạnh sẽ có các đặc điểm sau: tỷ lệ trang mồ côi thấp, có một thành phần liên thông chính chiếm ưu thế, bậc liên kết trung bình (average degree) nằm trong ngưỡng chuẩn, và trang chỉ mục có hơn vài trăm mục.

## Các tầng tóm tắt (Summary layers)

Giải pháp đầu tiên và thường là đã đủ để giải quyết vấn đề. Hãy thêm một trang chỉ mục cho từng mảng chủ đề nằm giữa chỉ mục tổng (master index) và các trang chi tiết, để Agent thực hiện ba lần đọc nhẹ nhàng thay vì một lần đọc quá tải. Xem thêm [mở rộng quy mô](../09-maintenance/scaling.md).

## Tách nhỏ Vault

Hãy tách theo lĩnh vực chuyên môn (domain), tuyệt đối không tách theo mốc thời gian. Tạo thành hai Vault thực sự không bổ trợ thông tin qua lại cho nhau.

Hãy chấp nhận rằng các kết nối xuyên lĩnh vực sẽ không còn diễn ra nữa. Đó thường lại là những liên kết thú vị nhất, và vì thế việc tách nhỏ Vault chỉ nên là nước đi cuối cùng thay vì là phản ứng đầu tiên.

## Lưu trữ lạnh (Archiving)

Đưa các tư liệu ít dùng ("lạnh") sang thư mục `archive/`, nằm bên ngoài `wiki/`. Chúng vẫn có thể tìm kiếm được, nhưng rút khỏi trang chỉ mục cũng như Knowledge graph, và hoàn toàn có thể khôi phục lại khi cần.

Cách này tốt hơn việc xóa bỏ hoàn toàn, bởi đánh giá một nội dung là "lạnh" chỉ mang tính phỏng đoán và những tư liệu đã lưu trữ hoàn toàn có thể trở nên hữu ích trở lại.

## Dựng lại trang chỉ mục

Đôi khi vấn đề đơn giản chỉ là trang chỉ mục đã bị trôi dạt lệch khỏi thực tế: vẫn còn giữ các mục trỏ tới những trang đã di chuyển đi nơi khác, hoặc thiếu mất các mục cho những trang được thêm vào từ các lượt chạy bị đứt gánh giữa đường.

```
Hãy dựng lại index.md từ nội dung thực tế hiện có trong thư mục wiki/. Nhóm theo loại trang và chủ đề, mỗi mục kèm một dòng mô tả ngắn gọn, và liệt kê các khoảng trống kiến thức (gaps) ở dưới cùng.
```

Thao tác này rất nhẹ nhàng, nhưng lại khắc phục được một tỷ lệ đáng kinh ngạc những lời phàn nàn kiểu "cảm giác như Vault đang bị hỏng".

## Tiếp theo

[Câu hỏi thường gặp (FAQ)](faq.md)
