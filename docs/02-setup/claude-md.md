# Viết file CLAUDE.md của bạn

File `CLAUDE.md` nằm tại thư mục gốc của Vault là tài liệu đầu tiên mà Agent đọc mỗi khi bắt đầu một phiên làm việc mới. Nó tạo nên sự khác biệt một trời một vực giữa một người trợ lý hiểu rõ hoàn cảnh của bạn và một người mà lần nào gặp bạn cũng phải giải thích lại từ đầu.

Một Vault trống rỗng nhưng có file `CLAUDE.md` chất lượng còn hữu ích hơn nhiều so với một Vault đầy ắp dữ liệu nhưng thiếu đi file này, bởi ngữ cảnh về cá nhân bạn sẽ định hình cách Agent biên soạn mọi trang wiki về sau.

## Đừng tự gõ thủ công, hãy để Agent phỏng vấn bạn

Việc ngồi tự viết file này từ trang giấy trắng thường dẫn đến một bản mô tả sơ sài và chung chung. Ngược lại, việc trả lời từng câu hỏi cụ thể sẽ tạo ra một bản hồ sơ sắc nét và sát thực tế. Hãy dán đoạn yêu cầu sau vào Agent:

```
You are setting up my second brain. Interview me ONE question at a time to
build my profile. Ask about: who I am and what I do, my goals for this year,
how I want you to talk to me, my strengths and weaknesses, and my current
projects. Wait for each answer before the next question. When finished, write
everything into CLAUDE.md at the vault root, structured with headers.
```

Hãy trả lời chi tiết như thể bạn đang bàn giao công việc cho một người đồng sáng lập trong ngày đầu tiên họ nhận việc. Những câu trả lời hời hợt sẽ tạo ra một file chỉ dẫn mơ hồ, và mọi phiên làm việc sau đó đều sẽ gánh chịu hệ quả từ sự mơ hồ ấy.

## Những nội dung cần có trong file

- **Bạn là ai và bạn đang làm công việc gì.** Đủ cụ thể để một người lạ đọc xong có thể hành động hỗ trợ bạn ngay.
- **Các mục tiêu có mốc thời gian rõ ràng.** Trong năm nay, hoặc trong quý này. Những mục tiêu không gắn thời hạn rất nhanh trở nên vô nghĩa.
- **Cách bạn muốn Agent giao tiếp với mình.** Độ dài câu trả lời, giọng điệu, và mức độ phản biện thẳng thắn mà bạn mong muốn.
- **Điểm mạnh và điểm yếu của bạn.** Thông tin này giúp Agent biết khi nào nên chất vấn lại quyết định của bạn thay vì chỉ gật đầu đồng tình.
- **Các dự án hiện tại,** mỗi dự án một dòng, kèm liên kết trỏ tới thư mục tương ứng của dự án đó.
- **Các quy tắc vận hành riêng của Vault:** bố cục thư mục, hợp đồng định dạng trang (page contracts), quy tắc liên kết. Phiên bản mẫu tại [`vault-template/CLAUDE.md`](../../vault-template/CLAUDE.md) là một điểm khởi đầu chuẩn chỉnh bạn có thể dùng ngay.

## Những nội dung không nên đưa vào

- Bất kỳ thông tin nào thay đổi liên tục hàng tuần. Những thứ đó thuộc về các file nằm trong thư mục dự án.
- Những đoạn giải thích dài dòng về các kiến thức phổ thông mà bản thân mô hình AI đã biết thừa.
- Mọi loại mật khẩu, khóa API hay thông tin xác thực (credentials).
- Những lời hô hào khẩu hiệu đẹp đẽ nhưng bạn không thực sự hành động theo. Agent sẽ hiểu và thực thi chúng theo đúng nghĩa đen.

## Hai cấp độ của CLAUDE.md

File `CLAUDE.md` ở thư mục gốc đóng vai trò là tầng chiến lược tổng thể: bạn là ai, bạn đang hướng tới mục tiêu gì, và toàn bộ Vault vận hành ra sao. Trong khi đó, mỗi thư mục dự án con sẽ có một file `CLAUDE.md` riêng chỉ bao quát phạm vi của đúng dự án đó. Khi bạn mở riêng một thư mục dự án như một Vault độc lập, Agent sẽ chỉ đọc file chỉ dẫn của dự án đó và ngừng mang theo toàn bộ câu chuyện cuộc đời bạn vào từng tác vụ nhỏ. Hãy xem bài [Giới hạn phạm vi theo dự án (Project scoping)](project-scoping.md).

## Liên tục tinh chỉnh theo thời gian

Khi Agent lặp lại cùng một lỗi tới lần thứ hai, đó là vấn đề của file `CLAUDE.md` chứ không phải lỗi do câu lệnh nhắc (prompt) nhất thời. Hãy bổ sung quy tắc khắc phục vào file, và nhớ ghi kèm lý do đằng sau quy tắc đó — bởi một quy tắc cứng nhắc không có lý do đi kèm sẽ bị Agent áp dụng máy móc vào những tình huống ngoại lệ mà bạn chưa lường trước.

Hãy đọc lại file này mỗi tháng một lần. Mục tiêu thay đổi, dự án khép lại, và một bản hồ sơ lỗi thời sẽ âm thầm làm giảm chất lượng của mọi nội dung mà Agent viết ra.

## Tiếp theo

[Cấu trúc Vault](vault-structure.md)
