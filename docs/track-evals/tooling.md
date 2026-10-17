# Công cụ đánh giá (Eval Tooling)

Thị trường hiện đã định hình xoay quanh hai nhóm chính: các nền tảng lấy đánh giá làm trung tâm (eval-first) gắn thêm tính năng quan sát (observability), và các nền tảng lấy truy vết làm trung tâm (tracing-first) gắn thêm tính năng đánh giá (`Evals`). Tất cả các công cụ dưới đây đều đang hoạt động tích cực và được bảo trì tốt tính đến cuối năm 2026. Hãy chọn một cái rồi bắt tay vào làm; bánh đà đánh giá trong bài [tại sao cần `Evals`](why-evals.md) quan trọng hơn nhà cung cấp công cụ gấp nhiều lần.

## Các nền tảng (Platforms)

- [Braintrust](https://www.braintrust.dev/) — nền tảng thương mại lấy `Evals` làm trung tâm, được xây dựng xoay quanh vòng lặp `Eval()`: tập dữ liệu, thử nghiệm, so sánh chênh lệch hồi quy (regression diffs) song song, và các cổng chặn (`Gate`) trên CI. Lựa chọn mặc định cho các đội ngũ thiên về kỹ thuật bắt đầu từ `Evals` thay vì từ các bảng biểu dashboard.
- [Langfuse](https://langfuse.com/) — lựa chọn mã nguồn mở trưởng thành nhất; cơ chế truy vết theo chuẩn OpenTelemetry mà bạn có thể tự triển khai (self-host) chỉ trong một buổi chiều, với tập dữ liệu và tính năng đánh giá bằng `LLM-as-judge` được đắp lên trên. Hãy chọn nó nếu yêu cầu lưu trữ dữ liệu nội bộ (data residency) hoặc giấy phép mở là điều kiện bắt buộc.
- [LangSmith](https://www.langchain.com/langsmith) — nền tảng của LangChain. Nếu bạn đang dùng LangChain/LangGraph, việc gắn đo lường chỉ tốn một dòng cấu hình và quy trình quản lý tập dữ liệu rất mượt mà; còn nếu bạn không dùng hệ sinh thái đó, hầu như chẳng có lý do gì để tìm đến đây.
- [W&B Weave](https://weave-docs.wandb.ai/) — công cụ đánh giá và truy vết từ Weights & Biases; chỉ cần gắn decorator vào hàm là có ngay `Traces` được quản lý phiên bản và bảng điều khiển `Evals`. Rất tự nhiên nếu tổ chức của bạn đã quen làm việc trên W&B.

## Các Framework và CLI

- [promptfoo](https://www.promptfoo.dev/) — CLI mã nguồn mở: khai báo các prompt, nhà cung cấp mô hình và các phép kiểm tra (assertions) trong tệp YAML để nhận về một ma trận so sánh trực quan. Con đường nhanh nhất để trả lời câu hỏi "prompt/mô hình nào tốt hơn", cộng thêm chế độ kiểm thử đối kháng (red-teaming) rất nghiêm túc. Chạy cực kỳ xuất sắc trong CI.
- [Inspect](https://inspect.aisi.org.uk/) — framework Python mã nguồn mở của Viện An toàn AI Vương quốc Anh (UK AISI): gồm các bộ giải (solvers), bộ chấm điểm (scorers) và môi trường `Agent` cô lập có tính khả ghép cao, đi kèm hơn 200 bài đánh giá dựng sẵn trong kho [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals). Được xây dựng với sự chặt chẽ cao độ; là tiêu chuẩn trong giới kiểm thử an toàn AI và cực kỳ tốt cho việc [đánh giá `Agent`](agent-evals.md) nói chung.
- [OpenAI Evals](https://github.com/openai/evals) — kho mã nguồn đăng ký từ năm 2023 vẫn còn đó, nhưng hướng đi được OpenAI chính thức hỗ trợ hiện nay là sản phẩm Evals tích hợp bên trong API và dashboard, đi kèm [tài liệu hướng dẫn thực hành đánh giá tốt nhất](https://developers.openai.com/api/docs/guides/evaluation-best-practices). Hãy dùng tài liệu hướng dẫn, đừng dùng kho mã nguồn cũ.
- [DeepEval](https://github.com/confident-ai/deepeval) — framework đánh giá mang phong cách pytest với các thước đo dựng sẵn (độ trung thực, độ liên quan của câu trả lời). Tiện lợi cho CI; nhưng hãy coi các thước đo dựng sẵn đó là điểm khởi đầu chứ không phải chân lý — bạn vẫn phải hiệu chuẩn chúng theo đúng hướng dẫn trong bài [`LLM-as-judge`](llm-as-judge.md).

## Đánh giá plugin trong `Claude Code`

Anthropic đã tích hợp sẵn một `Harness` đánh giá ngay bên trong `Claude Code` (từ bản v2.1.269+, tháng 9 năm 2026): lệnh `claude plugin eval` chạy một plugin hoặc kỹ năng (skill) trước một bộ các prompt thực tế, chấm điểm kết quả bằng sáu loại bộ chấm (`regex`, `tool_used`, `tool_order`, `file_exists`, `llm`, `baseline`), và — phần trung thực nhất — chạy lại *mà không có* plugin để báo cáo độ chênh lệch (delta) thực sự mà plugin đó đóng góp. Lệnh `claude plugin eval init` đề xuất các ca kiểm thử một cách tương tác; cờ `--threshold` dùng để đặt `Gate` chặn CI. Tài liệu chi tiết tại [code.claude.com/docs/en/plugin-evals](https://code.claude.com/docs/en/plugin-evals). Nếu bạn viết các kỹ năng (skills) cho `Agent`, đây chính là cùng kỷ luật đó được áp dụng cho phần khung giàn prompt của bạn.

## Lời khuyên chân thành

Mọi nền tảng đều có những màn demo tuyệt đẹp trên tập dữ liệu đồ chơi. Điểm tạo nên sự khác biệt thực sự là liệu đội ngũ của bạn có thực sự mở nó ra để đọc `Traces` hàng tuần hay không. Hãy dùng thử với chính bảng phân loại lỗi của bạn trong vòng hai tuần trước khi đặt bút ký hợp đồng với bất kỳ nền tảng nào.
