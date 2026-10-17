# Các script tiện ích (scripts)

Tập hợp các script Python nhỏ gọn, không phụ thuộc vào thư viện bên ngoài. Mọi công cụ tại đây đều đọc Vault dưới dạng các file văn bản thuần túy, vì vậy sẽ không có gì bị hỏng nếu bạn đổi trình soạn thảo hay đổi Agent.

| Script | Chức năng |
|---|---|
| `link_check.py` | Kiểm tra các Wikilink bị gãy, các trang mồ côi (orphan pages) và các trang sơ khai bỏ trống (stubs) |
| `vault_stats.py` | Thống kê số lượng trang, mật độ liên kết, tỷ lệ trang mồ côi và danh sách các trang được liên kết nhiều nhất |
| `graph_export.py` | Xuất đồ thị Wikilink ra định dạng danh sách cạnh CSV hoặc GraphML để dùng trong Gephi |
| `chat_export_to_md.py` | Chuyển đổi file xuất lịch sử trò chuyện thành từng file Markdown riêng cho mỗi cuộc hội thoại |

```bash
python3 scripts/vault_stats.py ~/brain
python3 scripts/link_check.py ~/brain
python3 scripts/graph_export.py ~/brain graph.graphml --format graphml
```

Hãy sao chép thư mục này vào bên trong Vault (`cp -r scripts ~/brain/scripts`, bước Quickstart đã thực hiện sẵn việc này) để các lệnh `/metrics`, `/health` và `/graph-export` có thể tìm thấy chúng. Các thư mục ẩn như `.claude/` và `.obsidian/`, cùng với `templates/`, `scripts/`, `raw/` và bất kỳ file `CLAUDE.md` hay `README.md` nào đều được tự động bỏ qua, nhờ đó các con số thống kê phản ánh chính xác tầng wiki của bạn chứ không tính gộp cả bộ công cụ đi kèm. Trên Windows, lệnh `python3` thường trỏ tới bản stub của Microsoft Store; hãy chạy các script này bằng lệnh `python`.

Agent hoàn toàn có thể thực hiện tất cả những việc này bằng ngôn ngữ tự nhiên, nhưng một script chuyên dụng sẽ luôn trả về kết quả đồng nhất trong mọi lần chạy và không tốn chi phí token nào — điều cực kỳ lý tưởng cho những chỉ số bạn cần kiểm tra định kỳ hàng tuần.
