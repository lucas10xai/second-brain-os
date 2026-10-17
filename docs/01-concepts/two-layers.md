# Cấu trúc hai tầng

Hầu hết các thiết lập Second Brain đều thất bại vì người dùng chỉ chọn một cấu trúc duy nhất nhưng lại ép nó gánh vác cùng lúc hai công việc hoàn toàn khác bản chất.

**Tầng tri thức (Knowledge layer)** trả lời câu hỏi "tôi đang biết gì về X". Nó được tổ chức xoay quanh các ý tưởng, phát triển tích lũy mãi mãi theo thời gian, và giá trị cốt lõi nằm ở mạng lưới liên kết giữa các trang. Đây chính là mô hình LLM wiki: nạp nguồn tài liệu vào, đúc kết các khái niệm ra, và kết nối mọi thứ lại với nhau.

**Tầng dự án (Project layer)** trả lời câu hỏi "tuần này tôi đang làm việc gì". Nó được tổ chức như một đường ống xử lý (pipeline) đi từ đầu vào đến đầu ra, và phần lớn dữ liệu trong đó sẽ hoàn thành sứ mệnh ngay tại thời điểm dự án kết thúc và bàn giao.

Khi bị trộn lẫn vào nhau, hai tầng này sẽ gây hỏng hệ thống theo hai kiểu khác nhau. Một hệ thống wiki chứa lẫn các thư mục dự án sẽ nhanh chóng ngập ngụa những danh sách công việc đã cũ, làm giảm chất lượng của mọi thao tác tìm kiếm. Ngược lại, một hệ thống quản lý dự án nhồi nhét thêm các ghi chú khái niệm trừu tượng sẽ chôn vùi các file đang làm việc hằng ngày dưới đống tài liệu tham khảo mà chẳng ai mở ra trong lúc đang chạy việc.

## Cách hai tầng kết nối với nhau

Các dự án tiêu thụ tri thức từ tầng wiki và sau đó bồi đắp ngược trở lại cho nó:

```
        wiki/concepts ──────> project Inputs/
              ▲                      │
              │                      ▼
        ingest what                Process/ ──> Outputs/
        you learned                              │
              └──────────────────────────────────┘
```

Quá trình làm việc thực tế luôn tạo ra những tư liệu rất đáng lưu giữ. Việc Ingest lại chính những thành phẩm đã hoàn thành của bản thân là bước mà hầu như ai cũng bỏ qua, nhưng đó lại chính là chìa khóa giúp dự án thứ hai của bạn trong cùng lĩnh vực diễn ra nhanh hơn vượt trội so với dự án đầu tiên.

## Nên xây dựng tầng nào trước

Hãy xây dựng **tầng tri thức** trước, nếu vấn đề của bạn là đọc rất nhiều nhưng đọng lại chẳng được bao nhiêu.

Hãy xây dựng **tầng dự án** trước, nếu vấn đề của bạn là sáng nào cũng phải ngồi giải thích lại từ đầu bối cảnh công việc của mình cho khung trò chuyện AI.

Và sớm muộn gì bạn cũng sẽ dùng cả hai. Hãy xem bài [Cấu trúc Vault](../02-setup/vault-structure.md) để nắm được cách bố trí giữ cho hai tầng này luôn tách biệt rõ ràng ngay bên trong cùng một thư mục gốc.
