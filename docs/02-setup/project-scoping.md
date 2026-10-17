# Giới hạn phạm vi theo dự án (Project scoping)

Đây là bước mà hầu hết các thiết lập đều bỏ qua, để rồi sau đó người dùng cứ thắc mắc vì sao chất lượng đầu ra của Agent lại ngày càng đi xuống khi Vault phình to.

Khi bạn trỏ Agent vào toàn bộ Vault, mỗi tác vụ nhỏ đều phải cạnh tranh sự chú ý với tất cả những gì bạn từng lưu trữ từ trước đến nay. Agent phải đọc file `CLAUDE.md` ở thư mục gốc bao quát toàn bộ cuộc đời bạn, cộng thêm đủ thứ tài liệu khác mà nó tự cho là có liên quan. Hệ quả là các câu trả lời ngày càng dàn trải và nông cạn.

Ngược lại, khi bạn chỉ trỏ Agent vào đúng một dự án cụ thể, nó sẽ chỉ đọc file `CLAUDE.md` của riêng dự án đó, chỉ nhìn thấy các file thuộc dự án đó, và tập trung giải quyết trọn vẹn công việc ngay trước mắt.

## Cách giới hạn phạm vi hoạt động

Trong Obsidian, hãy bấm vào tên Vault ở góc dưới bên trái, sau đó chọn:

**Manage vaults → Open folder as a vault → chọn thư mục dự án của bạn → Trust**

Nếu thao tác từ cửa sổ terminal, công việc tương tự chỉ đơn giản là:

```bash
cd ~/brain/projects/youtube-channel
claude
```

Lúc này, Agent sẽ chỉ đọc duy nhất các chỉ dẫn của dự án đó.

## Khi nào nên dùng phạm vi nào

**Toàn bộ Vault (Full vault)** dùng cho bất kỳ công việc nào trải rộng qua nhiều lĩnh vực: lập kế hoạch tổng thể, rà soát định kỳ, hỏi xem bạn đang biết những gì về một chủ đề, bảo trì hàng tuần, hoặc chạy quy trình Ingest. Tầng tri thức sinh ra chính là để phục vụ góc nhìn bao quát này.

**Một dự án đơn lẻ (Single project)** dùng khi bạn cần bắt tay vào sản xuất một thành phẩm cụ thể: viết bản thảo, xây dựng tính năng, hay phân tích số liệu của tuần này. Ngữ cảnh hẹp, một mục tiêu duy nhất, không bị xao nhãng.

Quy tắc ngón tay cái rất dễ nhớ: mở toàn bộ Vault để lập kế hoạch, mở từng dự án lẻ để thực thi ra sản phẩm.

## Đưa tri thức từ Wiki vào trong dự án

Việc thu hẹp phạm vi xuống một dự án sẽ ngắt quyền truy cập trực tiếp của Agent khỏi tầng `wiki/` — điều mà phần lớn thời gian là có lợi nhưng đôi khi lại gây bất tiện. Có hai cách để bắc cầu nối tri thức sang dự án:

- Đặt liên kết trỏ tới các trang khái niệm liên quan ngay trong file `CLAUDE.md` của dự án, đồng thời sao chép một vài trang thực sự cốt lõi vào thẳng thư mục `Inputs/` của dự án đó.
- Hoặc chạy câu hỏi nghiên cứu trên phạm vi toàn bộ Vault trước, lưu câu trả lời nhận được vào thư mục `Inputs/` của dự án, rồi sau đó mới thu hẹp phạm vi xuống dự án để bắt đầu làm việc.

Cách thứ hai hiệu quả hơn hẳn. Nó giữ quyền quyết định xem thông tin nào thực sự quan trọng nằm trong tay bạn — và đó chính là phần việc bạn không nên ủy thác cho AI.

## Tiếp theo

[Kết nối dữ liệu thời gian thực](live-data.md)
