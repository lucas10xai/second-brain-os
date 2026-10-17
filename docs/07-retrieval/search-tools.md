# Công cụ tìm kiếm

Truy xuất trong một Vault văn bản thuần túy chủ yếu là dùng `grep`. Nghe có vẻ thô sơ nhưng gần như lúc nào cũng là quá đủ.

## ripgrep

```bash
rg -i "graph rag" ~/brain --type md -l
rg -i "supersed" ~/brain -C 2
```

Trả kết quả tức thì trên hàng chục nghìn file. Agent mặc định sử dụng công cụ này khi làm việc trên hệ thống file, và với câu hỏi kiểu "tôi đã nhắc đến thứ này ở đâu", nó đánh bại mọi giải pháp cầu kỳ hơn cả về tốc độ lẫn tính nhất quán.

Giới hạn của nó là phụ thuộc vào từ ngữ chính xác. Nó không thể tìm ra trang viết về một khái niệm nếu bạn diễn đạt bằng từ khác — và đó chính là lúc cần đến Knowledge graph cùng trang chỉ mục.

## Tìm kiếm trong Obsidian

Đủ tốt cho nhu cầu tương tác trực tiếp. Các toán tử đáng biết gồm: `path:`, `file:`, `tag:` và `line:` cho các từ cùng xuất hiện trên một dòng — giúp loại bỏ phần lớn kết quả dương tính giả.

## Dataview

Truy vấn dựa trên Frontmatter, nơi giải đáp các câu hỏi mang tính cấu trúc:

````
```dataview
TABLE updated, tags FROM "wiki/concepts"
WHERE contains(tags, "unverified")
SORT updated ASC
```
````

Bất kỳ câu hỏi nào có dạng "những trang nào mang thuộc tính P" đều là một truy vấn Dataview, và việc trả lời chúng bằng cách bắt Agent đọc từng file sẽ vừa chậm hơn vừa kém tin cậy hơn.

## Kết hợp các công cụ

Mô hình hoạt động hiệu quả: dùng Dataview hoặc ripgrep để lấy ra tập hợp ứng viên ban đầu, dùng Knowledge graph để mở rộng từ tập hợp đó, và dùng Agent để đọc hiểu rồi tổng hợp.

```
Tìm mọi trang được gắn thẻ unverified, lần theo các liên kết của chúng, và cho tôi biết những nhận định nào đang phụ thuộc vào các nguồn chưa được kiểm chứng.
```

Lọc cơ học trước, phán đoán sau. Yêu cầu Agent thực hiện bước lọc bằng cách đọc toàn bộ mọi thứ sẽ làm lãng phí Context window vào những trang mà một câu truy vấn có thể loại bỏ chỉ trong vài mili-giây.

## Khi việc tìm kiếm trở nên chậm chạp

Ở quy mô cá nhân, bản thân công cụ tìm kiếm sẽ không bao giờ chậm. Chạy ripgrep trên mười nghìn file markdown vẫn cho kết quả tức thì; nếu bạn cảm thấy việc tìm kiếm bị chậm, nguyên nhân thường là do Agent đang đọc quá nhiều file, chứ không phải do bản thân lệnh tìm kiếm.

Đó là bài toán về ngữ cảnh, không phải bài toán tìm kiếm. Xem thêm [ngân sách ngữ cảnh (Context budget)](context-budget.md).

## Tiếp theo

[Bổ sung RAG khi cần thiết](rag-on-top.md)
