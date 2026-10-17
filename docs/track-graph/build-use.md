# Thực hành: Đưa vào vòng lặp (Loop)

Phần ba. Đồ thị đã tồn tại và trả lời được câu hỏi; giờ đây Agent cần tự mình chạm tới nó mà không cần bạn đứng làm trung gian ở giữa. Không cần máy chủ MCP, không cần bộ khung (framework) phức tạp — giao diện công cụ ở đây chỉ đơn giản là "gọi lệnh shell chạy một kịch bản in ra văn bản", việc mà Claude Code vốn đã làm cực kỳ tự nhiên và có thể sống sót qua mọi cuộc chuyển đổi framework.

## Dùng lệnh gạch chéo (Slash command), không dùng máy chủ

Hãy thả tệp này vào trong Vault tại đường dẫn `.claude/commands/connects.md`:

```markdown
---
description: What connects two pages
---

Regenerate the edge list with `python scripts/graph_export.py . edges.csv`,
then run `python scripts/graph_query.py connects` with the two page names
from $ARGUMENTS, each in quotes. Explain the chain in one short paragraph,
naming the edge types, and say plainly if nothing connects them.
```

Giờ đây, gõ `/connects "Jerry Liu" "Lost in the Middle"` sẽ cung cấp cho Agent một chuỗi liên kết đã được tính toán sẵn để diễn giải, thay vì để nó tự bịa ra một mối liên hệ. Việc xuất lại danh sách cạnh trước khi truy vấn là rất quan trọng: Agent chỉnh sửa các trang liên tục, và nếu truy vấn trên tệp CSV của ngày hôm qua thì câu trả lời chỉ phản ánh trạng thái Vault của ngày hôm qua. Các cạnh có định kiểu thì lâu lỗi thời hơn — bạn chỉ cần chạy lại lượt trích xuất trong bài [Thực hành: Trích xuất đồ thị](build-extract.md) mỗi tháng một lần, hoặc sau một đợt nạp tài liệu lớn.

Thay đổi sâu sắc hơn nằm ở phần chỉ dẫn thường trực của Agent. Hãy thêm một dòng vào tệp `CLAUDE.md` của Vault:

```text
Before answering any question about how two topics relate, run
scripts/graph_query.py connects with both page names and ground
the answer in the chain it returns.
```

Dòng chỉ dẫn đó biến đồ thị từ một công cụ mà Agent *có thể* dùng thành một công cụ mà nó *thực sự* dùng — tạo ra sự khác biệt giữa việc sở hữu một cuốn sách tham khảo trên kệ và việc thực sự trích dẫn nó.

## Kiểm tra sức khỏe định kỳ hàng tuần

Đồ thị sẽ dần mục nát theo thời gian, và bài [tại sao cần Knowledge Graph](why-graphs.md) đã nói rất thẳng rằng một đồ thị lỗi thời còn tệ hơn là không có đồ thị. Vì vậy, đồ thị cũng cần một vòng lặp bảo trì giống như mọi thành phần khác trong Vault. Hãy chạy lệnh nhắc này hàng tuần, bằng tay hoặc hẹn lịch tự động:

```text
Run python scripts/graph_export.py . edges.csv, then
python scripts/graph_query.py communities. Report three things:

1. Orphans: pages under wiki/ that appear in no edge at all
   (compare filenames against the nodes in edges.csv). Propose a
   page each should be linked from, or flag it for deletion.
2. Weak clusters: communities of three pages or fewer that are not
   from this week's ingestion. Say whether each should be linked
   into a larger cluster or left to grow.
3. One bridge worth building: the two largest communities with no
   typed edge between them, and the page or link that would
   connect them.

Keep the report to ten lines. Do not change anything without asking.
```

Các trang mồ côi (orphans) là lỗi ở khâu thu thập, các cụm yếu (weak clusters) là những chủ đề chưa kịp bén rễ, và cây cầu còn thiếu (missing bridge) thường là dòng thú vị nhất trong báo cáo — hai mảng tri thức bạn cùng sở hữu nhưng chưa từng gặp nhau. Quy tắc chỉ-đọc (read-only) ở cuối rất quan trọng: một bài kiểm tra sức khỏe mà tự ý nối lại các liên kết trong im lặng chính là con đường khiến chiếc Vault không còn là của bạn nữa.

## Khi nào cần nâng cấp (Graduate)

Những dấu hiệu cho thấy tầng lưu trữ CSV kết hợp NetworkX không còn đủ đáp ứng nữa, xếp theo thứ tự chúng thường xuất hiện:

- Các truy vấn cần yếu tố lịch sử — ví dụ "hồi tháng Ba tôi đã tin vào điều gì" — trong khi các cạnh phẳng không hề có dấu thời gian (timestamp).
- Nhiều Agent cùng ghi dữ liệu đồng thời, và cơ chế ai-ghi-cuối-thắng (last-write-wins) trên tệp CSV bắt đầu làm mất cạnh.
- Thời gian nạp lại đồ thị mất hàng giây thay vì vài mili-giây, thường xảy ra khi vượt qua ngưỡng hàng chục nghìn nút.

Mỗi dấu hiệu trên tương ứng với một bậc thang trong bài [kho lưu trữ đồ thị](graph-stores.md), và việc di trú dữ liệu chỉ tốn một buổi chiều vì danh sách cạnh vốn đã là định dạng trung gian chuẩn mà mọi hệ thống đều hỗ trợ nhập (import). Cho đến khi một trong các dấu hiệu đó thực sự xuất hiện, hãy cứ ở lại với thiết kế hiện tại: toàn bộ tầng đồ thị chỉ gồm hai kịch bản Python, một câu lệnh nhắc và hai tệp CSV, đồng thời mọi thành phần trong đó đều có thể đọc hiểu trực tiếp bởi chính người sở hữu nó.

## Những gì bạn đã có trong tay

Một bộ trích xuất, một công cụ truy vấn, một lệnh gạch chéo và một vòng lặp bảo trì — một hệ thống GraphRAG thu gọn hoạt động trơn tru ngay trên các ghi chú cá nhân với chi phí chỉ vỏn vẹn một buổi tối. Nếu nhu cầu của bạn lớn dần từ điểm khởi đầu này, các bộ khung được khảo sát trong bài [công cụ](tools.md) cũng mang hình hài tương tự, chỉ là được phóng lớn quy mô lên mà thôi.
