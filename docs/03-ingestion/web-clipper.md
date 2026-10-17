# Bài viết trên web

Các bài viết trên web chiếm phần lớn khối lượng nội dung mà mọi người thường lưu lại, và trình duyệt chính là nơi quyết định bấm lưu diễn ra. Bất kỳ quy trình nào đòi hỏi bạn phải chuyển sang cửa sổ ứng dụng khác đều sẽ sớm thất bại.

## Obsidian Web Clipper

Đây là [tiện ích mở rộng chính thức](https://obsidian.md/clipper) do đội ngũ Obsidian phát triển, hỗ trợ Chrome, Firefox, Safari, Edge, Brave và Arc. Công cụ này trích xuất phần nội dung văn bản sạch của trang web bằng thư viện Mozilla Readability — chính là bộ máy đứng sau chế độ đọc (Reader View) của Firefox — rồi lưu thẳng thành file Markdown vào bên trong Vault của bạn.

Hãy cài đặt tiện ích, mở phần cài đặt của nó lên và trỏ thư mục đích lưu file về `raw/`.

## Cấu hình biểu mẫu (Template)

Biểu mẫu mặc định chỉ lưu phần nội dung chính của trang. Hãy bổ sung thêm phần Frontmatter để Agent nắm được thông tin tổng quan về tài liệu mà không cần phải đọc lại toàn bộ file từ đầu đến cuối:

```
---
title: {{title}}
source: {{url}}
author: {{author}}
published: {{published}}
clipped: {{date}}
type: article
---

{{content}}
```

Trên khá nhiều trang web, hai trường `{{author}}` và `{{published}}` sẽ trả về giá trị rỗng. Điều đó hoàn toàn không sao cả — một trường để trống vẫn tốt hơn nhiều so với một thông tin đoán mò, và Agent sẽ xử lý khoảng trống này bằng cách ghi nhận nguồn tài liệu không rõ ngày tháng thay vì tự bịa ra một ngày giả.

## Nên lưu những gì

Hãy lưu lại những tài liệu mà một năm sau bạn vẫn muốn tìm đọc lại: các nguồn tư liệu gốc (primary sources), các bài viết kỹ thuật chuyên sâu, bài báo nghiên cứu, tài liệu hướng dẫn chính thức, hoặc những bài lập luận trái chiều với quan điểm của bạn mà bạn muốn phản biện lại sau này.

Hãy bỏ qua những tin tức thời sự sẽ nguội lạnh chỉ sau một tuần, các bài viết liệt kê hời hợt (listicles), và bất kỳ thứ gì bạn bấm lưu chỉ vì cảm giác áy náy sợ bỏ lỡ. Mỗi một trang kém giá trị nạp vào hệ thống sẽ bắt bạn trả giá tới hai lần: một lần tốn chi phí xử lý lúc Ingest, và hàng chục lần sau đó mỗi khi Agent phải đọc lướt qua nó trong lúc đi tìm kiếm thông tin khác.

Bài kiểm tra trung thực nhất ngay tại khoảnh khắc định bấm lưu là: bạn có gọi tên được câu hỏi mà sau này mình sẽ hỏi nguồn tài liệu này hay không. Nếu không nghĩ ra được, đừng lưu nó.

## Xử lý các trang web có cấu trúc đặc thù

- **Tường thu phí (Paywalls).** Web Clipper lưu lại những gì trình duyệt đã kết xuất ra màn hình. Nếu mắt bạn đọc được toàn bộ bài viết trên trình duyệt thì tiện ích sẽ lưu được. Nếu bạn bị chặn bởi tường thu phí, tiện ích sẽ chỉ lưu lại đúng dòng thông báo yêu cầu trả tiền — vì vậy hãy kiểm tra nhanh file trước khi đóng thẻ trình duyệt.
- **Các trang tài liệu kỹ thuật (Documentation sites).** Ngồi bấm lưu thủ công từng trang một là cách làm vô vọng. Hãy lưu lại trang mục lục gốc rồi để Agent tự tải phần còn lại, hoặc nhân bản (clone) thẳng kho mã nguồn tài liệu đó về `raw/` nếu dự án mở mã nguồn.
- **Ứng dụng trang đơn (SPA) và nội dung tải động.** Bộ trích xuất Readability đôi khi chỉ lấy về được một mảnh nội dung bị cắt cụt. Hãy mở file kiểm tra qua trước khi chạy Ingest.
- **Các luồng thảo luận (Threads) và mục bình luận.** Giá trị thực sự thường nằm ở các phản hồi phía dưới — thứ mà Web Clipper thường lược bỏ mất. Hãy sao chép thủ công luồng thảo luận hoặc chụp ảnh màn hình lưu vào `raw/assets/`.

## Lưu ngay lúc đọc, Ingest theo lô sau

Việc bấm lưu (clipping) và việc nạp dữ liệu (`Ingest`) được chủ đích tách thành hai bước riêng biệt. Bạn cứ thoải mái bấm lưu bài viết xuyên suốt cả ngày, rồi cuối ngày chạy lệnh `/ingest` gom thành một lô duy nhất — bởi nếu bạn chạy Ingest lẻ tẻ từng bài một ngay lúc lưu, Agent sẽ mất đi cơ hội phát hiện ra rằng ba bài viết khác nhau bạn lưu trong tuần này thực chất đang cùng bàn về một ý tưởng cốt lõi.

## Tiếp theo

[YouTube và podcast](youtube-transcripts.md)
