#!/usr/bin/env python3
"""In các chỉ số sức khỏe của một vault bộ não thứ hai.

Cách dùng:
    python3 vault_stats.py /path/to/vault

Báo cáo số lượng trang theo từng loại (type), mật độ liên kết, tỷ lệ trang mồ côi
(orphan rate) và danh sách các trang được kết nối nhiều nhất. Hãy theo dõi các
chỉ số này theo thời gian: tỷ lệ trang mồ côi tăng lên đồng nghĩa với việc quá
trình nạp tài liệu (ingestion) đang chạy mà không tạo liên kết — nguyên nhân phổ
biến nhất khiến một chiếc vault dần mất đi tính hữu dụng.
"""
import os
import re
import sys
from collections import Counter, defaultdict

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


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: vault_stats.py /path/to/vault")
    vault = sys.argv[1]

    pages, types = {}, Counter()
    for dirpath, dirnames, filenames in os.walk(vault):
        prune(dirnames)
        for name in filenames:
            if is_page(name):
                path = os.path.join(dirpath, name)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                pages[path] = text
                m = TYPE.search(text)
                types[m.group(1) if m else "untyped"] += 1

    if not pages:
        sys.exit("no markdown files found")

    stems = {os.path.splitext(os.path.basename(p))[0].lower(): p for p in pages}
    indeg = defaultdict(int)
    total = 0
    for path, text in pages.items():
        for target in LINK.findall(text):
            dest = stems.get(target.strip().lower())
            if dest and dest != path:
                indeg[dest] += 1
                total += 1

    orphans = [p for p in pages if indeg[p] == 0 and not p.endswith(("index.md", "log.md"))]
    words = sum(len(t.split()) for t in pages.values())

    print(f"pages          {len(pages)}")
    for t, c in types.most_common():
        print(f"  {t:<12} {c}")
    print(f"words          {words:,}")
    print(f"links          {total}")
    print(f"avg degree     {total / len(pages):.2f}")
    print(f"orphan rate    {100 * len(orphans) / len(pages):.1f}%")
    print("\nmost linked:")
    for path, n in sorted(indeg.items(), key=lambda kv: -kv[1])[:10]:
        print(f"  {n:>4}  {os.path.relpath(path, vault)}")


if __name__ == "__main__":
    main()
