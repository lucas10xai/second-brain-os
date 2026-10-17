# Thực hành: Vòng lặp chạy qua đêm (Build: the Overnight Loop)

Bản dựng cuối cùng sẽ chạy tự động không cần người giám sát. Mọi nguyên tắc từ [phần một và phần hai](build-goal-test.md) vẫn được giữ nguyên; điều thay đổi là không có ai ngồi canh, vì vậy các thanh ray an toàn phải làm cho kịch bản tệ nhất trở nên nhàm chán: một ngân sách giới hạn số vòng lặp, một chốt chặn một chiều (ratchet) dừng phiên chạy ngay khoảnh khắc tiến độ chững lại, một bản báo cáo buổi sáng viết bằng markdown, và git đóng vai trò lưới an toàn — chạy trên nhánh riêng, `reset --hard` ngay khi có suy thoái (regression), và tuyệt đối không bao giờ tự động `push`.

Trái tim của hệ thống là cơ chế ratchet. Mỗi vòng lặp bắt buộc phải vượt qua điểm số tốt nhất trước đó — ở đây là số lượng bài test vượt qua — nếu không `Loop` sẽ khôi phục (reset) lần thử đó và dừng lại ngay. Hoặc tiến lên đơn điệu, hoặc không gì cả; một `Loop` được phép đi ngang suốt đêm chắc chắn sẽ đi ngang suốt đêm. Lý giải chi tiết nằm ở bài [điều kiện dừng (`Stop condition`)](stop-conditions.md).

## Mã nguồn thực thi

```python
#!/usr/bin/env python3
"""overnight.py — unattended agent loop: budgeted, ratcheted, reported."""
import datetime
import json
import pathlib
import re
import subprocess

TASK = ("Open TODO.md. Implement the top unchecked item, add tests for it, "
        "and tick the item off. Do not delete, skip or weaken any existing test.")
MAX_ITERATIONS = 10
RATCHET = pathlib.Path("ratchet.json")
REPORT = pathlib.Path("MORNING-REPORT.md")


def sh(cmd, timeout=2400):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True,
                          timeout=timeout)


def score():
    """Progress metric: tests passing. Higher is better; it must never fall."""
    out = sh("python -m pytest -q --tb=no").stdout
    m = re.search(r"(\d+) passed", out)
    return int(m.group(1)) if m else 0


def main():
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    sh(f"git checkout -b overnight/{stamp}")  # rail 1: own branch, never pushed
    best = score()
    RATCHET.write_text(json.dumps({"best": best}))
    lines = [f"# Overnight report {stamp}", "",
             f"Baseline: {best} tests passing.", ""]

    for i in range(1, MAX_ITERATIONS + 1):
        sh('claude -p "{}" '
           '--allowedTools "Read,Edit,Bash(python -m pytest *)" '
           '--permission-mode acceptEdits '
           '--permission-prompts none'.format(TASK))
        now = score()
        if now > best:
            best = now
            RATCHET.write_text(json.dumps({"best": best}))
            sh(f'git add -A && git commit -m "overnight {i}: {now} passing"')
            lines.append(f"- iteration {i}: improved to {now} passing, committed")
        else:
            sh("git reset --hard")            # rail 2: a bad attempt never survives
            lines.append(f"- iteration {i}: {now} passing, no improvement; stopped")
            break
    else:
        lines.append(f"- iteration budget of {MAX_ITERATIONS} spent")

    lines += ["", f"Final: {best} passing on branch overnight/{stamp}. "
                  "Nothing was pushed; review and merge by hand."]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
```

Hãy chạy `python overnight.py` trước khi đi ngủ; và đọc `MORNING-REPORT.md` bên tách cà phê sáng hôm sau.

## Giải phẫu các thanh ray an toàn

**Tạo nhánh riêng, commit, không bao giờ push.** Mọi bước tiến đều được commit trên nhánh `overnight/<stamp>`, nhờ vậy quyết định vào buổi sáng chỉ đơn giản là một buổi duyệt code (code review) bình thường trên một nhánh bình thường. Script không chứa lệnh push nào và `Agent` hoàn toàn không có quyền chạy lệnh git — cờ `--allowedTools` của nó chỉ bao gồm quyền đọc, sửa tệp và chạy pytest, ngoài ra không còn gì khác. Cờ `--permission-prompts none` báo cho `Harness` biết không có ai trực máy: bất kỳ thao tác nào đòi hỏi hỏi ý kiến người dùng đều bị từ chối ngay thay vì treo máy chờ đến bình minh.

**Khôi phục cứng khi suy thoái (Reset on regression).** Khi điểm số không cải thiện được thêm, lệnh `git reset --hard` sẽ hủy bỏ ngay lần thử đó trước khi dừng vòng lặp. Kết hợp với cơ chế ratchet, tính bất biến (invariant) đạt được rất mạnh: nhánh làm việc chỉ chứa những trạng thái tốt hơn một cách đo lường được so với trạng thái trước đó, điều giúp bạn tin tưởng vào bản báo cáo mà không cần đọc lại từng dòng diff của các lần thử hỏng.

**Bản báo cáo chính là hộp thư.** Các `Loop` chạy không người giám sát sẽ mắc những sai lầm không người giám sát; bản báo cáo là nơi chúng lộ diện qua từng vòng lặp, kèm theo thông tin về chiếc phanh đã kích hoạt. Giữa các vòng lặp, chỉ có `TODO.md` và tệp ratchet được lưu giữ lại — một sự chủ đích tuân theo đúng nguyên lý [vệ sinh ngữ cảnh (`Context hygiene`)](context-hygiene.md). Mỗi phiên làm việc thức dậy từ trạng thái lạnh, đọc danh sách việc cần làm và thực hiện đúng một công việc có ranh giới rõ ràng.
