---
name: second-brain-changed-my-mind
description: >-
  Truy vết những điểm mà quan điểm đã ghi nhận của người dùng về một vấn đề đã
  thay đổi: các nhận định bị thay thế (superseded claims), sự mâu thuẫn giữa các
  nguồn ở những thời điểm khác nhau, và bằng chứng nào đã thúc đẩy sự thay đổi đó.
  Sử dụng kỹ năng này khi người dùng hỏi họ đã thay đổi suy nghĩ về điều gì, tư duy
  của họ về một chủ đề đã phát triển ra sao, trước đây họ từng tin vào điều gì, hoặc
  khi họ muốn nhìn lại quan điểm của bản thân theo từng quý. KHÔNG dùng để tìm mâu
  thuẫn giữa các nguồn không có chiều thời gian, hoặc để trả lời trạng thái hiện tại đơn thuần.
---

# Truy vết sự thay đổi quan điểm

Đây là câu hỏi mà một vault có thể trả lời được còn mọi công cụ khác thì không, và cũng chính là lý do tồn tại của các quy tắc kế thừa/thay thế nhận định (supersession rules). Kỹ năng này chỉ hoạt động được nhờ việc các mâu thuẫn luôn được ghi nhận lại thay vì bị ghi đè.

## Quy tắc cốt lõi

Báo cáo sự thay đổi kèm theo cả hai quan điểm, cả hai mốc thời gian và bằng chứng nằm giữa chúng. Một kết luận bị tước bỏ lịch sử hình thành thì chỉ còn là một nhận định nhất thời ở hiện tại.

## Quy trình thực hiện

1. **Tìm các nhận định đã bị thay thế (superseded claims)** trên khắp các trang khái niệm (`concept`), cùng những điểm mâu thuẫn mà các tài liệu nguồn có ngày tháng khác nhau.
2. **Tái dựng lại trình tự thời gian:** trang đó ban đầu nói gì, vào lúc nào, dựa trên nguồn nào; điều gì đã làm thay đổi nó, và vào thời điểm nào.
3. **Phân biệt giữa việc điều chỉnh nhận thức thực sự với việc đính chính lỗi.** Một lỗi sai số liệu được sửa lại không phải là sự thay đổi quan điểm. Một kết luận được xét lại nhờ có bằng chứng tốt hơn mới là thay đổi quan điểm.
4. **Gắn cờ những mâu thuẫn chưa được giải quyết.** Những bất đồng vẫn đang bỏ ngỏ chính là kết quả đầu ra có giá trị hành động cao nhất ở đây.
5. **Đánh giá độ vững chắc của quan điểm hiện tại,** dựa trên những bằng chứng đã làm dịch chuyển nó.

## Định dạng đầu ra

```
## <chủ đề>
Trước đây: <nhận định cũ> (<nguồn>, <ngày>)
Hiện tại: <nhận định mới> (<nguồn>, <ngày>)
Yếu tố làm thay đổi: <bằng chứng>
Độ vững chắc: <điều gì sẽ làm quan điểm này thay đổi một lần nữa>

## Vẫn chưa ngã ngũ
<các mâu thuẫn hiện chưa có quan điểm chốt>
```

## Hiệu chuẩn (Calibration)

Nếu không có gì thay đổi trong khoảng thời gian được hỏi, hãy trả lời ngắn gọn trong một dòng. Việc cố tình nhào nặn ra một sự "thay đổi quan điểm" giả tạo từ hai trang vốn chưa bao giờ bất đồng với nhau còn tệ hơn một kết quả trống.

Không bao giờ mặc định coi tài liệu nguồn mới hơn là đúng chỉ vì nó mới hơn.
