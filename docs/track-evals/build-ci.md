# Thực hành: Cổng kiểm soát CI (Build: the Gate)

Một bộ đánh giá chỉ chạy khi có ai đó sực nhớ ra là một bộ đánh giá sớm muộn sẽ ngừng chạy. Trang này kết nối tệp `eval_suite.py` từ bài [xây dựng bộ đánh giá](build-suite.md) vào GitHub Actions: một tập con làm cổng kiểm soát (`Gate`) cho mọi PR, toàn bộ bộ đánh giá chạy định kỳ hàng đêm (nightly), và con số kết quả sẽ được ghi vào một bảng điểm (scoreboard) commit thẳng vào kho mã nguồn. Các nguyên tắc nền tảng nằm ở phần CI của bài [đánh giá `Agent`](agent-evals.md).

## Cấu hình Workflow

Lưu thành tệp `.github/workflows/evals.yml`. Trước tiên hãy thêm biến `ANTHROPIC_API_KEY` vào mục repository secrets trên GitHub.

```yaml
name: evals

on:
  pull_request:
  schedule:
    - cron: "30 2 * * *"

permissions:
  contents: write

concurrency:
  group: evals-${{ github.ref }}
  cancel-in-progress: true

env:
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}

jobs:
  pr-gate:
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install anthropic
      - name: Run the smoke subset
        run: python eval_suite.py golden.jsonl --limit 20 --threshold 0.85

  nightly:
    if: github.event_name == 'schedule'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install anthropic
      - name: Run the full suite
        run: python eval_suite.py golden.jsonl --threshold 0.85
      - name: Append to the scoreboard
        if: always()
        run: |
          rate=$(python -c "import json; print(f\"{json.load(open('results.json'))['pass_rate']:.0%}\")")
          echo "| $(date -u +%Y-%m-%d) | ${rate} | ${GITHUB_SHA::7} |" >> scoreboard.md
          git config user.name "eval-bot"
          git config user.email "actions@users.noreply.github.com"
          git add scoreboard.md
          git commit -m "scoreboard: nightly eval run"
          git push
```

## Lựa chọn ngưỡng chặn (Threshold)

Hãy đặt ngưỡng thấp hơn một chút so với tỷ lệ đạt hiện tại của bạn, chứ đừng đặt bằng đúng con số đó. Các ca kiểm thử có giám khảo chấm mang tính ngẫu nhiên (stochastic): một bộ đánh giá đang ở mức 90% thỉnh thoảng sẽ in ra 87% dù không có gì thay đổi, và một `Gate` đặt cứng ở mức 90% sẽ biến nhiễu ngẫu nhiên đó thành những bản build đỏ lòm mà không ai còn tin tưởng. Hãy chạy toàn bộ bộ đánh giá ba lần, lấy con số tệ nhất, và đặt ngưỡng `Gate` thấp hơn mức đó một vài điểm phần trăm. Chỉ nâng rào chắn lên sau khi một cải tiến thực sự duy trì được kết quả ổn định qua suốt một tuần chạy nightly. Đồng thời, hãy ghim cố định mã định danh mô hình (model IDs) trong script — một tên gọi tắt (alias) của mô hình âm thầm trỏ sang phiên bản mới bên dưới chân bạn chính là một sự thay đổi, và nó phải đi vào qua một PR đối mặt với `Gate` giống như mọi thay đổi khác.

## Kiểm soát chi phí

Job chạy trên PR chỉ thực thi hai mươi ca kiểm thử đầu tiên; hãy giữ cho hai mươi ca đó là những ca rẻ nhất và có tính chẩn đoán cao nhất — tức là các ca chấm bằng code thuộc những kiểu lỗi lớn nhất của bạn, bởi việc sắp xếp thứ tự dòng trong `golden.jsonl` hoàn toàn miễn phí còn lệnh gọi giám khảo LLM mới là phần đắt đỏ. Hai mươi ca với hai lệnh gọi mỗi ca chỉ tốn một khoản tiền rất nhỏ cho mỗi PR; trong khi toàn bộ bộ đánh giá với đầy đủ các ca dùng giám khảo chỉ chạy mỗi đêm một lần bất kể kho mã nguồn bận rộn đến đâu. Cờ `cancel-in-progress` ngăn các thao tác `force-push` xếp chồng nhiều phiên chạy trùng lặp. Nếu chi phí chạy hàng đêm vẫn gây xót ruột, đó là dấu hiệu cho thấy bộ đánh giá đã phát triển vượt qua phiên bản một buổi chiều, và hướng dẫn về kích thước mẫu trong bài [thiết kế bộ đánh giá](designing-evals.md) sẽ chỉ cho bạn biết những ca kiểm thử nào thực sự xứng đáng giữ lại.

## Bảng điểm (The scoreboard)

Hãy tạo tệp mồi `scoreboard.md` bằng tay:

```markdown
# Eval scoreboard

| date | pass rate | commit |
|---|---|---|
```

Job chạy hàng đêm sẽ nối thêm một dòng và commit thẳng vào nhánh, kể cả trong những lần chạy thất bại — một con số xấu nằm trong lịch sử là một dữ kiện thực tế, còn một dòng bị khuyết lại là một bí ẩn. Mục đích của bảng điểm không phải là nghi thức hình thức; mà là biến con số chất lượng thành lịch sử hữu hình trong mọi bản clone của kho mã nguồn. Khi điểm số sụt giảm, lệnh `git log scoreboard.md` cùng nhật ký chạy hàng đêm sẽ chỉ đích danh ngày nào và bản commit nào đã gây ra điều đó. Vòng lặp ấy — đọc `Traces`, mã hóa các lỗi thành bài kiểm tra, đặt `Gate` chặn và theo dõi con số — chính là chiếc bánh đà trong bài [tại sao cần `Evals`](why-evals.md), nay đã tự động quay mà không cần đến bạn.
