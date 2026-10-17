# Các chỉ số đồ thị đáng theo dõi

Bốn con số, kiểm tra định kỳ hàng tháng. Xu hướng biến thiên của chúng theo thời gian sẽ cho bạn biết liệu hệ thống có đang vận hành tốt hay không — điều vốn không dễ nhận ra nếu chỉ nhìn vào việc sử dụng hàng ngày.

```bash
python3 scripts/vault_stats.py ~/brain
```

## Tỷ lệ trang mồ côi (Orphan rate)

Số trang không có bất kỳ liên kết trỏ tới nào (inbound links), tính theo tỷ lệ phần trăm trên tổng số trang.

Đây là con số có giá trị chẩn đoán cao nhất trong toàn bộ `Vault`. Tỷ lệ trang mồ côi tăng lên đồng nghĩa với việc quá trình `Ingest` đang viết ra các trang mới mà không kết nối chúng vào mạng lưới — đây chính xác là kiểu lỗi biến một `wiki/` quay trở lại thành một thư mục chứa file đơn thuần.

Dưới 5% là mức lành mạnh. Vượt quá 15% nghĩa là có thứ gì đó đã bị hỏng trong bộ chỉ dẫn `Ingest`, chứ không phải do thói quen của bạn.

## Bậc trung bình (Average degree)

Số lượng liên kết trung bình trên mỗi trang.

Dưới 2, đồ thị hầu như chưa được kết nối và việc truy xuất theo đồ thị không thể mang lại kết quả tốt hơn tìm kiếm từ khóa thông thường. Từ 3 đến 8 là khoảng hoạt động hiệu quả cho một `Vault` cá nhân. Nếu vượt xa mức 10, hãy kiểm tra xem liệu các liên kết có đang bị thêm vào một cách máy móc để trang trí hay không — việc đó chỉ làm phình con số thống kê trong khi lại khiến đồ thị kém hữu ích đi.

Hãy theo dõi chỉ số này song song với tổng số trang. Bậc trung bình giữ nguyên không đổi trong khi kích thước `Vault` tăng gấp đôi là tín hiệu tốt; còn nếu bậc trung bình sụt giảm tức là các trang mới đang được kết nối ít hơn so với các trang cũ trước đây.

## Số thành phần liên thông (Component count)

Số lượng các ốc đảo bị ngắt kết nối hoàn toàn với nhau.

Lý tưởng nhất là một thành phần liên thông lớn chứa hầu hết các trang, cộng thêm một vài chủ đề thực sự tách biệt hẳn. Nếu thành phần chính chứa ít hơn khoảng 80% tổng số trang, `Vault` của bạn đang bị phân mảnh và các câu trả lời nhận được sẽ luôn thiếu sót một cách có hệ thống dù bề ngoài trông chẳng có vẻ gì là đang bị lỗi.

## Tỷ lệ trang cũ kỹ (Stale page rate)

Các trang khái niệm có ngày `updated` đã cũ hơn chín mươi ngày, tính theo tỷ lệ trên tổng số trang khái niệm.

Một mức độ cũ nhất định là hoàn toàn hợp lý: một trang đã được viết tốt về một ý tưởng đã ngã ngũ thì không cần phải động vào nữa. Nhưng một `Vault` mà phần lớn các trang khái niệm không hề được chạm tới trong suốt nhiều tháng trời trong khi tài liệu nguồn mới vẫn liên tục đổ về có nghĩa là thông tin mới đang bị đẩy vào các trang mới toanh thay vì cập nhật bổ sung vào các trang hiện có. Đó chính là con đường khiến bạn kết thúc với bốn trang khác nhau cùng viết về một thứ.

```dataview
TABLE updated FROM "wiki/concepts"
WHERE updated < date(today) - dur(90 days)
SORT updated ASC
```

## Những chỉ số không cần theo dõi

Tổng số trang và tổng số từ. Cả hai con số này đều luôn tăng lên bất kể `Vault` của bạn đang tốt lên hay tệ đi — điều khiến chúng mang lại cảm giác thỏa mãn giả tạo nhưng hoàn toàn vô dụng. Một `Vault` tăng gấp đôi số trang trong khi cũng tăng gấp đôi tỷ lệ trang mồ côi thực chất là đang ngày càng tệ đi.

## Ghi chép lại các chỉ số

Hãy ghi nối tiếp (append) bốn con số này vào một trang ghi chú mỗi tháng một lần. Xu hướng biến đổi mới là thông tin có giá trị; một lần đo đơn lẻ hầu như chẳng nói lên điều gì, và bạn sẽ không thể nào nhớ nổi tỷ lệ trang mồ côi của quý trước là bao nhiêu đâu.

## Tiếp theo

[Agents](../06-agents/README.md), để vận hành toàn bộ hệ thống này mà không cần đến tay bạn.
