---
name: second-brain-transcript
description: >-
  Làm sạch một bản gỡ băng thô (raw transcript) trước khi nạp vào vault: đặt dấu
  câu, chia đoạn văn, gắn nhãn người nói, sửa các thuật ngữ chuyên ngành bị nhận
  diện sai, và tách các bản ghi âm dài theo từng chủ đề. Sử dụng kỹ năng này khi
  người dùng thả một bản phụ đề tự động, file subtitle, bản gỡ băng podcast hoặc
  bài giảng, văn bản ghi âm cuộc họp, hoặc yêu cầu xử lý nguồn video hay âm thanh.
  KHÔNG dùng cho văn bản vốn đã là văn xuôi hoàn chỉnh, để tóm tắt bản gỡ băng,
  hoặc để thực hiện luôn bước nạp (ingest) vào wiki.
---

# Làm sạch bản gỡ băng (Clean a transcript)

Các trang khái niệm được xây dựng trực tiếp từ những đống phụ đề tự động không chấm câu luôn có chất lượng tệ hơn hẳn, bởi vì mô hình phải tiêu tốn sự chú ý vào việc đoán ranh giới câu thay vì tập trung hiểu các luận điểm.

## Quy tắc cốt lõi

Chỉ làm sạch, không bao giờ tóm tắt. Không cắt bỏ bất kỳ nội dung nào. Đây là một lượt chuẩn hóa định dạng trên bản lưu gốc, và bản lưu đó phải giữ nguyên tính trung thực.

## Quy trình thực hiện

1. **Đặt dấu câu và chia đoạn văn.** Xác định ranh giới câu trước, sau đó ngắt đoạn tại những điểm chuyển chủ đề.
2. **Gắn nhãn người nói** ở những chỗ đổi lượt lời. Trong một cuộc phỏng vấn, bước này mang lại phần lớn giá trị của bản gỡ băng.
3. **Sửa các thuật ngữ chuyên ngành.** Phụ đề tự động thường xuyên làm biến dạng tên riêng và thuật ngữ kỹ thuật. Hãy gắn cờ bất kỳ từ nào bạn không thể xác định chắc chắn thay vì đoán mò.
4. **Giữ lại các mốc thời gian thô (coarse timestamps)** cách nhau mỗi vài phút, để một luận điểm trên trang wiki có thể được kiểm chứng lại trong mười giây thay vì phải nghe lại từ đầu.
5. **Đề xuất các điểm cắt nhỏ** nếu bản ghi âm đi qua nhiều chủ đề tách biệt. Một tập podcast dài ba tiếng đồng hồ không phải là một tài liệu nguồn đơn nhất.
6. **Viết phần frontmatter:** tiêu đề (`title`), kênh hoặc người nói (`author`), `url`, ngày xuất bản (`published`).

## Định dạng đầu ra

Toàn bộ văn bản gỡ băng đã được làm sạch, tiếp theo là:

```
Cleaned: <tên nguồn>
Speakers labelled: <n>
Terms corrected: <danh sách thuật ngữ đã sửa>
Uncertain: <danh sách những chỗ chưa thể xác định chắc chắn>
Suggested splits: <các chủ đề kèm mốc thời gian, hoặc none>
```

## Hiệu chuẩn (Calibration)

Không bao giờ lược bỏ những từ đệm nhưng mang hàm ý quan trọng, chẳng hạn như lời nói rào đón (hedging) hoặc khi người nói tự đính chính lại câu vừa phát biểu. Chính những chi tiết đó giúp phân biệt một khẳng định chắc chắn với một lời bình luận buột miệng.

Nếu bản gỡ băng bị lỗi quá nặng không thể làm sạch một cách đáng tin cậy, hãy nói rõ điều đó và khuyến nghị trích xuất lại bản mới thay vì tự dựng nên một văn bản nghe có vẻ hợp lý.
