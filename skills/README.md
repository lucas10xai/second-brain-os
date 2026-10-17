# skills

Mười tám kỹ năng (skills) bao quát toàn bộ các quy trình làm việc trong cẩm nang hướng dẫn. Tất cả đều là các file `SKILL.md` thuần túy, vì vậy chúng hoạt động trực tiếp với Claude Code cũng như bất kỳ agent nào hỗ trợ định dạng Agent Skills.

| Kỹ năng | Chức năng |
|---|---|
| `second-brain-backfill` | Nhập bổ sung kho lưu trữ cũ (Backfill an archive) |
| `second-brain-changed-my-mind` | Truy vết sự thay đổi quan điểm (Trace changed positions) |
| `second-brain-chat-import` | Nhập lịch sử trò chuyện (Import chat history) |
| `second-brain-graph` | Phân tích đồ thị liên kết (Analyse the graph) |
| `second-brain-ingest` | Nạp tài liệu nguồn (Ingest a source) |
| `second-brain-lint` | Kiểm lỗi cấu trúc vault (Lint the vault) |
| `second-brain-merge` | Gộp các trang trùng lặp (Merge duplicate pages) |
| `second-brain-metrics` | Ghi nhận chỉ số sức khỏe (Record metrics) |
| `second-brain-privacy` | Kiểm toán quyền riêng tư (Audit privacy) |
| `second-brain-project` | Thiết lập dự án mới (Set up a project) |
| `second-brain-publish` | Chuẩn bị xuất bản công khai (Prepare to publish) |
| `second-brain-query` | Truy vấn tri thức trong vault (Query the vault) |
| `second-brain-quiz` | Tự kiểm tra kiến thức từ trang đã lưu (Quiz from your own pages) |
| `second-brain-rename` | Đổi tên trang an toàn (Rename a page) |
| `second-brain-report` | Viết báo cáo nghiên cứu (Write a research report) |
| `second-brain-review` | Tổng kết định kỳ vault (Review the vault) |
| `second-brain-transcript` | Làm sạch bản gỡ băng (Clean a transcript) |
| `second-brain-write` | Viết bài từ tư liệu trong vault (Write from the vault) |

## Cài đặt

```bash
mkdir -p ~/.claude/skills
cp -r skills/second-brain-* ~/.claude/skills/
```

Hoặc đặt chúng ngay bên trong vault tại `.claude/skills/` để chúng luôn đi kèm với vault và được quản lý phiên bản (versioned) cùng với các ghi chú của bạn.

## Những kỹ năng nào quan trọng nhất

`second-brain-ingest` và `second-brain-query` là trụ cột gánh vác toàn bộ hệ thống. Quy tắc liên kết ở kỹ năng thứ nhất và quy tắc trích dẫn ở kỹ năng thứ hai là hai chốt chặn giữ cho một vault không bị thoái hóa thành một thư mục chỉ chứa các bản tóm tắt rời rạc; chỉ cần nới lỏng một trong hai, mọi phần còn lại sẽ mất đi giá trị.

Tất cả các kỹ năng còn lại bạn đều có thể tùy chỉnh thoải mái. Đây là những góc nhìn mang tính định hướng, và cách làm của bạn hoàn toàn có thể khác.
