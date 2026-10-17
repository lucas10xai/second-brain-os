# Thực hành: Bài kiểm tra mục tiêu (Build: the Goal Test)

Ba trang thực hành sẽ lắp ráp một `Loop` hoàn chỉnh bao quanh một coding `Agent` chạy ngầm (headless). Trang đầu tiên này cung cấp bộ khung xương: định nghĩa trạng thái hoàn thành dưới dạng một script, chạy `Agent`, chạy bài kiểm tra mục tiêu (goal test), đưa các lỗi ngược trở lại và giới hạn số lần thử. Các ví dụ dưới đây điều khiển chế độ không tương tác của `Claude Code` (`claude -p`) — `Harness` tham chiếu từ [sổ tay `Harness`](../track-harness/claude-code-as-harness.md) — nhưng bất kỳ CLI `Agent` nào nhận prompt và sửa tệp tin đều có thể lắp vào tương tự.

Bạn cần cài sẵn `claude` và `jq` trong `PATH`, cùng một kho mã nguồn có sẵn bộ test. Các cờ (flags) dưới đây được cập nhật tính đến tháng 9 năm 2026: `-p` chạy một phiên không tương tác, `--allowedTools` phê duyệt trước các công cụ bằng cú pháp quy tắc phân quyền (dấu ` *` ở cuối là khớp tiền tố), `--permission-mode acceptEdits` cho phép ghi tệp tin mà không hỏi lại, và `--output-format json` trả về kết quả kèm dữ liệu đặc tả (metadata) bao gồm cả `total_cost_usd`.

## Định nghĩa hoàn thành dưới dạng một script

Bài kiểm tra mục tiêu chính là toàn bộ bản thiết kế. Nó phải thực thi được, cho kết quả nhị phân (đạt/trượt) và nằm ngoài tầm kiểm soát của `Agent` — ở đây là chạy test cộng với lint:

```bash
#!/usr/bin/env bash
# goal-loop.sh — run a coding agent until the goal test passes or attempts run out.
set -u

TASK="Make every test under tests/ pass. Do not delete, skip or weaken any test."
MAX_ATTEMPTS=5

goal_test() {
    python -m pytest -q --tb=short && ruff check .
}

feedback=""
attempt=1
while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
    echo "=== attempt $attempt of $MAX_ATTEMPTS ==="

    prompt="$TASK"
    if [ -n "$feedback" ]; then
        prompt="$TASK

The previous attempt failed the goal test with this output:
$feedback

Fix these specific failures."
    fi

    claude -p "$prompt" \
        --allowedTools "Read,Edit,Bash(python -m pytest *),Bash(ruff *)" \
        --permission-mode acceptEdits \
        --output-format json | jq -r '.total_cost_usd as $c | "agent done (cost $\($c))"'

    if feedback=$(goal_test 2>&1); then
        echo "PASS: goal test green on attempt $attempt"
        exit 0
    fi
    echo "FAIL: goal test still red"
    attempt=$((attempt + 1))
done

echo "STOP: $MAX_ATTEMPTS attempts spent; handing back to the human"
exit 1
```

Hãy lưu tệp lại, chạy `chmod +x goal-loop.sh`, thực thi nó trong một kho mã nguồn đang có test lỗi, và quan sát nó hội tụ hoặc dừng lại.

## Lý do tồn tại của từng mảnh ghép

**Bài kiểm tra mục tiêu chạy trong script bọc ngoài, không phải trong `Agent`.** Bản thân `Agent` cũng chạy pytest trong lúc làm việc — điều đó hoàn toàn ổn, đó là cách nó định hướng. Nhưng phán quyết kết thúc `Loop` phải đến từ shell của bạn, trong một tiến trình mà mô hình không bao giờ chạm tới. Đây chính là quy tắc "tự kiểm tra, không bao giờ hỏi" từ bài [bộ phản biện và xác minh](critics-and-verification.md) ở hình thái nhỏ gọn nhất.

**Đầu ra lỗi là thứ duy nhất được mang sang vòng sau.** Mỗi lần thử là một phiên `claude -p` mới tinh: ngữ cảnh sạch, tác vụ gốc và bằng chứng chưng cất về những gì vẫn đang sai. Không có bản ghi hội thoại nào về sự bối rối của lần thử trước đi theo nó — đúng với lập luận ngữ cảnh mới cho mỗi lần thử trong bài [vệ sinh ngữ cảnh (`Context hygiene`)](context-hygiene.md).

**Giới hạn nhỏ và mã thoát trung thực.** Năm lần thử, sau đó thoát với mã `exit 1` cùng một thông báo rõ ràng. Điều này giúp script có tính khả ghép (composable): CI có thể đặt `Gate` dựa trên nó, cron có thể gửi cảnh báo từ nó, và hai trang thực hành tiếp theo có thể bọc lấy nó.

## Những gì vòng lặp này chưa làm được

`Loop` này chấp nhận bất cứ thứ gì làm cho bộ test chuyển xanh. Một `Agent` vượt qua bài test bằng những thủ đoạn xấu xí — code chết, nuốt lỗi im lặng, hoặc một thay đổi lén lút nằm ngay ngoài tầm phủ của bộ test — vẫn sẽ lọt qua trót lọt. Phần hai sẽ bổ sung một vị thẩm phán cho chính vấn đề đó: [Thực hành: Bộ phản biện (`Critic`)](build-critic.md).
