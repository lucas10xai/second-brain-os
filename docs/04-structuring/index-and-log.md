# index.md và log.md

Hai file này bản thân chúng không phải là tri thức, nhưng nếu thiếu chúng thì tri thức sẽ rất khó tiếp cận và không thể nào kiểm toán (audit) được.

## index.md

Danh mục tổng (catalog). Mọi trang trong `Vault`, được nhóm theo loại, cùng với các khoảng trống (gaps) được liệt kê ở cuối file.

Công việc thực sự của nó là tiết kiệm chi phí truy xuất (retrieval economy). Khi `Agent` nhận được một câu hỏi, việc đọc `index.md` đầu tiên sẽ cho nó biết những gì đang tồn tại và những trang nào đáng để mở ra. Nếu không có file này, giải pháp thay thế duy nhất là quét toàn văn (full-text sweep) — vừa chậm hơn, tốn nhiều `Context window` hơn, lại vừa bỏ sót những trang có cách dùng từ khác với câu hỏi.

Hãy giữ cho nó dễ điều hướng thay vì cố làm cho nó trông có vẻ vét cạn chi tiết:

```markdown
## Concepts

### Retrieval
- [[Retrieval augmented generation]] - chunking, embeddings, when it beats a wiki
- [[GraphRAG]] - entity graph plus community summaries

### Agents
- [[Agent harness]] - the loop around a model
```

Một dòng mô tả cho mỗi mục. Dòng mô tả đó chính là thứ giúp `Agent` quyết định có nên mở trang đó ra hay không, và nó hoàn toàn xứng đáng với số token bỏ ra.

## Các khoảng trống (Gaps)

Ở dưới cùng của file chỉ mục là danh sách những trang đã được liên kết tới nhưng chưa hề tồn tại.

Phần này là thứ mang tính định hướng hành động cao nhất trong toàn bộ `Vault`. Nó là danh sách những chủ đề mà tài liệu của chính bạn cứ nhắc đi nhắc lại nhưng bạn lại chưa từng viết xuống — và đó thường là một tấm bản đồ chính xác chỉ ra những gì bạn nên đọc tiếp theo.

## log.md

Mỗi thao tác một dòng, chỉ ghi nối tiếp vào cuối file (append), mục mới nhất nằm ở dưới cùng.

```
2026-09-07 ingest raw/karpathy-gist.md -> 1 source, 2 concepts, 1 entity, 9 links
2026-09-07 merge [[RAG]] <- [[Retrieval-augmented generation]]
2026-09-08 lint -> 3 broken links fixed, 2 orphans flagged
```

File nhật ký (`log.md`) là thứ giúp một `Vault` do `Agent` duy trì có thể kiểm toán được. Khi một trang nói điều gì đó mà bạn không nhận ra, nhật ký sẽ cho bạn biết lượt chạy nào đã tạo ra nó. Khi một thứ gì đó biến mất, nhật ký chính là sự khác biệt giữa một cú gộp trang có thể truy vết và một sự biến mất bí ẩn.

Nó cũng cung cấp nguyên liệu đầu vào cho [skill rà soát (review skill)](../../skills/README.md): những gì đã thay đổi trong tuần này được lấy từ đây, chứ không phải từ việc đoán mò qua mốc thời gian sửa đổi file (file timestamps).

## Giữ cho cả hai file không bị phình to

Chỉ mục (`index.md`) lớn dần theo `Vault`, điều đó hoàn toàn bình thường, nhưng các danh sách phẳng sẽ không còn dễ điều hướng nữa khi chạm mốc khoảng hai trăm mục. Hãy nhóm theo chủ đề, và một khi chủ đề nào vượt quá khoảng ba mươi mục, hãy tách cho nó một trang chỉ mục riêng và liên kết tới nó từ trang chỉ mục chính.

Nhật ký (`log.md`) sẽ dài ra mãi mãi và chẳng ai đọc lại các dòng quá cũ. Hãy gom các mục cũ hơn vài tháng thành một dòng tóm tắt cho mỗi tháng, hoặc lưu trữ (archive) chúng vào một file gắn theo ngày tháng. Giữ lại chi tiết gần đây, nén lịch sử cũ lại.

## Quy tắc sống còn

Cả hai file phải được cập nhật ngay trong cùng lượt chạy với phần công việc mà chúng mô tả.

Một chỉ mục bị trễ nhịp còn tệ hơn là không có chỉ mục, bởi vì `Agent` tin tưởng vào nó và sẽ ngừng tìm kiếm những trang không được liệt kê trong đó. Còn một dòng nhật ký được viết bù sau đó chỉ là sự tái dựng, không phải là một bản ghi thực tế.

## Tiếp theo

[Đồ thị (Graphs)](../05-graphs/README.md), nơi những cấu trúc này bắt đầu sinh lời.
