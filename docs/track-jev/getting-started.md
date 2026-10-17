# Bắt đầu với Jev

Tài liệu công khai của Jev mới chỉ xuất hiện được khoảng một tuần. Trang này phản ánh những thông tin đã được công bố tính đến ngày 21 tháng 9 năm 2026; hãy lường trước rằng nội dung này sẽ cũ đi rất nhanh.

## Quyền truy cập

Jev hiện đang mở truy cập sớm qua danh sách chờ (waitlist). Bạn đăng ký tại [console.typesafe.ai](https://console.typesafe.ai/), và TypeSafe cho biết họ đang duyệt dần các nhà phát triển từ danh sách chờ theo từng đợt. Khóa API (API keys) nằm tại đường dẫn `console.typesafe.ai/settings/keys`; một số cổng trung gian (Vercel AI Gateway, Netlify, Cloudflare) cũng hỗ trợ chuyển tiếp (proxy) dịch vụ này. Trên bảng điều khiển (console) có sẵn một khu vực thử nghiệm (playground) miễn phí để bạn vọc thử trước khi được cấp hạn ngạch (quota) chính thức.

## Hình thái API

Toàn bộ API chỉ gói gọn trong một điểm cuối (endpoint) duy nhất — `POST https://api.typesafe.ai/v1/systemone` — với tên mô hình mặc định là `jev-latest` (hiện tại là bản `jev-1.13.0`). Các bộ SDK chính thức gồm: `pip install typesafe-sdk` và `npm install @typesafe-ai/sdk`, cả hai đều tự động đọc biến môi trường `TYPESAFE_API_KEY`.

Một yêu cầu gửi đi bao gồm một trạng thái `state` (chuỗi ký tự, đối tượng JSON, hoặc mảng văn bản — hiện tại chỉ hỗ trợ văn bản) cộng với các câu hỏi được đặt tên sử dụng ba kiểu nguyên thủy:

```python
from typesafe import Choice, Score, Noul

questions = {
    "team": Choice(instructions="Which team should handle this",
                   criteria={"billing": "Payment issues", "technical": "Bugs"}),
    "frustration": Score(instructions="Customer frustration level",
                         criteria=["Calm", "Frustrated but civil", "Very angry"]),
    "refund": Noul(instructions="Customer explicitly requesting a refund"),
}
```

Tất cả các câu hỏi đều được trả lời trong một lượt chạy song song duy nhất. Các giới hạn theo tài liệu công bố: tối đa 64k token cho phần `state`, 32k token cho tổng của `state` cộng với câu hỏi dài nhất, và tối đa 255 lựa chọn cho mỗi `Choice`. Mức giá là \$0.042 cho mỗi triệu token đầu vào; đầu ra không tính phí.

## Một dự án khởi đầu thực tế

Phân loại sơ bộ phiếu hỗ trợ (support-ticket triage) là bài toán khởi đầu kinh điển: hãy lấy 200 phiếu hỗ trợ trong lịch sử mà bạn đã gắn nhãn sẵn, hỏi Jev ba câu hỏi ở ví dụ trên, rồi đem câu trả lời cùng xác suất của nó đối chiếu với nhãn thực tế của bạn. Thử nghiệm này mang lại cho bạn hai thông tin quan trọng nhất — độ chính xác ngay trên *phân phối dữ liệu của chính bạn*, và liệu điểm tự tin của nó có đủ trung thực để đặt ngưỡng chặn (threshold) như đã bàn trong bài [Jev trong ngăn xếp Agent](jev-in-an-agent-stack.md) hay không. Những báo cáo ban đầu về việc dựng xong bản demo chạy được trong chưa đầy một giờ là hoàn toàn khả thi; nhưng hãy coi kết quả đánh giá trên dữ liệu của chính bạn mới là cột mốc thực sự.

Hãy lưu tâm đến những điểm bẫy (gotchas) đã được ghi nhận: Jev đọc hiểu rất máy móc theo nghĩa đen (rất dễ sập bẫy câu phủ định), không biết đếm, không sắp xếp được thứ tự ngày tháng, và suy giảm chất lượng khi ngữ cảnh bị phình to — vì vậy hãy truy xuất và lọc bớt dữ liệu bằng mã nguồn trước khi gửi vào `state`. Hãy kiểm thử kỹ các đòn tấn công tiêm nhiễm câu lệnh (adversarial injection) nếu bên trong `state` có chứa văn bản do người dùng nhập vào.

## Những gì vẫn chưa rõ hoặc chưa phát hành

Nói thẳng: kiến trúc, kích thước mô hình và bộ trọng số đều không được tiết lộ. Không hỗ trợ tự lưu trữ (self-hosting), không tinh chỉnh (fine-tuning), không nhận đầu vào hình ảnh/âm thanh/video, chưa có tài liệu công khai về giới hạn tần suất gọi (rate-limit) hay cam kết chất lượng dịch vụ (SLA), chưa có bài kiểm chuẩn độc lập, và cũng chưa có bằng chứng nào cho thấy mức giá hiện tại là bền vững chứ không phải đang được bù lỗ. Ngày mở cửa rộng rãi (General Availability) vẫn chưa được ấn định. Nếu bất kỳ điểm nào trong số này là rào cản chặn đứng dự án của bạn, hãy chờ đợi — xem lại bài [Jev phù hợp với việc gì](what-jev-is-good-for.md) để cân nhắc xem có đáng xếp hàng chờ hay không, và tra cứu trang [tài nguyên tham khảo](resources.md) để đọc tài liệu gốc.
