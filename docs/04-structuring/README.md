# Tổ chức cấu trúc (Structuring)

Những quy tắc quyết định liệu `Vault` của bạn sẽ trở thành một đồ thị tri thức hay một bãi rác dữ liệu.

Quá trình `Ingest` quyết định những gì được đưa vào. Cấu trúc quyết định liệu có thứ gì trong số đó lấy ra dùng lại được hay không. Hai `Vault` chứa cùng một nghìn tài liệu nguồn có thể trở thành một cộng sự nghiên cứu đắc lực hoặc một đống hỗn độn không thể tìm kiếm, và sự khác biệt nằm hoàn toàn ở các quy tắc dưới đây.

Mọi thứ ở đây đều thuộc về file `CLAUDE.md` của bạn, bởi vì một quy tắc mà `Agent` chỉ đọc một lần trong khung chat sẽ chỉ tồn tại trong một phiên làm việc, còn quy tắc nằm trong `CLAUDE.md` sẽ áp dụng cho mọi trang mà nó từng viết.

## Các trang trong chương

- [Mỗi trang một ý tưởng](atomic-pages.md)
- [Bốn loại trang](page-types.md)
- [Quy tắc liên kết](linking-rules.md)
- [Lược đồ Frontmatter](frontmatter-schema.md)
- [Đặt tên và Aliases](naming-and-aliases.md)
- [Khử trùng lặp và gộp trang](dedupe-and-merge.md)
- [Mâu thuẫn và thay thế thông tin](contradictions-and-supersession.md)
- [index.md và log.md](index-and-log.md)

---

[Quay lại hướng dẫn đầy đủ](../README.md)
