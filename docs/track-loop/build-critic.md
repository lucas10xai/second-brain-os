# Thực hành: Bộ phản biện (Build: the Critic)

[Phần một](build-goal-test.md) dừng lại khi test xanh. Phần này bổ sung tầng phán quyết thứ hai: xanh và sạch. Một lượt chạy `Critic` tách biệt sẽ duyệt qua bản diff dựa trên một bảng tiêu chí (rubric) hẹp, và danh sách khiếm khuyết mà nó chỉ ra — chứ không phải những lời khuyên chung chung — sẽ được nạp vào lần thử tiếp theo. Lý thuyết đã nằm ở bài [bộ phản biện và xác minh](critics-and-verification.md); còn đây là bốn mươi dòng code bổ sung để hiện thực hóa nó.

Hai quy tắc thiết kế gánh vác toàn bộ cơ chế này. Thứ nhất, `Critic` là một **phiên chạy tách biệt**: một lệnh gọi `claude -p` mới tinh chỉ nhìn thấy bản diff và bảng tiêu chí, không bao giờ nhìn thấy lịch sử hội thoại làm việc trước đó, nhờ vậy nó không thể bị lây nhiễm những lời tự biện minh của kẻ tạo tác. Thứ hai, bảng tiêu chí phải **hẹp và kiểm chứng được**: bốn quy tắc rõ ràng, một định dạng phán quyết bắt buộc và lệnh cấm tuyệt đối việc bình luận về bất kỳ điều gì khác.

## Mã nguồn thực thi

```bash
#!/usr/bin/env bash
# critic-loop.sh — the goal test decides correct; a critic pass decides acceptable.
set -u

TASK="Make every test under tests/ pass. Do not delete, skip or weaken any test."
MAX_ATTEMPTS=5
BASE_REF=$(git rev-parse HEAD)

goal_test() {
    python -m pytest -q --tb=short && ruff check .
}

critic() {
    git diff "$BASE_REF" | claude -p \
"You are a code reviewer. Judge this diff against exactly four rules:
1. No test was deleted, skipped or weakened.
2. No debug prints, dead code or commented-out blocks were added.
3. Errors are handled, not silently swallowed.
4. The change stays inside the task; no drive-by refactoring.
If all four hold, reply with the single word PASS.
Otherwise list each violation as: file, the problem, the one-line fix.
Judge only these rules. Never comment on style or architecture." \
        --output-format json | jq -r '.result'
}

feedback=""
for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
    echo "=== attempt $attempt of $MAX_ATTEMPTS ==="

    prompt="$TASK"
    if [ -n "$feedback" ]; then
        prompt="$TASK

The previous attempt was rejected:
$feedback

Fix exactly these points, nothing else."
    fi

    claude -p "$prompt" \
        --allowedTools "Read,Edit,Bash(python -m pytest *),Bash(ruff *)" \
        --permission-mode acceptEdits > /dev/null

    if ! feedback=$(goal_test 2>&1); then
        echo "goal test red; retrying with failures"
        continue
    fi

    verdict=$(critic)
    case "$verdict" in
        PASS*)
            echo "green and clean on attempt $attempt"
            exit 0
            ;;
        *)
            feedback="The goal test passes, but the reviewer found defects:
$verdict"
            echo "critic rejected; retrying with defects"
            ;;
    esac
done

echo "STOP: $MAX_ATTEMPTS attempts spent; handing back to the human"
exit 1
```

## Cách các mảnh ghép ăn khớp với nhau

Thứ tự thực thi ở đây cực kỳ quan trọng: kiểm tra mục tiêu trước, `Critic` sau. Chẳng có lý do gì để trả tiền đánh giá một đoạn code còn chưa chạy được, vì vậy `Critic` tất định sẽ làm màng lọc đầu tiên cho `Critic` dùng LLM — thẩm phán giá rẻ đứng trước thẩm phán đắt tiền. Bản diff được lấy so với mốc `BASE_REF` đã ghim cố định trước khi `Loop` bắt đầu, đảm bảo `Critic` luôn đánh giá tổng thể thay đổi chứ không chỉ nhìn vào phần chênh lệch của bước cuối cùng.

Hãy chú ý xem đầu ra của `Critic` biến thành thứ gì: nó trở thành biến `feedback` của lần thử tiếp theo, được đóng khung bằng mệnh lệnh "chỉ sửa chính xác những điểm này, không làm gì khác". Những khiếm khuyết cụ thể kèm vị trí tệp tin được chuyển hóa trực tiếp thành một tác vụ có ranh giới rõ ràng. Đó là lý do bảng tiêu chí cấm bình luận về phong cách code — một `Critic` khuyên "hãy cân nhắc cách tiếp cận hướng hàm (functional) hơn" sẽ đẩy lần thử tiếp theo vào một chuyến du lịch tái cấu trúc (refactoring) lan man, và năm lần thử của bạn sẽ bốc hơi trong những xáo trộn vô ích.

`Critic` này vẫn chia sẻ các kiểu lỗi chung với bất kỳ thẩm phán LLM nào — sự khoan dung quá mức, hay thiên kiến tự ưu ái khi người làm và người chấm dùng chung một mô hình. Quy tắc số một trong bảng tiêu chí ở đây cũng mới chỉ được thực thi bằng lời nhắc cho `Critic`; một bản dựng nghiêm ngặt hơn sẽ chặn thẳng quyền ghi của `Agent` vào thư mục `tests/`. Cả hai thanh ray bảo vệ đó, cộng với việc cho toàn bộ hệ thống chạy tự động không cần người canh, sẽ nằm ở [phần ba](build-overnight.md).
