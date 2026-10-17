# Tài liệu đọc (Reading)

## Tài liệu nguồn khởi thủy

**[Karpathy's llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**. Xuất bản ngày 4 tháng 4 năm 2026. Mô hình cốt lõi làm nền tảng cho mọi thứ trong kho lưu trữ này.

Tài liệu này rất ngắn gọn, được viết như một tệp ý tưởng dùng để dán thẳng vào `Agent` của bạn thay vì một bản đặc tả kỹ thuật khô khan. Lập luận cốt lõi: đại đa số mọi người khi dùng LLM với tài liệu đều dừng ở mức `RAG`, nơi mô hình phải khám phá lại tri thức từ con số không ở mỗi câu hỏi và chẳng có gì được tích lũy lại.

Hãy đọc nó trước tiên. Mọi thứ khác, bao gồm cả bộ hướng dẫn này, đều là một cách diễn giải và hiện thực hóa từ ý tưởng gốc đó.

## Mô hình này ở quy mô doanh nghiệp

**[An organizational second brain: AI that learns from experts](https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/)**. Meta Engineering, tháng 9 năm 2026. Cùng mô hình mà bộ hướng dẫn này truyền tải, được vận hành bên trong Meta với đối tượng sử dụng là cả một đội ngũ chuyên môn.

Rất đáng đọc chỉ riêng vì kiến trúc của nó: hơn 200 tệp tri thức có cấu trúc kèm YAML frontmatter tạo thành một đồ thị phụ thuộc — gồm các tệp lập trường (position files), bảng phân loại (taxonomies), chỉ mục định tuyến (routing indexes), tệp cổng vào (gateway files) — được tách biệt hoàn toàn khỏi các "công thức" (recipes), tức những quy trình suy luận chỉ tham chiếu đến tri thức chứ không chứa đựng tri thức bên trong. Nhờ vậy, các bản sửa lỗi luôn mang tính phẫu thuật chính xác: sửa đổi tri thức không chạm vào quy trình, và sửa đổi phương pháp luận không làm xáo trộn các dữ kiện thực tế. Quy tắc phân tách của họ trùng khớp hoàn toàn với chúng ta: tri thức đậm đặc, thường xuyên sử dụng sẽ sống trong wiki; tài liệu tham khảo thưa thớt thì nằm lại phía sau tầng truy xuất. Các hiệu chỉnh từ chuyên gia đi qua một vòng lặp chẩn đoán - biên dịch - xác thực - cập nhật (diagnose-compile-validate-land) có kiểm thử hồi quy, hoàn toàn không cần huấn luyện lại mô hình. Sau sáu tuần triển khai: thời gian đánh giá giảm từ nhiều ngày xuống chỉ còn vài phút, không phát sinh bất kỳ lỗi hồi quy nào. Đây là bằng chứng công khai mạnh mẽ nhất tính đến nay cho thấy một hệ thống wiki được bảo trì liên tục đánh bại hoàn toàn phương pháp khám phá lại từ đầu bằng `RAG` ở quy mô lớn.

## Truyền thống tư tưởng đứng đằng sau

- **How to Take Smart Notes**, Sönke Ahrens. Phương pháp Zettelkasten. Lập luận về các ghi chú nguyên tử (atomic notes) và mạng lưới liên kết dày đặc đến nay vẫn còn nguyên giá trị; chính khối lượng lao động thủ công nặng nề mà nó đòi hỏi mới là thứ đã giết chết phương pháp này đối với đại đa số người dùng.
- **Building a Second Brain**, Tiago Forte. Nơi khai sinh ra thuật ngữ "bộ não thứ hai" cùng phương pháp phân loại PARA. Cuốn sách được viết trước khi các `Agent` ra đời, và chính điều đó làm cho nó trở nên hữu ích vào lúc này: phần lớn cuốn sách bàn về những công việc bảo trì thủ công mà giờ đây một `Agent` có thể gánh vác hoàn toàn.
- **[Andy Matuschak's notes](https://notes.andymatuschak.org)**. Các ghi chú xanh mãi (Evergreen notes), được viết công khai như một ví dụ sống động cho chính ý tưởng đó. Đây là luận cứ thuyết phục nhất cho việc viết ghi chú để đọc lại, đồng thời là một đối trọng đáng suy ngẫm cho toàn bộ cách tiếp cận tự động hóa này: quan điểm của ông là quá trình tự tay viết chính là quá trình tư duy, vì vậy ủy thác việc viết cũng đồng nghĩa với việc từ bỏ tư duy.

## Tại sao lập luận về công sức bảo trì lại quan trọng

Mọi phương pháp kể trên đều hiệu quả. Nhưng chúng đều thất bại ở cùng một điểm: con người duy trì chúng rồi sẽ mệt mỏi. Ràng buộc duy nhất đó đã định hình toàn bộ các quyết định thiết kế của chúng, và đó chính là ràng buộc vừa mới thay đổi nhờ AI `Agent`.

Việc đọc lại các tác phẩm gốc rất đáng giá vì lý do cụ thể đó: bạn sẽ phân biệt rõ phần nào thực sự bàn về bản chất của tri thức, và phần nào chỉ là giải pháp tình thế để đối phó với giới hạn sức lực của con người.

## Bài nói chuyện và video

Mục này được chủ đích để trống thay vì nhồi nhét bất cứ video nào đang có thứ hạng cao trên YouTube. Nếu bạn từng xem được một nội dung về chủ đề này thực sự xứng đáng với thời gian bỏ ra, hãy mở một issue hoặc gửi pull request kèm theo đường dẫn và một dòng giải thích lý do.
