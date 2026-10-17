# Thực hành: Điểm cuối quyết định định kiểu

Jev hiện vẫn đang trong danh sách chờ, nên hầu hết độc giả chưa thể gọi trực tiếp nó ngay lúc này — xem tình trạng cấp quyền truy cập tại bài [bắt đầu với Jev](getting-started.md). Thứ bạn hoàn toàn có thể xây dựng ngay hôm nay chính là cái khuôn mà nó sẽ lắp vừa khít vào: một hàm nhận đầu vào là lược đồ (schema) cùng trạng thái dữ liệu, rồi trả về một quyết định có định kiểu kèm theo điểm số tự tin (confidence score). Hãy xây dựng đường khớp nối (seam) đó ngay bây giờ bằng một mô hình LLM thông thường, để sau này [mô hình System One](system-one-models.md) có thể lắp thế chỗ (drop-in) một cách nhẹ nhàng. Trang này xây dựng điểm cuối quyết định đó; trang tiếp theo sẽ đấu nối nó vào một bộ định tuyến (Router).

## Bản hợp đồng giao tiếp (Contract)

Một hàm duy nhất, `decide(schema, question, state)`, trả về `{"value": ..., "confidence": ...}`, trong đó `value` tuân thủ đúng lược đồ được truyền vào và `confidence` là một số thực nằm giữa 0 và 1. Cấu trúc này phản chiếu chính xác những gì các kiểu nguyên thủy của Jev mang lại cho bạn — một câu trả lời có định kiểu cộng với một xác suất — mà không cần giả vờ bắt chước cách Jev tính toán ra chúng bên dưới.

## Tại sao dùng tính nhất quán tự thân (Self-consistency) thay vì logprobs

Có hai con đường thực tế để lấy ra một con số đo độ tự tin từ LLM. Dùng xác suất logarit của token (`logprobs`) lẽ ra là con đường trực tiếp nhất, nhưng cánh cửa đó hiện đang đóng: API của Claude hoàn toàn không cung cấp `logprobs`, còn trên các mô hình hiện tại của OpenAI, các nhà phát triển phản ánh rằng mảng `logprobs` trả về luôn trống rỗng mỗi khi bật chế độ đầu ra có cấu trúc (`json_schema`) — mà đây lại là chế độ bắt buộc phải có của mẫu thiết kế này. Con đường thực sự hoạt động được là dựa vào tính nhất quán tự thân (self-consistency): lấy mẫu (sample) cùng một câu hỏi nhiều lần, chọn câu trả lời chiếm đa số, và lấy tỷ lệ đồng thuận làm độ tự tin. Tuy thô sơ hơn, nhưng nó đo lường một đại lượng có thật — mức độ ổn định trong phán đoán của mô hình trước đầu vào của bạn.

## Mã nguồn triển khai

Sử dụng đầu ra có ràng buộc thông qua tính năng structured outputs của Claude API (`output_config`, đã phát hành chính thức, không cần cờ beta), chạy năm mẫu song song trên mô hình nhỏ và nhanh. Cần cài đặt `pip install anthropic` và thiết lập biến môi trường `ANTHROPIC_API_KEY`.

```python
# decision.py
import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

import anthropic  # pip install anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
MODEL = "claude-haiku-4-5"      # small and fast: this seat is System One work
SAMPLES = 5

def _ask_once(schema: dict, question: str, state: str) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        temperature=1.0,  # the default, stated on purpose: samples must vary
        messages=[{"role": "user", "content": f"{question}\n\nState:\n{state}"}],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {"value": schema},
                    "required": ["value"],
                    "additionalProperties": False,
                },
            }
        },
    )
    text = next(b.text for b in response.content if b.type == "text")
    return json.dumps(json.loads(text)["value"], sort_keys=True)  # normalise for voting

def decide(schema: dict, question: str, state: str) -> dict:
    with ThreadPoolExecutor(max_workers=SAMPLES) as pool:
        futures = [pool.submit(_ask_once, schema, question, state) for _ in range(SAMPLES)]
        answers = [f.result() for f in futures]
    winner, votes = Counter(answers).most_common(1)[0]
    return {"value": json.loads(winner), "confidence": votes / SAMPLES}

if __name__ == "__main__":
    print(decide(
        schema={"type": "string", "enum": ["billing", "technical", "account", "other"]},
        question="Which team should handle this support ticket?",
        state="My card was charged twice for the same invoice this month.",
    ))
```

## Cách làm này khác gì so với một mô hình System One thực thụ

Hãy nhìn nhận thật tỉnh táo về khoảng cách giữa hai bên. Jev là mô hình phi tự hồi quy và trả lời cả một loạt câu hỏi chỉ trong một lượt chạy song song duy nhất; trong khi cách làm trên tốn năm lệnh gọi sinh văn bản cho mỗi câu hỏi. Độ tự tin của Jev là xác suất đã được hiệu chuẩn thông qua huấn luyện RLCD; còn của chúng ta là phép đếm phiếu bầu chỉ nhận sáu giá trị rời rạc và không nói lên điều gì về độ hiệu chuẩn. Độ trễ ở đây rơi vào khoảng một đến hai giây so với con số công bố 70–500ms của Jev, và mỗi quyết định tiêu tốn năm lệnh gọi Haiku so với mức giá \$0.042 trên mỗi triệu token. Thứ giữ nguyên không đổi sau khi hoán đổi chính là bản hợp đồng giao tiếp (contract) — và đó mới là phần duy nhất mà mã nguồn ứng dụng của bạn phụ thuộc vào. Tiếp theo: [bộ định tuyến có ngưỡng tự tin](build-router.md).
