# Git, đồng bộ hóa và sao lưu

Bản chất một Vault chỉ là một thư mục chứa các file văn bản, điều này biến nó thành một kho lưu trữ Git (git repository) gần như lý tưởng — và chính Git là mảnh ghép giúp việc cho phép Agent tự động chạy ngầm không cần giám sát trở nên an toàn tuyệt đối.

Nếu không có hệ thống quản lý phiên bản, một lượt chạy lỗi của Agent sẽ trở thành một vụ án bí ẩn không lời giải. Ngược lại, khi có Git, mọi thay đổi do Agent tạo ra đều hiện rõ thành từng dòng so sánh (diff) mà bạn có thể đọc duyệt và hoàn tác chỉ bằng một câu lệnh duy nhất.

```bash
cd ~/brain
git init
git add .
git commit -m "initial vault"
```

## Những file cần loại trừ (.gitignore)

```
.obsidian/workspace*
.obsidian/cache
.DS_Store
.trash/
```

Hãy đưa toàn bộ phần còn lại của thư mục `.obsidian/` vào commit để danh sách plugin cùng các thiết lập cá nhân của bạn luôn đi theo Vault. Tuyệt đối không bao giờ commit các khóa API; khóa của plugin Local REST API nằm bên trong thư mục dữ liệu của plugin, vì vậy hãy kiểm tra kỹ xem `.obsidian/plugins/` đang chứa những gì trước khi thực hiện lệnh `git push` đầu tiên.

Nếu có bất kỳ phần nội dung nào trong Vault mang tính riêng tư, hãy đặt kho lưu trữ từ xa (remote repository) ở chế độ riêng tư (private). Một Second Brain chính là một trong những tài liệu chứa mật độ thông tin nhạy cảm cao nhất về một con người.

## Tạo thói quen commit bọc quanh các lượt chạy của Agent

Hãy tạo một bản commit trước khi chạy một đợt Ingest lớn và thêm một bản commit nữa ngay sau khi hoàn tất. Nhờ đó, nếu cả lô xử lý gặp lỗi, bạn chỉ cần gõ `git checkout .` thay vì mất cả buổi chiều ngồi sửa lại từng file bằng tay. Các tác vụ chạy tự động theo lịch cũng nên tự động commit kết quả của chính mình kèm theo thông điệp ghi rõ tên lượt chạy, để lịch sử thay đổi vẫn dễ dàng tra cứu lại sau hàng tháng trời.

## Đồng bộ hóa giữa nhiều thiết bị

- **Git remote:** miễn phí, có quản lý lịch sử phiên bản, hoạt động ở mọi môi trường, chỉ đòi hỏi bạn duy trì thói quen `pull` và `push` đều đặn.
- **Obsidian Sync:** trả phí, mã hóa đầu cuối (end-to-end encrypted), xử lý đồng bộ trên thiết bị di động cực kỳ mượt mà.
- **Các dịch vụ ổ đĩa đám mây thông thường (Google Drive, iCloud, Dropbox):** dùng được, nhưng kèm theo một lưu ý quan trọng. Việc trình đồng bộ đám mây tự động ghi lại file đúng vào lúc Agent cũng đang mở file đó để ghi sẽ tạo ra hàng loạt bản sao xung đột (conflict copies). Nếu bạn chọn hướng này, hãy giới hạn việc chạy các tác vụ Agent kéo dài cố định trên một máy tính duy nhất.

## Sao lưu dữ liệu (Backups)

Đồng bộ hóa không phải là sao lưu. Một công cụ đồng bộ hóa sẽ nhân bản một lệnh xóa nhầm tai hại sang toàn bộ mọi thiết bị của bạn ngay lập tức.

Hãy luôn duy trì ít nhất một bản sao nằm tách biệt hoàn toàn khỏi luồng đồng bộ tự động: chẳng hạn như nén lưu trữ định kỳ ra ổ cứng gắn ngoài hoặc đẩy lên một kho lưu trữ từ xa độc lập. Hãy thử diễn tập khôi phục dữ liệu (restore) một lần trước khi bạn thực sự rơi vào tình huống khẩn cấp. Rủi ro lớn nhất mà bạn cần phòng vệ ở đây không phải là việc hỏng ổ cứng vật lý, mà là trường hợp một tiến trình tự động hóa âm thầm viết đè làm hỏng hai trăm trang wiki từ ba tuần trước mà bạn không hề hay biết.

## Tiếp theo

Hệ thống Vault đến đây đã được thiết lập hoàn chỉnh. Hãy chuyển sang chương [Thu thập dữ liệu (Ingestion)](../03-ingestion/README.md) để bắt đầu nạp tư liệu cho nó, hoặc đọc chương [Cấu trúc hóa](../04-structuring/README.md) để nắm vững các quy tắc định hình diện mạo chuẩn cho từng trang wiki.
