#!/usr/bin/env python3
"""Xuất đồ thị wikilink của một vault dưới dạng danh sách cạnh CSV hoặc GraphML.

Cách dùng:
    python3 graph_export.py /path/to/vault edges.csv
    python3 graph_export.py /path/to/vault graph.graphml --format graphml

File CSV có thể nạp vào NetworkX, Kuzu, Neo4j hoặc bảng tính. File GraphML mở được
bằng Gephi. Không yêu cầu thư viện phụ thuộc bên ngoài.
"""
import argparse
import csv
import os
import re
from xml.sax.saxutils import escape

LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
TYPE = re.compile(r"^type:\s*(\S+)", re.M)
# Các thư mục ẩn (.claude, .obsidian, .git, .trash), thư mục mẫu trang (templates)
# và thư mục scripts chỉ chứa chỉ dẫn cùng công cụ chứ không phải tri thức, nên
# không bao giờ được tính là các trang wiki. Tương tự đối với CLAUDE.md và README.md
# ở bất kỳ vị trí nào.
SKIP_DIRS = {"node_modules", "raw", "templates", "scripts"}
SKIP_FILES = {"CLAUDE.md", "README.md"}


def is_page(name):
    return name.endswith(".md") and name not in SKIP_FILES


def prune(dirnames):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]


def load(vault):
    pages = {}
    for dirpath, dirnames, filenames in os.walk(vault):
        prune(dirnames)
        for name in filenames:
            if is_page(name):
                path = os.path.join(dirpath, name)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    pages[path] = fh.read()
    return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("out")
    ap.add_argument("--format", choices=["csv", "graphml"], default="csv")
    args = ap.parse_args()

    pages = load(args.vault)
    stems = {os.path.splitext(os.path.basename(p))[0]: p for p in pages}
    lower = {k.lower(): k for k in stems}

    nodes = {}
    for stem, path in stems.items():
        m = TYPE.search(pages[path])
        nodes[stem] = m.group(1) if m else "untyped"

    edges = []
    for stem, path in stems.items():
        for target in LINK.findall(pages[path]):
            key = lower.get(target.strip().lower())
            if key and key != stem:
                edges.append((stem, key))

    if args.format == "csv":
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["source", "target"])
            w.writerows(edges)
    else:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            fh.write('<graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
            fh.write('<key id="t" for="node" attr.name="type" attr.type="string"/>\n')
            fh.write('<graph edgedefault="directed">\n')
            for n, t in nodes.items():
                fh.write(f'<node id="{escape(n)}"><data key="t">{escape(t)}</data></node>\n')
            for i, (s, t) in enumerate(edges):
                fh.write(f'<edge id="e{i}" source="{escape(s)}" target="{escape(t)}"/>\n')
            fh.write("</graph>\n</graphml>\n")

    print(f"{len(nodes)} nodes, {len(edges)} edges -> {args.out}")


if __name__ == "__main__":
    main()
