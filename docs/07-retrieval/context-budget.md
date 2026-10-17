# Ngân sách ngữ cảnh (Context budget)

Mỗi trang mà Agent đọc đều tiêu tốn ngữ cảnh, và chất lượng phản hồi sẽ suy giảm trước cả khi Context window bị lấp đầy. Đọc nhiều hơn không đồng nghĩa với đọc tốt hơn.

## Tiết lộ lũy tiến (Progressive disclosure)

Mô hình hoạt động hiệu quả:

1. **Đọc chỉ mục trước.** Nắm được những gì đang tồn tại, mỗi mục một dòng.
2. **Mở các trang thực sự quan trọng.** Thường là từ ba đến tám trang.
3. **Lần theo các liên kết từng bước một (one hop),** dừng lại khi các trang mới không còn mang lại thêm thông tin.

Mỗi bước đều nhẹ nhàng và làm cơ sở định hướng cho bước tiếp theo. Cách làm ngược lại — nạp toàn bộ những gì có vẻ liên quan ngay từ đầu — sẽ đốt phần lớn ngân sách vào những trang hóa ra chẳng mấy ăn nhập, đồng thời đẩy các trang thực sự hữu ích vào khoảng giữa của một ngữ cảnh dài, nơi khả năng tập trung (attention) của mô hình yếu nhất.

## Tại sao không dán toàn bộ Vault vào

Các mô hình có Context window dài có thể chứa được rất nhiều dữ liệu, và người ta rất dễ bị cám dỗ bỏ qua hẳn bước truy xuất.

Có hai lý do không nên làm vậy. Thứ nhất, độ tập trung (attention) phân bổ không đồng đều trên một ngữ cảnh dài, và dữ liệu nằm ở phần giữa thường được sử dụng kém tin cậy hơn so với dữ liệu ở hai đầu — đây là phát hiện từ nghiên cứu "Lost in the Middle" và cũng là lý do vị trí đặt thông tin lại quan trọng đến thế. Thứ hai, một câu trả lời được tổng hợp từ tất cả mọi thứ sẽ không thể kiểm chứng: bạn hoàn toàn không biết mô hình thực sự đã dùng những trang nào.

Một câu trả lời trích dẫn năm trang mà bạn có thể mở ra kiểm tra luôn tốt hơn một câu trả lời trôi chảy được nhào nặn từ bốn trăm trang mà bạn không tài nào đối chiếu nổi.

## Các tầng tóm tắt (Summary layers)

Khi vượt quá vài trăm trang, hãy thêm một tầng chỉ mục trung gian giữa chỉ mục tổng (master index) và các trang chi tiết: một trang ngắn cho mỗi mảng chủ đề, liệt kê những gì có trong mảng đó và nội dung chính của từng trang.

Agent sẽ đọc chỉ mục tổng, mở đúng một chỉ mục chủ đề liên quan, rồi mới mở các trang chi tiết. Ba lần đọc nhẹ nhàng thay vì một lần đọc quá tải.

Đừng để các tầng tóm tắt chồng chất lên nhau. Hai cấp độ là đủ; đến cấp thứ ba nghĩa là bạn đang xây một hệ thống phân cấp không ai duy trì nổi, và bản tóm tắt của các bản tóm tắt sẽ dần lệch khỏi nội dung gốc bên dưới.

## Đo lường những gì đã được đọc

```
Liệt kê các trang bạn đã đọc để trả lời câu hỏi vừa rồi, theo đúng thứ tự bạn đã mở chúng.
```

Thỉnh thoảng rất đáng để chạy lệnh này. Nó phơi bày hai vấn đề: một là Agent đọc tới ba mươi trang trong khi chỉ cần sáu trang là đủ, và hai là Agent trả lời chỉ từ ba trang trong khi Vault có tới hai mươi trang liên quan. Cả hai đều có thể khắc phục bằng cách tinh chỉnh lại chỉ dẫn, và không vấn đề nào lộ diện nếu chỉ nhìn vào câu trả lời.

## Dùng Subagents cho các tác vụ đọc diện rộng

Khi một câu hỏi thực sự cần duyệt qua lượng lớn tài liệu, hãy giao việc đó cho một [Subagent](../06-agents/subagents.md). Subagent sẽ đọc trong Context window riêng của nó và chỉ trả về bản tóm tắt, nhờ vậy phiên làm việc chính chỉ tốn ngữ cảnh cho câu trả lời chứ không phải gánh toàn bộ tài liệu nguồn.

## Tiếp theo

[Đầu ra (Outputs)](../08-outputs/README.md), nơi Vault bắt đầu tạo ra sản phẩm thay vì chỉ trả lời câu hỏi.
