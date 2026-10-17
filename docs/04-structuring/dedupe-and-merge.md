# Khử trùng lặp và gộp trang

Sự trùng lặp là điều không thể tránh khỏi. Hai tài liệu nguồn dùng những từ khác nhau cho cùng một ý tưởng, một alias bị thiếu, hoặc một đợt nhập dữ liệu hàng loạt (bulk import) đã chạy trước khi `Vault` định hình được khái niệm đó. Câu hỏi đặt ra không phải là làm sao để ngăn chặn hoàn toàn sự trùng lặp, mà là làm sao để phát hiện ra chúng trước khi cả hai trang đều tích lũy hàng loạt liên kết.

## Cách tìm ra trang trùng lặp

Các tín hiệu nhận biết, xếp theo thứ tự độ tin cậy giảm dần:

- **Tiêu đề tương tự nhau.** Rất nhẹ để kiểm tra, bắt được các trường hợp số nhiều và từ viết tắt.
- **`Aliases` chồng lấp nhau.** Hai trang cùng nhận chung một alias luôn luôn là một lỗi (bug).
- **Chia sẻ chung các liên kết trỏ tới (inbound links).** Hai trang mà cùng được năm tài liệu nguồn liên kết tới thường thực chất chỉ là một trang.
- **Độ tương đồng về nội dung.** Tốn chi phí tính toán hơn, nhưng bắt được các trường hợp mà tên gọi trông chẳng liên quan gì đến nhau.

Skill `second-brain-lint` sẽ chạy ba bước kiểm tra đầu tiên và đề xuất các trang cần gộp. Nó không tự động thực hiện việc gộp trang, và đây là thiết kế có chủ đích.

## Tại sao không tự động gộp trang

Gộp trang là một thao tác không thể đảo ngược theo một nghĩa rất quan trọng: một khi hai trang đã gộp làm một, bạn không thể phân biệt nhận định nào đến từ trang nào nữa, và phán đoán của `Agent` về việc "hai thứ này là một" lại chính là kiểu phán đoán dễ sai lầm nhất.

Hai ý tưởng trông giống hệt nhau qua phần tóm tắt thường lại là một trường hợp tổng quát và một trường hợp cụ thể; việc gộp chúng lại sẽ làm mất đi sự phân biệt đó vĩnh viễn.

Vì vậy: `Agent` đề xuất, bạn quyết định. Việc duyệt một đề xuất gộp trang chỉ mất mười lăm giây.

## Quy trình gộp trang

Khi bạn phê duyệt một đề xuất gộp:

1. **Chọn trang giữ lại (survivor)** dựa theo tên chuẩn tắc, không phải dựa theo trang nào dài hơn.
2. **Gộp nội dung,** giữ lại mọi nhận định riêng biệt kèm theo nguồn của nó. Các nhận định trùng lặp thì gộp lại, các nhận định khác biệt thì giữ lại cả hai.
3. **Gộp `Aliases`,** bao gồm cả việc đưa tiêu đề của trang bị xóa làm một alias trên trang giữ lại.
4. **Chuyển hướng các liên kết trỏ tới (inbound links)** sang trang giữ lại.
5. **Để lại một trang sơ khai (stub)** ở đường dẫn cũ chỉ khi nó từng được liên kết từ bên ngoài `Vault`. Nếu không, hãy xóa hẳn file cũ.
6. **Ghi lại vào `log.md`** kèm theo cả hai tên trang, để một trang biến mất luôn có thể truy vết được.

Bước 6 là bước mà các `Agent` thường bỏ qua nhưng lại là bước bạn sẽ cần đến nhất. Một trang biến mất không để lại dấu vết sẽ không thể phân biệt được với một trang bị xóa nhầm.

## Đừng khử trùng lặp ngay trong lúc Ingest

Việc gộp trang ngay trong một lượt chạy `Ingest` đồng nghĩa với việc `Agent` vừa cấu trúc lại `Vault` vừa thêm mới vào đó, và một cú gộp sai sẽ nằm lẫn vào giữa những phần việc đang làm tốt khác.

Hãy chạy khử trùng lặp như một lượt riêng biệt, hàng tuần hoặc sau một đợt nhập dữ liệu lớn, trên một trạng thái `Git` sạch (clean git state). Khi đó, nếu có một cú gộp sai, bạn chỉ cần một lệnh `git checkout` là khôi phục lại được ngay.

## Tiếp theo

[Mâu thuẫn và thay thế thông tin](contradictions-and-supersession.md)
