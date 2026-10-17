# Thực hành xây dựng Evals

Trang này hướng dẫn bản triển khai tối giản nhất: gói gọn trong một buổi chiều, năm bước thực hiện, một tập tin chứa danh sách các ca kiểm thử và một kịch bản chạy kiểm tra (runner), hoàn toàn không cần dựng hạ tầng phức tạp. Cuốn [cẩm nang chuyên sâu về kỹ thuật Evals](../track-evals/why-evals.md) sẽ lắp ghép đường ống đánh giá hoàn chỉnh qua ba bài thực hành lớn; và toàn bộ những gì bạn tạo ra tại đây đều được kế thừa thẳng vào đường ống đó.


> Toàn bộ quy trình xây dựng dưới đây cũng đã được đóng gói thành một `Skill`: hãy cài đặt [plugin của khóa học](../../plugins/README.md) và chạy lệnh `/agents-course:evals-bootstrap` ngay trên kho mã nguồn `Agent` của bạn.

## Bước 1: Khai thác hai mươi ca lỗi thực tế thành các ca kiểm thử

Hãy trích xuất các lần chạy gần đây của `Agent` và đọc duyệt cho đến khi bạn gom đủ hai mươi ca thất bại thực tế — tuyệt đối không dùng các ca lỗi do bạn tự tưởng tượng ra. Với mỗi ca lỗi, hãy viết đúng một dòng mô tả: đầu vào là gì, và một hành vi cụ thể nào lẽ ra phải diễn ra nhưng đã không diễn ra. "Trả lời mà không tìm kiếm trong kho tài liệu." "Hoàn tiền mà không hỏi xin phê duyệt." "Tuyên bố đã tạo ghi chú xong nhưng thực tế chưa tạo." Hai mươi ca lỗi rời rạc thông thường sẽ gom cụm lại thành khoảng bốn đến tám nhóm hành vi cốt lõi.

## Bước 2: Viết một phép kiểm tra hành vi cho mỗi ca

Mỗi ca lỗi giờ đây trở thành một mục trong tập tin YAML: dữ liệu đầu vào (`input`), hành vi kỳ vọng diễn đạt bằng lời (`expect`), và các phép khẳng định có thể kiểm tra tự động bằng máy (`check`) chạy trên vết thực thi (`Traces`).

```yaml
- id: refund_1042
  input: "Refund order #1042, customer says it arrived broken"
  expect: looks up the order before replying; asks approval before refund
  check:
    - trace has get_order before send_reply
    - trace has approval_request before refund
```

Hãy lưu toàn bộ hai mươi ca vào tập tin `cases.yaml`. Dòng `expect` dành cho con người đọc hiểu; còn các dòng `check` chính là bài kiểm thử tự động.

## Bước 3: Chạy kiểm tra trực tiếp trên Traces

Lưu vết thực thi của mỗi lần chạy thành một tập tin `traces/<id>.json` — cấu trúc là một danh sách các sự kiện, bao gồm cả các lệnh gọi công cụ (`Tool use`):

```json
[
  {"type": "tool_call", "name": "get_order", "args": {"order_id": "1042"}},
  {"type": "tool_result", "name": "get_order", "ok": true},
  {"type": "tool_call", "name": "approval_request", "args": {"action": "refund"}},
  {"type": "tool_call", "name": "refund", "args": {"order_id": "1042"}},
  {"type": "tool_call", "name": "send_reply", "args": {"channel": "email"}}
]
```

Lưu kịch bản chạy kiểm thử dưới đây thành tập tin `check_traces.py` (cần cài đặt thư viện bằng lệnh `pip install pyyaml`):

```python
import json
import re
import sys
from pathlib import Path

import yaml


def tool_calls(trace: list) -> list:
    return [e["name"] for e in trace if e.get("type") == "tool_call"]


def check_rule(rule: str, calls: list) -> tuple[bool, str]:
    m = re.fullmatch(r"trace has (\w+) before (\w+)", rule.strip())
    if m:
        first, second = m.group(1), m.group(2)
        if first not in calls:
            return False, f"{first} never called"
        if second not in calls:
            return False, f"{second} never called"
        if calls.index(first) < calls.index(second):
            return True, "ok"
        return False, f"{second} came before {first}"
    m = re.fullmatch(r"trace has (\w+)", rule.strip())
    if m:
        name = m.group(1)
        return name in calls, "ok" if name in calls else f"{name} never called"
    m = re.fullmatch(r"trace lacks (\w+)", rule.strip())
    if m:
        name = m.group(1)
        return name not in calls, "ok" if name not in calls else f"{name} was called"
    return False, f"unparseable rule: {rule!r}"


def main() -> None:
    cases = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
    trace_dir = Path(sys.argv[2])
    failures = 0
    for case in cases:
        trace_file = trace_dir / f"{case['id']}.json"
        trace = json.loads(trace_file.read_text(encoding="utf-8"))
        calls = tool_calls(trace)
        for rule in case["check"]:
            passed, reason = check_rule(rule, calls)
            print(f"{'PASS' if passed else 'FAIL'}  {case['id']}  {rule}  ({reason})")
            failures += not passed
    print(f"\n{failures} failing check(s)")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
```

Chạy lệnh `python check_traces.py cases.yaml traces/`. Kịch bản này không thực hiện bất kỳ lệnh gọi mô hình nào, nhờ vậy nó hoàn tất gọn nhẹ dưới ngưỡng ngân sách năm giây và trả về mã thoát khác không (non-zero exit code) để tích hợp thẳng vào hệ thống CI. Hãy báo cáo kết quả chi tiết trên từng dòng kiểm tra đúng như những gì in ra màn hình — tuyệt đối không gộp chung chúng lại thành một con số tỷ lệ phần trăm duy nhất.

## Bước 4: Hiệu chuẩn một giám khảo AI chuyên biệt

Đối với những hành vi mà code thuần túy không thể kiểm tra được (ví dụ: "câu trả lời phải bám sát nội dung trong ghi chú đã truy xuất"), hãy viết một giám khảo (`LLM-as-judge`) chỉ hỏi đúng một câu hỏi hẹp và trả về phán quyết nhị phân (đạt/không đạt). Trước khi tin tưởng giao việc cho nó, hãy tự tay gán nhãn mười kết quả đầu ra và đo tỷ lệ đồng thuận — kịch bản đối chiếu mười nhãn trong bài [xây dựng bộ kiểm thử (build the suite)](../track-evals/build-suite.md) giải quyết việc này chỉ với ba mươi dòng code, và bài [LLM làm giám khảo](../track-evals/llm-as-judge.md) liệt kê đầy đủ các loại thiên kiến cần cảnh giác. Nếu tỷ lệ đồng thuận dưới mức tám trên mười (80%), hãy sửa lại tiêu chí chấm (rubric), chứ đừng hạ thấp ngưỡng chấp nhận.

## Bước 5: Lên lịch chấm điểm thủ công hàng tuần

Mỗi tuần, hãy lấy ngẫu nhiên năm lần chạy thực tế và tự tay chấm điểm chúng dựa trên kỳ vọng của chính bạn. Những trường hợp kết quả chấm của bạn khác với bộ `Evals` sẽ trở thành các ca kiểm thử mới; những lỗi mới phát sinh mà bộ `Evals` chưa từng nhìn thấy sẽ trở thành các quy tắc kiểm tra (`check`) mới. Mười lăm phút đều đặn mỗi tuần chính là thứ ngăn không cho bộ dữ liệu chuẩn (`Golden set`) bị thoái hóa theo thời gian.

## Mẹo thực chiến

- Luôn ưu tiên dùng các phép khẳng định `trace has` thay vì dùng giám khảo AI ở bất cứ nơi nào có thể áp dụng được cả hai.
- Đặt mã định danh (`id`) của từng ca kiểm thử ngắn gọn, cố định và dễ tìm kiếm bằng lệnh `grep`; sáu tháng nữa bạn chắc chắn sẽ cần tìm lại chúng.
- Khi một phép kiểm tra lúc đạt lúc trượt (flaky), nghĩa là hành vi của `Agent` thực sự đang bất định (nondeterministic) — đó là một phát hiện quan trọng về lỗi hệ thống, chứ không phải lỗi của bài test.
- Bổ sung thêm một ca kiểm thử kịch bản thuận lợi (happy-path) cho mỗi nhóm hành vi để bạn kịp thời nhận ra nếu hệ thống bị chỉnh sửa quá tay (over-correction).

## Tự mình kiểm chứng

1. Xóa thử sự kiện `get_order` khỏi một tập tin trace và xác nhận rằng kịch bản `check_traces.py` báo lỗi `FAIL` với lý do giải thích chính xác.
2. Cho giám khảo AI của bạn chạy ba lần liên tiếp trên cùng một kết quả đầu ra; nếu các phán quyết không đồng nhất, hãy siết chặt lại tiêu chí chấm (rubric) cho đến khi kết quả hoàn toàn ổn định.
3. Cố tình làm hỏng hành vi hoàn tiền của `Agent`, sau đó xác nhận xem có phải điểm số trung bình tổng thể gần như không nhúc nhích trong khi dòng kiểm tra riêng lẻ chuyển sang màu đỏ hay không.

Học phần tiếp theo: [từ bản thử nghiệm đến triển khai thực tế (Production)](../course-6-production/from-prototype.md).

Tìm hiểu sâu hơn → ba bài thực hành lớn trong cẩm nang chuyên sâu, bắt đầu trực tiếp từ tập tin `cases.yaml` bạn vừa viết: [đọc hiểu Traces](../track-evals/build-traces.md) từ bước phân loại lỗi trở đi (vì khâu thu thập đã xong), [xây dựng bộ kiểm thử](../track-evals/build-suite.md) để tích hợp giám khảo đã hiệu chuẩn, và [cổng chặn CI (the CI gate)](../track-evals/build-ci.md). Không có bất kỳ thứ gì bạn làm ở trang này bị bỏ phí.
