# Chọn Agent hay Workflow

Có một quyết định phải được đưa ra trước khi bắt tay vào xây dựng bất cứ thứ gì: bạn có thể viết sẵn các bước thực hiện ra không? Nếu có thể, hãy viết chúng ra thành code. Đoạn code chạy các bước đã biết theo một trình tự xác định trước được gọi là `Workflow`, và một `Workflow` vượt trội hơn `Agent` trên mọi phương diện, ngoại trừ một điểm duy nhất.

Bài viết [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) của Anthropic đã vạch ra ranh giới rất rõ ràng: `Workflow` là hệ thống nơi các lệnh gọi mô hình và công cụ (`Tool use`) chạy dọc theo các nhánh code mà bạn đã định nghĩa trước; còn `Agent` là hệ thống nơi mô hình tự điều hướng quy trình của chính mình và tự quyết định bước tiếp theo trong quá trình chạy. Lời khuyên của họ là hãy tìm giải pháp đơn giản nhất có thể hoạt động và chỉ thêm sự phức tạp khi nó thực sự xứng đáng — các hệ thống `Agent` đánh đổi độ trễ và chi phí để lấy năng lực xử lý linh hoạt, và sự đánh đổi đó phải mang lại giá trị tương xứng.

## Tại sao Workflow luôn là lựa chọn ưu tiên mặc định

`Workflow` rẻ hơn: mỗi bước chỉ mang theo phần `Context` mà bước đó cần, chứ không phải một bản ghi lịch sử (transcript) ngày càng phìnhto của toàn bộ quá trình từ đầu đến giờ. Chúng có thể chạy song song: các bước độc lập có thể phân nhánh xử lý đồng thời, trong khi một `Loop` về bản chất phải chạy tuần tự — mỗi quyết định tiếp theo đều phải chờ kết quả quan sát từ bước trước đó. Chúng dễ gỡ lỗi (debug) hơn: một bước bị lỗi có tên cụ thể, có dữ liệu đầu vào rõ ràng và có dòng log tương ứng, trong khi một `Loop` bị lỗi buộc bạn phải đọc lại tới bốn mươi lượt hội thoại trong transcript. Và chúng có thể kiểm thử từng bước một, đảm bảo lỗi đã sửa sẽ không tái phát.

## Khi nào Loop xứng đáng với chi phí bỏ ra

`Loop` thuộc về những bài toán mà các bước thực hiện không thể biết trước. Chẳng hạn như tác vụ nghiên cứu, nơi truy vấn tiếp theo phụ thuộc vào kết quả trả về của truy vấn trước đó. Tác vụ gỡ lỗi phần mềm, nơi không ai biết trước tập tin nào trong số hàng ngàn tập tin đang chứa lỗi. Hoặc tác vụ tổng hợp mở, nơi hình hài của câu trả lời chỉ dần lộ diện từ tài liệu thu thập được. Dấu hiệu nhận biết luôn giống nhau: bạn không thể liệt kê trước các nhánh rẽ từ đầu, nhưng bạn có thể kiểm tra kết quả sau khi hoàn thành. Nếu không thỏa mãn cả hai vế này, bạn đang phải trả mức giá đắt đỏ của `Agent` cho một công việc vốn dĩ chỉ cần `Workflow`.

## Thực tế về chi phí

Hệ số nhân chi phí không phải là lời đồn đại; Anthropic đã công bố con số thực tế từ chính lưu lượng hệ thống của họ. Trong bài viết [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system), họ báo cáo rằng các `Agent` thông thường tiêu thụ lượng token gấp khoảng 4 lần so với một tương tác chat truyền thống, và các hệ thống đa `Agent` (multi-agent) tiêu thụ gấp khoảng 15 lần — đồng thời kiến trúc đa `Agent` chỉ có ý nghĩa về mặt kinh tế khi giá trị của tác vụ đủ lớn để bù đắp hóa đơn chi phí đó. Cũng bài viết này thừa nhận rằng những lĩnh vực đòi hỏi chia sẻ chung `Context` hoặc có sự phụ thuộc chặt chẽ giữa các `Agent` — mà hầu hết các tác vụ lập trình (coding) nằm trong số đó — hiện tại chưa phù hợp với kiến trúc đa `Agent`.

Vì vậy, các nấc thang triển khai nên đi theo thứ tự: một lệnh gọi mô hình đơn lẻ, tiếp đến là một `Workflow`, rồi mới đến một `Agent` đơn lẻ, và cuối cùng là hệ thống đa `Agent` — mỗi khi bước lên một nấc thang mới, bạn phải chứng minh được tính hợp lý của việc nâng cấp đó. Hầu hết các hệ thống nên dừng lại từ những nấc thang đầu. Câu hỏi mà sách trắng chưa bao giờ hỏi thẳng thắn, khóa học này sẽ đặt ra đầu tiên.

## Cách học khóa học này

Hãy học theo đúng thứ tự và gắn liền với một dự án thực tế bạn đang xây dựng. Học phần này là tấm bản đồ tổng quan: `Agent` thực sự là gì, khung kiến trúc năm tầng, và quyết định lựa chọn kiến trúc này. Các học phần từ 1 đến 5 sau đó sẽ đi sâu vào từng tầng một, theo đúng trình tự các câu hỏi phát sinh — nó nhìn thấy gì, ai ra quyết định, ai phân loại luồng, nó chạm tới đâu, và làm sao bạn biết nó chạy đúng. Mỗi học phần cung cấp cho bạn những thiết lập mặc định dùng được ngay; các cuốn cẩm nang chuyên sâu (handbook) đi kèm sẽ giải thích lý thuyết đằng sau chúng, và bạn có thể tra cứu sâu vào từng cẩm nang ngay khi tầng kiến trúc tương ứng bắt đầu bộc lộ vấn đề trong hệ thống của bạn. Hãy đọc kỹ [Agent là gì](what-an-agent-is.md) và [Năm tầng kiến trúc, một hệ thống](five-layers.md) trước tiên; những phần còn lại sẽ lần lượt nối tiếp.

- Học phần 0 — Bản đồ tổng quan: trang này và hai bài viết đi kèm
- [Học phần 1 — Context](../course-1-context/how-models-read.md): [Cách mô hình đọc Context](../course-1-context/how-models-read.md)
- [Học phần 2 — Loop](../course-2-loop/loops-vs-workflows.md), cùng cẩm nang chuyên sâu [Kỹ thuật thiết kế Loop là gì](../track-loop/what-loop-engineering-is.md)
- [Học phần 3 — Gate](../course-3-gate/cheap-decisions.md), cùng cẩm nang chuyên sâu [Các mô hình System One](../track-jev/system-one-models.md)
- [Học phần 4 — Harness](../course-4-harness/the-office.md), cùng cẩm nang chuyên sâu [Harness là gì](../track-harness/what-a-harness-is.md)
- [Học phần 5 — Evals](../course-5-evals/two-kinds-of-checks.md), cùng cẩm nang chuyên sâu [Tại sao cần Evals](../track-evals/why-evals.md)
- [Học phần 6 — Production](../course-6-production/from-prototype.md): từ bản thử nghiệm đến triển khai thực tế, và kế hoạch ngày đầu tiên
