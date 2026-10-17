# Liên kết định kiểu (Typed links)

Một `[[wikilink]]` thông thường chỉ cho biết hai trang có liên quan đến nhau. Nó không cho biết liên quan *như thế nào*, và khi quy mô lớn dần thì đó là một sự mất mát thông tin thực sự.

Bạn không thể hỏi một đồ thị không định kiểu xem điều gì đang mâu thuẫn với một nhận định, bằng chứng nào ủng hộ nó, hay những trang nào mở rộng một phương pháp. Mọi cạnh nối đều giống hệt nhau, nên mọi câu hỏi đều bị thu gọn về mức "những gì đang nằm gần đây".

## Bộ từ vựng tối giản

Đủ nhỏ để nhớ thuộc lòng, đủ sức biểu đạt để xứng đáng với công sức bỏ ra:

- **supports** (ủng hộ) - trang này là bằng chứng củng cố cho trang kia
- **contradicts** (mâu thuẫn) - trang này đưa ra lập luận phản bác lại trang kia
- **extends** (mở rộng) - xây dựng dựa trên trang kia, bổ sung thêm vào đó
- **part-of** (thuộc về) - là một thành phần nằm trong một tổng thể lớn hơn
- **applies** (áp dụng) - ứng dụng một phương pháp vào thực tế

Con số năm loại là sự giới hạn có chủ đích. Mỗi loại thêm vào là thêm một lựa chọn mà `Agent` phải phân định chính xác trên từng liên kết, và một bộ từ vựng gồm hai mươi loại sẽ dẫn đến việc gắn nhãn thiếu nhất quán — điều còn tệ hơn cả việc không định kiểu.

## Hai cách để mã hóa kiểu liên kết

**Nội dòng (Inline), ngay cạnh liên kết:**

```markdown
Kết quả về độ nhạy vị trí (supports:: [[Lost in the Middle]]) cho thấy
chỉ riêng độ dài ngữ cảnh không giải quyết được bài toán truy xuất.
```

Dataview đọc được các trường nội dòng (inline fields), nên cú pháp này có thể truy vấn trực tiếp ngay bên trong `Obsidian` mà không cần công cụ phụ trợ nào.

**Trong `Frontmatter`, ở cấp độ từng trang:**

```yaml
contradicts: ["[[Long context replaces RAG]]"]
extends: ["[[Retrieval augmented generation]]"]
```

Cách này giúp truy vấn gọn gàng hơn, nhưng lại tách rời khỏi câu văn cụ thể sinh ra liên kết đó. Hãy dùng `Frontmatter` cho các mối quan hệ ở cấp độ toàn trang, và dùng cú pháp nội dòng cho các mối quan hệ ở cấp độ từng nhận định cụ thể.

## Lợi ích mang lại

```dataview
LIST FROM "wiki/concepts"
WHERE contains(contradicts, this.file.link)
```

Truy vấn trên trả về "mọi thứ trong `Vault` của tôi có lập luận phản bác lại trang này" — một câu hỏi mà đồ thị thuần túy hoàn toàn bó tay.

Ở cấp độ `Agent`, lợi ích này còn mạnh mẽ hơn nữa. Một lượt chạy `Ingest` khi ghi nhận một tài liệu nguồn mới là `contradicts` (mâu thuẫn) với một trang hiện có tức là đã hoàn thành việc gắn cờ báo hiệu sự bất đồng ngay ở tầng cấu trúc, thay vì chôn vùi nó trong những dòng văn xuôi chỉ lộ diện khi có ai đó tình cờ đọc tới trang đó.

## Đừng định kiểu cho mọi liên kết

Hầu hết các liên kết chỉ là những lần nhắc tên thông thường và nên được giữ nguyên ở dạng thuần túy. Việc gán kiểu cho mọi liên kết sẽ làm cho bộ từ vựng trở nên vô nghĩa, đồng thời khiến quá trình `Ingest` chậm hơn và dễ phát sinh lỗi hơn.

Chỉ định kiểu cho những liên kết mà bản thân mối quan hệ chính là trọng tâm: bằng chứng ủng hộ, sự bất đồng, sự mở rộng. Trên thực tế, tỷ lệ này rơi vào khoảng một trên năm liên kết.

## Chỉ dẫn cho Agent

```
Khi một tài liệu nguồn ủng hộ (supports), mâu thuẫn (contradicts) hoặc mở rộng (extends) một nhận định trên trang hiện có,
hãy ghi nhận mối quan hệ đó bằng một liên kết định kiểu (typed link). Dùng Wikilink thông thường cho các lần
nhắc tên bình thường. Không được gán kiểu cho một mối quan hệ do bạn tự suy diễn; chỉ gán kiểu cho những gì
tài liệu nguồn khẳng định trực tiếp.
```

Câu cuối cùng cực kỳ quan trọng. Một `Agent` tự đoán mò các mối quan hệ sẽ tạo ra một đồ thị trông có vẻ chặt chẽ nhưng thực chất lại mã hóa chính những giả định chủ quan của nó vào cấu trúc dữ liệu.

## Tiếp theo

[Đồ thị và Embeddings](graph-vs-vectors.md)
