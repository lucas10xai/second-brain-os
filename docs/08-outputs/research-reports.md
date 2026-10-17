# Báo cáo nghiên cứu

Báo cáo nghiên cứu là sản phẩm bạn tạo ra khi một câu hỏi đòi hỏi nhiều thông tin hơn những gì Vault hiện có. Khi đó, Vault đóng vai trò là điểm xuất phát chứ không phải toàn bộ câu trả lời.

## Xác định phạm vi dựa trên những gì đã có trước

```
Tôi cần tìm hiểu cách các công ty đang triển khai Agent Harness trong môi trường thực tế (production). Vault của tôi đã bao phủ những phần nào, phần nào còn mỏng, và phần nào còn thiếu hoàn toàn?
```

Câu trả lời đó chính là kế hoạch nghiên cứu của bạn. Phần lớn công sức trong một báo cáo tốt nằm ở việc biết rõ những gì bạn không cần phải tra cứu lại, và bắt đầu từ Vault đồng nghĩa với việc bạn không phải đọc lại những tài liệu mình đã đọc từ năm ngoái.

## Lấp đầy các khoảng trống một cách có chủ đích

Hãy đi tìm các nguồn tài liệu cho những khoảng trống đó, Ingest chúng đàng hoàng qua thư mục `raw/`, và để chúng xây dựng nên các trang ghi chú theo đúng quy trình như mọi tài liệu khác.

Việc cưỡng lại lối tắt ở bước này là rất quan trọng. Dán thẳng một bài viết mới tinh vào bản nháp báo cáo sẽ giúp bạn viết xong báo cáo đó, nhưng chẳng giúp Vault tốt lên chút nào — nghĩa là ở báo cáo tiếp theo về một chủ đề lân cận, bạn lại phải bắt đầu từ con số không.

## Cấu trúc báo cáo

```
Câu hỏi nghiên cứu
Những gì tôi tìm thấy                (kèm trích dẫn trang)
Những điểm các nguồn bất đồng
Những điều tôi chưa thể xác lập
Điều gì sẽ làm thay đổi kết luận này
```

Hai mục cuối cùng chính là thứ khiến một bản báo cáo đáng được đọc lại. Một báo cáo chỉ trình bày các phát hiện trông có vẻ thuyết phục hơn nhưng thực chất lại ít hữu ích hơn, vì người đọc không thể biết được đâu là phần trụ cột vững chắc và đâu là phần lập luận còn mỏng.

## Lưu báo cáo lại như một tài liệu nguồn

Các báo cáo được đặt trong thư mục `output/`, sau đó được Ingest ngược trở lại vào Vault như những tài liệu nguồn.

Một bản báo cáo là bức ảnh chụp nhanh (snapshot) ghi lại mức độ hiểu biết của bạn tại một thời điểm cụ thể; việc lưu nó trong Vault như một tài liệu nguồn giúp các tài liệu về sau có thể phản bác nó một cách tường minh thay vì âm thầm ghi đè lên nó. Xem thêm [quy tắc thay thế thông tin cũ](../04-structuring/contradictions-and-supersession.md).

## Tiếp theo

[Xuất bản và trích xuất](publishing-and-export.md)
