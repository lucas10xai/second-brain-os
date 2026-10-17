---
name: context-audit
description: >-
  Kiểm toán bố cục ngữ cảnh (context layout) của agent dựa trên bốn vùng:
  system prompt, công cụ (tools), lịch sử (history), và phần đuôi (tail).
  Sử dụng khi người dùng yêu cầu kiểm toán, đánh giá hoặc tối ưu ngữ cảnh
  của agent, bộ nhớ đệm prompt (prompt caching), lượng token tiêu thụ mỗi lượt,
  hoặc bố cục CLAUDE.md / AGENTS.md. Chỉ đọc: báo cáo phát hiện và danh sách
  khắc phục, không tự ý thay đổi file. KHÔNG dùng để viết bộ kiểm thử đánh giá
  (evals-bootstrap) hoặc thiết kế vòng lặp (goal-test).
---

# Kiểm toán cửa sổ ngữ cảnh (Context Window)

Lý thuyết: [Cách mô hình đọc ngữ cảnh](https://secondbrainos-vn.pages.dev/#/read/course-1-context/how-models-read)
và [Bốn vùng ngữ cảnh](https://secondbrainos-vn.pages.dev/#/read/course-1-context/the-four-places).
Mỗi mảnh thông tin trong ngữ cảnh đều thuộc về đúng một trong bốn vùng — một system prompt cố định từng byte, một tập công cụ đóng băng, một lịch sử được nén gọn, và một phần đuôi trực tiếp ngắn gọn — và hầu hết các vấn đề của agent đều bắt nguồn từ việc đặt nhầm thông tin vào sai vùng.

## Quy tắc cốt lõi

Báo cáo và xếp hạng; không bao giờ tự chỉnh sửa. Đầu ra là một bản báo cáo kiểm toán, và người dùng sẽ quyết định áp dụng phần nào. Nếu sau đó họ yêu cầu bạn thực hiện các sửa đổi, đó là một phiên chỉnh sửa bình thường, không thuộc phạm vi của kỹ năng này.

## Quy trình thực hiện

1. **Tìm các nguồn ngữ cảnh.** Xác định những gì thực sự được gửi tới mô hình: system prompt (hoặc `CLAUDE.md` / `AGENTS.md` đối với thiết lập Claude Code), định nghĩa công cụ (tool definitions), và — nếu dự án có ghi log request — một payload đầy đủ ở giữa cuộc hội thoại. Nếu không có log, hãy nêu rõ điều đó và kiểm toán các file tĩnh; chỉ hỏi xin một bản chụp request nếu người dùng có thể lấy nó dễ dàng.
2. **Đo lường năm con số.** Ước tính số lượng token cho: system prompt, định nghĩa công cụ, lịch sử tin nhắn, nội dung truy xuất (retrieved content), và truy vấn hiện tại. Một phép tính ước lượng (số ký tự / 4) là đủ; hãy ghi rõ cả năm con số ra.
3. **Truy lùng các yếu tố phá bộ nhớ đệm (cache killers).** Gắn cờ mọi giá trị động nằm trong system prompt — dấu thời gian (timestamps), tên người dùng, bộ nhớ được tiêm vào, các dòng "tác vụ hiện tại". Mỗi giá trị động này chắc chắn gây trượt bộ nhớ đệm (cache miss) ở mọi lệnh gọi. Kiểm tra xem danh sách công cụ có bị thay đổi giữa chừng khi đang chạy hay không; một danh sách thay đổi sẽ làm mất hiệu lực toàn bộ phần tiền tố (prefix).
4. **Truy lùng sự phình to cửa sổ ngữ cảnh (window bloat).** Tìm mục đơn lẻ lớn nhất trong lịch sử. Một kết quả trả về nguyên văn từ công cụ vượt quá ~2.000 token lẽ ra chỉ nên là một đường dẫn file kèm một dòng biên nhận. Đếm số lượng công cụ: nếu vượt quá 20 công cụ (hoặc ~10K token định nghĩa), hãy khuyến nghị sử dụng cơ chế trì hoãn tải công cụ (deferred tools) kết hợp tìm kiếm công cụ (tool search).
5. **Kiểm tra phần đuôi (tail).** Xác định vị trí của mục tiêu hiện tại. Nếu nó chỉ xuất hiện ở tin nhắn mở đầu, tức là nó đang nằm ở vùng giữa yếu ớt của cửa sổ ngữ cảnh — hãy khuyến nghị nhắc lại mục tiêu ở phần đuôi sau mỗi ba đến năm bước.
6. **Kiểm tra các file chỉ dẫn (guides).** Nếu có `CLAUDE.md` / `AGENTS.md`: nó chỉ nên gồm vài dòng ràng buộc mà mã nguồn không thể tự nói lên, chứ không phải bốn trang văn xuôi dài dòng. Hãy gắn cờ bất kỳ thông tin nào mà bản thân repo đã tự thể hiện rõ (cấu trúc thư mục, lịch sử git).

## Định dạng đầu ra

```
Context audit — <dự án>
system prompt   <n> tok   <sạch | N giá trị động: ...>
tools           <n> tok   <n> tools  <đóng băng | thay đổi giữa chừng>
history         <n> tok   mục lớn nhất: <là gì, n tok>
tail            <có mặt | mục tiêu chỉ nằm ở tin nhắn mở đầu>

Các mục cần khắc phục hàng đầu, xếp theo số token tiết kiệm được mỗi lượt:
1. ...
2. ...
```

Mỗi mục khắc phục cần chỉ rõ tên file và dòng (nếu có thể), nêu rõ nội dung nào cần chuyển sang vùng nào trong bốn vùng, và ước tính mức tiết kiệm. Kết thúc bằng quy tắc một dòng: tiền tố ổn định, công cụ đóng băng, lịch sử nén gọn, phần đuôi sống động (stable prefix, frozen tools, compact history, live tail).
