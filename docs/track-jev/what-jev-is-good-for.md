# Jev phù hợp với việc gì

Jev không phải là một mô hình đa dụng. Nó chỉ trả lời các câu hỏi có định kiểu về một khối ngữ cảnh đầu vào, không hơn không kém. Điều đó làm cho câu hỏi về mức độ phù hợp trở nên rất đơn giản: tác vụ của bạn có quy về việc chọn câu trả lời từ một không gian hữu hạn được định trước hay không? Nếu có, nó mang hình hài của Jev. Nếu câu trả lời cần phải được viết ra thành lời, thì không. Xem thêm kiến thức nền tảng tại bài [các mô hình System One](system-one-models.md).

## Các hình thái tác vụ phù hợp

- **Phân loại (Classification).** Nhận diện ý định (intent detection), phân loại phiếu hỗ trợ (ticket), gắn nhãn nội dung — một phép chọn `Choice` trên tối đa 255 phương án kèm theo xác suất cho từng phương án.
- **Định tuyến (Routing).** Quyết định xem đội ngũ nào, công cụ nào, hay mô hình hạ nguồn (downstream) nào sẽ xử lý yêu cầu này. Vẫn dùng cùng kiểu nguyên thủy đó, nhưng được đấu nối trực tiếp vào luồng điều khiển (control flow).
- **Trích xuất theo lược đồ.** Trả lời đồng loạt một loạt câu hỏi có định kiểu về cùng một tài liệu: đây có phải là hóa đơn không (`Noul`), thuộc nhà cung cấp nào (`Choice`), mức độ khẩn cấp ra sao (`Score`). Việc hỏi thêm câu hỏi hầu như không làm tăng độ trễ vì mọi thứ được trả lời trong một lượt chạy song song duy nhất.
- **Hàng rào bảo vệ (Guardrails).** Kiểm tra tiền khả thi (pre-flight checks) đối với các lệnh gọi công cụ của Agent: đặt câu hỏi "hành động này có tính phá hủy không?" dưới dạng một `Noul`, và chặn lại nếu vượt quá ngưỡng cho phép.
- **Xếp hạng và chấm điểm.** Đặt các mục dữ liệu lên một thang đo có thứ tự — chất lượng khách hàng tiềm năng, mức độ bức xúc, độ liên quan — ở quy mô lưu lượng mà việc dùng LLM chấm điểm là quá đắt đỏ không thể kham nổi.

## Nơi LLM vẫn chiếm ưu thế

- Bất kỳ tác vụ nào cần sinh ra văn bản, mã nguồn, hoặc bản tóm tắt. Jev hoàn toàn không sinh ra chuỗi ký tự nào.
- Suy luận mở (open-ended reasoning) khi bạn không thể liệt kê trước danh sách các câu trả lời.
- Các tác vụ đòi hỏi lời giải thích. Jev đưa cho bạn một con số xác suất chứ không đưa ra lý lẽ giải trình — đây là một rào cản thực sự đối với công tác kiểm toán trong các lĩnh vực chịu sự quản lý chặt chẽ.
- Đọc hiểu tỉ mỉ. Những người dùng thử đầu tiên phản ánh rằng Jev đọc hiểu rất máy móc theo nghĩa đen: các từ phủ định và từ giới hạn phạm vi dễ làm nó vấp ngã, nó không đếm số lượng một cách đáng tin cậy, và cũng không coi ngày tháng là các đại lượng có thứ tự.
- Độ chính xác thuần túy ở ngưỡng biên (frontier). Ngay trên bộ đánh giá (eval) của chính TypeSafe, Claude Opus 5 đạt 73,1% so với mức 67,8% của Jev.

## Bài toán độ trễ và chi phí

Tất cả các con số dưới đây đều là tuyên bố do TypeSafe công bố, chưa phải phép đo độc lập:

- Độ trễ đầu-cuối (end-to-end) từ 70–500ms, so với mức 3–329 giây được trích dẫn cho các luồng công việc dùng LLM hàng đầu — tương ứng với khoảng tuyên bố "nhanh hơn 40–200 lần".
- Mức giá \$0.042 cho mỗi triệu token đầu vào, miễn phí token đầu ra. Trên bài đánh giá gồm bốn luồng công việc của họ, chi phí tính ra vào khoảng \$0.0004 cho mỗi trường hợp, so với \$0.0304 của GPT-5.6 Terra (độ chính xác 67,9%, mất 10,1 giây) và \$0.1761 của Claude Opus 5 (mất 37,8 giây).
- Những con số đỉnh điểm như nhanh hơn 193,6 lần và rẻ hơn 444,6 lần đến từ các luồng công việc do chính đội ngũ phát triển năng lực của TypeSafe xây dựng và chạy trên máy của họ. Họ thừa nhận đây là những con số ở ngưỡng kịch trần thuận lợi, và hiện chưa thể chứng minh mức giá này không được trợ giá.

Góc nhìn công tâm nhất (steel-manned): đối với quy mô một triệu quyết định phân loại hoặc định tuyến mỗi ngày, chỉ cần tiết kiệm được 10 lần trong thực tế cũng đủ làm thay đổi hoàn toàn bài toán kinh tế về những gì khả thi để xây dựng. Còn việc con số tiết kiệm thực sự là 10 lần hay 400 lần chính là điều mà các thử nghiệm độc lập vẫn chưa xác lập được. Để tích hợp nó vào một Agent, hãy xem bài [Jev trong ngăn xếp Agent](jev-in-an-agent-stack.md); để bắt tay vào dự án đầu tiên, hãy xem bài [bắt đầu với Jev](getting-started.md).
