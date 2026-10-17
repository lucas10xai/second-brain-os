# Kiểm tra sức khỏe Vault bằng Lint

Sự xuống cấp về mặt cấu trúc diễn ra rất âm thầm. Chẳng có thông báo lỗi nào hiện lên cả. Vault chỉ đơn giản là trả lời ngày một kém đi vì một phần ba số trang của nó đã không còn đường dẫn tới mà không ai nhận ra.

## Một lượt chạy Lint kiểm tra những gì

**Các liên kết gãy (Broken links).** Có hai trường hợp riêng biệt: lỗi gõ nhầm hoặc đổi tên trang — trường hợp này sẽ được sửa tự động; và một khoảng trống kiến thức thực sự — trường hợp này sẽ được đưa vào mục Gaps trong `index.md`.

**Các trang mồ côi (Orphans).** Những trang không có bất kỳ trang nào khác liên kết tới. Hoặc tìm đúng vị trí của chúng để gắn liên kết, hoặc xóa chúng đi.

**Các trang sơ sài (Stubs).** Những trang dưới khoảng bốn mươi từ và không có liên kết nào, thường là hậu quả của một lần Ingest thất bại. Hãy gắn cờ để Ingest lại từ tài liệu gốc trong `raw/`.

**Vi phạm cấu trúc dữ liệu (Schema violations).** Thiếu Frontmatter, sai loại trang (type), hoặc dùng thẻ (tags) nằm ngoài bộ từ vựng quy định.

**Các trang gần như trùng lặp (Near-duplicates).** Tiêu đề tương tự nhau, các Aliases chồng lấn, hoặc dùng chung các liên kết trỏ đến.

**Độ lệch chỉ mục (Index drift).** Các trang có tồn tại nhưng thiếu mặt trong `index.md`, hoặc các mục trong chỉ mục lại trỏ vào hư không.

## Báo cáo trước khi sửa chữa

Các lỗi cơ học sẽ được sửa tự động. Bất kỳ thay đổi nào đòi hỏi sự phán đoán đều sẽ được đề xuất và chờ bạn phê duyệt.

Ranh giới đó rất quan trọng, bởi một công cụ Lint tự ý gộp các trang theo phán đoán riêng sẽ phá hỏng công sức của bạn, còn một công cụ chỉ biết liệt kê báo cáo thì lại tạo ra một danh sách dài dằng dặc mà chẳng ai buồn động tay vào. Liên kết gãy và lỗi cấu trúc Schema là lỗi cơ học. Gộp trang và xóa trang thì không.

## Cách chạy kiểm tra

```
/lint
```

Hãy chạy hàng tuần, hoặc sau bất kỳ đợt nhập dữ liệu nào lớn hơn khoảng hai mươi tài liệu nguồn. Đừng chạy sau mỗi lần Ingest đơn lẻ, vì chi phí bỏ ra sẽ lớn hơn những lỗi mà nó bắt được.

Hãy chạy lệnh khi trạng thái Git đang sạch (clean git state), để nếu có một bước sửa lỗi sai thì bạn chỉ cần một lệnh `git checkout` là khôi phục lại được ngay.

Bên trong Obsidian, plugin [Find orphaned files and broken links](https://github.com/Vinzent03/find-unlinked-files) cũng kiểm tra trực quan hai vấn đề tương tự.

Để kiểm tra nhanh mà không cần gọi Agent:

```bash
python3 scripts/link_check.py ~/brain
```

## Cách đọc kết quả đầu ra

Các con số thống kê tổng quan quan trọng hơn từng mục lỗi riêng lẻ. Ba liên kết gãy sau một tuần là chuyện bình thường. Nhưng bốn mươi liên kết gãy nghĩa là có điều gì đó trong chỉ dẫn Ingest đã thay đổi và đang tạo ra các liên kết trỏ tới những trang mà nó chẳng bao giờ khởi tạo.

Hãy theo dõi tỷ lệ lỗi theo thời gian thay vì chỉ nhìn vào con số tuyệt đối, vì cả hai đều tăng lên cùng với quy mô của Vault. Xem thêm [các chỉ số đo lường](../05-graphs/metrics.md).

## Tiếp theo

[Nhịp độ rà soát định kỳ](review-cadence.md)
