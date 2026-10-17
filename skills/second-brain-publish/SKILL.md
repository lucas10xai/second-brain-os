---
name: second-brain-publish
description: >-
  Chuẩn bị một tập con của vault để xuất bản công khai: kiểm tra cờ cho phép xuất
  bản (opt-in flags), tìm tư liệu riêng tư, và báo cáo những thông tin có nguy cơ
  rò rỉ qua các liên kết trước khi xuất bất kỳ dữ liệu nào ra ngoài. Sử dụng kỹ năng
  này khi người dùng muốn xuất bản ghi chú thành trang web hoặc khu vườn số (digital
  garden), hỏi những trang nào an toàn để công khai, hoặc đang thiết lập quy trình
  xuất dữ liệu. KHÔNG dùng để xuất một tài liệu đơn lẻ, hoặc để trực tiếp chạy công cụ
  build trang web xuất bản.
---

# Chuẩn bị xuất bản (Prepare to publish)

Một khi nội dung đã bị các trình thu thập dữ liệu (crawlers) quét qua, nó đã thuộc về không gian công cộng. Mọi phép kiểm tra ở đây đều rất rẻ; nhưng tai nạn mà nó ngăn chặn được thì mang tính vĩnh viễn.

## Quy tắc cốt lõi

Chỉ xuất bản khi được bật cờ chủ động (explicit opt-in only). Một trang được xuất bản chỉ vì nó có dòng `publish: true`, tuyệt đối không bao giờ vì "không có quy tắc nào loại trừ nó".

## Quy trình thực hiện

1. **Liệt kê tập hợp được phép xuất bản (opt-in set).** Mọi trang được đánh dấu cho phép xuất bản công khai.
2. **Lần theo các liên kết của chúng.** Một trang công khai liên kết tới một trang riêng tư sẽ hoặc làm lộ tiêu đề nhạy cảm, hoặc tạo ra một liên kết chết. Hãy báo cáo cả hai trường hợp.
3. **Quét tìm bất kỳ nội dung nào không bao giờ được phép lọt ra ngoài:** thông tin xác thực (credentials), thông tin riêng tư của người khác, tài liệu công việc bảo mật, hoặc chi tiết cá nhân nằm trong các ví dụ minh họa.
4. **Kiểm tra phần frontmatter** để tìm các trường không dành cho công chúng, chẳng hạn như nhãn mức độ tự tin cá nhân hoặc đường dẫn nguồn nội bộ.
5. **Chỉ báo cáo, không tự xuất dữ liệu.** Chính người dùng sẽ là người chạy lệnh build cuối cùng.

## Định dạng đầu ra

```
Publishable: <n> trang
Links to unpublished pages: <n>
  [[trang công khai]] -> [[trang riêng tư]]
Flagged content: <danh sách kèm lý do>
Frontmatter to strip: <các trường cần lược bỏ>
Verdict: <safe to build | fix these first>
```

## Hiệu chuẩn (Calibration)

Hãy ưu tiên bắt nhầm còn hơn bỏ sót (err toward flagging). Một cảnh báo dư thừa chỉ làm tốn của người dùng mười giây kiểm tra; một lần bỏ sót sẽ để lại hậu quả vĩnh viễn.

Nếu người dùng yêu cầu xuất bản toàn bộ chiếc vault, hãy hỏi rõ họ dự định xử lý các tư liệu riêng tư như thế nào trước, thay vì cứ thế thực hiện.
