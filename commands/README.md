# commands

Bảy mươi hai lệnh gạch chéo (slash commands) dành cho Claude Code, được nhóm theo công việc bạn đang thực hiện.

```bash
mkdir -p ~/brain/.claude/commands
cp commands/*.md ~/brain/.claude/commands/ && rm ~/brain/.claude/commands/README.md
```

Hãy loại bỏ file README này khi sao chép: bất kỳ file nào trong `.claude/commands/` đều sẽ trở thành một lệnh gạch chéo, và `/README` chắc chắn không phải là lệnh bạn muốn.

Các lệnh được thiết kế mỏng có chủ đích: mỗi lệnh chỉ trỏ tới một skill và xác định phạm vi hoạt động của nó. Hành vi thực sự nằm ở trong skill, vì vậy dù bạn chạy `/ingest-youtube`, chạy tác vụ định kỳ hay yêu cầu bằng ngôn ngữ tự nhiên thì tất cả đều cho ra cùng một kết quả.

Hầu hết các lệnh đều nhận một tham số tùy chọn. Nếu không truyền tham số, chúng sẽ mặc định áp dụng cho phạm vi tổng thể hợp lý nhất: `/lint` kiểm tra toàn bộ kho tri thức, `/ingest` xử lý mọi tài liệu đang chờ trong `raw/`.

### Nạp dữ liệu (Ingestion)

| Lệnh | Chức năng |
|---|---|
| `/ingest` | Nạp tài liệu mới từ raw/ vào wiki |
| `/ingest-url` | Lưu và nạp một trang web |
| `/ingest-youtube` | Nạp bản gỡ băng video hoặc podcast |
| `/ingest-pdf` | Nạp một file PDF |
| `/ingest-paper` | Nạp một bài báo khoa học |
| `/ingest-chats` | Nhập lịch sử trò chuyện đã xuất |
| `/ingest-voice` | Nạp một ghi chú giọng nói |
| `/ingest-newsletter` | Nạp bản tin (newsletter) không gây trùng lặp |
| `/ingest-highlights` | Nạp các đoạn tô sáng (highlights) từ sách hoặc bài viết |
| `/backfill` | Nhập hàng loạt kho lưu trữ theo từng đợt |

### Cấu trúc hóa (Structuring)

| Lệnh | Chức năng |
|---|---|
| `/link` | Tìm và bổ sung các liên kết còn thiếu |
| `/dedupe` | Tìm các trang gần như trùng lặp |
| `/merge` | Gộp hai trang làm một |
| `/rename` | Đổi tên trang và cập nhật mọi liên kết |
| `/split` | Tách một trang bị quá tải nội dung |
| `/retype` | Sửa lại phân loại trang |
| `/schema` | Kiểm tra frontmatter theo đúng schema |
| `/tags` | Kiểm toán bộ từ vựng thẻ (tag) |
| `/aliases` | Tìm các tên gọi thay thế (aliases) còn thiếu |
| `/contradictions` | Liệt kê các mâu thuẫn chưa được giải quyết |
| `/index` | Xây dựng lại trang chỉ mục |

### Đồ thị (Graph)

| Lệnh | Chức năng |
|---|---|
| `/graph` | Báo cáo hình thái của đồ thị tri thức |
| `/graph-export` | Xuất đồ thị để phân tích bên ngoài |
| `/orphans` | Tìm các trang mồ côi không thể truy cập |
| `/hubs` | Tìm các trang trung tâm đang nuốt chửng đồ thị |
| `/bridges` | Tìm các trang cầu nối giữ đồ thị liên kết với nhau |
| `/clusters` | Cho biết kho tri thức thực sự xoay quanh những cụm chủ đề nào |
| `/typed-links` | Bổ sung loại quan hệ cho liên kết ở những nơi cần thiết |
| `/stale` | Tìm các trang khái niệm lâu ngày chưa được cập nhật |

### Truy xuất (Retrieval)

| Lệnh | Chức năng |
|---|---|
| `/ask` | Đặt câu hỏi và chỉ trả lời từ dữ liệu trong kho tri thức |
| `/know` | Tôi đang biết những gì về một chủ đề |
| `/connect` | Tìm đường dẫn kết nối giữa hai ý tưởng |
| `/compare` | So sánh hai đối tượng dựa trên các nguồn của chính bạn |
| `/sources` | Hiển thị các nguồn làm cơ sở cho một nhận định |
| `/gaps` | Những khoảng trống nào còn thiếu trong hiểu biết của tôi |
| `/contradicts` | Phản biện lại quan điểm của tôi |
| `/timeline` | Các nguồn tài liệu của tôi đã phát triển theo thời gian như thế nào |
| `/trace` | Hiển thị những trang nào đã được dùng để tạo câu trả lời |
| `/changed-my-mind` | Những quan điểm tôi đã thay đổi hoặc điều chỉnh |

### Bảo trì (Maintenance)

| Lệnh | Chức năng |
|---|---|
| `/lint` | Kiểm toán cấu trúc và tự động sửa các lỗi cơ học |
| `/health` | Kiểm tra nhanh sức khỏe kho tri thức |
| `/metrics` | Ghi lại bản chụp chỉ số có gắn ngày tháng |
| `/review` | Ôn tập định kỳ những gì kho tri thức đã học được |
| `/weekly` | Tổng kết hàng tuần |
| `/monthly` | Đánh giá cấu trúc hàng tháng |
| `/prune` | Tìm những nội dung có thể xóa an toàn |
| `/archive` | Chuyển tài liệu ít dùng ra khỏi wiki |
| `/commit` | Commit trạng thái hiện tại với thông điệp hữu ích |

### Đầu ra (Outputs)

| Lệnh | Chức năng |
|---|---|
| `/outline` | Lập dàn ý bài viết từ các trang khái niệm của bạn |
| `/draft` | Viết bản nháp từ kho tri thức |
| `/report` | Viết báo cáo nghiên cứu |
| `/publish` | Kiểm tra những nội dung an toàn để xuất bản |
| `/export` | Xuất một trang hoặc một tập hợp trang |
| `/quiz` | Tự kiểm tra kiến thức trên chính các trang của bạn |
| `/explain` | Tự giải thích lại để tìm ra khoảng trống kiến thức |
| `/ingest-mine` | Nạp tác phẩm đã hoàn thành của chính bạn |

### Dự án (Projects)

| Lệnh | Chức năng |
|---|---|
| `/project` | Tạo một dự án mới |
| `/project-status` | Kiểm tra tiến độ hiện tại của dự án |
| `/decisions` | Liệt kê các quyết định đã đưa ra |
| `/commitments` | Liệt kê các cam kết đang mở |
| `/handoff` | Chuẩn bị bản tóm tắt bàn giao công việc |
| `/scope` | Kéo tri thức liên quan vào một dự án |

### An toàn (Safety)

| Lệnh | Chức năng |
|---|---|
| `/privacy` | Kiểm toán những nội dung không nên có trong kho tri thức |
| `/secrets` | Quét tìm thông tin xác thực và khóa bí mật |
| `/dry-run` | Xem trước kết quả chạy thử mà không ghi vào file |
| `/rollback` | Hoàn tác lần chạy gần nhất |
| `/audit` | Kiểm toán những gì agent đã thực hiện |

### Thiết lập (Setup)

| Lệnh | Chức năng |
|---|---|
| `/init` | Khởi tạo khung thư mục cho kho tri thức mới |
| `/claude-md` | Xây dựng hoặc cập nhật file CLAUDE.md của bạn |
| `/install` | Cài đặt bộ skills, commands và agents |
| `/doctor` | Kiểm tra thiết lập hệ thống có hoạt động bình thường không |
| `/schedule` | Thiết lập lịch bảo trì định kỳ |

## Tại sao lại có nhiều lệnh đến vậy

Chín lệnh trong số này thực hiện phần việc cốt lõi, còn lại là các điểm truy cập đã được giới hạn phạm vi sẵn trỏ vào cùng những skill đó. Đó chính là mục đích thiết kế: bạn không cần phải nhớ cách diễn đạt câu lệnh cho một việc mà tuần nào bạn cũng làm.

Nếu thiếu một lệnh bạn cần, thường chỉ cần viết một dòng trỏ tới một skill sẵn có. Hãy sao chép file lệnh gần giống nhất và thay đổi phạm vi của nó.
