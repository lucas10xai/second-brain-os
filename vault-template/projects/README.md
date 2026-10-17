# projects/

Mỗi dự án một thư mục. Mỗi thư mục chứa file `CLAUDE.md` riêng cùng quy trình 4 giai đoạn:

```
project-name/
  CLAUDE.md    dự án này là gì, mục tiêu duy nhất của nó, vai trò của agent
  Inputs/      ý tưởng, bản đề bài (brief), tài liệu nguồn cho dự án này
  Process/     công việc đang thực hiện
  Outputs/     sản phẩm hoàn chỉnh
  Feedback/    kết quả, số liệu, những gì thực sự đã diễn ra
```

`Feedback/` là thư mục mà mọi người thường bỏ qua nhưng lại chính là nơi giúp hệ thống ngày càng tốt lên. Không có nó, agent sẽ không hề biết sản phẩm của tháng trước có hiệu quả hay không.

Hãy mở riêng từng dự án như một vault độc lập khi bạn làm việc trên đó, để agent chỉ tập trung vào một mục tiêu duy nhất thay vì toàn bộ cuộc sống của bạn. Xem thêm [khoanh vùng dự án (project scoping)](../../docs/02-setup/project-scoping.md).
