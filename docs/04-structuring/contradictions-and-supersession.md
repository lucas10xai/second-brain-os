# Mâu thuẫn và thay thế thông tin

Đây là quy tắc phân biệt một `Second Brain` với một công cụ tìm kiếm, và cũng là quy tắc mà hầu hết các bản triển khai đều làm sai.

Khi một tài liệu nguồn mới bất đồng với những gì một trang hiện có đang nói, trang đó phải ghi nhận cả hai. Nó không được phép ghi đè.

## Tại sao ghi đè là kiểu lỗi tệ hại nhất

Một `Vault` âm thầm cập nhật theo nhận định mới nhất sẽ không có ký ức về những gì bạn từng tin tưởng và lý do tại sao. Nó luôn trình bày thứ gần nhất bạn đọc được như là chân lý — tức là xếp hạng theo độ mới (recency) chứ không phải theo bằng chứng.

Tệ hơn nữa, sự thay đổi này hoàn toàn vô hình. Không có lỗi nào được báo ra. Trang đó chỉ đơn giản là nói một điều khác hẳn so với tháng trước, với cùng một giọng điệu tự tin như vậy, và bạn không có cách nào để nhận ra hay kiểm tra xem điều gì đã thay đổi.

Lịch sử nhận thức chính là tài sản quý giá nhất. Việc biết rằng bạn từng tin vào X vì một tài liệu nguồn năm 2024, sau đó điều chỉnh sang Y sau khi có bằng chứng tốt hơn, có giá trị hơn nhiều so với bản thân từng nhận định đơn lẻ, bởi nó cho bạn biết mức độ vững chắc thực sự của Y.

## Một sự mâu thuẫn trông như thế nào trên trang

Cả hai quan điểm đều được trình bày, mỗi quan điểm đều có trích dẫn nguồn và ngày tháng rõ ràng:

```markdown
## Quan điểm hiện tại

Chất lượng truy xuất suy giảm khi vượt quá khoảng 50k token ngữ cảnh
([[Lost in the Middle]], 2023).

## Đang tranh cãi

[[Some 2026 benchmark]] báo cáo không có sự suy giảm nào lên tới 200k token trên cùng
nhóm tác vụ. Cả hai sử dụng thiết lập đánh giá khác nhau: nghiên cứu đầu đo lường độ nhạy
vị trí (position sensitivity), nghiên cứu thứ hai đo độ chính xác tác vụ cuối (end-task accuracy). Chưa ngã ngũ.
```

Người đọc có thể hành động dựa trên thông tin đó. Còn một trang âm thầm chấp nhận bất cứ thứ gì được `Ingest` sau cùng thì hoàn toàn không thể dùng làm cơ sở hành động được.

## Thay thế thông tin cũ (Supersession)

Đôi khi đó không phải là một sự bất đồng quan điểm thực sự, mà chỉ là thông tin đã lỗi thời. Một công cụ thay đổi API, một công ty bị mua lại, một bài báo khoa học bị rút lại (retracted).

Hãy đánh dấu nhận định cũ là đã bị thay thế (superseded) và vẫn giữ nó lại:

```markdown
~~Yêu cầu Node 18 trở lên~~ đã được thay thế 2026-05: bộ cài đặt gốc (native installer) không
còn yêu cầu Node nữa ([[source]]).
```

Việc xóa bỏ hoàn toàn có nghĩa là khi bạn đọc một tài liệu nào đó được viết trước thời điểm thay đổi, bạn sẽ không có cách nào đối chiếu nó với những gì `Vault` hiện tại đang nói.

## Độ tin cậy (Confidence)

Không phải mọi thứ được `Ingest` đều xứng đáng có trọng số ngang nhau. Chỉ cần một thẻ (tag) hoặc một trường trong `Frontmatter` là đủ:

- **stated** (được khẳng định): bởi một nguồn sơ cấp (primary source) mà bạn tin tưởng
- **reported** (được tường thuật): bởi các nguồn tin thứ cấp
- **self-reported** (tự công bố): bởi chính bên hưởng lợi từ thông tin đó
- **unverified** (chưa kiểm chứng)

Đặc biệt, những con số tự công bố (`self-reported`) không bao giờ được phép đánh mất nhãn này. Việc một tuyên bố về hiệu năng của chính một công ty được lặp lại như một sự thật hiển nhiên trong trang khái niệm chính là cách biến một `Vault` trở nên sai lầm một cách đầy tự tin.

## Chỉ dẫn cho Agent

Trong `CLAUDE.md`, hãy diễn đạt sao cho quy tắc có tính khái quát hóa thay vì chỉ bao phủ những trường hợp hiển nhiên:

```
Khi một tài liệu nguồn mới mâu thuẫn với một trang hiện có, không được ghi đè. Hãy ghi nhận cả hai
quan điểm kèm theo nguồn và ngày tháng, đồng thời nêu rõ điều gì sẽ giúp phân định mâu thuẫn đó. Nếu nguồn
mới rõ ràng là bằng chứng tốt hơn, hãy đánh dấu nhận định cũ là đã bị thay thế (superseded) thay vì
xóa bỏ nó. Không bao giờ giải quyết mâu thuẫn chỉ bằng cách chọn nguồn mới hơn về mặt thời gian.
```

## Tiếp theo

[index.md và log.md](index-and-log.md)
