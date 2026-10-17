---
name: evals-bootstrap
description: >-
  Khởi tạo bộ kiểm thử đánh giá (eval suite) đầu tiên cho một agent: khai thác
  các lỗi thực tế thành kịch bản kiểm thử (cases), viết các phép kiểm tra hành vi
  trên vết thực thi (traces), và sinh script chạy kiểm thử. Sử dụng khi người dùng
  muốn có evals, kiểm thử hồi quy cho agent, tập dữ liệu chuẩn (golden set), hoặc
  hỏi làm sao để biết một thay đổi về prompt/mô hình không làm hỏng hệ thống.
  KHÔNG dùng để kiểm tra điều kiện hoàn thành của một tác vụ đơn lẻ (goal-test)
  hoặc kiểm toán ngữ cảnh (context-audit).
---

# Khởi tạo bộ kiểm thử đánh giá (Eval Suite)

Lý thuyết: [Hai loại phép kiểm tra](https://secondbrainos-vn.pages.dev/#/read/course-5-evals/two-kinds-of-checks)
và hướng dẫn chi tiết trong [Thực hành Evals](https://secondbrainos-vn.pages.dev/#/read/course-5-evals/evals-practice).
Một bộ eval là cùng một bài kiểm tra được chạy lại sau mỗi lần thay đổi. Kiểm tra hành vi (behavioural checks) đọc từng bước trong vết thực thi (trace); kiểm tra đầu-cuối (end-to-end checks) chỉ đọc kết quả cuối cùng. Hãy bắt đầu bằng kiểm tra hành vi: chúng có tính tất định, chạy trong vài giây, và giúp chẩn đoán nguyên nhân thay vì chỉ chấm điểm.

## Quy trình thực hiện

1. **Tìm các lỗi thực tế.** Hỏi xem lịch sử các lượt chạy của agent được lưu ở đâu (logs, transcripts, thư mục traces). Hãy đọc cho đến khi bạn thu thập được tối đa hai mươi lỗi thực tế — không phải các lỗi tự tưởng tượng ra. Nếu chưa có lượt chạy nào được ghi log, hãy xây dựng cơ chế ghi vết thực thi trước (bước 3) và khởi tạo bộ kiểm thử với ba lỗi mà người dùng còn nhớ được; một bộ kiểm thử nhỏ nhưng trung thực luôn tốt hơn một bộ kiểm thử lớn nhưng bịa đặt.
2. **Mỗi lỗi một dòng.** Với mỗi lỗi: ghi rõ đầu vào, và một hành vi cụ thể lẽ ra phải diễn ra nhưng đã không diễn ra. Các lỗi thường gom cụm lại thành bốn đến tám nhóm hành vi; hãy đặt tên cho chúng.
3. **Đảm bảo vết thực thi (traces) tồn tại.** Mỗi lượt chạy phải được lưu dưới dạng `traces/<id>.json` — một danh sách các sự kiện bao gồm cả các lệnh gọi công cụ (tool calls). Nếu khung điều phối của người dùng là Claude Code, bản thân file transcript đã là một trace; hãy kết nối script sao chép hoặc chuyển đổi nó. Không có trace thì không thể kiểm tra hành vi.
4. **Viết file `cases.yaml`.** Mỗi lỗi là một mục:

```yaml
- id: refund_1042
  input: "Refund order #1042, customer says it arrived broken"
  expect: tra cứu đơn hàng trước khi trả lời; xin phê duyệt trước khi hoàn tiền
  check:
    - trace has get_order before send_reply
    - trace has approval_request before refund
```

   Dòng `expect` dành cho con người đọc; các dòng `check` là bài kiểm thử máy chạy. Hãy giữ cho ngôn ngữ quy tắc thật tối giản: `trace has X`, `trace has X before Y`, `trace lacks X`.
5. **Sinh file `check_traces.py`.** Một trình chạy nhỏ gọn: đọc `cases.yaml`, phân tích từng quy tắc bằng biểu thức chính quy (regex), duyệt qua danh sách lệnh gọi công cụ, in ra một dòng cho mỗi kịch bản, và thoát với mã khác 0 (non-zero) nếu có bất kỳ kịch bản nào thất bại. Giữ cho nó ít phụ thuộc nhất có thể (chỉ dùng `pyyaml`) và chạy thật nhanh — toàn bộ bộ kiểm thử nên hoàn tất trong vài giây mà không cần gọi mô hình AI.
6. **Chạy thử và bàn giao bánh đà (flywheel).** Hiển thị các dòng kết quả pass/fail. Sau đó, để lại quy trình vận hành bằng văn bản ở cuối báo cáo: đọc các trace mới hàng tuần, thêm mỗi lỗi mới thành một kịch bản kiểm thử, sửa cụm lỗi lớn nhất, rồi chạy lại.

## Quy tắc

- Mọi kịch bản kiểm thử đều phải xuất phát từ một lỗi thực tế; chỉ xóa một kịch bản khi hành vi mà nó bảo vệ đã bị loại bỏ khỏi hệ thống, chứ không phải vì nó gây bất tiện.
- Không dùng mô hình làm giám khảo (LLM-as-judge) ở bước khởi tạo. Chỉ thêm giám khảo LLM về sau cho những khía cạnh mà các câu lệnh điều kiện (assertions) không thể kiểm tra tới, và phải hiệu chuẩn nó dựa trên nhãn do con người gán trước.
- Bộ kiểm thử phải chạy được bằng một lệnh duy nhất (`python check_traces.py`) để có thể làm cổng chặn trong CI hoặc thói quen kiểm tra trước khi phát hành mà không cần thủ tục rườm rà.
