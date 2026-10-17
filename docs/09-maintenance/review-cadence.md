# Nhịp độ rà soát định kỳ

Lint giữ cho cấu trúc luôn vững vàng. Còn rà soát định kỳ (Review) là thứ giữ cho chính bạn luôn nắm bắt được mạch thông tin, và đây cũng là tác vụ bảo trì duy nhất tạo ra thứ để bạn đọc thay vì chỉ âm thầm chạy ngầm.

## Hàng tuần: mười phút

Agent chuẩn bị nội dung; bạn là người đọc.

```
/review
```

Những gì được trả về gồm: nội dung nào mới được thêm vào, những khái niệm nào nhận được nhiều liên kết mới nhất, các mâu thuẫn đã được ghi nhận nhưng vẫn chưa giải quyết, các câu hỏi còn bỏ ngỏ, và ba gợi ý cụ thể về những thứ nên đọc hoặc viết tiếp theo.

Các cụm liên kết mới tập trung (clusters) là phần đáng chú ý nhất. Nơi mà các liên kết của bạn đổ về trong tuần qua chính là nơi sự chú ý thực sự của bạn hướng tới — và nó thường khác xa so với những gì bạn vẫn tưởng mình đang tập trung vào.

## Hàng tháng: nhìn vào cấu trúc

Mỗi tháng một lần, hãy nhìn vào tổng thể Vault thay vì chỉ nhìn vào một tuần vừa qua:

- Bốn [chỉ số đo lường](../05-graphs/metrics.md), được nối thêm vào một trang ghi chú để bạn theo dõi xu hướng biến đổi
- Các trang khái niệm không được chạm tới trong suốt chín mươi ngày dù chủ đề của chúng vẫn liên tục nhận thêm tài liệu nguồn mới
- Danh sách Gaps trong `index.md` — đây chính là danh sách tài liệu cần đọc mà bạn đã tự tạo ra một cách tự nhiên mà không cần cố gắng
- Một đồ thị cục bộ (local graph) của một trang bạn mới viết gần đây, dùng làm bước kiểm tra xác suất về chất lượng gắn liên kết

## Hàng quý: thành thật với chính mình

Có hai câu hỏi cần trả lời.

**Tôi đã thay đổi suy nghĩ về điều gì?** Câu hỏi này chỉ có thể trả lời được nhờ [quy tắc thay thế thông tin cũ](../04-structuring/contradictions-and-supersession.md), và chỉ riêng giá trị của nó thôi đã đủ bù đắp công sức xây dựng toàn bộ hệ thống này.

**Tôi đang giữ lại thứ gì mà mình sẽ chẳng bao giờ dùng đến?** Hãy đưa chúng vào kho lưu trữ (archive). Một Vault ôm đồm đầy những tư liệu chết sẽ làm cho mọi câu truy vấn tệ đi một chút, mãi mãi.

## Những gì cần cắt tỉa

Các tài liệu nguồn thuộc những chủ đề bạn không còn quan tâm nữa: hãy đưa vào lưu trữ thay vì xóa hẳn; chúng chẳng tốn bao nhiêu chỗ trong `raw/` còn các trang trong `wiki/` thì có thể dọn đi.

Các trang khái niệm không bao giờ có thêm được tài liệu nguồn thứ hai: điều này thường có nghĩa là ý tưởng đó thực chất không quan trọng với bạn đến thế.

Đừng xóa bất kỳ trang nào đang được nhiều nơi khác liên kết tới. Một trang mà năm trang khác phụ thuộc vào là một trang trụ cột, bất kể nội dung bản thân nó trông như thế nào.

## Giữ cho bản rà soát luôn ngắn gọn

Một bản rà soát liệt kê tất cả mọi thứ sẽ chỉ được đọc lướt qua rồi bị bỏ xó. Chỉ nêu ba khuyến nghị, đừng nêu mười. Nếu một tuần trôi qua mà không có gì đáng báo cáo, một dòng duy nhất thông báo điều đó chính là kết quả đầu ra chuẩn xác nhất.

## Tiếp theo

[Quản lý phiên bản với Git](versioning-with-git.md)
