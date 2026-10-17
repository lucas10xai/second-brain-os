---
name: second-brain-metrics
description: >-
  Ghi lại bản chụp (snapshot) có gắn ngày tháng về các chỉ số sức khỏe của vault
  và so sánh với các bản chụp trước đó để thấy rõ xu hướng biến động. Sử dụng kỹ
  năng này cho các đợt kiểm tra hàng tháng hoặc hàng quý, khi người dùng hỏi liệu
  vault có đang tốt lên không, hoặc yêu cầu theo dõi các chỉ số theo thời gian.
  KHÔNG dùng để phân tích đồ thị một lần đơn lẻ — việc đó thuộc về second-brain-graph —
  hoặc để sửa chữa cấu trúc.
---

# Ghi nhận các chỉ số sức khỏe (Record metrics)

Một lần đo đơn lẻ hầu như chẳng cho bạn biết điều gì cả. Chiều hướng dịch chuyển qua nhiều tháng mới là thông tin có giá trị, và không ai có thể nhớ nổi tỷ lệ trang mồ côi của quý trước là bao nhiêu nếu không ghi lại.

## Quy tắc cốt lõi

Bốn con số, được ghi nối tiếp vào một bản nhật ký có gắn ngày tháng, và đối chiếu với lần ghi liền trước. Không bao giờ lấy tổng số trang hay tổng số từ làm thước đo sức khỏe.

## Quy trình thực hiện

1. **Chạy** `scripts/vault_stats.py` và `scripts/link_check.py`.
2. **Ghi nhận:** tỷ lệ trang mồ côi (`orphan rate`), bậc liên kết trung bình (`average degree`), số thành phần liên thông (`component count`), tỷ lệ khái niệm cũ bị bỏ quên (`stale-concept rate`), kèm theo ngày tháng và tổng số trang để làm ngữ cảnh tham chiếu.
3. **Ghi nối tiếp (append)** vào trang theo dõi chỉ số (metrics note). Không bao giờ ghi đè lên các lần ghi trước.
4. **So sánh** với bản chụp liền trước và chỉ rõ chỉ số nào đã dịch chuyển.
5. **Chỉ diễn giải những gì đã thay đổi.** Một con số giữ nguyên sự ổn định thì không cần bình luận thêm.

## Định dạng đầu ra

```
<ngày> | pages <n>
orphan rate    <n>%   (<+/-n> từ <ngày trước>)
avg degree     <n>    (<+/-n>)
components     <n>    (main <n>%)
stale concepts <n>%   (<+/-n>)

Moved: <chỉ số nào đã thay đổi và nguyên nhân khả dĩ>
Watch: <một chỉ số duy nhất cần chú ý khắc phục, hoặc none>
```

## Hiệu chuẩn (Calibration)

Tỷ lệ trang mồ côi tăng lên cùng lúc với tổng số trang tăng lên đồng nghĩa với việc quá trình nạp tài liệu (ingestion) đã ngừng tạo liên kết. Đó là khuôn mẫu quan trọng nhất trong báo cáo này và phải được chỉ đích danh bằng lời, chứ không chỉ để mặc trong các con số.

Không khuyến nghị quá một việc cần sửa trong mỗi lần báo cáo. Một báo cáo chỉ số đi kèm tới năm đầu việc cần làm sẽ bị bỏ qua hoàn toàn.
