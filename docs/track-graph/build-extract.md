# Thực hành: Trích xuất đồ thị

Một bài thực hành gọn trong một buổi tối gồm ba phần: xây dựng tầng đồ thị có thể truy vấn được ngay trên chiếc Vault mà Agent của bạn đang duy trì. Trang này giúp bạn đi từ một thư mục chứa các tệp Markdown đến hai tệp lưu cạnh (edge files); phần [Thực hành: Truy vấn đồ thị](build-query.md) sẽ nạp chúng vào NetworkX, và phần [Thực hành: Đưa vào vòng lặp (Loop)](build-use.md) sẽ trao quyền truy vấn đó cho Agent.

Tiền đề xuất phát từ bài [tại sao cần Knowledge Graph](why-graphs.md): một hệ thống wiki với các liên kết được biên tập cẩn thận bản thân nó đã là một Knowledge graph. Thứ nó thiếu là định kiểu (types) — mọi cạnh đều chỉ nói chung chung là "có liên quan", không cạnh nào nói rõ liên quan như thế nào. Vì vậy, kế hoạch là xuất tự động đồ thị liên kết thuần túy bằng kịch bản (script), sau đó cho Claude Code chạy một lượt quét qua các trang để gắn kiểu cho liên kết.

## Xuất đồ thị liên kết bằng một câu lệnh

Kho mã nguồn đã có sẵn tệp `scripts/graph_export.py`, chỉ dùng thư viện chuẩn của Python. Hãy chạy lệnh này ngay tại thư mục gốc của Vault:

```
python scripts/graph_export.py . edges.csv
```

Dùng lệnh `python3` nếu bạn ở trên máy Mac; còn trên Windows thì tên lệnh đó thường trỏ tới bản stub của Microsoft Store. Kịch bản này sẽ duyệt qua mọi trang nằm ngoài các thư mục ẩn, thư mục mẫu (template) và thư mục chứa script, phân giải các `[[wikilinks]]` không phân biệt hoa thường đối chiếu với tên tệp, rồi ghi ra kết quả:

```csv
source,target
GraphRAG,RAG
Lost in the Middle,RAG
```

Các liên kết trỏ tới những trang không tồn tại sẽ bị loại bỏ, điều này hoàn toàn hợp lý cho bài thực hành này: một cạnh trỏ vào hư không là một lỗ hổng cần vá, chứ không phải một mối quan hệ để truy vấn. Tùy chọn `--format graphml` sẽ xuất ra định dạng dùng cho Gephi — xem thêm trang [công cụ](tools.md) để biết cách khai thác tệp này.

## Định hình lược đồ trước khi trích xuất

Bài [xây dựng đồ thị bằng LLM](building-graphs-with-llms.md) đã nhấn mạnh nguyên tắc phải quyết định bản thể luận (ontology) trước, và nguyên tắc đó vẫn đúng ở quy mô của một Vault. Sáu loại cạnh là đủ bao phủ một kho ngữ liệu mà các trang xoay quanh con người, công cụ, bài báo khoa học và các luận điểm (claims). Càng nhiều loại cạnh thì xác suất chọn sai trên mỗi liên kết càng cao, vì vậy hãy kìm lòng trước việc thêm loại thứ bảy cho đến khi loại thứ sáu thực sự chứng minh được giá trị của nó.

## Câu lệnh nhắc (Prompt) trích xuất

Hãy chạy câu lệnh nhắc này trong Claude Code tại thư mục gốc của Vault:

```text
Read every markdown page under wiki/, skipping templates and raw.
Build a typed edge list on top of the plain wikilinks.

For each page, note its type from the frontmatter (person, tool,
claim, concept, paper, note). Then emit one row per relationship
you can ground in the text, using only these edge types:

  built        person -> tool
  authored     person -> paper or claim
  uses         page -> tool
  supports     paper or claim -> claim
  contradicts  paper or claim -> claim
  extends      page -> page

Rules:
- Source and target must both be existing page names, spelt
  exactly as the filenames are, without the .md.
- Only record what a page states. If the relationship is your
  inference rather than the page's claim, skip it.
- Append rows to typed_edges.csv with the header
  source,target,type,found_in — where found_in is the page the
  relationship was stated on.

Work in batches of twenty pages and append after each batch, so
an interruption keeps partial work. When finished, report the row
count and the five most connected nodes.
```

Hai dòng quy tắc gánh vác phần lớn chất lượng công việc. Việc giới hạn hai đầu mút vào tên các trang hiện có giúp giữ các cạnh có định kiểu nằm trong cùng không gian tên (namespace) với đồ thị liên kết thuần, nhờ đó cả hai tệp có thể nạp chung vào một cấu trúc duy nhất ở bước tiếp theo. Và quy tắc "chỉ ghi nhận những gì trang viết nêu rõ" (`Only record what a page states`) chính là nguyên tắc liên kết có định kiểu của Vault: một Agent tự suy diễn các mối quan hệ sẽ tạo ra một đồ thị âm thầm mã hóa những định kiến của riêng nó.

## Kết quả thu được

```csv
source,target,type,found_in
Jerry Liu,LlamaIndex,built,Jerry Liu
RAG,LlamaIndex,uses,RAG
Lost in the Middle,Long context replaces RAG,contradicts,Long context replaces RAG
```

Cột `found_in` chính là thông tin truy nguyên nguồn gốc (provenance) — câu trả lời cho thắc mắc "tại sao đồ thị lại tin vào điều này". Nếu bạn muốn thông tin truy nguyên phong phú hơn, hãy yêu cầu xuất ra định dạng JSONL: mỗi dòng một đối tượng JSON, giữ nguyên các trường trên cộng thêm khóa `quote` lưu lại nguyên văn câu chữ mà cạnh đó được rút ra. Tệp CSV là định dạng mà trang tiếp theo sẽ nạp, vì vậy hãy giữ nó làm đầu ra chính.

## Đọc kiểm tra trước khi tin tưởng

Hãy lấy mẫu hai mươi dòng và đối chiếu với các trang gốc trước khi đi tiếp. Hãy chuẩn bị tinh thần sẽ gặp vài cạnh tuy có căn cứ về mặt câu chữ nhưng vô dụng, hoặc đôi chỗ chiều mũi tên bị ngược. Hãy sửa câu lệnh nhắc (prompt) chứ đừng sửa tay từng dòng dữ liệu, rồi cho chạy lại — một lượt quét qua vài trăm trang chỉ mất vài phút. Sau đó, hãy nạp kết quả vào bước tiếp theo tại [Thực hành: Truy vấn đồ thị](build-query.md).
