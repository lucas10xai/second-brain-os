# Obsidian và Vault đầu tiên của bạn

Obsidian đóng vai trò là nửa lưu trữ trong hệ thống này. Ứng dụng hoàn toàn miễn phí, lưu giữ mọi thứ dưới dạng các file văn bản thuần túy ngay trên máy tính của bạn, và trực quan hóa các liên kết giữa những ghi chú thành một đồ thị. Không có bất kỳ dữ liệu nào bị đẩy lên đám mây của nhà sản xuất, và toàn bộ các file vẫn có thể mở đọc bình thường bằng bất kỳ trình soạn thảo văn bản nào nếu sau này bạn không dùng ứng dụng nữa.

## Cài đặt

Tải ứng dụng tại [obsidian.md](https://obsidian.md) và tiến hành cài đặt.

Nếu bạn đã chạy các câu lệnh Quickstart ở trang [README](../../README.md), trên máy của bạn đã có sẵn thư mục `~/brain` chứa cấu trúc mẫu khởi đầu. Tại màn hình chào mừng của Obsidian, hãy bấm vào **Open folder as vault** và chọn thư mục đó.

Nếu bạn bắt đầu từ con số không, hãy bấm vào **Create new vault**. Đặt cho nó một cái tên ngắn gọn mà bạn có thể gõ nhanh thường xuyên, chẳng hạn như `brain`. Chọn một thư mục lưu trữ trên máy tính và bấm **Create**, sau đó sao chép toàn bộ nội dung bên trong thư mục [`vault-template/`](../../vault-template/) vào đó.

Dù theo cách nào, thư mục đó giờ đây chính là Second Brain của bạn. Mọi nội dung do Agent viết ra đều sẽ nằm tại đây dưới dạng các file Markdown.

## Tự tay tạo một ghi chú đầu tiên

Hãy làm thử thao tác này một lần trước khi tự động hóa bất cứ thứ gì, để bạn nắm rõ cơ chế hoạt động thực tế chứ không chỉ hình dung trừu tượng.

Hãy bấm vào biểu tượng tạo ghi chú mới, gõ một câu bất kỳ, sau đó gõ `[[goals]]`. Từ nằm trong cặp ngoặc vuông sẽ lập tức biến thành một liên kết trỏ tới trang có tên `goals`, bất kể trang đó đã tồn tại hay chưa. Khi bạn nhấp chuột vào liên kết đó, Obsidian sẽ tự động tạo ra trang mới.

Toàn bộ mô hình dữ liệu chỉ đơn giản như vậy: các ghi chú trỏ sang các ghi chú khác. Mọi công việc mà Agent thực hiện về sau đều chỉ là thao tác này, nhưng ở quy mô lớn và bạn không phải tự tay làm.

## Nên đặt thư mục Vault ở đâu

Hãy đặt nó ở một vị trí có đường dẫn ổn định, dễ gõ từ cửa sổ dòng lệnh (terminal). Tránh đặt trong các thư mục mà trình đồng bộ đám mây (cloud sync client) liên tục can thiệp ghi lại file, bởi việc một Agent đang ghi file cùng lúc với trình đồng bộ đám mây sẽ đẻ ra hàng loạt bản sao xung đột (conflict copies) cực kỳ đau đầu khi phải dọn dẹp. Hãy xem bài [Git, đồng bộ hóa và sao lưu](git-and-sync.md) để chọn các phương án đồng bộ an toàn.

Tránh đặt tên thư mục có chứa khoảng trắng (dấu cách), vì bạn sẽ thường xuyên phải dán đường dẫn này vào các câu lệnh.

## Những thiết lập đáng thay đổi ngay từ đầu

- **Files and links → New link format:** chọn đường dẫn tương đối (`Relative path to file`) hoặc đường dẫn ngắn nhất (`Shortest path when possible`), và giữ nhất quán một kiểu duy nhất. Việc trộn lẫn nhiều định dạng đường dẫn chính là nguyên nhân phổ biến nhất gây gãy liên kết sau khi đổi tên file.
- **Files and links → Automatically update internal links:** bật (`On`).
- **Editor → Show frontmatter:** bật (`On`). Bạn sẽ muốn nhìn thấy rõ phần siêu dữ liệu (metadata) mà Agent ghi vào đầu mỗi trang, ít nhất là trong vài tuần đầu tiên.

## Tiếp theo

[Chạy Claude Code bên trong Vault](claude-code-setup.md)
