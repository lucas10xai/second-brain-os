# Lập lịch tự động (Scheduling)

Các lượt chạy theo lịch định kỳ chính là thứ làm cho `Vault` có cảm giác như một thực thể sống. Bạn thức dậy và thấy nó đã phân loại xong những gì bạn lưu qua `Web Clipper` hôm qua, phát hiện ra một điểm mâu thuẫn, và để lại cho bạn đúng ba dòng tóm tắt những gì đã thay đổi.

Nhưng đó cũng là những thao tác ghi tự động không có người giám sát trực tiếp vào kho ghi chú của bạn, vì vậy trình tự triển khai rất quan trọng: hãy thiết lập [Guardrails (Rào chắn an toàn)](safety-and-guardrails.md) thật chuẩn chỉnh trước, rồi mới lên lịch chạy tự động.

## Nhịp độ chạy cho từng tác vụ

**`Ingest`, hàng ngày.** Chạy qua đêm, xử lý bất cứ thứ gì đã tích lũy trong thư mục `raw/` suốt cả ngày hôm đó. Nhịp độ hàng ngày là vừa đẹp vì gom theo lô (batch) giúp `Agent` có cơ hội nhận ra rằng ba bài viết bạn lưu thực chất đang cùng bàn về một ý tưởng. Chạy hàng giờ sẽ không làm được điều đó.

**`Link`, hàng tuần.** Việc tạo kết nối cần có đủ nguyên liệu mới để kết nối. Hãy chạy nó sau một tuần `Ingest` dữ liệu.

**`Lint`, hàng tuần.** Chạy ngay sau `linker`, để nó bắt được bất kỳ lỗi nào mà lượt kết nối vừa rồi vô tình gây ra.

**`Review`, hàng tuần.** Đây là kết quả đầu ra duy nhất mà bạn thực sự dành thời gian đọc kỹ. Hãy đặt lịch chạy vào buổi sáng mà bạn thường lên kế hoạch tuần mới.

**`Metrics`, hàng tháng.** Bốn con số được ghi nối tiếp vào một trang ghi chú. Xem thêm [Các chỉ số đồ thị đáng theo dõi](../05-graphs/metrics.md).

## Cách thiết lập một lịch chạy

Trong ứng dụng Claude Desktop, mở tab Schedule, sau đó tạo một tác vụ mới:

```
Frequency:  Daily, 7:00am
Folder:     your vault
Prompt:     File anything new in raw/ into the wiki following CLAUDE.md.
            Link it to existing pages. Update index.md and log.md. Commit
            with a message naming the run. Then write me three lines on
            what changed.
```

Hoặc yêu cầu trực tiếp ngay trong một phiên làm việc: *"thiết lập một tác vụ hàng ngày lúc 7 giờ sáng để ingest thư mục raw/ và tóm tắt những gì đã thay đổi"*.

Từ cửa sổ dòng lệnh (terminal), dùng `cron` hoặc Task Scheduler gọi `Claude Code` ở chế độ không giao diện (headless) cũng hoạt động theo cách tương tự, và đây là lựa chọn tốt hơn nếu bạn muốn lượt chạy đó tự động được đóng gói bên trong một bản commit `Git`.

## Ba thứ mọi lượt chạy bắt buộc phải tạo ra

Ba thứ, không thiếu lần nào.

**Một dòng nhật ký trong `log.md`.** Nếu không có nó, bạn không thể kiểm toán (audit) được chuyện gì đã diễn ra trong lúc mình đang ngủ.

**Một bản commit `Git`.** Mỗi lượt chạy một commit, với tên lượt chạy được ghi rõ trong thông điệp commit. Đây là thứ giúp một lượt chạy lỗi có thể được hoàn tác (revert) chỉ bằng một câu lệnh thay vì mất cả buổi tối để dọn dẹp.

**Một báo cáo ngắn gửi cho bạn.** Dù chỉ là một dòng. Một tác vụ chạy ngầm theo lịch mà không tạo ra bất kỳ tín hiệu hiển thị nào là thứ bạn sẽ dần mất niềm tin và rồi ngừng ngó ngàng tới.

## Phát hiện lỗi âm thầm (Silent failure)

Kiểu lỗi nguy hiểm nhất không phải là ứng dụng bị sập (crash). Mà là một lượt chạy báo hoàn tất thành công nhưng thực chất chẳng làm được việc gì hữu ích: tài liệu nguồn bị rỗng, lệnh gọi API bị đứt gánh giữa đường, hoặc bộ chỉ dẫn không khớp với bất kỳ file nào.

Có hai bước kiểm tra rất rẻ. Thứ nhất, yêu cầu lượt chạy báo cáo các con số đếm cụ thể thay vì chỉ báo hoàn thành, để những dòng như *"đã ingest 0 tài liệu nguồn"* lập tức đập vào mắt bạn. Thứ hai, hãy nhìn vào tần suất commit mỗi tháng một lần: một tuần trôi qua mà không có commit nào từ tác vụ hàng ngày có nghĩa là nó đã âm thầm chết từ hôm thứ Ba rồi.

## Hãy bắt đầu bằng cách chạy thủ công

Hãy tự tay kích hoạt từng tác vụ trong suốt một tuần trước khi đưa nó vào lịch chạy tự động. Mục đích là để bạn kiểm tra xem chất lượng đầu ra đã đủ tốt để chấp nhận mà không cần đọc săm soi từng chữ hay chưa — bởi vì chấp nhận không cần đọc kỹ chính xác là bản chất của việc lập lịch tự động.

Hãy lên lịch tự động cho tác vụ `Ingest` sau cùng. Vì đó là tác vụ thực hiện việc ghi nhiều nhất.

## Tiếp theo

[Subagents và xử lý song song](subagents.md)
