# Kho mã nguồn (Repositories)

Các dự án về đồ thị, truy xuất và bộ nhớ rất đáng để biết tới. Số lượng sao được lấy từ GitHub API vào tháng 9 năm 2026. Đối với các kỹ năng của `Agent`, hãy xem [skills.md](skills.md); đối với các plugin `Obsidian`, hãy xem [plugins.md](plugins.md).

## `GraphRAG` và truy xuất trên đồ thị

| Repo | Stars | What it is |
|---|---|---|
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 39,467 | Đồ thị hai tầng kết hợp vector, hướng tới việc cập nhật tăng trưởng (incremental updates) chi phí thấp. EMNLP 2025 |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 35,875 | Bản hiện thực hóa tham chiếu chính thức của [bài báo GraphRAG](papers.md) |
| [gusye1234/nano-graphrag](https://github.com/gusye1234/nano-graphrag) | 3,983 | Cùng ý tưởng trên nhưng gói gọn trong khoảng 1.100 dòng code dễ đọc. Hãy mở kho này nếu muốn hiểu rõ đường ống xử lý |
| [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 3,985 | Bản hiện thực của bài báo tại NeurIPS'24. Chạy thuật toán PageRank cá nhân hóa trên đồ thị tri thức |
| [DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 2,635 | Bản đồ tổng hợp được tuyển chọn gồm các bài khảo sát, benchmark và dự án trong lĩnh vực này |

## Bộ nhớ cho `Agent` (Agent memory)

Bài toán lân cận, sử dụng cùng các kỹ thuật. Những dự án này cung cấp bộ nhớ bền vững cho một `Agent`; còn bộ hướng dẫn này cung cấp cơ sở tri thức cho một con người. Rất đáng đọc để tham khảo thiết kế truy xuất ngay cả khi bạn không bao giờ chạy chúng.

| Repo | Stars | What it is |
|---|---|---|
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 64,863 | Tầng bộ nhớ lắp-là-chạy (drop-in) dành cho các `Agent` và ứng dụng AI |
| [getzep/graphiti](https://github.com/getzep/graphiti) | 30,680 | Đồ thị tri thức theo thời gian thực (temporal knowledge graphs) dành cho `Agent` |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 30,568 | Biến dữ liệu thành đồ thị tri thức, kết hợp giữa truy xuất đồ thị và truy xuất vector |
| [doobidoo/mcp-memory-service](https://github.com/doobidoo/mcp-memory-service) | 1,928 | Dịch vụ bộ nhớ bền vững qua giao thức MCP, kết hợp REST API và đồ thị tri thức |

## Các `RAG` Framework

Dành cho trường hợp bạn xác định `Vault` của mình đã vượt quá quy mô quản lý bằng tệp tin thuần túy. Xem bài [bổ sung `RAG` khi thực sự cần thiết](../docs/07-retrieval/rag-on-top.md) để biết ngưỡng chuyển đổi cụ thể — ngưỡng mà hầu hết các `Vault` cá nhân không bao giờ chạm tới.

| Repo | Stars | What it is |
|---|---|---|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 90,216 | Hệ thống `RAG` toàn diện tích hợp khả năng hiểu cấu trúc tài liệu chuyên sâu |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 52,058 | Framework nạp dữ liệu và xây dựng `Agent` làm việc với tài liệu |
| [neuml/txtai](https://github.com/neuml/txtai) | 12,931 | Cơ sở dữ liệu embeddings và luồng công việc LLM, đủ nhỏ gọn để đọc hiểu trực tiếp mã nguồn |

## MCP (Model Context Protocol)

| Repo | Stars | What it is |
|---|---|---|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 94,575 | Danh mục tổng hợp toàn diện các máy chủ MCP |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 90,141 | Các máy chủ MCP tham chiếu chính thức, bao gồm cả máy chủ quản lý hệ thống tệp tin và bộ nhớ |
| [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | 4,376 | Máy chủ MCP bên thứ ba dành cho `Obsidian` hoạt động thông qua plugin REST |

Vì plugin Local REST API hiện đã tích hợp sẵn máy chủ MCP của riêng nó, việc cài đặt một máy chủ tách biệt là tùy chọn. Xem chi tiết tại [MCP cho `Obsidian`](../docs/02-setup/mcp-obsidian.md).

## Cách đánh giá một dự án trong danh sách này

**Nó chiếm quyền sở hữu dữ liệu của bạn hay chỉ đọc dữ liệu?** Bất kỳ công cụ nào chỉ đọc các tệp markdown của bạn và ghi ra đầu ra phái sinh đều an toàn để dùng thử và an toàn để từ bỏ. Ngược lại, bất kỳ công cụ nào trở thành nơi duy nhất lưu giữ một mảnh tri thức đều đã tước đi tính khả chuyển (portability) — lý do cốt lõi khiến bạn chọn định dạng markdown ngay từ đầu.

**Dự án có còn được bảo trì không?** Hãy kiểm tra ngày đẩy code (push) gần nhất chứ đừng nhìn vào tổng số sao. Hệ sinh thái này sản sinh ra rất nhiều kho mã nguồn chỉ trong vài tuần sau khi một bản gist nổi tiếng xuất hiện, và phần lớn trong số đó đều ngừng hoạt động chỉ sau một tháng.

**Số sao có đang đo lường đúng thứ bạn cần không?** Đối với các plugin, số lượt cài đặt là tín hiệu tốt hơn nhiều, và ở nhiều nơi hai con số này chênh lệch nhau tới cả một bậc độ lớn.
