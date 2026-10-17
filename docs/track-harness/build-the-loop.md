# Thực hành: Vòng lặp (Loop)

Trang [cấu trúc giải phẫu](what-a-harness-is.md) đã khẳng định phần lõi của mọi `Harness` chỉ là một vòng lặp `while`. Trang này sẽ chứng minh điều đó bằng mã nguồn thực tế. Chỉ với khoảng bảy mươi dòng mã Python, bạn sẽ có ngay một `Agent` biết đọc tệp tin và chạy các câu lệnh hệ thống thông qua Claude API trực tiếp; còn [phần tiếp theo](build-guardrails.md) sẽ lắp thêm các cơ chế bảo vệ để biến nó thành một bộ `Harness` thực thụ. Hãy dành ra một buổi tối cho trọn bộ cả ba trang thực hành, tổng cộng chỉ khoảng 150 dòng mã.

Bạn cần cài sẵn Python 3.10 trở lên, chạy `pip install anthropic` (bộ SDK nhánh 1.x), và thiết lập biến môi trường `ANTHROPIC_API_KEY`.

## Hai công cụ cơ bản

Công cụ (`Tool use`) thực chất là các lược đồ JSON cộng với các hàm xử lý tương ứng. Phần văn bản mô tả quan trọng không kém gì mã nguồn — mô hình chọn công cụ bằng cách đọc mô tả đó, một nguyên tắc mà bài [công cụ (Tools) và MCP](tools-and-mcp.md) đã phân tích rất kỹ.

## Mã nguồn triển khai

```python
import json
import subprocess
import sys

import anthropic

MODEL = "claude-opus-5"
SYSTEM = "You are a coding agent working in the current directory. Investigate before you conclude."

TOOLS = [
    {
        "name": "read_file",
        "description": "Read a text file and return its full contents. Use for source files, configs and logs. Paths are relative to the working directory.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "File path, e.g. src/main.py"}},
            "required": ["path"],
        },
    },
    {
        "name": "run_command",
        "description": "Run a shell command and return its exit code, stdout and stderr. Use for listing files, searching and running tests. Times out after 30 seconds.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string", "description": "The command, e.g. ls -la"}},
            "required": ["command"],
        },
    },
]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
    return f"exit code {result.returncode}\n{result.stdout}{result.stderr}"


def execute(name, tool_input):
    if name == "read_file":
        return read_file(tool_input["path"])
    if name == "run_command":
        return run_command(tool_input["command"])
    raise ValueError(f"unknown tool: {name}")


def agent(task):
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": task}]
    while True:
        response = client.messages.create(
            model=MODEL, max_tokens=8000, system=SYSTEM, tools=TOOLS, messages=messages
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


if __name__ == "__main__":
    agent(" ".join(sys.argv[1:]) or "List the files here and describe this project.")
```

## Từng bộ phận đang làm gì

API báo hiệu ý định tiếp theo của mô hình thông qua trường `stop_reason`. Chừng nào giá trị này còn là `tool_use`, phản hồi trả về sẽ chứa các khối `tool_use` — mỗi khối mang một định danh `id`, một tên công cụ `name` và một từ điển tham số đầu vào `input` đã được phân tích cú pháp. Bạn nối nguyên vẹn toàn bộ `response.content` của phía assistant vào lại danh sách lịch sử mà không chỉnh sửa gì (các mô hình hiện tại có kèm theo cả các khối suy nghĩ `thinking` bắt buộc phải đi cùng nhau), thực thi từng lệnh gọi công cụ, rồi gói tất cả kết quả trả về dưới dạng các khối `tool_result` nằm trong một tin nhắn `user` duy nhất, khớp nối chính xác qua mã `tool_use_id`. Nếu có lỗi xảy ra khi chạy công cụ, thông báo lỗi cũng được gửi trả lại kèm cờ `is_error: True` — một thông báo lỗi rõ ràng sẽ giúp mô hình tự sửa sai ngay ở lượt kế tiếp thay vì phải đoán mò.

Hãy lưu đoạn mã trên thành tệp `agent.py`, chạy lệnh `python agent.py "find the TODO comments in this repo and summarise them"`, và tận mắt quan sát vòng lặp (`Loop`) vận hành. Bài hướng dẫn của Thorsten Ball trong trang [tài nguyên tham khảo](resources.md) cũng làm điều tương tự bằng ngôn ngữ Go; việc nhìn thấy nó tự chạy ngay trên cửa sổ dòng lệnh của chính bạn chính là mục tiêu lớn nhất của bước này.

## Những gì nó vẫn chưa có

Đây mới chỉ là một bản demo. Nó sẽ răm rắp chạy bất kỳ câu lệnh nào mà mô hình hứng lên yêu cầu, và nếu gặp một tác vụ dài hơi thì biên bản hội thoại sẽ phình to không giới hạn. Việc khắc phục hai điểm yếu chí mạng đó — kiểm soát quyền hạn và quản lý ngữ cảnh — sẽ nằm ở [phần hai](build-guardrails.md).
