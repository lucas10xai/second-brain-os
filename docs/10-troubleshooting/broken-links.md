# Liên kết gãy và các trang mồ côi

```bash
python3 scripts/link_check.py ~/brain
```

## Tại sao việc đổi tên file lại làm gãy liên kết

Obsidian tự động cập nhật các liên kết khi bạn đổi tên file ngay bên trong ứng dụng. Nhưng khi một Agent đổi tên file trực tiếp trên hệ thống file thì cơ chế đó không diễn ra, và đây chính là nguyên nhân phổ biến nhất gây ra liên kết gãy trong một Vault do Agent duy trì.

Hãy ngăn chặn điều này bằng một quy tắc trong `CLAUDE.md`: mỗi khi đổi tên trang phải cập nhật toàn bộ các liên kết trỏ đến (inbound links), thêm tên cũ vào trường Aliases, và ghi nhận thao tác đó vào `log.md`. Xem thêm [đặt tên và Aliases](../04-structuring/naming-and-aliases.md).

## Sửa lỗi hàng loạt

Có hai nhóm liên kết gãy, và mỗi nhóm cần được xử lý theo cách khác nhau.

**Lỗi gõ nhầm và đổi tên** thì cần được sửa lại: trỏ liên kết đó về đúng trang đích. Nhóm này hoàn toàn an toàn để tự động hóa.

**Khoảng trống kiến thức thực sự (Genuine gaps)** — nơi trang đích chưa từng tồn tại — thì đưa vào `index.md` dưới mục Gaps. Đừng tạo ra các trang rỗng chỉ để làm vừa lòng bộ kiểm tra liên kết; một trang rỗng còn tệ hơn một khoảng trống được ghi nhận rõ ràng, vì nó tạo cảm giác giả tạo rằng chủ đề đó đã được bao phủ.

Hãy luôn thực hiện trên một trạng thái Git sạch (clean git state), để nếu một đợt sửa lỗi hàng loạt đi chệch hướng, bạn chỉ cần một câu lệnh là hoàn tác được ngay.

## Các trang mồ côi (Orphans)

Những trang không có bất kỳ trang nào khác liên kết tới. Thường rơi vào ba trường hợp sau.

**Lẽ ra phải được liên kết nhưng lại bị bỏ sót.** Hãy tìm những trang đáng lý phải tham chiếu tới nó và bổ sung liên kết vào. Đây là trường hợp phổ biến nhất sau một đợt nhập dữ liệu hàng loạt (bulk import).

**Thực sự đứng độc lập.** Trường hợp này hiếm gặp và thường là dấu hiệu cho thấy tư liệu đó không thuộc về khu vực `wiki/`. Các tài liệu tra cứu nhanh hay danh sách kiểm tra (checklists) nên nằm trong thư mục dự án riêng.

**Ingest thất bại.** Một trang sơ sài (stub) được tạo ra dở dang và chưa bao giờ được kết nối vào mạng lưới. Hãy Ingest lại từ tài liệu gốc trong `raw/`.

## Ngăn chặn cả hai lỗi ngay từ khâu Ingest

Quy tắc giúp loại bỏ phần lớn công việc dọn dẹp này: không một tài liệu nào được coi là đã Ingest xong cho đến khi nó được gắn liên kết đầy đủ theo cả hai chiều ngay trong cùng một lượt chạy.

Một lượt Ingest kết thúc mà để lại các trang chưa được liên kết là một lượt Ingest chưa hoàn thành. Hãy ép buộc quy tắc này ngay trong Skill thay vì đợi đến cuối tuần mới đi dọn dẹp.

## Sau một đợt nhập dữ liệu lớn

Hãy luôn chạy Lint. Một đợt nạp bù dữ liệu (backfill) quy mô lớn chắc chắn sẽ sinh ra các trang mồ côi và các trang gần như trùng lặp, bởi Agent đã phải xử lý nhanh qua nhiều tài liệu có nội dung giao thoa nhau.

Hãy dự trù sẵn thời gian cho bước này: sau khi nhập một nghìn tài liệu nguồn, bắt buộc phải có một lượt chạy Lint và một lượt rà soát gộp trang — bỏ qua bước đó chính là lý do khiến một Vault trở nên lộn xộn vĩnh viễn.

## Tiếp theo

[Vault phình ra quá lớn](vault-too-big.md)
