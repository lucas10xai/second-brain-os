# Thực hành: Hoán đổi sang Jev

Mục đích của hai trang trước là làm cho trang này trở nên đơn giản đến mức nhàm chán. [Điểm cuối quyết định](build-decision-endpoint.md) và [bộ định tuyến (Router)](build-router.md) đã thống nhất với nhau trên một bản hợp đồng giao tiếp duy nhất — hàm `decide(schema, question, state)` trả về một giá trị kèm độ tự tin — nhờ đó việc thay thế bản đóng thế dùng LLM bằng Jev chỉ là thao tác sửa một tệp duy nhất, chứ không phải viết lại từ đầu. Việc bạn đã có thể thực hiện bước chuyển đổi này ngay hay chưa phụ thuộc vào danh sách chờ; xem tình trạng cấp quyền truy cập hiện tại ở bài [bắt đầu với Jev](getting-started.md).

## Đường khớp nối (The seam)

Hãy cung cấp cho Router một điểm nhập (import) duy nhất không gắn cứng với bất kỳ cách triển khai cụ thể nào. Tệp dưới đây là nơi duy nhất cần thay đổi về sau:

```python
# decider.py — the seam. Swapping implementations is an edit here, nowhere else.
from decision import decide  # today: the LLM stand-in

# from jev_decider import decide  # later: Jev, once access arrives
```

Chỉ cần đổi dòng import trong `router.py` thành `from decider import decide` là quá trình hoán đổi đã sẵn sàng vào bệ phóng. Ở phía Jev, mã nguồn sẽ ánh xạ các hình thái lược đồ (schema) sang các kiểu nguyên thủy tương ứng — danh sách liệt kê (`enum`) trở thành `Choice`, kiểu logic (`boolean`) trở thành `Noul`, và bất kỳ kiểu đầu ra mở nào khác đều bị từ chối thẳng, bởi Jev chỉ trả lời các câu hỏi có phạm vi hữu hạn:

```python
# jev_decider.py — written from TypeSafe's published docs, UNTESTED until you
# have quota. Verify call shapes against docs.typesafe.ai before relying on it.
from typesafe import TypeSafe, Choice, Noul  # pip install typesafe-sdk

client = TypeSafe()  # reads TYPESAFE_API_KEY

def decide(schema: dict, question: str, state: str) -> dict:
    if "enum" in schema:
        q = Choice(instructions=question,
                   criteria={str(o): str(o) for o in schema["enum"]})
    elif schema.get("type") == "boolean":
        q = Noul(instructions=question)
    else:
        raise ValueError("Jev answers bounded questions only; keep this on the LLM.")
    answer = client.decide(state=state, questions={"value": q})["value"]
    return {"value": answer.value, "confidence": answer.probability}
```

## Chạy chế độ ẩn (Shadow mode) trước

Đừng vội gạt công tắc đổi dòng import ngay trong ngày đầu tiên. Hãy cho Jev chạy ở chế độ ẩn (shadow mode): bản đóng thế LLM vẫn trả lời mọi yêu cầu thực tế, Jev âm thầm trả lời cùng yêu cầu đó ở nhánh phụ, và kết quả của cả hai cùng được ghi vào nhật ký. Nếu Jev gặp lỗi thì hệ thống thực tế (production) cũng không hề hấn gì vì chưa có luồng nghiệp vụ nào đọc câu trả lời của nó cả.

```python
# shadow.py — point the seam here during the trial period.
import json
import time

import decision as standin
import jev_decider as jev

LOG_PATH = "shadow.jsonl"

def decide(schema: dict, question: str, state: str) -> dict:
    t0 = time.perf_counter()
    live = standin.decide(schema, question, state)
    live_ms = round((time.perf_counter() - t0) * 1000)
    try:
        t1 = time.perf_counter()
        shadow = jev.decide(schema, question, state)
        shadow_ms = round((time.perf_counter() - t1) * 1000)
    except Exception as exc:
        shadow, shadow_ms = {"error": str(exc)}, None
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": time.time(), "state": state,
                            "live": live, "live_ms": live_ms,
                            "shadow": shadow, "shadow_ms": shadow_ms}) + "\n")
    return live  # callers only ever see the stand-in
```

## Những chỉ số cần đo lường trước khi chuyển hẳn

Hãy thu thập số liệu cơ sở (baseline) của bản đóng thế trong một tuần, sau đó đem so sánh trên tệp nhật ký chạy ẩn (`shadow.jsonl`):

- **Độ trễ (Latency).** Phân vị p50 và p95 của `live_ms` đối chiếu với `shadow_ms`, được đo trực tiếp từ hạ tầng mạng của bạn — chứ không phải con số quảng cáo 70–500ms của TypeSafe.
- **Chi phí (Cost).** Năm lệnh gọi Haiku cho mỗi quyết định đặt cạnh lượng token đầu vào tính phí của Jev, quy chuẩn trên mỗi một nghìn quyết định.
- **Tỷ lệ đồng thuận (Agreement rate).** Tần suất hai trường `value` khớp nhau là bao nhiêu. Tỷ lệ đồng thuận cao đi kèm độ trễ tốt hơn là tín hiệu đèn xanh để chuyển đổi; tỷ lệ đồng thuận thấp có nghĩa là một trong hai bên đã sai, và chỉ có bộ nhãn của con người mới phân xử được ai đúng ai sai.
- **Độ hiệu chuẩn (Calibration).** Gom nhóm (bucket) các mức xác suất của Jev và kiểm tra độ chính xác thực tế trong từng nhóm đối chiếu với nhãn của bạn — đây chính là bước kiểm chứng tuyên bố cốt lõi của nhà cung cấp ngay trên lưu lượng dữ liệu thực của bạn.

Hãy đổi dòng import trong `decider.py` khi các con số thực tế chứng minh nó xứng đáng, và luôn giữ bản đóng thế cách đó đúng một dấu chú thích (`#`) làm phương án quay lui (rollback) tức thì.
