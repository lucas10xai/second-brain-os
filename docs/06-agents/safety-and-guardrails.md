# Guardrails (Rào chắn an toàn)

Quy tắc nền tảng mà toàn bộ chương này dựa vào:

**Kiểm soát bằng quyền hạn (Keys), không phải bằng lời dặn trong prompt.**

Việc dặn một `Agent` đừng làm điều gì đó chỉ là bày tỏ một nguyện vọng (preference). Đó không phải là một ranh giới an toàn (boundary). Nếu về mặt kỹ thuật, `Agent` có đủ quyền để xóa một file, làm rỗng một thư mục hoặc gửi đi một bức email, thì một ngày nào đó, trong một ngữ cảnh mà bạn không lường trước được, nó chắc chắn sẽ làm thế.

Hãy kiểm soát những gì có thể xảy ra ngay ở tầng phân quyền hệ thống (permission level). Khi đó, chỉ dẫn trong `CLAUDE.md` sẽ đóng vai trò là định hướng hành vi nằm bên trên một ranh giới cứng, thay vì là thứ mỏng manh duy nhất chắn giữa kho ghi chú của bạn và một lượt chạy thảm họa.

## Giới hạn phạm vi quyền ghi (Scope write access)

`Agent` cần quyền ghi vào bên trong `Vault`. Nó hoàn toàn không cần quyền ghi vào thư mục gốc của người dùng (home directory), và một tác vụ chạy tự động theo lịch được cấp quyền truy cập hệ thống tệp tin quá rộng sẽ tạo ra một bán kính sát thương (blast radius) khổng lồ chỉ để đổi lấy một chút tiện lợi nhỏ nhoi.

Nguyên tắc tương tự cũng áp dụng cho các bộ kết nối (connectors): hãy luôn chọn chế độ chỉ đọc (read-only) ở bất cứ nơi nào có tùy chọn đó. Một bộ kết nối lịch làm việc chỉ có quyền đọc thì không bao giờ có thể tự ý hủy một cuộc họp của bạn, bất kể nó có hiểu lầm câu chỉ dẫn trong prompt đến mức nào đi chăng nữa.

## Không bao giờ xóa mà không lưu vết

Xóa là thao tác duy nhất bạn không thể phục hồi thông tin chỉ bằng cách đọc lướt qua bản diff, bởi vì toàn bộ nội dung đã biến mất và thứ duy nhất còn sót lại chỉ là sự vắng mặt của nó.

Quy tắc bắt buộc: không có bất kỳ trang nào được phép xóa đi mà không có một dòng ghi nhận trong `log.md` nêu rõ tên trang và lý do xóa. Việc gộp trang (merge) cũng được tính là một thao tác xóa. Khi được áp dụng nhất quán, bất kỳ trang nào biến mất cũng đều có thể truy vết được hoàn toàn, và câu hỏi *"trang đó biến đâu mất rồi?"* sẽ không bao giờ còn là một bí ẩn không lời giải.

## Git mới là tấm lưới an toàn thực sự

Mọi rào chắn (`Guardrails`) nêu trên đều mang tính phòng ngừa. Còn `Git` chính là thứ cứu mạng bạn khi một trong các rào chắn đó bị thủng.

Hãy luôn tạo commit trước bất kỳ lượt chạy nào có thực hiện ghi dữ liệu ở quy mô lớn. Các lượt chạy tự động theo lịch phải tự commit phần việc của chính mình. Nhờ vậy, nếu có một lượt `Ingest` tệ hại, bạn chỉ cần gõ `git checkout .`, và nếu có một cú gộp trang sai lầm, bạn chỉ cần đúng một lệnh revert.

Thỉnh thoảng hãy mở xem lại các bản diff từ những lượt chạy tự động theo lịch, đặc biệt là trong những tuần đầu tiên mới vận hành. Đó là cách duy nhất giúp bạn thực sự hiểu `Agent` của mình đang làm những gì vào lúc 7 giờ sáng — thứ thường rất khác so với những gì bạn vẫn đinh ninh trong đầu.

## Chạy thử nghiệm (Dry runs)

Đối với bất kỳ thao tác nào chạm tới nhiều file cùng lúc, hãy chạy nó một lần ở chế độ chỉ báo cáo (report-only mode).

```
Hãy chạy thử (dry run): liệt kê mọi trang bạn dự định tạo mới, cập nhật hoặc xóa bỏ, cùng các liên kết
bạn sẽ thêm vào. Tuyệt đối không ghi bất kỳ thay đổi nào xuống file.
```

Kết quả đầu ra chỉ mất khoảng một phút để đọc lướt qua nhưng sẽ giúp bạn bắt gọn những chỉ dẫn bị hiểu sai trước khi chúng biến thành bốn trăm lượt chỉnh sửa file thực tế.

## Cảnh giác với hiện tượng tự ý mở rộng phạm vi (Scope creep)

Các `Agent` rất hay tự ý làm thêm việc ngoài yêu cầu. Khi được yêu cầu `Ingest` tài liệu, một `Agent` có thể tiện tay dọn dẹp lại một trang khác không liên quan, sửa lại định dạng Markdown, hay đổi tên một vài thứ cho đồng bộ. Từng hành động nhỏ đó nhìn riêng thì đều có lý lẽ bảo vệ được; nhưng khi gộp chung lại, chúng khiến bạn không thể nào biết được một lượt chạy thực sự đã làm những gì nếu không đọc lại toàn bộ mọi file.

Hãy chỉ dẫn thật dứt khoát: chỉ làm đúng công việc được yêu cầu, liệt kê bất kỳ vấn đề nào khác mà bạn phát hiện ra vào báo cáo, và tuyệt đối không tự ý thay đổi thêm bất cứ thứ gì khác.

## Những gì tuyệt đối không đưa vào Vault

Thông tin đăng nhập (credentials), API keys, bất kỳ tài liệu nào bạn có nghĩa vụ bảo mật, hoặc thông tin đời tư cá nhân của người khác.

Không phải vì sợ `Agent` sẽ tự ý làm rò rỉ chúng, mà bởi vì bản chất `Vault` là một cây thư mục văn bản thuần túy liên tục được đồng bộ hóa (sync), đẩy lên `Git` commit, sao lưu dự phòng (backup) và đôi khi được chia sẻ cho người khác. Mỗi một bản sao như vậy lại là thêm một nơi mà nội dung nhạy cảm đó tồn tại. Xem thêm [Quyền riêng tư và thông tin bí mật](../09-maintenance/privacy-and-secrets.md).

## Tiếp theo

[Truy xuất thông tin (Retrieval)](../07-retrieval/README.md), để lấy ra các câu trả lời chất lượng từ toàn bộ hệ thống mà bạn đã dày công xây dựng.
