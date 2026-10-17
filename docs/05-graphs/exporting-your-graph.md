# Xuất dữ liệu đồ thị

Chế độ xem đồ thị của `Obsidian` chỉ là một công cụ hiển thị. Để tính toán bất kỳ chỉ số nào, bạn cần đưa đồ thị ra bên ngoài ứng dụng.

## Xuất dữ liệu (Export)

```bash
python3 scripts/graph_export.py ~/brain edges.csv
python3 scripts/graph_export.py ~/brain graph.graphml --format graphml
```

Script này phân tích cú pháp mọi `Wikilink` thành một danh sách cạnh (edge list), mang theo trường `type` của trang làm thuộc tính nút (node attribute), và không yêu cầu cài đặt thêm thư viện phụ thuộc nào. Định dạng CSV dùng cho viết code, còn GraphML dùng cho Gephi.

## Phân tích bằng code

```python
import networkx as nx, csv

g = nx.DiGraph()
with open("edges.csv") as f:
    next(f)
    g.add_edges_from(tuple(r) for r in csv.reader(f))

print(nx.number_weakly_connected_components(g))
print(sorted(nx.pagerank(g).items(), key=lambda kv: -kv[1])[:10])
print([n for n in g if g.in_degree(n) == 0])
```

Ba câu hỏi được giải quyết trong mười dòng code: `Vault` đang bị phân mảnh đến mức nào, những trang nào đóng vai trò trung tâm về mặt cấu trúc, và những trang nào đang không thể tiếp cận được.

Chạy thuật toán PageRank trên một `Knowledge graph` là việc rất đáng thử ít nhất một lần. Những trang đứng đầu bảng xếp hạng chính là chủ đề thực sự mà `Vault` của bạn đang xoay quanh — và kết quả này thường khác xa một cách đáng ngạc nhiên so với những gì bạn tự nghĩ về `Vault` của mình.

## Độ trung gian (Betweenness) — chỉ số đáng bỏ công tính toán nhất

```python
b = nx.betweenness_centrality(g)
```

Độ trung gian (betweenness centrality) đo lường tần suất một trang nằm trên đường đi ngắn nhất giữa hai trang bất kỳ khác. Những trang có độ trung gian cao chính là những cây cầu nối giữa các cụm chủ đề.

Chúng quan trọng vì hai lý do. Thứ nhất, chúng là những trang giá trị nhất của bạn, nắm giữ những mối liên kết mà không một tài liệu nguồn đơn lẻ nào chứa đựng. Thứ hai, chúng là những điểm xung yếu mỏng manh: nếu một trang cầu nối bị sai lệch hoặc vô tình bị xóa mất trong lúc gộp trang, hai mảng kiến thức trong `Vault` sẽ âm thầm ngừng bổ trợ thông tin cho nhau.

## Cơ sở dữ liệu đồ thị (Graph databases)

Kuzu là hệ quản trị cơ sở dữ liệu dạng nhúng (embedded), không cần cài đặt server, đọc trực tiếp file CSV, và việc viết các truy vấn Cypher trên chính kho ghi chú của mình thực sự là một trải nghiệm rất thú vị cho một buổi tối. Neo4j là phiên bản đầy đủ tính năng và sẽ là quá mức cần thiết (overkill) trừ khi bạn đang xây dựng một ứng dụng thực thụ chạy bên trên đó.

Hãy xác định rõ bản chất của việc này: đây là một tầng phân tích (analysis layer), không phải là sự thay thế. Các file Markdown vẫn là nguồn chuẩn tắc (canonical), còn cơ sở dữ liệu đồ thị chỉ là một bản phái sinh có thể tái tạo lại bất cứ lúc nào. Khoảnh khắc bạn bắt đầu ghi những tri thức chỉ tồn tại duy nhất trong cơ sở dữ liệu, bạn đã đánh mất tính khả chuyển (portability) — phẩm chất cốt lõi khiến toàn bộ phương pháp tiếp cận này đáng để lựa chọn ngay từ đầu.

## Gephi

Dành cho việc quan sát trực quan hơn là tính toán thuần túy. Hãy nạp file GraphML vào, chạy thuật toán bố cục ForceAtlas2, chỉnh kích thước nút theo bậc (degree), và tô màu theo loại trang (`type`). Gephi kết xuất các đồ thị lớn theo cách mà `Obsidian` không thể làm được, và đây chính là công cụ nên dùng nếu bạn muốn có một bức ảnh chụp màn hình thực sự giá trị để trình bày.

## Giữ dữ liệu đồng bộ

Bản xuất đồ thị chỉ là một ảnh chụp nhanh tại một thời điểm (snapshot) và nó sẽ lỗi thời ngay lập tức. Hãy chạy xuất lại mới thay vì cố bảo trì file đã xuất, và đừng bao giờ chỉnh sửa trực tiếp trên đồ thị đã xuất rồi kỳ vọng `Vault` sẽ tự cập nhật theo.

## Tiếp theo

[Các chỉ số đồ thị đáng theo dõi](metrics.md)
