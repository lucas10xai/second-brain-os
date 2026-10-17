# Thực hành: Đọc nhật ký thực thi (Build: Read Your Traces)

Trang đầu tiên trong chuỗi ba trang thực hành: bài này sẽ đưa bạn từ cảm giác mơ hồ "con bot thỉnh thoảng lại làm sai" đến việc có một tệp `Golden set` nằm ngay ngắn trên ổ đĩa. Bài [Thực hành: Xây dựng bộ đánh giá](build-suite.md) sẽ biến tệp đó thành chương trình chạy được; và trang cổng kiểm soát sẽ nối nó vào CI. Chỉ cần một buổi chiều là làm xong cả ba. Kiến thức nền tảng, nếu bạn đã lỡ bỏ qua: [tại sao cần `Evals`](why-evals.md).

Bạn đi tới đây từ [bài thực hành của học phần 5](../course-5-evals/evals-practice.md)? Khi đó bạn đã có sẵn hai mươi ca kiểm thử và một trình chạy — hãy bỏ qua bước thu thập và đi thẳng tới lượt phân loại lỗi bên dưới; `Golden set` sẽ phát triển tiếp từ những gì bạn đang có.

## Thu thập 30 `Traces`

Hãy trích xuất ba mươi bản ghi hội thoại thực tế từ môi trường production — từ tệp log, bản xuất cơ sở dữ liệu, hay bất cứ thứ gì hiện có. Đầu vào thực tế luôn đánh bại đầu vào tự bịa mọi lúc. Chưa có người dùng thực tế? Hãy tự sinh một bộ khởi đầu bằng cách chạy qua chính ứng dụng của bạn: viết ba mươi câu hỏi mà một người dùng hợp lý sẽ hỏi vào tệp `starter_inputs.txt` (đa dạng hóa chân dung người dùng, cách diễn đạt, độ dài; đưa vào thêm vài câu cần phải từ chối trả lời), sau đó cho chúng chạy qua điểm vào (entry point) thực tế của ứng dụng:

```python
import json

from app import answer  # your product's entry point: str -> str

with open("starter_inputs.txt", encoding="utf-8") as f:
    inputs = [line.strip() for line in f if line.strip()]

with open("traces.jsonl", "w", encoding="utf-8") as out:
    for text in inputs:
        out.write(json.dumps({"input": text, "output": answer(text)}) + "\n")
```

## Lượt phân tích lỗi (The error-analysis pass)

Đọc lần lượt từng bản ghi `Traces` và viết đúng một dòng cho mỗi bản ghi vào một tệp văn bản thuần túy. Một định dạng hiệu quả trông như sau:

```
trace_id | verdict | one-sentence failure note | verbatim quote
014 | fail | invented an order number not present in context | "your order #88412 shipped"
015 | ok   |  |
016 | fail | apologised and asked a question instead of acting | "could you clarify which invoice"
```

Bốn quy tắc: một câu cho mỗi lỗi; luôn trích dẫn nguyên văn đầu ra; ghi nhận cả các ca thành công là `ok` để bạn biết mẫu số chung; và không sửa bất kỳ thứ gì cho đến khi đọc xong cả ba mươi bản ghi. Một giờ đồng hồ bỏ ra cho việc này là giờ làm việc có tính đòn bẩy cao nhất của toàn bộ quá trình xây dựng.

## Gom cụm thành bảng phân loại lỗi (Taxonomy)

Với ba mươi ghi chú, bạn hoàn toàn có thể gom nhóm bằng tay, nhưng một mô hình LLM sẽ là người phân loại bước đầu khá tốt. Hãy dán các ghi chú của bạn vào prompt sau:

```text
Below are failure notes from an error-analysis pass over one AI product,
one note per line, prefixed with a trace id.

Cluster them into 3 to 8 failure modes. For each mode give:
- a snake_case name
- a one-sentence definition
- the trace ids it covers

Every note must land in exactly one mode. Put genuine one-offs in a mode
called "other" rather than inventing a mode for a single note. Do not
propose fixes. Return a markdown list.

<notes>
PASTE YOUR NOTES HERE
</notes>
```

Hãy coi kết quả trả về là một bản nháp: gộp các kiểu lỗi thực chất là một, đặt lại tên cho những mục còn mơ hồ, hạ cấp bất cứ thứ gì bạn không đồng tình. Mô hình làm việc sắp xếp; còn bạn mới là chủ sở hữu của bảng phân loại lỗi.

## Viết `Golden set`

Chuyển hóa bảng phân loại lỗi thành tệp `golden.jsonl`, mỗi dòng một ca kiểm thử:

```json
{"id": "hallucinated_id_003", "failure_mode": "hallucinated_order_id", "input": "where is my order?", "checks": {"must_not_contain": ["#"]}, "judge_expectation": null, "source": "trace 014"}
{"id": "clarify_loop_001", "failure_mode": "clarify_instead_of_acting", "input": "cancel my March invoice", "checks": null, "judge_expectation": "The reply cancels or begins cancelling the invoice rather than asking a clarifying question.", "source": "trace 016"}
{"id": "happy_path_002", "failure_mode": "none", "input": "what is your refund window?", "checks": {"must_contain": ["30 days"]}, "judge_expectation": null, "source": "trace 015"}
```

Có năm trường dữ liệu. `id` cố định và dễ tìm kiếm bằng `grep`. `failure_mode` lấy từ bảng phân loại lỗi (đặt là `none` cho các ca chạy chuẩn happy-path). `input` là nội dung sản phẩm nhận vào. Chỉ đặt giá trị cho đúng một trong hai trường `checks` (các phép kiểm tra chuỗi mà code có thể tự chấm: `must_contain`, `must_not_contain`) hoặc `judge_expectation` (một câu đơn lẻ để giám khảo LLM xác minh) — hãy luôn ưu tiên `checks` bất cứ nơi nào nó có thể gánh vác được ca kiểm thử. Trường `source` trỏ ngược về bản ghi `Traces` gốc, bởi vì bạn sẽ muốn xem lại bản gốc khi ca kiểm thử đó bắt đầu báo lỗi.

Mỗi kiểu lỗi đã đặt tên cần có một vài ca kiểm thử đại diện, cộng thêm những ca thành công nhàm chán để bạn không bị tối ưu lệch (over-fit) vào các ca bệnh lý — lý giải chi tiết nằm ở bài [thiết kế bộ đánh giá](designing-evals.md). Hãy commit tệp này ngay cạnh mã nguồn của bạn và chuyển sang bước xây dựng bộ chạy đánh giá.
