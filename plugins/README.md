# plugins

Các plugin Claude Code đóng gói sẵn bộ công cụ thực hành của khóa học. Kho mã nguồn (repo) này hoạt động như một kho ứng dụng (plugin marketplace): chỉ cần thêm một lần và cài đặt những gì bạn cần.

```bash
claude plugin marketplace add lucas10xai/second-brain-os
claude plugin install agents-course@second-brain-os
```

## agents-course

Mỗi công cụ thực thi đúng phần bài tập thực hành của một học phần trong khóa học, ngay bên trong repo của riêng bạn.

| Công cụ | Lệnh gọi | Học phần |
|---|---|---|
| Context audit | `/agents-course:context-audit` | [1 · Ngữ cảnh (Context)](../docs/course-1-context/context-practice.md) — đo lường bốn vùng ngữ cảnh, tìm các yếu tố phá bộ nhớ đệm (cache killers) và gây phình cửa sổ ngữ cảnh |
| Goal test | `/agents-course:goal-test` | [2 · Vòng lặp (Loop)](../docs/course-2-loop/loop-practice.md) — biến một tác vụ thành tiêu chí hoàn thành có thể kiểm thử, sinh script kiểm tra và vòng lặp có giới hạn |
| Gate check | `/agents-course:gate-check` | [3 · Cổng kiểm soát (The gate)](../docs/course-3-gate/gate-practice.md) — tìm các quyết định không cần đến mô hình lớn, đề xuất các cổng định tuyến an toàn (fail-closed gates) |
| Harness audit | `/agents-course:harness-audit` | [4 · Khung điều phối (Harness)](../docs/course-4-harness/harness-practice.md) — rà soát bốn vòng bảo vệ, xác định bán kính ảnh hưởng (blast radius), xếp hạng danh sách gia cố |
| Evals bootstrap | `/agents-course:evals-bootstrap` | [5 · Đánh giá (Evals)](../docs/course-5-evals/evals-practice.md) — khai thác các lỗi thực tế thành kịch bản kiểm thử, sinh công cụ kiểm tra vết thực thi (trace checker) |
| Loop critic | agent `agents-course:loop-critic` | [2 · Vòng lặp (Loop)](../docs/course-2-loop/the-four-parts.md) — bộ kiểm tra nằm ngoài mô hình thực thi: đánh giá kết quả vòng lặp trong một ngữ cảnh sạch |

Các kỹ năng này là những file `SKILL.md` thuần túy, vì vậy chúng cũng hoạt động bình thường khi được sao chép vào `~/.claude/skills/` hoặc dùng với bất kỳ khung điều phối (harness) nào hỗ trợ định dạng Agent Skills.
