---
name: goal-test
description: >-
  Biến một tác vụ mơ hồ thành tiêu chí hoàn thành (definition of done) có thể
  kiểm thử và sinh script kiểm tra mục tiêu (goal-test) có thể thực thi, tùy chọn
  đi kèm một vòng lặp thử lại có giới hạn bao quanh một agent chạy ngầm (headless agent).
  Sử dụng khi người dùng muốn cho agent chạy trong vòng lặp, hỏi làm sao để biết
  khi nào tác vụ của agent hoàn tất, hoặc nói rằng một mục tiêu như "cải thiện X"
  cần được chuyển thành điều kiện kiểm tra được. KHÔNG dùng để xây dựng bộ kiểm thử
  đánh giá trên nhiều trường hợp — việc đó thuộc về evals-bootstrap.
---

# Viết tiêu chí hoàn thành dưới dạng Script

Lý thuyết: [Bốn thành phần của một vòng lặp](https://secondbrainos-vn.pages.dev/#/read/course-2-loop/the-four-parts)
và [trang thực hành xây dựng goal test](https://secondbrainos-vn.pages.dev/#/read/track-loop/build-goal-test).
Một yêu cầu như "Cải thiện việc xử lý lỗi" không thể làm điều kiện dừng cho một vòng lặp, bởi vì không có gì có thể khẳng định khi nào nó đã hoàn tất. Mục tiêu phải được phát biểu sao cho một chương trình máy tính — chứ không phải con người, và càng không phải bản thân mô hình — có thể trả về đúng (`true`) hoặc sai (`false`) khi kiểm tra nó.

## Quy trình thực hiện

1. **Trích xuất mệnh đề kiểm chứng.** Hỏi người dùng xem họ muốn điều gì trở thành sự thật khi công việc kết thúc, sau đó phát biểu lại thành các sự kiện có thể kiểm chứng: lệnh nào thoát với mã 0, file nào phải tồn tại, chuỗi ký tự nào phải xuất hiện, con số nào phải vượt qua ngưỡng nào. Nếu có phần nào không thể kiểm tra bằng chương trình, hãy nói rõ và thương lượng để rút gọn về những gì máy có thể kiểm tra được.
2. **Ưu tiên các phép kiểm tra đã có sẵn.** Bộ test suite, công cụ kiểm lỗi (linter), quá trình build, trình kiểm tra kiểu (type checker). Một bài kiểm tra mục tiêu gọi thẳng lệnh `make test` luôn tốt hơn việc viết lại logic kiểm tra đó từ đầu.
3. **Viết file `goal-test.sh`** (hoặc `.py` nếu kiểm tra bằng Python dễ hơn) tại thư mục gốc của dự án: chạy từng phép kiểm tra, in ra một dòng cho mỗi phép kiểm tra kèm trạng thái pass/fail, và chỉ thoát với mã 0 khi tất cả cùng vượt qua. Giữ độ dài dưới ~40 dòng; script phải chạy xong trong vài giây và an toàn khi chạy lặp đi lặp lại.
4. **Chạy thử ngay lập tức.** Nó phải thất bại (fail) trước khi công việc được thực hiện — một bài kiểm tra mục tiêu mà vượt qua ngay trên trạng thái hiện tại thì thực chất chẳng kiểm tra được gì cả. Hãy hiển thị kết quả báo lỗi đó.
5. **Đề xuất vòng lặp.** Nếu người dùng muốn điều khiển agent chạy tự động cho đến khi hoàn thành, hãy bọc nó trong một script:

```bash
#!/usr/bin/env bash
# goal-loop.sh — chạy headless agent cho đến khi vượt qua goal test hoặc hết số lần thử.
set -u
MAX_ATTEMPTS=5
for i in $(seq 1 "$MAX_ATTEMPTS"); do
  FEEDBACK=$(./goal-test.sh 2>&1) && { echo "done in $i attempt(s)"; exit 0; }
  claude -p "Goal: <mục tiêu>. The goal test currently fails with:
$FEEDBACK
Fix the code so the goal test passes." \
    --permission-mode acceptEdits --output-format json > ".attempt-$i.json"
done
echo "goal test still failing after $MAX_ATTEMPTS attempts — falling back to a human"
exit 1
```

Điều chỉnh lệnh gọi agent cho khớp với CLI mà người dùng đang sử dụng. Giữ cho ba chiếc phanh an toàn luôn hiện diện rõ ràng và có tên cụ thể: bộ kiểm tra nằm ngoài mô hình (`goal-test.sh`), quy tắc dừng (vượt qua bài test), và ngân sách giới hạn (`MAX_ATTEMPTS`, cộng thêm trần chi phí đô-la đọc từ đầu ra JSON nếu họ muốn).

## Quy tắc

- Bộ kiểm tra không bao giờ hỏi ý kiến của mô hình; việc mô hình tự đánh giá (self-review) không phải là một bộ kiểm tra.
- Truyền nguyên văn kết quả đầu ra của bộ kiểm tra quay ngược lại — nội dung báo lỗi chính là prompt cho lượt tiếp theo.
- Nếu người dùng không thể diễn đạt trạng thái hoàn thành thành một phép kiểm tra, tức là họ chưa có một tác vụ có thể đưa vào vòng lặp; hãy nói thẳng điều đó với họ và gợi ý làm việc qua một phiên tương tác trực tiếp.
