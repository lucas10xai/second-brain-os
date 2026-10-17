---
name: second-brain-quiz
description: >-
  Tạo câu hỏi ôn tập từ chính các trang khái niệm của người dùng để họ phát hiện ra
  những gì mình đã lưu lại nhưng chưa thực sự học, đồng thời đối chiếu câu trả lời
  của họ với nội dung ghi trên trang. Sử dụng kỹ năng này khi người dùng muốn tự
  kiểm tra kiến thức, ôn tập, tạo thẻ ghi nhớ (flashcards) từ ghi chú, hoặc hỏi xem
  họ đã quên những gì. KHÔNG dùng để đố vui kiến thức chung về một chủ đề mà vault
  không đề cập, hoặc để trả lời câu hỏi tra cứu từ vault.
---

# Tự kiểm tra kiến thức từ trang của bạn (Quiz from your own pages)

Đọc một điều gì đó không đồng nghĩa với việc đã học được nó. Một chiếc vault chứa đầy những trang viết rất hay nhưng không bao giờ được đọc lại thì chỉ là một cái thư viện, và việc sở hữu thư viện không tự khắc biến ai thành người hiểu biết cả.

## Quy tắc cốt lõi

Câu hỏi phải xuất phát từ chính các trang của người dùng, ở đúng độ sâu mà những trang đó ghi nhận. Không bao giờ lấy từ kiến thức phổ thông bên ngoài về chủ đề đó.

## Quy trình thực hiện

1. **Chọn phạm vi ôn tập:** một chủ đề, một cụm liên kết, hoặc các trang vừa được cập nhật gần đây.
2. **Đặt hai loại câu hỏi:** câu hỏi gợi nhớ (recall) về những gì trang đó trình bày, và câu hỏi vận dụng (application) áp dụng ý tưởng đó vào một tình huống mới.
3. **Giấu đáp án** cho đến khi người dùng tự mình trả lời xong.
4. **Chấm điểm dựa trên nội dung trang wiki, chứ không dựa trên sự thật chung bên ngoài.** Nếu người dùng trả lời đúng về mặt thực tế nhưng trang wiki lại ghi khác, đó là một lỗi của trang wiki rất đáng được chỉ ra để cập nhật.
5. **Báo cáo các lỗ hổng kiến thức:** những trang nào người dùng không thể trả lời được. Đó chính là những thứ đã được lưu lại nhưng chưa bao giờ thực sự đi vào đầu.

## Định dạng đầu ra

```
<n> câu hỏi từ <n> trang

1. <câu hỏi>
...

[sau khi người dùng trả lời]
Solid: <các chủ đề đã nắm vững>
Shaky: <các chủ đề còn mơ hồ, kèm theo tên trang cần đọc lại>
Page problems found: <các trang viết chưa rõ ràng hoặc bị sai>
```

## Hiệu chuẩn (Calibration)

Chỉ giới hạn ở một vài trang thực sự quan trọng trong mỗi lượt. Việc kiểm tra toàn bộ mọi thứ từng lưu trong đời là một gánh nặng khổ sai chứ không phải một thói quen học tập.

Một trang không thể dùng để đặt ra nổi một câu hỏi vận dụng hay thường là trang chỉ chép lại lời lẽ của tài liệu nguồn chứ chưa thực sự tiêu hóa thành sự hiểu biết. Hãy chỉ rõ điều đó cho người dùng.
