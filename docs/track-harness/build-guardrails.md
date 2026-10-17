# Thực hành: Phân quyền và ngữ cảnh (Guardrails)

[Phần một](build-the-loop.md) đã mang lại cho bạn một bản demo chạy được: một `Agent` chạy bất cứ lệnh gì nó thích và làm phình to biên bản hội thoại không giới hạn. Phần này sẽ lắp thêm ba mảnh ghép biến nó thành một bộ `Harness` thực thụ — một cổng kiểm soát quyền hạn (permission gate), một ngân sách ngữ cảnh (context budget), và một điều kiện dừng (stop condition). Trang [cấu trúc giải phẫu](what-a-harness-is.md) đã gọi đây là những bộ phận cho phép bạn yên tâm để mặc một Agent tự chạy mà không cần ngồi canh; ở đây chúng chỉ tốn của bạn khoảng tám mươi dòng mã.

Toàn bộ những gì từ phần một — các câu lệnh import, danh sách `TOOLS`, hàm `read_file`, `run_command` — đều được giữ nguyên. Hãy thay thế hai hàm `execute` và `agent`, đồng thời bổ sung thêm các hàm dưới đây.

## Mã nguồn triển khai

```python
MAX_TURNS = 30
CONTEXT_BUDGET = 100_000  # characters, roughly 25k tokens

ALLOWLIST = ["ls", "pwd", "cat", "head", "grep", "find",
             "git status", "git diff", "git log", "python", "pytest"]


def permitted(command):
    command = command.strip()
    if any(command == entry or command.startswith(entry + " ") for entry in ALLOWLIST):
        return True
    answer = input(f"\nAgent wants to run: {command}\nAllow? [y/N] ")
    return answer.strip().lower() in ("y", "yes")


def execute(name, tool_input):
    if name == "read_file":
        return read_file(tool_input["path"])
    if name == "run_command":
        if not permitted(tool_input["command"]):
            return "The user declined to run this command. Try another approach or ask them why."
        return run_command(tool_input["command"])
    raise ValueError(f"unknown tool: {name}")


def size_of(message):
    content = message["content"]
    if isinstance(content, str):
        return len(content)
    return sum(len(json.dumps(b)) if isinstance(b, dict) else len(b.model_dump_json())
               for b in content)


def describe(message):
    content = message["content"]
    if isinstance(content, str):
        return content[:150]
    parts = []
    for block in content:
        if isinstance(block, dict):
            parts.append(f"tool output, {len(json.dumps(block))} chars")
        elif block.type == "text":
            parts.append(block.text[:150])
        elif block.type == "tool_use":
            parts.append(f"ran {block.name}({json.dumps(block.input)[:100]})")
    return "; ".join(parts) or "(empty turn)"


def enforce_budget(messages, summaries):
    while sum(size_of(m) for m in messages) > CONTEXT_BUDGET and len(messages) > 5:
        summaries.append(describe(messages.pop(1)))
        summaries.append(describe(messages.pop(1)))


def with_summary(messages, task, summaries):
    if not summaries:
        return messages
    header = (task + "\n\n[Older turns were removed to fit the context budget. "
              "Summary of what happened in them:\n- " + "\n- ".join(summaries) + "]")
    return [{"role": "user", "content": header}] + messages[1:]


def agent(task):
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": task}]
    summaries = []
    for turn in range(MAX_TURNS):
        enforce_budget(messages, summaries)
        response = client.messages.create(
            model=MODEL, max_tokens=8000, system=SYSTEM, tools=TOOLS,
            messages=with_summary(messages, task, summaries),
        )
        for block in response.content:
            if block.type == "text":
                print(block.text)
        if response.stop_reason != "tool_use":
            return
        messages.append({"role": "assistant", "content": response.content})
        results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            print(f"-> {block.name} {json.dumps(block.input)}")
            try:
                results.append({"type": "tool_result", "tool_use_id": block.id,
                                "content": execute(block.name, block.input)})
            except Exception as exc:
                results.append({"type": "tool_result", "tool_use_id": block.id,
                                "content": f"Error: {exc}", "is_error": True})
        messages.append({"role": "user", "content": results})
    print("Stopped: hit the turn limit without finishing.")
```

## Cổng kiểm soát quyền hạn (The permission gate)

Các câu lệnh chỉ-đọc nằm trong danh sách cho phép (`ALLOWLIST`) sẽ được chạy êm thấm không cần hỏi; bất kỳ câu lệnh nào khác đều phải xin phép bạn qua hàm `input()`. Nếu bạn từ chối, lời từ chối sẽ được gửi trả lại cho mô hình như một kết quả công cụ thông thường chứ không quăng ra ngoại lệ (exception) làm sập chương trình — mô hình sẽ đọc thông báo đó như một dữ kiện đầu vào và tự điều chỉnh hướng đi. Hãy lưu ý sự thẳng thắn cần thiết ở đây: cách khớp tiền tố chuỗi như trên vẫn có lỗ hổng (ví dụ lệnh `git diff; rm -rf ~` vẫn bắt đầu bằng `git diff `), đó là lý do vì sao các bộ `Harness` thực tế phải phân tích cú pháp cây câu lệnh shell đàng hoàng và đồng thời nhốt quá trình thực thi vào trong môi trường hộp cát (sandbox). Cổng gác nhỏ này dạy cho bạn hình hài kiến trúc của `Guardrails`, chứ chưa phải là một giải pháp bảo mật hoàn chỉnh.

## Ngân sách ngữ cảnh (The context budget)

Khi biên bản hội thoại vượt quá ngân sách ký tự cho phép, các lượt trao đổi cũ nhất ngay sau yêu cầu gốc sẽ bị cắt bỏ theo từng cặp — gồm lượt trả lời của assistant đi kèm với lượt kết quả công cụ tương ứng, nhằm đảm bảo không có khối `tool_use` nào bị mồ côi mất cặp — đồng thời một dòng tóm tắt ngắn gọn của mỗi lượt bị xóa sẽ được nối vào bản tóm tắt tích lũy nằm ngay trong tin nhắn đầu tiên. Cách làm này tuy thô sơ nhưng hoàn toàn có chủ đích: đầu ra của công cụ thường rất cồng kềnh và hiếm khi cần đọc lại nguyên văn, khớp chính xác với sự đánh đổi đã được phân tích trong bài [Context engineering](context-engineering.md).

## Điều kiện dừng (The stop condition)

Hằng số `MAX_TURNS` đặt ra mức trần bảo vệ hóa đơn tiền túi của bạn khi mô hình bị kẹt trong vòng lặp vô tận trước một tác vụ mà nó không thể hoàn thành. Mọi bộ `Harness` thực tế đều có chốt chặn này; và bất kỳ người xây dựng hệ thống nào cũng từng quên nó ít nhất một lần.

Giờ đây bạn đã có trong tay một bộ `Harness` thu nhỏ hoàn chỉnh. Những gì nó vẫn còn thiếu — và khi nào những khoảng trống đó thực sự trở thành vấn đề — sẽ được mổ xẻ ở [phần ba](build-graduate.md).
