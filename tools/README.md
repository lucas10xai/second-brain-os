# Bộ công cụ xây dựng trang web (tools)

Trang web tại địa chỉ [secondbrainos-vn.pages.dev](https://secondbrainos-vn.pages.dev/) được tạo tự động trực tiếp từ kho lưu trữ này, nhờ đó nội dung trên web không bao giờ bị lệch so với bộ cẩm nang gốc.

## Trang chủ: một đồ thị duy nhất cho toàn bộ trang web

```bash
pip install markdown
python3 tools/build_graph_site.py   # -> assets/site/graph-data.js, assets/site/pages-data.js
python3 -m http.server 4173         # then open http://localhost:4173
```

File `index.html` vẽ toàn bộ các chương, trang bài viết, thuật ngữ, Skill, Slash command, Subagent, script và tài nguyên thành các nút (nodes) trong một đồ thị không gian 3D, đồng thời biểu diễn mọi liên kết thực tế giữa chúng thành các cạnh nối (edges). Hãy nhấp vào một nút để bay tới vị trí của nó, quan sát những gì nó liên kết tới và những gì liên kết ngược về nó, cũng như mở đọc nội dung trang ngay trong khung đọc mà không cần rời khỏi giao diện đồ thị.

| File | Vai trò |
|---|---|
| `index.html` | Khung giao diện trang chính. Được viết thủ công |
| `assets/site/app.css` | Bố cục và kiểu chữ. Bảng màu và phông chữ đồng bộ với cẩm nang |
| `assets/site/app.js` | Xử lý đồ thị, các bảng điều khiển, khung đọc bài viết, tìm kiếm và định tuyến (routing) |
| `assets/site/graph-data.js` | File sinh tự động: dữ liệu các nút và cạnh của đồ thị |
| `assets/site/pages-data.js` | File sinh tự động: nội dung các trang cẩm nang đã được kết xuất |
| `tools/build_graph_site.py` | Script biên dịch cả hai file dữ liệu trên từ mã nguồn Markdown |
| `tools/glossary.json` | Dữ liệu duy nhất được duy trì thủ công: danh sách các thuật ngữ hiển thị trên đồ thị |

Script `build_graph_site.py` giữ nguyên thứ tự đọc được khai báo trong file `README.md` của từng chương, phân giải mọi liên kết tương đối thành nút trang, nút chương hoặc nút công cụ tương ứng, kết nối các Slash commands với Skill mà chúng gọi tới, nối các trang bài viết với những tài nguyên có URL được trích dẫn trong bài, và gắn kết các thuật ngữ với những trang nhắc đến chúng nhiều nhất. Để thêm một thuật ngữ mới, bạn chỉ cần thêm một dòng vào `glossary.json` rồi chạy lại script.

Đồ thị được dựng bằng thư viện [3d-force-graph](https://github.com/vasturiano/3d-force-graph) và three.js, tải qua jsDelivr ở các phiên bản đã được cố định. Mọi thành phần khác đều nằm sẵn trong kho lưu trữ. Các đường dẫn kiểu cũ như `index.html#02-setup/claude-md` vẫn mở đúng trang bài viết tương ứng.

## Các trang phụ khác

```bash
python3 tools/extract_site.py   # docs and resources -> site_data.json
python3 tools/build_site.py     # -> resources.html
python3 scripts/build_tree.py   # -> tree.html
```

Hai trang `resources.html` và `tree.html` vẫn được biên dịch theo quy trình cũ. Không có script nào trong số này can thiệp vào `index.html`, kể cả `scripts/build_tracks.py` — công cụ hiện chỉ làm nhiệm vụ giữ cho các file `README.md` của khóa học và bộ sổ tay chuyên đề luôn tuân thủ đúng thứ tự đã khai báo.
