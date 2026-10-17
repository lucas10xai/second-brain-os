# Jev trong ngăn xếp Agent

Cách ứng dụng ban đầu đáng tin cậy nhất của Jev không phải là thay thế hoàn toàn một mô hình LLM, mà là đặt cạnh nó. Các vòng lặp (Loop) của Agent chứa đầy những quyết định nhỏ có phạm vi giới hạn — chọn mô hình nào, gọi công cụ nào, thao tác này có an toàn không, chúng ta đã hoàn thành tác vụ chưa — và hiện nay mỗi quyết định như vậy đều tiêu tốn một lệnh gọi LLM trọn vẹn. Mẫu thiết kế đang nổi lên, mới chỉ một tuần tuổi nhưng đã hiện diện rõ nét trong [bài viết về xây dựng Harness cùng Jev của LangChain](https://www.langchain.com/blog/building-a-harness-with-jev), là giao phó những quyết định đó cho một mô hình System One và giữ LLM lại cho những phần thực sự cần đến ngôn ngữ. Xem bối cảnh nền tảng tại bài [các mô hình System One](system-one-models.md).

## Đặt Jev ở phía trước vòng lặp (Loop)

- **Router (Bộ định tuyến).** Jev phân loại yêu cầu đi vào và điều hướng nó: đẩy sang mô hình nhỏ, nhanh, rẻ cho các tra cứu đơn giản; chuyển sang mô hình suy luận đắt tiền cho những ca khó. Với độ trễ công bố từ 70–500ms, bước định tuyến này gần như miễn phí so với lệnh gọi LLM mà nó giúp tiết kiệm.
- **Triage gate (Cổng phân loại sơ bộ).** Một câu hỏi dạng `Noul` ("yêu cầu này có cần con người can thiệp không?") đặt ngay trước Agent giúp chặn đứng các nội dung rác không cho lọt vào vòng lặp ngay từ đầu.

## Đặt Jev ở bên trong vòng lặp (Loop)

- **Guardrails cho lệnh gọi công cụ.** Thành phần `AutoModeMiddleware` của LangChain sử dụng Jev để kiểm tra một lệnh gọi công cụ vừa được đề xuất xem có chứa hành động rủi ro hay không và chặn nó lại trước khi thực thi — đây là một phán đoán có định kiểu rõ ràng, chứ không phải cảnh dùng một LLM thứ hai ngồi bình phẩm về đầu ra của LLM thứ nhất.
- **Kiểm tra trạng thái (State checks).** "Tác vụ đã hoàn tất chưa?", "lệnh gọi công cụ vừa rồi có thành công không?", "người dùng có đang bực bội không?" — mỗi câu đều là một câu hỏi định kiểu chạy trên biên bản hội thoại (transcript), và bởi vì Jev trả lời tất cả các câu hỏi trong một lượt chạy song song duy nhất, việc hỏi mười câu hầu như không tốn thêm thời gian so với hỏi một câu.

Bản tích hợp của LangChain cung cấp cơ chế này dưới tên gọi `TypeSafeClassifier`: bạn truyền một `state` cùng một từ điển (dict) chứa các câu hỏi vào phương thức `.invoke()` và nhận về các câu trả lời có định kiểu kèm theo xác suất, để rồi chính mã nguồn của bạn — chứ không phải mô hình — ra quyết định hành động dựa trên đó.

## Xử lý lỗi bằng ngưỡng tự tin (Confidence thresholds)

Con số xác suất đi kèm mỗi câu trả lời chính là trụ cột chịu lực của thiết kế này. Mẫu xử lý mà những người áp dụng sớm đều hội tụ về gồm các bước:

- Thiết lập một ngưỡng (threshold) riêng cho từng quyết định, định giá dựa trên cái giá phải trả nếu làm sai. Tự động phê duyệt hoàn tiền có thể cần ngưỡng 0.98; còn chọn hàng đợi hỗ trợ kỹ thuật có thể chỉ cần 0.7 là ổn.
- Nếu thấp hơn ngưỡng, hãy chuyển cấp (escalate) — đẩy lên cho LLM lớn, chuyển cho con người, hoặc lùi về một phương án mặc định an toàn. Khi đó, Jev đóng vai trò là luồng xử lý nhanh (fast path), chứ không phải luồng duy nhất.
- Ghi nhật ký (log) toàn bộ các con số xác suất. Jev không đưa ra lời giải thích lý do, vì vậy trạng thái `state` bạn gửi đi cộng với bảng điểm bạn nhận về chính là toàn bộ dấu vết kiểm toán (audit trail) của bạn. Hãy lưu giữ chúng cẩn thận.

Một lời cảnh báo thẳng thắn: toàn bộ cơ chế này giả định rằng các con số xác suất đã được hiệu chuẩn thực sự chuẩn xác — đây là tuyên bố cốt lõi của TypeSafe nhưng đến nay vẫn chưa được kiểm chứng độc lập trên lưu lượng dữ liệu lệch phân phối (out-of-distribution). Những người hoài nghi lưu ý rằng một điểm số tự tin cao tự thân nó không phải là bằng chứng cho thấy dự đoán đó đáng tin cậy. Hãy bắt đầu với các ngưỡng bảo thủ và đo lường đối chiếu với bộ nhãn thực tế của chính bạn. Hướng dẫn thiết lập thực tế nằm ở bài [bắt đầu với Jev](getting-started.md); cách đánh giá mức độ phù hợp của tác vụ nằm ở bài [Jev phù hợp với việc gì](what-jev-is-good-for.md).
