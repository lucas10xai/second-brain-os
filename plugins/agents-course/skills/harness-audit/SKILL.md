---
name: harness-audit
description: >-
  Kiểm toán khung điều phối (harness) của agent dựa trên bốn vòng bảo vệ:
  cô lập (containment), chỉ dẫn (guides), cảm biến (sensors), và phân quyền
  (permissions). Sử dụng khi người dùng hỏi liệu thiết lập agent của họ có an toàn
  không, muốn rà soát lại cơ chế sandbox / quyền hạn / hooks / các rào chắn trong
  AGENTS.md, hoặc hỏi một phiên chạy lỗi có thể phá hỏng những gì. Chỉ đọc: báo cáo
  bán kính ảnh hưởng (blast radius) và danh sách gia cố, không tự ý thay đổi gì.
  KHÔNG dùng cho bố cục ngữ cảnh (context-audit) hoặc định tuyến chi phí (gate-check).
---

# Kiểm toán bốn vòng bảo vệ (The Four Rings)

Lý thuyết: [Bốn vòng bảo vệ](https://secondbrainos-vn.pages.dev/#/read/course-4-harness/the-four-rings)
và [Thực hành Harness](https://secondbrainos-vn.pages.dev/#/read/course-4-harness/harness-practice).
Hãy xây dựng từ ngoài vào trong: cô lập (containment), chỉ dẫn (guides), cảm biến (sensors), và phân quyền (permissions). Thứ tự này cực kỳ quan trọng bởi vì mỗi vòng bên ngoài phải đứng vững khi tất cả các vòng bên trong nó thất bại — một lời chỉ dẫn có thể bị phớt lờ, một cảm biến có thể bỏ sót, một hộp thoại xin phép có thể bị bấm nhầm; nhưng một bức tường vật lý thì không quan tâm.

## Quy tắc cốt lõi

Báo cáo và xếp hạng; không bao giờ tự mình gia cố bất kỳ thứ gì. Câu hỏi trọng tâm duy nhất của buổi kiểm toán là bán kính ảnh hưởng (blast radius): mô tả phiên chạy tồi tệ nhất có thể xảy ra dưới thiết lập hiện tại và thiệt hại mà nó gây ra. Nếu sau đó người dùng yêu cầu bạn áp dụng các biện pháp khắc phục, đó là một phiên chỉnh sửa bình thường, không thuộc kỹ năng này.

## Quy trình thực hiện

1. **Vòng một — Cô lập (containment): về mặt vật lý, agent có thể chạm tới đâu?** Agent chạy ở đâu: trực tiếp trên thư mục làm việc chính của người dùng hay trong một worktree/container tách biệt? Những thông tin xác thực (credentials) nào đang nằm trong biến môi trường của nó — một tài khoản cơ sở dữ liệu chỉ đọc hay tài khoản chính của ứng dụng? Kết nối internet mở toàn bộ hay chỉ qua danh sách cho phép (allowlist)? Khóa API thật hay khóa thử nghiệm (test keys)? Kết luận được tóm gọn trong một câu: "phiên chạy tồi tệ nhất sẽ xóa X và tiêu tốn Y."
2. **Vòng hai — Chỉ dẫn (guides): agent đọc gì trước khi hành động?** Tìm `CLAUDE.md` / `AGENTS.md` và phần mô tả công cụ. Mỗi dòng phải là một quy tắc mà agent có thể hành động theo — hãy gắn cờ những đoạn triết lý chung chung, lịch sử dài dòng, và bất kỳ tài liệu nào dài quá một trang. Gắn cờ việc thiếu quy tắc cho những "bãi mìn" thực sự trong repo (migrations, các file sinh tự động, script triển khai).
3. **Vòng ba — Cảm biến (sensors): cái gì sẽ kích hoạt khi agent mắc lỗi?** Có một lệnh duy nhất nào (`make check` hoặc tương đương) chạy đồng thời cả test, linter và kiểm tra kiểu (types) không? Khung điều phối có tự động chạy lệnh đó sau mỗi lần chỉnh sửa — thông qua một hook — hay tính đúng đắn hoàn toàn phụ thuộc vào việc mô hình có tự nhớ để chạy hay không? Một cảm biến mà mô hình phải tự nguyện gọi thì chỉ là một lời chỉ dẫn, không phải là cảm biến.
4. **Vòng bốn — Phân quyền (permissions): việc gì vẫn cần con người phê duyệt?** Liệt kê những thao tác đang được tự động phê duyệt. Nhóm hành động không thể đảo ngược — đẩy code lên nhánh `main`, triển khai (deploy), chi tiêu tiền, xóa dữ liệu, gửi tin nhắn ra ngoài — bắt buộc phải có con người duyệt; mọi hành động có thể đảo ngược nằm bên trong các bức tường cô lập thì không nên hỏi. Hãy gắn cờ cả hai thái cực lỗi: tự động phê duyệt các hành động không thể đảo ngược, và hỏi xin phép các hành động có thể đảo ngược nhiều đến mức người dùng bấm duyệt theo quán tính (sự mệt mỏi vì phê duyệt — approval fatigue — chính là một lỗ hổng ở vòng này, chứ không phải là một ưu điểm).
5. **Kiểm tra thứ tự các vòng.** Dấu hiệu bất ổn kinh điển là việc bắt một vòng bên trong làm công việc của vòng bên ngoài: viết một dòng prompt dặn "không bao giờ được chạm vào môi trường prod" ở nơi mà lẽ ra phải gỡ bỏ thông tin xác thực prod ngay từ đầu. Những quy tắc trong file chỉ dẫn mà có thể biến thành tường chắn thì phải thuộc về vòng số một.

## Định dạng đầu ra

```
Harness audit — <dự án>
blast radius: <phiên chạy tồi tệ nhất gói gọn trong một câu>

ring 1 containment  <vững | hở>  <phát hiện>
ring 2 guides       <vững | hở>  <phát hiện>
ring 3 sensors      <vững | hở>  <phát hiện>
ring 4 permissions  <vững | hở>  <phát hiện>

Danh sách gia cố, ưu tiên từ vòng ngoài cùng vào trong:
1. ...
```

Xếp hạng các biện pháp khắc phục từ ngoài vào trong — dựng một bức tường trước khi viết một prompt hay hơn, đặt một cảm biến trước khi viết một quy tắc lịch sự hơn. Kết thúc bằng cách phát biểu lại bán kính ảnh hưởng sẽ giảm xuống như thế nào chỉ riêng sau khi hoàn thành biện pháp số 1.
