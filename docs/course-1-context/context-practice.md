# Thực hành quản trị Context

Bạn đã nắm được cơ chế vận hành và [bốn vị trí đặt Context](the-four-places.md). Trang này là buổi thực hành trực tiếp: kiểm toán (audit) một `Agent` hiện có, tái cấu trúc nó, và bổ sung hai nâng cấp quan trọng khi hệ thống vượt qua một quy mô nhất định.


> Toàn bộ quy trình kiểm toán dưới đây cũng đã được đóng gói thành một `Skill`: hãy cài đặt [plugin của khóa học](../../plugins/README.md) và chạy lệnh `/agents-course:context-audit` ngay trong dự án của bạn.

## Kiểm toán Context window

Hãy thực hiện quy trình này trên một `Agent` thực tế đang chạy, đừng chỉ nhẩm tính trong đầu.

1. Thu thập trọn vẹn một gói dữ liệu yêu cầu (request payload) — ghi log chính xác chuỗi JSON mà framework của bạn gửi tới mô hình ở một lượt hội thoại nằm giữa quá trình chạy.
2. Đếm số lượng token riêng biệt cho từng thành phần: system prompt, định nghĩa công cụ (`Tool use`), lịch sử tin nhắn, nội dung truy xuất (retrieved content), và truy vấn hiện tại. Viết rõ năm con số này ra giấy.
3. Khoanh tròn mọi giá trị động nằm bên trong system prompt — dấu thời gian, tên người dùng, các đoạn bộ nhớ được chèn vào. Mỗi giá trị động này chắc chắn sẽ gây trượt bộ nhớ đệm (cache miss) ở mọi lệnh gọi.
4. Kiểm tra xem danh sách công cụ ở lượt 1 và lượt 20 có giống hệt nhau không. Nếu danh sách này thay đổi giữa chừng, bạn đã phải trả giá bằng việc mất trắng hiệu lực `Prompt caching` sau mỗi lần thay đổi.
5. Tìm mục đơn lẻ chiếm dung lượng lớn nhất trong lịch sử hội thoại. Gần như lúc nào đó cũng là một kết quả trả về nguyên văn từ công cụ mà lẽ ra chỉ nên là một đường dẫn tập tin.
6. Xác định vị trí của mục tiêu hiện tại. Nếu nó chỉ xuất hiện duy nhất ở tin nhắn mở đầu, thì giờ đây nó đã bị trôi vào vùng trũng chú ý yếu ớt ở giữa `Context window`.
7. Đọc thông số `cache_read_input_tokens` từ phản hồi của API. Nếu con số này bằng 0 trong một cuộc hội thoại đã chạy nhiều lượt, điều đó có nghĩa là có thứ gì đó trong phần tiền tố (prefix) của bạn đang bị biến đổi.

## Tái cấu trúc về đúng bốn vị trí

Hãy lần lượt xử lý các vấn đề phát hiện được sau kiểm toán theo đúng thứ tự. Gọt giũa system prompt để chỉ giữ lại những gì luôn đúng ở mọi lệnh gọi, và chuyển toàn bộ các giá trị động đã khoanh tròn sang phần lịch sử tin nhắn. Đóng băng danh sách công cụ ngay từ đầu cuộc hội thoại và thay thế bất kỳ thao tác xóa công cụ giữa chừng nào bằng cơ chế chặn lệnh gọi trả về một chuỗi từ chối. Viết lại các công cụ trả về dữ liệu lớn sao cho chúng ghi kết quả ra ổ đĩa và chỉ trả về đường dẫn kèm theo một dòng biên nhận tóm tắt. Sau đó bổ sung phần đuôi (tail): cứ sau mỗi vài kết quả công cụ, hãy nối thêm một dòng nhắc lại mục tiêu hiện tại. Chạy lại bài kiểm toán; năm con số thống kê sẽ dịch chuyển rõ rệt theo hướng một phần tiền tố nhỏ gọn, cố định và một phần đuôi ngắn gọn, cập nhật trực tiếp.

## Chuyển sang cơ chế tìm kiếm công cụ khi vượt quá hai mươi công cụ

Bài viết [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) của Anthropic báo cáo rằng việc nạp sẵn toàn bộ định nghĩa công cụ sẽ không còn hiệu quả khi mở rộng quy mô: khi bật tính năng tìm kiếm công cụ (tool search) thay thế, điểm số của Opus 4 đã tăng từ 49% lên 74% trong bài đánh giá `MCP` của họ, và Opus 4.5 tăng từ 79,5% lên 88,1%. Ngưỡng khuyến nghị của chính Anthropic là từ mười công cụ trở lên hoặc trên 10.000 token định nghĩa; khóa học này vạch ra ranh giới cứng ở con số hai mươi. Hãy giữ một nhóm nhỏ các công cụ cốt lõi luôn dùng được nạp sẵn, đánh dấu phần còn lại ở chế độ trì hoãn (deferred), và để mô hình tự tìm kiếm định nghĩa công cụ theo nhu cầu thực tế. Phần tiền tố sẽ thu nhỏ lại và, theo đúng những con số thực nghiệm kia, độ chính xác khi lựa chọn công cụ cũng tăng lên theo.

## Bổ sung Subagent tóm tắt

Một `Subagent` chính là một bức tường lửa ngăn cách `Context` (context firewall). Khi một tác vụ đòi hỏi phải đọc năm mươi tập tin, đừng đọc chúng ngay trong `Context window` chính — hãy khởi tạo một `Subagent` để cửa sổ riêng của nó hấp thụ toàn bộ năm mươi tập tin đó và chỉ trả về một bản tóm tắt dài một trang. `Agent` chính chỉ giữ lại phần kết luận, chứ không ôm đồm toàn bộ bằng chứng thô. Mô hình tương tự áp dụng hoàn hảo cho bất kỳ tác vụ đọc dữ liệu hàng loạt nào: rà soát nhật ký hệ thống (log trawls), kiểm tra các bản diff code lớn, hoặc đọc chồng tài liệu dày. Cuốn [cẩm nang chuyên sâu về Harness](../track-harness/context-engineering.md) sẽ hướng dẫn chi tiết cách thiết lập các bức tường lửa ngữ cảnh này vào một hệ thống thực tế.

## Mẹo thực chiến

- Nhắc lại mục tiêu ở phần đuôi (tail) sau mỗi ba đến năm bước thực thi.
- Không để bất kỳ kết quả công cụ nguyên văn nào dài quá khoảng 2.000 token tồn tại trong lịch sử hội thoại; hãy thay bằng đường dẫn tập tin cộng với biên nhận tóm tắt.
- Chặn công cụ khi cần, tuyệt đối không xóa định nghĩa của chúng giữa chừng.
- Coi mọi thay đổi trên system prompt như các bản phát hành phần mềm (releases); hãy kiểm tra diff cẩn thận.
- Theo dõi sát các chỉ số bộ nhớ đệm (cache metrics) trên môi trường `Production` — một lỗi trượt cache âm thầm sẽ làm hóa đơn tăng gấp 10 lần.

## Tự mình kiểm chứng

1. Cài cắm một thông tin tự bịa vào chính giữa một bản ghi hội thoại dài 30.000 token rồi đặt câu hỏi về nó; sau đó chuyển đúng thông tin đó xuống tin nhắn cuối cùng và hỏi lại. Hãy so sánh hai câu trả lời.
2. Gửi một yêu cầu giống hệt nhau hai lần liên tiếp và đọc chỉ số `cache_read_input_tokens`; sau đó thêm một dấu thời gian (timestamp) vào đầu system prompt và quan sát chỉ số này tụt về 0.
3. Chạy cùng một tác vụ tóm tắt năm mươi tập tin: một lần chạy trực tiếp trong `Context window` chính và một lần chạy thông qua `Subagent`; hãy so sánh kích thước `Context` cuối cùng và chất lượng câu trả lời.

Học phần tiếp theo: [Loop so với Workflow](../course-2-loop/loops-vs-workflows.md).

Tìm hiểu sâu hơn → [trang Context engineering trong cẩm nang chuyên sâu về Harness](../track-harness/context-engineering.md): cách áp dụng cùng nguyên tắc kỷ luật này vào một hệ thống thực tế.
