---
name: second-brain-merge
description: >-
  Gộp hai trang cùng mô tả về một đối tượng duy nhất: bảo toàn mọi luận điểm
  riêng biệt, chuyển hướng các liên kết đến (inbound links), và ghi nhật ký thao tác
  gộp. Sử dụng kỹ năng này khi người dùng phê duyệt việc gộp trang trùng lặp, nói
  "hai trang này là một", "gộp X vào Y", hoặc yêu cầu dọn dẹp các trang gần trùng lặp
  mà một lượt chạy lint đã đề xuất. KHÔNG dùng để tự ý gộp trang theo phán đoán cá nhân,
  xóa thẳng một trang, hoặc tách một trang thành nhiều trang.
---

# Gộp các trang trùng lặp (Merge duplicate pages)

Gộp trang là một thao tác không thể đảo ngược ở khía cạnh quan trọng nhất: sau khi gộp xong, bạn không thể phân biệt được nhận định nào từng thuộc về trang nào. Hai ý tưởng thoạt nhìn có vẻ giống hệt nhau qua bản tóm tắt lại thường là một trường hợp tổng quát và một trường hợp cụ thể.

## Quy tắc cốt lõi

Không bao giờ tự ý gộp trang khi chưa được yêu cầu. Hãy đề xuất, chờ phê duyệt, sau đó mới thực hiện chính xác theo quy trình.

## Quy trình thực hiện

1. **Chọn trang giữ lại (survivor)** dựa theo tên chuẩn tắc (canonical name), chứ không phải dựa vào việc trang nào dài hơn.
2. **Gộp nội dung.** Mọi luận điểm riêng biệt đều phải được giữ lại cùng với nguồn trích dẫn của nó. Các luận điểm trùng khớp thì gộp làm một; các luận điểm khác biệt thì giữ lại cả hai, tuân thủ đúng quy tắc xử lý mâu thuẫn.
3. **Gộp danh sách tên gọi khác (`aliases`),** bao gồm việc đưa tiêu đề của trang bị xóa vào trường `aliases` của trang được giữ lại. Đây là bước giúp các liên kết cũ và trí nhớ của người dùng tiếp tục hoạt động trơn tru.
4. **Chuyển hướng các liên kết đến (inbound links)** về trang được giữ lại. Kiểm tra toàn bộ các liên kết ngược (backlinks).
5. **Xóa trang cũ,** hoặc chỉ để lại một trang chuyển hướng ngắn (stub) nếu trang đó từng được liên kết từ bên ngoài vault.
6. **Ghi nhận vào `log.md`:** tên hai trang, ngày thực hiện, và lý do gộp.

## Định dạng đầu ra

```
Merged: [[trang cũ]] -> [[trang giữ lại]]
Claims kept from old page: <n>
Aliases added: <danh sách>
Inbound links redirected: <n>
Conflicts recorded: <none | mô tả>
```

## Hiệu chuẩn (Calibration)

Nếu hai trang bất đồng với nhau về bất kỳ dữ kiện thực tế nào, đó là tín hiệu cho thấy có thể chúng không phải là hai trang trùng lặp. Hãy nêu bật điểm bất đồng đó ra và hỏi lại người dùng trước khi tiếp tục.

Không bao giờ gộp một trang được đánh dấu `maintained_by: human` vào trang khác mà không có xác nhận rõ ràng chỉ đích danh tên trang đó.
