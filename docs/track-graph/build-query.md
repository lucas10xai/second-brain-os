# Thực hành: Truy vấn đồ thị

Phần hai của bài thực hành. Bước [Thực hành: Trích xuất đồ thị](build-extract.md) đã để lại hai tệp ở thư mục gốc của Vault: `edges.csv` chứa các liên kết thuần và `typed_edges.csv` chứa kết quả từ lượt quét gắn kiểu. Trang này sẽ biến chúng thành câu trả lời chỉ với hơn bốn mươi dòng mã Python.

Kho lưu trữ ở đây là NetworkX nằm trên bộ nhớ trong (in-memory), được nạp mới từ các tệp CSV trong mỗi lần gọi — bậc thang thứ hai trong bài [kho lưu trữ đồ thị](graph-stores.md). Không máy chủ, không kịch bản di trú lược đồ, và ở quy mô một Vault cá nhân thì việc nạp toàn bộ dữ liệu chỉ mất vài mili-giây. Chỉ cần cài đặt một thư viện phụ thuộc duy nhất:

```
pip install networkx
```

Phiên bản NetworkX là 3.7 tại thời điểm viết bài; bất kỳ bản nào thuộc nhánh 3.x đều hoạt động tốt.

## Kịch bản truy vấn

Hãy lưu đoạn mã sau thành tệp `scripts/graph_query.py` trong Vault:

```python
#!/usr/bin/env python3
"""Query the vault graph. Reads edges.csv and typed_edges.csv from the
current directory.

Usage:
    python graph_query.py neighbors "Page"
    python graph_query.py path "Page A" "Page B"
    python graph_query.py communities
    python graph_query.py connects "Page A" "Page B"
"""
import csv
import os
import sys

import networkx as nx

FILES = ["edges.csv", "typed_edges.csv"]


def load():
    g = nx.DiGraph()
    for name in FILES:
        if not os.path.exists(name):
            continue
        with open(name, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                g.add_edge(row["source"], row["target"],
                           type=row.get("type", "links-to"))
    return g


def neighbors(g, node):
    out = [f"-> {t} ({g.edges[node, t]['type']})" for t in sorted(g.successors(node))]
    out += [f"<- {s} ({g.edges[s, node]['type']})" for s in sorted(g.predecessors(node))]
    return "\n".join(out) or "No links."


def path(g, a, b):
    try:
        return nx.shortest_path(g.to_undirected(as_view=True), a, b)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return None


def communities(g):
    found = nx.community.label_propagation_communities(g.to_undirected())
    groups = sorted((sorted(c) for c in found), key=len, reverse=True)
    return "\n".join(f"[{len(c)}] " + ", ".join(c) for c in groups)


def connects(g, a, b):
    p = path(g, a, b)
    if p is None:
        return f"Nothing connects {a} and {b}."
    hops = []
    for s, t in zip(p, p[1:]):
        d = g.get_edge_data(s, t)
        hop = f"{s} -[{d['type']}]-> {t}" if d else f"{s} <-[{g.edges[t, s]['type']}]- {t}"
        hops.append(hop)
    return "\n".join(hops)


if __name__ == "__main__":
    g = load()
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "neighbors":
        print(neighbors(g, args[0]))
    elif cmd == "path":
        print(" -> ".join(path(g, args[0], args[1]) or ["No path."]))
    elif cmd == "communities":
        print(communities(g))
    elif cmd == "connects":
        print(connects(g, args[0], args[1]))
    else:
        print(__doc__)
```

Đôi dòng ghi chú ngắn về thiết kế. Việc nạp các cạnh có định kiểu sau các cạnh liên kết thuần có nghĩa là cạnh có định kiểu sẽ ghi đè lên nhãn `links-to` giữa cùng một cặp nút — đây là chủ đích thiết kế, bởi cạnh có định kiểu mô tả chính xác hơn về cùng mối liên kết đó. Phép tìm đường đi (`path`) chạy trên góc nhìn vô hướng (undirected view), vì câu hỏi "hai thứ này liên quan thế nào" không quan tâm trang nào đặt liên kết sang trang nào. Và thuật toán lan truyền nhãn (label propagation) đóng vai trò thay thế cho bước phân cụm Leiden trong [GraphRAG](graphrag.md): thô sơ hơn, nhưng chỉ cần thư viện chuẩn cộng với NetworkX và cho kết quả tức thì ở quy mô này.

## Câu trả lời từ mỗi lệnh

```
$ python scripts/graph_query.py neighbors "RAG"
-> GraphRAG (links-to)
-> LlamaIndex (uses)
<- GraphRAG (extends)
<- Lost in the Middle (links-to)

$ python scripts/graph_query.py communities
[4] GraphRAG, Long context replaces RAG, Lost in the Middle, RAG
[2] Jerry Liu, LlamaIndex
```

Lệnh `neighbors` cung cấp góc nhìn một bước nhảy (one-hop) quanh một trang theo cả hai chiều đi và đến, kèm theo tên mối quan hệ. Lệnh `communities` chính là tầng chủ đề: mỗi dòng là một cụm, xếp từ cụm lớn nhất trở xuống.

## Điều gì kết nối X và Y

Đây chính là lý do bài thực hành này tồn tại. Lệnh `connects` trả về chuỗi liên kết ngắn nhất giữa hai trang cùng kiểu quan hệ rõ ràng trên từng bước nhảy:

```
$ python scripts/graph_query.py connects "Jerry Liu" "Lost in the Middle"
Jerry Liu -[built]-> LlamaIndex
LlamaIndex <-[uses]- RAG
RAG <-[links-to]- Lost in the Middle
```

Đó là một phép kết nối đa bước (multi-hop join) được tính toán đàng hoàng thay vì đoán mò — đúng dạng câu hỏi mà bài [tại sao cần Knowledge Graph](why-graphs.md) đã chỉ ra rằng truy xuất Vector sẽ thất bại. Bản thân nó cũng chỉ là một hàm thuần túy nhận vào hai chuỗi ký tự và trả về một chuỗi ký tự, khớp hoàn hảo với hình hài mà một công cụ của Agent (Agent tool) mong muốn. Việc đấu nối hàm này vào hệ thống sẽ nằm ở phần [Thực hành: Đưa vào vòng lặp (Loop)](build-use.md).
