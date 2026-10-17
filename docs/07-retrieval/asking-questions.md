# Đặt câu hỏi cho Vault

Bạn xây dựng Vault để câu trả lời xuất phát từ những gì bạn thực sự đã đọc. Một Agent âm thầm quay về dùng kiến thức sẵn có của chính nó sẽ phá hỏng mục đích đó một cách vô hình: câu trả lời nghe rất trôi chảy, hợp lý nhưng lại không thể kiểm chứng.

## Quy tắc cốt lõi

Mọi nhận định trong câu trả lời phải xuất phát từ một trang cụ thể và chỉ rõ tên trang đó.

```
Chỉ trả lời dựa trên Vault của tôi. Trích dẫn trang tương ứng cho từng nhận định. Nếu Vault không bao hàm phần nào của câu hỏi, hãy nói rõ phần đó thay vì tự điền thêm.
```

Chỉ dẫn đó phải nằm trong `CLAUDE.md`, chứ không phải gõ lại mỗi lần hỏi. Một quy tắc mà bạn phải tự nhớ thì sớm muộn cũng sẽ bị bỏ quên đúng vào ngày quan trọng nhất.

## Bắt đầu từ trang chỉ mục

Agent nên đọc `index.md` trước tiên, sau đó mở các trang có vẻ liên quan, rồi lần theo các liên kết từ những trang đó mở rộng ra ngoài.

Cách làm ngược lại — quét toàn văn (full-text sweep) — vừa chậm hơn, vừa tốn Context window vào những kết quả gần giống nhưng không trúng đích, lại vừa bỏ sót các trang dùng cách diễn đạt khác với câu hỏi của bạn. Trang chỉ mục tồn tại là để giúp bước này trở nên gọn nhẹ; xem thêm [index.md và log.md](../04-structuring/index-and-log.md).

## Gắn nhãn rõ ràng cho kiến thức bên ngoài

Đôi khi mô hình biết một thông tin hữu ích mà Vault chưa có. Điều đó hoàn toàn ổn miễn là nó được đánh dấu rõ ràng:

```
Trích dẫn các trang trong Vault cho bất kỳ nội dung nào lấy từ ghi chú của tôi. Bất kỳ điều gì bạn biết mà Vault của tôi không có, hãy đặt dưới một tiêu đề riêng được đánh dấu là ngoài phạm vi Vault.
```

Khi được tách bạch, đó là ngữ cảnh bổ trợ hữu ích. Khi bị trộn lẫn, nó làm cả câu trả lời mất đi độ tin cậy, vì bạn không còn biết phần nào có thể truy nguyên nguồn gốc.

## "Không có thông tin" là một câu trả lời hợp lệ

Nếu Vault không có gì về một chủ đề, phản hồi đúng đắn nhất là một câu duy nhất nói rõ điều đó.

Việc Agent cố lấp đầy một kết quả trống rỗng bằng kiến thức chung chính là kiểu lỗi cần cảnh giác nhất, bởi nghe qua nó rất giống một câu trả lời hay. Hãy để ý khi một câu trả lời không hề chứa bất kỳ trích dẫn trang nào; đó chính là dấu hiệu cảnh báo.

## Kết thúc câu trả lời bằng những gì còn thiếu

```
Đã đọc: [[page]], [[page]], [[page]]
Chưa được đề cập: liệu điều này có đúng cho trường hợp truyền phát trực tiếp (streaming) hay không
```

Chỉ hai dòng, nhưng tác dụng lớn hơn vẻ bề ngoài rất nhiều. Chúng cho bạn biết câu trả lời dựa trên bao nhiêu phần của Vault, và dòng chỉ ra khoảng trống thường là nửa giá trị hơn, vì nó nêu chính xác thứ bạn cần tìm đọc tiếp theo.

## Tiếp theo

[Các mẫu truy vấn](query-patterns.md)
