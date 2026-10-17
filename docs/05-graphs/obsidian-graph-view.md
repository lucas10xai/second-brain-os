# Cách đọc Graph View trong Obsidian

Đồ thị toàn cục (global graph) là bức ảnh chụp màn hình mà ai cũng thích đăng lên mạng. Nhưng đó lại là chế độ xem ít hữu dụng nhất trong ứng dụng.

Ở quy mô hai trăm trang, nó trông như một búi tóc rối, và một búi tóc rối thì chẳng cho bạn biết điều gì ngoài việc bạn đang có rất nhiều trang. Tác dụng thực sự của nó chỉ là giúp phát hiện hình thái tổng thể qua một cái nhìn lướt qua: những cụm bị cô lập, một nút trung tâm (hub) khổng lồ lấn át tất cả, hay một đám các chấm rời rạc không có liên kết dạt ra ngoài rìa.

## Đồ thị cục bộ (Local graph)

Đây mới là chế độ xem thực sự làm việc hiệu quả. Hãy mở một trang bất kỳ, bật đồ thị cục bộ (local graph), và đặt độ sâu (depth) bằng 2.

Bạn cần tìm kiếm hai thứ. Những gì cách đó một bước nhảy (hop) phải có mối liên hệ hiển nhiên với trang hiện tại; bất kỳ thứ gì gây ngạc nhiên ở khoảng cách này hoặc là một liên kết trang trí dư thừa cần xóa bỏ, hoặc là một mối liên hệ thú vị đáng để đọc lại. Còn những gì bị khuyết thiếu ở khoảng cách hai bước nhảy sẽ cho bạn biết trang này đang bị kết nối yếu ở mảng nào.

Xem lại đồ thị cục bộ của một trang bạn vừa mới viết xong là bài kiểm tra chất lượng nhanh nhất hiện có, và nó chỉ mất đúng năm giây.

## Các bộ lọc giúp chế độ xem toàn cục trở nên hữu dụng

- **Lọc theo loại trang.** Cú pháp `-path:sources` sẽ ẩn các trang nguồn đi và chỉ giữ lại đồ thị khái niệm — phần thực sự mang ý nghĩa. Số lượng trang nguồn thường áp đảo hoàn toàn số lượng khái niệm và làm chìm nghỉm chúng về mặt thị giác.
- **Nhóm theo màu sắc.** Tô màu khác nhau cho các trang khái niệm (concepts), thực thể (entities) và tổng hợp (synthesis). Một cụm hoàn toàn không có trang khái niệm nào bên trong chính là một đống tài liệu nguồn chất đống chưa được ai xử lý.
- **Bật/tắt trang mồ côi (Orphan toggle).** Hãy chủ động bật hiển thị các trang mồ côi lên, quan sát những gì xuất hiện, sau đó sửa liên kết hoặc xóa chúng đi.
- **Độ sâu và lực đẩy (Depth and forces).** Giảm lực hút liên kết (link force) sẽ giúp kéo giãn các cụm ra xa nhau đủ để bạn nhìn rõ các trang cầu nối (bridges).

## Những dấu hiệu cần chú ý

**Các chấm ở ngoài rìa, chỉ nối với duy nhất một thứ.** Thường là các lượt `Ingest` bị lỗi. Trang nguồn đã được viết ra nhưng các trang khái niệm chưa bao giờ liên kết ngược trở lại.

**Một nút khổng lồ nằm chính giữa.** Một trang trung tâm (hub) đã nuốt chửng cả đồ thị. Hãy tách nhỏ nó ra.

**Hai cụm lớn chỉ nối với nhau qua một trang duy nhất.** Trang đó đang gánh vác một vai trò cực kỳ quan trọng. Nhưng nó cũng rất mong manh: nếu nội dung trang đó sai, cả hai cụm sẽ hiểu sai về nhau.

**Một cụm mà bạn không hề nhận ra.** Thường là thứ thú vị nhất trên màn hình. Điều đó có nghĩa là `Vault` đã âm thầm tích lũy đủ tài liệu về một chủ đề mà bạn chưa từng chủ đích theo dõi.

## Những điều chế độ xem này không thể cho bạn biết

Nó chỉ cho thấy các trang có kết nối với nhau, chứ không bao giờ cho biết *tại sao*. Mọi cạnh nối trông đều giống hệt nhau, bất kể nó mang ý nghĩa là "ủng hộ", "mâu thuẫn" hay chỉ là "tình cờ nhắc thoáng qua một lần".

Giới hạn đó chính là toàn bộ lý do dẫn tới trang tiếp theo.

## Tiếp theo

[Liên kết định kiểu (Typed links)](typed-links.md)
