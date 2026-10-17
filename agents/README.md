# agents

Sáu định nghĩa subagent dành cho Claude Code. Hãy sao chép vào thư mục `.claude/agents/` trong vault của bạn.

| Agent | Quyền ghi | Tần suất chạy |
|---|---|---|
| `ingestor` | có | khi có tài liệu mới được đưa vào `raw/` |
| `linker` | chỉ thêm liên kết | sau khi nhập hàng loạt, hoặc hàng tuần |
| `reviewer` | không | hàng tuần |
| `researcher` | không | theo yêu cầu |
| `graph-analyst` | không | hàng tháng, hoặc khi việc điều hướng trở nên khó khăn |
| `curator` | không | hàng quý |

Bốn trong sáu agent được thiết kế chỉ đọc (read-only). Việc tách quyền ghi theo cách này đồng nghĩa với việc một lượt chạy nghiên cứu hay phân tích bị lỗi sẽ không thể làm hỏng vault, đồng thời giữ cho lịch sử git luôn dễ đọc: mọi thay đổi về nội dung đều bắt nguồn từ một lượt nạp tài liệu (`ingest`) hoặc một lượt rà soát liên kết (`link pass`).

Hai agent có quyền ghi cũng chính là hai agent có chỉ dẫn hẹp và chặt chẽ nhất. Đó không phải là sự trùng hợp ngẫu nhiên.

Xem [lập lịch bảo trì (scheduling)](../docs/06-agents/scheduled-maintenance.md) để kết nối các agent này vào một lịch chạy định kỳ.
