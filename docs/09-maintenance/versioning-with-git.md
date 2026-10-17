# Quản lý phiên bản với Git

Git chính là thứ giúp việc cho phép một Agent chạy tự động không cần giám sát trở nên an toàn. Không có Git, một lượt chạy lỗi sẽ là một bí ẩn không lời giải; có Git, mọi thay đổi đều hiển thị rõ ràng dưới dạng một bản so sánh (diff) mà bạn có thể đọc và hoàn tác chỉ bằng một câu lệnh.

## Độ chi tiết của mỗi Commit

Mỗi lượt chạy tương ứng với một commit, có ghi rõ tên lượt chạy:

```
ingest 2026-09-07: 4 sources, 9 pages
lint 2026-09-07: 3 broken links, 1 merge
```

Đừng tạo một commit cho từng file riêng lẻ vì nó sẽ làm ngập lụt lịch sử thay đổi, và cũng đừng gộp cả tuần vào một commit duy nhất vì bạn sẽ không thể hoàn tác một lượt chạy lỗi mà không làm mất đi những lượt chạy tốt trước đó.

Các tác vụ chạy theo lịch trình cần tự commit phần việc của mình ngay trong lượt chạy đó. Xem thêm [lập lịch bảo trì tự động](../06-agents/scheduled-maintenance.md).

## Đọc các bản so sánh (diffs) của những trang do Agent tạo ra

Việc này rất đáng làm trong những tuần đầu tiên, và thỉnh thoảng duy trì về sau.

Bạn cần tìm kiếm hai dấu hiệu: những trang bị thay đổi dù lẽ ra không nên bị chạm tới, và những trang bị viết lại toàn bộ trong khi yêu cầu chỉ là cập nhật bổ sung. Hành vi Agent âm thầm viết lại cả một trang khi chỉ được yêu cầu nối thêm thông tin là kiểu lỗi chỉ lộ diện khi bạn nhìn vào bản diff.

Lệnh `git log --stat` sau một tuần sẽ cho bạn biết những trang nào bị các tác vụ tự động hóa chạm tới nhiều nhất — một thông tin thường mang lại rất nhiều góc nhìn hữu ích.

## Hoàn tác (Reverting)

```bash
git revert HEAD          # hoàn tác một lượt chạy, giữ nguyên lịch sử
git checkout .           # hủy bỏ các thay đổi chưa được commit
git checkout HEAD~3 -- wiki/concepts/some-page.md   # khôi phục một trang về 3 commit trước
```

Câu lệnh ở giữa chính là lý do bạn phải luôn commit trước khi thực hiện bất kỳ thao tác quy mô lớn nào. Một đợt nạp bù dữ liệu (backfill) bị lỗi giữa chừng sẽ chỉ làm bạn mất công sức của lượt chạy đó chứ không làm hỏng cả Vault.

## Nhánh (Branches)

Rất đáng dùng cho những thử nghiệm tác động đến cấu trúc: một quy ước trang (page contract) mới, một thay đổi về Schema, hoặc một đợt Ingest lại hàng loạt theo bộ chỉ dẫn khác.

```bash
git checkout -b new-schema
```

Hãy chạy thử nghiệm, đọc kết quả, rồi quyết định gộp (merge) hoặc xóa bỏ nhánh đó. Làm thẳng những việc này trên nhánh `main` rồi mới tính tiếp chính là nguyên nhân khiến nhiều Vault rơi vào trạng thái chuyển đổi dở dang mà chẳng ai muốn dọn dẹp cho xong.

## Những thứ không nên đưa vào Commit

`.obsidian/workspace*`, các thư mục bộ nhớ đệm (caches), và bất kỳ thứ gì có chứa khóa bảo mật (key). Khóa của plugin Local REST API nằm trong thư mục dữ liệu plugin, vì vậy hãy kiểm tra kỹ `.obsidian/plugins/` trước lần đẩy dữ liệu (push) đầu tiên.

Hãy giữ kho lưu trữ từ xa (remote repository) ở chế độ riêng tư trừ khi bạn thực sự có chủ đích công khai toàn bộ Vault.

## Tiếp theo

[Sao lưu và tính khả chuyển](backups-and-portability.md)
