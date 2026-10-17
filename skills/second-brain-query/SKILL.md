---
name: second-brain-query
description: >-
  Trả lời câu hỏi từ vault bộ não thứ hai bằng cách đọc chính các trang trong vault,
  trích dẫn các trang đã sử dụng, và nói rõ ràng khi vault không chứa câu trả lời.
  Sử dụng kỹ năng này bất cứ khi nào người dùng hỏi họ biết gì về một chủ đề, họ đã
  đọc được gì về một vấn đề, điều gì kết nối hai ý tưởng với nhau, họ đã thay đổi
  suy nghĩ về điều gì, hoặc bất kỳ câu hỏi nào cần được trả lời từ chính ghi chú của
  họ thay vì kiến thức chung bên ngoài. KHÔNG dùng để nạp tư liệu mới, trả lời các
  câu hỏi kiến thức phổ thông không liên quan gì đến vault, hoặc khi người dùng chủ
  động yêu cầu tìm câu trả lời từ nguồn web bên ngoài.
---

# Truy vấn dữ liệu từ Vault (Query the vault)

Một truy vấn âm thầm quay về dùng kiến thức tổng quát của mô hình là điều gây hại lớn nhất mà hệ thống này có thể làm. Chủ sở hữu xây dựng chiếc vault này là để mọi câu trả lời đều bám rễ vào những gì họ thực sự đã đọc; một câu trả lời pha trộn giữa định kiến sẵn có của mô hình với ghi chú cá nhân của họ còn tệ hơn là không có câu trả lời, bởi vì không thể kiểm chứng được đâu là thật.

## Quy tắc cốt lõi

Mọi nhận định trong câu trả lời đều phải xuất phát từ một trang trong vault và chỉ rõ tên trang đó. Bất kỳ điều gì bạn biết nhưng không có trong vault thì phải được gắn nhãn rõ ràng là kiến thức bên ngoài hoặc lược bỏ hoàn toàn.

## Quy trình thực hiện

1. **Bắt đầu từ `index.md`**, chứ không phải quét toàn văn (full-text sweep) toàn bộ kho. Trang chỉ mục chính là tấm bản đồ; đọc nó trước giúp bảo toàn ngân sách ngữ cảnh cho các trang nội dung thực sự.
2. **Lần theo các liên kết tỏa ra ngoài** từ những trang liên quan nhất, từng bước nhảy (hop) một. Dừng lại khi các trang mới không còn đóng góp thêm thông tin gì mới.
3. **Trả lời bằng ngôn ngữ giản dị, rõ ràng**, kèm theo tham chiếu `[[tên trang]]` ngay trong dòng văn bản.
4. **Chỉ rõ những khoảng trống.** Nếu câu hỏi có ba phần mà vault chỉ mới bao phủ được hai phần, hãy nói rõ phần nào chưa có câu trả lời.
5. **Đề xuất bước đi tiếp theo** khi thấy rõ hướng hành động: một tài liệu nguồn đáng nạp thêm, hoặc một trang tổng hợp (`synthesis`) đáng được viết ra.

## Định dạng đầu ra

Văn xuôi trực diện, sau đó kết thúc bằng:

```
Read: <các trang đã tham khảo>
Not covered: <những phần vault chưa giải đáp được>
```

## Hiệu chuẩn (Calibration)

Đọc quá ít là lỗi phổ biến nhất: trả lời chỉ từ ba trang trong khi vault có tới mười lăm trang liên quan. Đọc tất cả mọi thứ là thái cực lỗi ngược lại, làm đốt sạch ngân sách ngữ cảnh vào những trang chẳng mang lại thêm giá trị gì.

Nếu vault hoàn toàn không có thông tin gì về chủ đề được hỏi, hãy nói rõ điều đó trong một câu duy nhất rồi dừng lại. Tuyệt đối không bồi đắp câu trả lời bằng kiến thức phổ thông chỉ để tránh trả về kết quả trống.
