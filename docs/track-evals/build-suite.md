# Thực hành: Xây dựng bộ đánh giá (Build: the Suite)

Bạn đã có tệp `golden.jsonl` từ bài [đọc nhật ký thực thi (`Traces`)](build-traces.md). Trang này sẽ biến nó thành một bộ đánh giá có thể chạy được: chỉ một tệp Python thuần túy, không cần framework. Các phép kiểm tra bằng code sẽ chấm điểm mọi thứ chúng có thể đảm nhận; một giám khảo có tiêu chí hẹp sẽ xử lý phần còn lại, theo đúng nguyên tắc trong bài [`LLM-as-judge`](llm-as-judge.md). Đối tượng được đánh giá trong ví dụ này là một trợ lý hỗ trợ khách hàng đứng sau một prompt đơn lẻ — hãy thay hàm `run_target` bằng cách gọi ứng dụng thực tế của bạn.

## Kịch bản mã nguồn

Lưu thành tệp `eval_suite.py`. Cần chạy `pip install anthropic` và thiết lập biến môi trường `ANTHROPIC_API_KEY`. Mô hình làm giám khảo được chủ đích chọn khác với mô hình đích đang bị đánh giá.

```python
import argparse
import json
import re
import sys

import anthropic

client = anthropic.Anthropic()

TARGET_MODEL = "claude-opus-5"
JUDGE_MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = (
    "You are the support assistant for Acme Invoicing. Answer only from the "
    "provided account context. If the context does not contain the answer, say so."
)

JUDGE_PROMPT = """You are grading one output from an invoicing assistant.

Statement to verify:
{expectation}

Assistant output:
<output>
{output}
</output>

First write one or two sentences of reasoning. Then, on the final line, write
exactly VERDICT: pass if the statement is true of the output, or VERDICT: fail
if it is not. Do not reward length, politeness, or effort.
"""


def run_target(case: dict) -> str:
    response = client.messages.create(
        model=TARGET_MODEL,
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": case["input"]}],
    )
    return "".join(b.text for b in response.content if b.type == "text")


def grade_code(output: str, checks: dict) -> tuple[bool, str]:
    for needle in checks.get("must_contain", []):
        if needle.lower() not in output.lower():
            return False, f"missing required text: {needle!r}"
    for needle in checks.get("must_not_contain", []):
        if needle.lower() in output.lower():
            return False, f"contains forbidden text: {needle!r}"
    return True, "code checks passed"


def grade_judge(output: str, expectation: str) -> tuple[bool, str]:
    response = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": JUDGE_PROMPT.format(expectation=expectation, output=output),
        }],
    )
    text = "".join(b.text for b in response.content if b.type == "text")
    match = re.search(r"VERDICT:\s*(pass|fail)", text, re.IGNORECASE)
    passed = bool(match) and match.group(1).lower() == "pass"
    return passed, text.strip().splitlines()[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("golden", help="path to golden.jsonl")
    parser.add_argument("--limit", type=int, default=0, help="run only the first N cases")
    parser.add_argument("--threshold", type=float, default=0.0, help="exit 1 below this pass rate")
    args = parser.parse_args()

    with open(args.golden, encoding="utf-8") as f:
        cases = [json.loads(line) for line in f if line.strip()]
    if args.limit:
        cases = cases[: args.limit]

    results = []
    for case in cases:
        output = run_target(case)
        if case.get("checks"):
            passed, reason = grade_code(output, case["checks"])
        else:
            passed, reason = grade_judge(output, case["judge_expectation"])
        results.append({"id": case["id"], "passed": passed, "reason": reason})
        print(f"{'PASS' if passed else 'FAIL'}  {case['id']}  {reason}")

    rate = sum(r["passed"] for r in results) / len(results)
    print(f"\npass rate: {rate:.0%}")
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump({"pass_rate": rate, "results": results}, f, indent=2)
    if args.threshold and rate < args.threshold:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

Hãy chạy bằng lệnh `python eval_suite.py golden.jsonl`. Chương trình sẽ in ra một dòng cho mỗi ca kiểm thử, ghi kết quả vào `results.json`, và — khi có cờ `--threshold` — trả về mã thoát khác 0 nếu tỷ lệ đạt thấp hơn ngưỡng, đó là tất cả những gì CI cần.

## Hiệu chuẩn giám khảo trước khi tin tưởng

Trước tiên, hãy tự tay gán nhãn cho mười đầu ra cần giám khảo chấm: tạo tệp `labels.jsonl`, mỗi dòng một đầu ra gồm `id`, `output`, `expectation`, và nhãn `label` của chính bạn (`true`/`false`). Sau đó kiểm tra độ đồng thuận:

```python
import json

from eval_suite import grade_judge

with open("labels.jsonl", encoding="utf-8") as f:
    labels = [json.loads(line) for line in f if line.strip()]

agree = 0
for row in labels:
    verdict, reason = grade_judge(row["output"], row["expectation"])
    agree += verdict == row["label"]
    if verdict != row["label"]:
        print(f"disagree on {row['id']}: judge={verdict} you={row['label']} - {reason}")
print(f"agreement: {agree}/{len(labels)}")
```

Hãy đọc kỹ từng trường hợp bất đồng; thông thường là do câu mô tả kỳ vọng (`expectation`) còn mơ hồ, và đôi khi là do chính nhãn của bạn chưa chuẩn. Mười nhãn là phiên bản rút gọn trong một buổi chiều — quy trình đầy đủ với 50–100 nhãn nằm ở bài [`LLM-as-judge`](llm-as-judge.md).

## Khi nào thì một framework đáng đồng tiền bát gạo

Một tệp script này là quá đủ cho một đối tượng đích, một giám khảo và vài trăm ca kiểm thử. Hãy tìm đến `promptfoo` khi bạn muốn đặt nhiều prompt hoặc nhiều mô hình cạnh nhau để so sánh mà không muốn tự viết ma trận chạy, và tìm đến `Inspect` khi bạn cần môi trường `Agent` cô lập (sandboxed), các bộ giải (solvers) và cơ chế chấm điểm từng bước. Cả hai đều được khảo sát trong bài [công cụ đánh giá](tooling.md); không công cụ nào thay thế được công việc phân loại lỗi — chúng chỉ giúp chạy công việc đó ở quy mô lớn hơn.
