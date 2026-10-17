# Nạp bù dữ liệu tồn đọng nhiều năm (Bulk backfill)

Sẽ đến lúc bạn muốn nhập toàn bộ kho dữ liệu cũ của mình vào hệ thống: thư mục dấu trang (bookmarks) tích tụ nhiều năm, thư mục tải xuống (Downloads), ba năm lịch sử trò chuyện AI, hay danh sách đọc sau chất chứa tám trăm bài viết chưa mở.

Đây chính là lượt chạy dễ gặp thảm họa nhất. Nó tiêu tốn nhiều chi phí, mất hàng giờ đồng hồ xử lý, và nếu thực hiện sai thứ tự, nó sẽ biến hệ thống wiki thành một bãi tập kết hỗn độn thay vì một cấu trúc tri thức mạch lạc. Nhưng đồng thời, đây cũng là lượt chạy có thể biến Vault của bạn trở nên cực kỳ hữu ích chỉ sau một buổi ngồi làm, vì vậy rất đáng để thực hiện một cách cẩn trọng.

## Thứ tự xử lý quyết định tất cả

Hãy luôn xử lý từ tài liệu cũ nhất trở đi.

Lý do là vì các nguồn tài liệu mới hơn cần cập nhật và bổ sung vào những trang mà các nguồn tài liệu cũ trước đó đã khởi tạo nên. Khi chạy theo đúng trình tự thời gian từ cũ đến mới, hệ thống wiki sẽ phản ánh trung thực quá trình nhận thức của bạn phát triển dần ra sao: từ trang ghi chú ban đầu về một chủ đề, tiếp đến là những đính chính bổ sung, và cuối cùng là quan điểm hoàn thiện hiện tại.

Ngược lại, nếu bạn nạp từ tài liệu mới nhất lùi về cũ, mọi nguồn tư liệu cũ khi đi vào hệ thống sẽ bị coi là một thông tin mâu thuẫn cần phải hòa giải với một trang wiki vốn đã mang sẵn kết luận cuối cùng. Agent sẽ phải tốn công sức vô ích để xử lý mâu thuẫn ngược, dòng thời gian lịch sử bị đảo lộn hoàn toàn, và bạn đánh mất đúng giá trị quý giá nhất mà cấu trúc này mang lại so với một công cụ tìm kiếm thông thường.

## Luôn luôn chia theo từng lô nhỏ (Batching)

Chỉ xử lý mười nguồn tài liệu mỗi lô (batch). Sau khi xong mỗi lô: cập nhật `index.md`, ghi nối vào `log.md`, tạo bản commit Git, và xuất báo cáo ngắn.

```
/backfill raw/archive/2024
```

Lệnh `backfill` nằm trong thư mục [`commands/`](../../commands/README.md) được thiết kế vận hành theo đúng nguyên tắc này và sẽ tự động tạm dừng giữa các lô để chờ bạn xác nhận cho phép chạy tiếp.

Việc chia lô tồn tại vì ba lý do sống còn. Thứ nhất, chi phí luôn hiển thị rõ ràng trong tầm mắt khi bạn vẫn còn kịp bấm dừng. Thứ hai, chất lượng luôn nằm trong tầm kiểm soát, giúp bạn phát hiện sớm lỗi hợp đồng định dạng trang (page contract) ngay ở trang thứ mười thay vì đợi đến khi hỏng mất bốn trăm trang. Và thứ ba, nếu tiến trình chẳng may bị treo giữa chừng, bạn chỉ mất công chạy lại đúng một lô nhỏ thay vì mất trắng cả buổi chạy.

## Kiểm tra thật kỹ lô đầu tiên

Hãy đọc từng trang một mà lô đầu tiên vừa tạo ra. Đọc hết không sót trang nào.

Đây là thời điểm vàng để bắt gọn các lỗi mang tính hệ thống: những trang chỉ tóm tắt nông cạn thay vì giải thích sâu bản chất, các khái niệm bị chia nhỏ vụn vặt quá mức, các liên kết chỉ mang tính trang trí hình thức, hoặc cấu trúc Frontmatter bị lệch chuẩn. Hãy chỉnh sửa lại file `CLAUDE.md` và chạy lại lô đầu tiên cho đến khi ưng ý rồi mới cho phép chạy tiếp các lô sau.

Một hạt sạn bạn tặc lưỡi cho qua ở lô thứ nhất sẽ nhân bản thành lỗi trên bốn trăm trang vào cuối buổi, và chi phí để dọn dẹp đống hỗn độn đó về sau sẽ đắt đỏ hơn nhiều so với chi phí chạy ban đầu.

## Kiểm soát chi phí

Việc nạp bù một nghìn nguồn tài liệu sẽ tạo ra một hóa đơn tiền token không hề nhỏ. Dưới đây là những cách giữ cho chi phí nằm trong ngưỡng hợp lý:

- **Lọc thô trước tiên.** Phần lớn các kho lưu trữ cũ có tới một nửa là các đường dẫn đã chết và những thứ bạn bấm lưu theo quán tính chứ chẳng bao giờ đọc. Hãy để Agent duyệt qua danh sách tiêu đề để phân loại sơ bộ trước khi bắt tay vào Ingest thực sự.
- **Giới hạn kích thước mỗi lô** và theo dõi sát chi phí thực tế của vài lô đầu tiên trước khi mở rộng quy mô.
- **Bỏ qua tầng lưu trữ lạnh.** Không phải tài liệu nào cũng cần đúc thành trang wiki riêng; việc giữ nguyên các tư liệu ít quan trọng nằm trong `raw/` vẫn đảm bảo bạn có thể tìm kiếm toàn văn trên đó bất cứ lúc nào cần.

## Xử lý các đường dẫn đã chết (Dead links)

Các file xuất dấu trang (bookmarks) từ nhiều năm trước thường chứa đầy những trang web nay đã không còn tồn tại. Hãy kiểm tra tình trạng sống chết của đường dẫn trước khi Ingest thay vì để chạy được nửa đường mới phát hiện ra:

```bash
python3 -c "import sys,urllib.request as u;[print(l.strip()) for l in sys.stdin]"
```

Đối với những bài viết giá trị nhưng trang gốc đã biến mất, kho lưu trữ Internet Archive (Wayback Machine) thường vẫn giữ được bản sao. Hãy lưu nội dung từ đó về và ghi chú rõ trong phần Frontmatter rằng đường dẫn gốc đã chết — bởi một trang nguồn trỏ tới địa chỉ báo lỗi 404 sẽ không thể kiểm chứng lại được sau này.

## Tiếp tục lại sau khi tạm dừng (Resuming)

Hãy ghi nhận tiến độ vào file `log.md` xuyên suốt quá trình chạy, mỗi lô một dòng nêu rõ thư mục và phạm vi các file đã xử lý xong. Khi tiến trình bị ngắt giữa chừng — và thực tế khi chạy dữ liệu lớn chắc chắn sẽ có lúc dừng — bạn có thể dựa vào nhật ký để chạy tiếp từ điểm dừng một cách chính xác thay vì phải ngồi đoán xem những file nào đã được nạp xong.

## Sau khi hoàn tất đợt nạp bù

Hãy chạy kiểm tra lỗi (Lint) trên toàn bộ hệ thống. Một đợt nhập dữ liệu quy mô lớn luôn để lại các trang mồ côi, các trang gần như trùng lặp và những liên kết chưa hoàn chỉnh.

```
/lint
```

Sau đó, hãy chạy lệnh rà soát tổng quan để xem Vault của bạn hiện đang nắm giữ những tri thức gì — bởi sau một đợt nạp bù lớn, hệ thống sẽ biết rõ những điều mà chính bạn đã quên bẵng là mình từng lưu lại. Khoảnh khắc khám phá lại kho tàng đó chính là phần thưởng xứng đáng nhất cho toàn bộ công sức bạn vừa bỏ ra.

## Tiếp theo

Chuyển sang chương [Cấu trúc hóa](../04-structuring/README.md) để nắm vững các quy tắc định hình diện mạo và cấu trúc chi tiết của toàn bộ các trang wiki này.
