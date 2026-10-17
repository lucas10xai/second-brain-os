# Thực hành: Bộ định tuyến (Router) có ngưỡng tự tin

[Điểm cuối quyết định định kiểu](build-decision-endpoint.md) phát huy trọn vẹn giá trị khi được đặt ngay phía trước một Agent. Mẫu thiết kế này, như đã mô tả trong bài [Jev trong ngăn xếp Agent](jev-in-an-agent-stack.md), vận hành như sau: phân loại yêu cầu đi vào với chi phí rẻ, hành động trực tiếp ngay khi bộ phân loại đủ tự tin, và chỉ chuyển tiếp (fall through) xuống mô hình LLM đầy đủ khi độ tự tin không đạt ngưỡng. Đầu ra quyết định đóng vai trò là luồng xử lý nhanh (fast path), chứ không bao giờ là luồng duy nhất.

## Thiết kế cốt lõi

Ba quy tắc gánh vác toàn bộ công việc:

- Mọi tuyến (route) có sẵn hàm xử lý tất định (deterministic handler) đều có thể được phục vụ ngay mà không cần chạm tới mô hình lớn.
- Luồng xử lý nhanh chỉ kích hoạt khi độ tự tin vượt qua ngưỡng quy định *và* tuyến đó có hàm xử lý. Mọi trường hợp còn lại đều chảy xuống mô hình lớn.
- Mọi quyết định đều được ghi vào nhật ký (log), bất kể đi theo luồng nhanh hay chuyển tiếp. Tệp nhật ký này chính là bộ dữ liệu đánh giá (eval set) trong tương lai của bạn: một khi bạn có nhãn của con người cho các phiếu hỗ trợ này, bạn có thể đo lường độ chính xác của bộ phân loại, tinh chỉnh ngưỡng tự tin dựa trên chi phí sai sót thực tế, và sau này đem so sánh trực tiếp với câu trả lời của Jev trên cùng đầu vào.

## Mã nguồn triển khai

Đoạn mã dưới đây có thể chạy trực tiếp ngay khi đặt cùng thư mục với tệp `decision.py` từ trang trước.

```python
# router.py
import json
import time

import anthropic

from decision import decide

client = anthropic.Anthropic()
FULL_MODEL = "claude-opus-5"   # the fall-through: full-strength, full price
THRESHOLD = 0.8                # start conservative; tune against labels later
LOG_PATH = "decisions.jsonl"

# Routes with a handler get a fast path. "other" is a deliberate catch-all
# with no handler, so anything unfamiliar always falls through.
ROUTES = {
    "billing": lambda t: "Routed to billing queue with a receipt request.",
    "password_reset": lambda t: "Sent the automated password-reset link.",
    "cancellation": lambda t: "Escalated to a human retention agent.",
    "other": None,
}
ROUTE_SCHEMA = {"type": "string", "enum": list(ROUTES)}
QUESTION = "Which route should handle this support ticket?"

def log_decision(entry: dict) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def fall_through(ticket: str) -> str:
    response = client.messages.create(
        model=FULL_MODEL,
        max_tokens=16000,
        messages=[{"role": "user", "content": f"Handle this support ticket:\n{ticket}"}],
    )
    return next(b.text for b in response.content if b.type == "text")

def handle(ticket: str) -> str:
    start = time.perf_counter()
    decision = decide(ROUTE_SCHEMA, QUESTION, ticket)
    decide_ms = round((time.perf_counter() - start) * 1000)

    handler = ROUTES.get(decision["value"])
    fast = handler is not None and decision["confidence"] >= THRESHOLD
    outcome = handler(ticket) if fast else fall_through(ticket)

    log_decision({
        "ts": time.time(),
        "ticket": ticket,
        "value": decision["value"],
        "confidence": decision["confidence"],
        "threshold": THRESHOLD,
        "path": "fast" if fast else "fall_through",
        "decide_ms": decide_ms,
    })
    return outcome

if __name__ == "__main__":
    print(handle("I was charged twice for the same invoice this month."))
    print(handle("Your app deleted three years of my data and I am furious."))
```

## Những điểm cần theo dõi

Ngưỡng tự tin (threshold) là một quyết định kinh doanh chứ không phải quyết định mô hình hóa — hãy định giá nó bằng chi phí thiệt hại khi luồng nhanh hành động sai, theo đúng nguyên tắc thảo luận về ngưỡng ở bài trước. Với bản đóng thế tạm thời này, hãy nhớ rằng độ tự tin chỉ là tỷ lệ đồng thuận giữa các mẫu thử chứ không phải xác suất đã hiệu chuẩn: chuyện cả năm mẫu thử cùng đồng thuận sai trên một phiếu hỗ trợ mơ hồ là rất bình thường, vì vậy hãy luôn giữ lại tuyến vét cạn (`other`) và kiểm toán tệp nhật ký hàng tuần đối chiếu với phán đoán của con người trước khi hạ thấp ngưỡng. Thứ duy nhất tuyệt đối không được bỏ qua là việc ghi nhật ký. Khi bạn được cấp quyền truy cập Jev, tệp tin lưu trữ đầu vào, quyết định và độ tự tin này chính là thứ bạn sẽ phát lại (replay) qua Jev — và đó cũng là nội dung của trang tiếp theo: [hoán đổi sang Jev](build-swap-in-jev.md).
