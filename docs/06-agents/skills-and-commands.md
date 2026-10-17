# Skills và Slash commands

Hai cơ chế trông có vẻ giống nhau nhưng thực chất đảm nhận hai công việc khác nhau.

**Một `Skill`** dạy cho `Agent` một hành vi có thể lặp lại. Nó tự động được nạp vào khi phù hợp với ngữ cảnh và định hình cách `Agent` thực hiện công việc, bất kể là bạn gọi tên nó một cách tường minh hay chỉ mô tả yêu cầu bằng lời tự nhiên.

**Một `Slash command`** (lệnh gạch chéo) là phím tắt cho một tác vụ bạn thường xuyên chạy. Nó trỏ tới một skill và giúp bạn tiết kiệm công sức gõ lại các dòng chỉ dẫn.

Hành vi xử lý cốt lõi phải nằm ở trong skill. Nhờ vậy, quá trình `Ingest` sẽ luôn hoạt động theo cùng một chuẩn mực thống nhất, dù nó được kích hoạt bằng lệnh `/ingest`, bởi một tác vụ chạy theo lịch định kỳ, hay chỉ bằng câu nói tự nhiên của bạn: *"thêm tài liệu này vào `Vault` giúp tôi"*.

## Những gì kho mã nguồn (repo) này cung cấp sẵn

Mười tám `Skills` nằm trong thư mục [`skills/`](../../skills/README.md), mỗi skill tương ứng với một `Workflow` trong hướng dẫn này. Bảy mươi hai lệnh trong thư mục [`commands/`](../../commands/README.md), mỗi lệnh chỉ dài vài dòng trỏ về một skill tương ứng và thiết lập phạm vi (scope) hoạt động cho nó.

Tỷ lệ chênh lệch này là có chủ đích. Hành vi cốt lõi chỉ nên nằm gọn trong một số lượng nhỏ các `Skills` được biên soạn kỹ lưỡng; còn các lệnh (`commands`) thì rất nhẹ và dễ tạo, nên chẳng có lý do gì bắt bạn phải nhớ cách diễn đạt dài dòng cho một yêu cầu mà tuần nào bạn cũng dùng tới.

Hãy cài đặt chúng ngay bên trong `Vault` tại đường dẫn `.claude/skills/` và `.claude/commands/` để chúng được quản lý phiên bản cùng với kho ghi chú và luôn đi kèm theo `Vault` tới bất cứ đâu.

## Tự viết Skill của riêng bạn

Một skill đáng để viết ra khi hội tụ đủ ba tính chất: bạn lặp đi lặp lại việc đó nhiều lần, bạn có quan điểm và tiêu chuẩn riêng về cách thực hiện nó, và những tiêu chuẩn đó không đủ hiển nhiên để mô hình có thể tự đoán trúng.

Cấu trúc hiệu quả trên thực tế:

```markdown
---
name: skill-name
description: >-
  Nó làm việc gì. Khi nào cần dùng nó, được viết với giọng điệu thúc giục mạnh mẽ, bởi vì các Agent
  thường có xu hướng lười kích hoạt skill. Tuyệt đối KHÔNG dùng cho các trường hợp gần giống dễ gây nhầm lẫn.
---

# Tên Skill

[Lý do skill này tồn tại: nó ngăn chặn kiểu lỗi cụ thể nào. Đoạn văn mở đầu này chính là kim chỉ nam (rubric)
để Agent tự suy luận cho mọi trường hợp ngoại lệ mà các quy tắc bên dưới chưa liệt kê hết.]

## Quy tắc cốt lõi (Core rule)
## Quy trình thực hiện (Workflow)
## Định dạng đầu ra (Output format)
## Tinh chỉnh (Calibration)
## Ví dụ (Example)
```

Đoạn văn mở đầu làm được nhiều việc hơn cả danh sách các quy tắc cộng lại. Các quy tắc chỉ bao phủ được những trường hợp bạn đã nghĩ tới; còn lý do tồn tại sẽ bao phủ toàn bộ phần còn lại.

## Hãy giải thích lý do "Tại sao"

Chỉ dẫn kiểu *"Không bao giờ được ghi đè lên một thông tin mâu thuẫn"* sẽ bị áp dụng một cách máy móc theo nghĩa đen và thất bại ngay ở các trường hợp biên (edge cases). Ngược lại, chỉ dẫn *"Không bao giờ được ghi đè lên một thông tin mâu thuẫn, bởi vì lịch sử những gì bạn từng tin tưởng chính là tài sản duy nhất mà `Vault` này có được còn công cụ tìm kiếm thì không"* sẽ giúp mô hình tự khái quát hóa để xử lý đúng ngay cả trong những tình huống bạn chưa từng mô tả.

Một chữ NEVER viết hoa toàn bộ mà không kèm theo lời giải thích thường là dấu hiệu của một chỉ dẫn còn thiếu chiều sâu.

## Quản lý phiên bản (Versioning)

Các `Skills` nằm ngay bên trong `Vault`, vì vậy `Git` sẽ theo dõi lịch sử thay đổi của chúng. Khi chất lượng đầu ra của `Agent` bỗng nhiên thay đổi, bản diff của thư mục skills chính là nơi đầu tiên bạn nên mở ra xem.

Hãy thử nghiệm một skill mới trên ba hoặc bốn trường hợp thực tế trước khi giao nó cho một tác vụ chạy tự động theo lịch. Một khiếm khuyết nhỏ trong một skill chạy tự động hàng đêm sẽ nhân bản thành một khiếm khuyết nằm trên ba trăm trang ghi chú vào thời điểm cuối năm.

## Tiếp theo

[Guardrails (Rào chắn an toàn)](safety-and-guardrails.md)
