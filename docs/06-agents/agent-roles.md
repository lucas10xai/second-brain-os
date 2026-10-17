# Các vai trò của Agent

Một `Agent` ôm đồm mọi việc sẽ tạo ra kết quả tầm thường ở mọi khâu. Những chỉ dẫn tạo nên một bộ nạp dữ liệu (`ingestor`) giỏi hoàn toàn khác với những chỉ dẫn tạo nên một người rà soát (`reviewer`) giỏi, và khi bị nhồi nhét chung vào một prompt, chúng sẽ làm loãng lẫn nhau.

Sáu vai trò là đủ để bao quát toàn bộ một `Vault`, trong đó có bốn vai trò chỉ đọc (read-only). Các định nghĩa chi tiết nằm trong thư mục [`agents/`](../../agents/README.md).

## Ingestor (Bộ nạp dữ liệu)

Đọc thư mục `raw/`, viết các trang vào `wiki/`, liên kết chúng, cập nhật `index.md` và `log.md`. Vai trò này thực hiện thao tác ghi nhiều hơn bất kỳ vai trò nào khác, và chất lượng đầu ra của nó quyết định mọi thứ ở các khâu phía sau.

Chỉ dẫn dành cho nó được giới hạn hẹp một cách có chủ đích: nó không trả lời câu hỏi, không tái cấu trúc các trang hiện có ngoài việc thêm liên kết mới, và không xóa bất kỳ thứ gì. Một `ingestor` vừa nạp dữ liệu vừa sắp xếp lại tổ chức trang sẽ tạo ra những lượt chạy mà bạn không thể nào kiểm duyệt (review) nổi, bởi vì các thay đổi về nội dung và các thay đổi về cấu trúc bị trộn lẫn vào nhau trong cùng một bản diff.

## Linker (Bộ kết nối liên kết)

Tìm kiếm các mối liên hệ giữa những trang hiện có mà quá trình `Ingest` đã bỏ sót.

Chạy sau các đợt nhập dữ liệu lớn và định kỳ hàng tuần. Chỉ thêm liên kết, không tạo trang mới, không viết lại nội dung. Việc tách riêng nó khỏi `ingestor` rất quan trọng vì để liên kết tốt đòi hỏi phải đọc rộng khắp toàn bộ `Vault` — một công việc hoàn toàn khác với việc đọc kỹ từng tài liệu nguồn đơn lẻ.

Quy tắc duy nhất của nó: bất kỳ liên kết nào nó thêm vào phải là một liên kết mà chính bạn cũng sẽ đồng tình khi đặt hai trang đó cạnh nhau để đọc. Một `linker` chỉ chăm chăm tối ưu số lượng liên kết sẽ làm suy thoái chất lượng đồ thị trong khi bề ngoài trông có vẻ rất năng suất.

## Reviewer (Bộ rà soát định kỳ)

Chỉ đọc (Read-only). Tạo ra bản báo cáo rà soát định kỳ: những gì đã thay đổi, sự chú ý của bạn đã dồn vào đâu, nội dung nào đang mâu thuẫn với nội dung nào, và tiếp theo nên đọc gì.

Cơ chế chỉ đọc không phải vì sự thận trọng quá mức, mà chính là yếu tố làm nên độ tin cậy của bản rà soát. Một `reviewer` có quyền chỉnh sửa sẽ tiện tay sửa luôn những lỗi nhỏ trên đường đi, và kết quả là bản báo cáo của nó lại mô tả một `Vault` đã không còn tồn tại như lúc đầu nữa.

## Researcher (Bộ nghiên cứu truy vấn)

Chỉ đọc (Read-only). Trả lời các câu hỏi dựa trên dữ liệu trong `Vault`, trích dẫn trang rõ ràng, và chỉ đích danh những thông tin nào đang còn thiếu.

Đây cũng là vai trò mà bạn trò chuyện nhiều nhất, và là vai trò cần tuân thủ nghiêm ngặt nhất quy tắc không được tự ý lấy kiến thức phổ thông bên ngoài để trả lời thay cho `Vault`. Xem thêm [skill truy vấn (query skill)](../../skills/README.md).

## Graph analyst (Bộ phân tích đồ thị)

Chỉ đọc (Read-only). Chạy tính toán các chỉ số đo lường, tìm kiếm các trang trung tâm (hubs), trang cầu nối (bridges) và các cụm (clusters), đồng thời giải thích ý nghĩa của những con số đó đối với chất lượng truy xuất. Chạy định kỳ hàng tháng.

Được tách riêng khỏi bộ kiểm tra lỗi (`linter`) bởi vì việc phân tích và việc sửa chữa đòi hỏi hai khuynh hướng hoàn toàn trái ngược nhau: một bên cần quan sát và nhận diện mọi thứ, bên kia lại cần can thiệp ít nhất có thể.

## Curator (Bộ giám tuyển nội dung)

Chỉ đọc (Read-only). Đề xuất những trang nào cần cắt tỉa (prune), lưu trữ (archive) hoặc gộp lại (merge), chạy định kỳ hàng quý.

Chỉ đưa ra đề xuất, tuyệt đối không tự thực thi hành động. Xóa bỏ là thao tác duy nhất bạn không thể khôi phục bằng cách đọc lướt qua bản diff, vì vậy nó luôn phải là quyết định do chính chủ nhân của `Vault` đưa ra.

## Những vai trò không đáng tạo ra

**Bộ xóa dữ liệu (Deleter).** Việc xóa trang phải là quyết định của bạn, được thực thi có lưu vết nhật ký. `curator` đề xuất; bạn định đoạt.

**Bộ tóm tắt (Summariser).** Việc tóm tắt lại những trang vốn dĩ đã là bản chất lọc sẽ sinh ra một tầng thông tin kém chân thực hơn phần gốc nằm bên dưới, nhưng người ta lại cứ đọc nó thay vì đọc bản gốc.

**Bộ gắn thẻ (Tagger).** Gắn thẻ là một phán đoán chỉ mất năm giây được thực hiện ngay trong lúc `Ingest` khi đang có đầy đủ ngữ cảnh nhất. Một lượt chạy tách biệt sau đó có ít ngữ cảnh hơn và chỉ tạo ra những thẻ kém chất lượng hơn.

## Chuyển giao công việc giữa các vai trò (Handoffs)

Các vai trò giao tiếp với nhau thông qua chính `Vault`, chứ không gọi trực tiếp nhau. `ingestor` ghi các khoảng trống (gaps) vào `index.md`; `linker` đọc chúng từ đó. `ingestor` ghi nhật ký lượt chạy vào `log.md`; `reviewer` đọc nhật ký để tổng hợp.

Đây là thiết kế có chủ đích. Lấy file làm giao diện chung (interface) có nghĩa là bất kỳ lượt chạy nào cũng có thể kiểm tra lại sau đó, và bạn có thể thay thế một vai trò bất kỳ mà không hề làm ảnh hưởng đến các vai trò còn lại.

## Tiếp theo

[Lập lịch tự động (Scheduling)](scheduled-maintenance.md)
