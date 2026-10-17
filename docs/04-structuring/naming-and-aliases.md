# Đặt tên và Aliases

Các `Wikilink` phân giải theo tên, vì vậy tên trang không chỉ mang tính thẩm mỹ. Nó chính là khóa chính (key) mà toàn bộ đồ thị được xây dựng dựa trên đó.

## Tiêu đề chuẩn tắc (Canonical titles)

Mỗi trang có một tiêu đề chuẩn tắc duy nhất, và đó là cái tên bạn sẽ dùng khi trò chuyện với một người trong ngành.

Những quy tắc thực tế giúp tránh được hầu hết các rắc rối:

- **Dùng số ít, không dùng số nhiều.** `Vector database`, không phải `Vector databases`.
- **Viết đầy đủ từ viết tắt trong tiêu đề, đưa từ viết tắt vào `Aliases`.** Tiêu đề dành cho người đọc, còn alias dành cho liên kết.
- **Không đưa ngày tháng, không đưa phiên bản vào tiêu đề** trừ khi bản thân đối tượng đó thực sự là một phiên bản cụ thể. Một trang có tên `MCP spec 2026-07` sẽ trở nên sai lệch sau một tháng; còn một trang tên là `MCP` có mục lịch sử phiên bản bên trong thì không.
- **Không dùng tiền tố riêng lẻ kiểu tự chế trong `Vault`.** Kiểu đặt tên như `Concept - RAG` chỉ gây xung đột với cú pháp liên kết mà không mang lại lợi ích gì.

## Aliases (Tên gọi thay thế)

Mọi tên gọi khác của cùng một chủ đề sẽ được liệt kê trong `Frontmatter`:

```yaml
title: Retrieval augmented generation
aliases: [RAG, retrieval-augmented generation]
```

`Aliases` chính là thứ ngăn không cho `Vault` âm thầm mọc ra ba trang khác nhau cho cùng một thứ. Nếu không có alias, một tài liệu nguồn viết là RAG sẽ tạo ra trang `RAG`, còn một tài liệu nguồn viết đầy đủ sẽ tạo ra trang thứ hai, và chẳng trang nào biết đến sự tồn tại của trang kia.

Hãy thêm `Aliases` ngay lúc tạo trang, chứ không phải để sau này. Đến khi bạn nhận ra sự trùng lặp thì cả hai trang đều đã có các liên kết trỏ tới (inbound links) mất rồi.

## Hai thứ trùng tên nhau

Hãy phân biệt rõ ngay trong tiêu đề, thay vì dùng những hậu tố ký hiệu mà chẳng ai gõ:

```
Mercury (planet)
Mercury (element)
```

Sau đó gán alias từ gốc cho trang nào chiếm ưu thế hơn trong `Vault` của bạn, hoặc không gán cho trang nào cả nếu cả hai đều quan trọng như nhau — cách này buộc `Agent` phải chọn rõ ràng thay vì đoán mò.

Quy tắc tương tự cũng áp dụng cho những người trùng tên nhau và cho các dự án cá nhân của bạn bị trùng tên với một sản phẩm nổi tiếng.

## Đổi tên trang (Renaming)

`Obsidian` sẽ tự động cập nhật các liên kết khi bạn đổi tên bên trong ứng dụng. Nhưng khi `Agent` đổi tên file trực tiếp trên hệ thống tệp thì không, và đó là nguyên nhân phổ biến số một gây ra lỗi đứt gãy liên kết (broken links) trong một `Vault` do `Agent` duy trì.

Quy tắc cần đưa vào `CLAUDE.md`: việc đổi tên phải tuân theo một quy trình được ghi chép rõ ràng. Cập nhật file, cập nhật mọi liên kết trỏ tới nó (inbound links), thêm tên cũ vào `Aliases`, và ghi lại vào `log.md`. Việc giữ tên cũ làm alias rất quan trọng vì nó giúp các tham chiếu bên ngoài cũng như trí nhớ của chính bạn tiếp tục hoạt động bình thường.

Sau đó hãy chạy `scripts/link_check.py` để xác nhận không có liên kết nào bị treo.

## Tiếp theo

[Khử trùng lặp và gộp trang](dedupe-and-merge.md)
