#!/usr/bin/env python3
"""Chuyển đổi file JSON xuất lịch sử trò chuyện thành mỗi cuộc hội thoại một file Markdown.

Cách dùng:
    python3 chat_export_to_md.py conversations.json ./raw --min-words 150

Hoạt động với cấu trúc xuất dữ liệu phổ biến của Claude và ChatGPT: một mảng JSON
chứa các cuộc hội thoại, mỗi cuộc hội thoại có tên/tiêu đề (name/title) và danh sách
tin nhắn. Các cấu trúc lạ sẽ được bỏ qua kèm cảnh báo thay vì đoán mò.

Hãy đọc trang hướng dẫn về quyền riêng tư trước khi chạy công cụ này trên bản xuất
dữ liệu thật. Lịch sử trò chuyện là thứ nhạy cảm nhất mà hầu hết mọi người có thể
đưa vào một chiếc vault.
"""
import argparse
import json
import os
import re
import sys


def slug(text, limit=60):
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[\s_]+", "-", s)
    return (s[:limit] or "untitled").strip("-")


def text_of(message):
    content = message.get("content", message.get("text", ""))
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for c in content:
            if isinstance(c, str):
                parts.append(c)
            elif isinstance(c, dict):
                parts.append(c.get("text", ""))
        return "\n".join(p for p in parts if p)
    if isinstance(content, dict):
        return "\n".join(content.get("parts", []) or [])
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("outdir")
    ap.add_argument("--min-words", type=int, default=150,
                    help="skip conversations shorter than this")
    args = ap.parse_args()

    with open(args.export, encoding="utf-8") as fh:
        data = json.load(fh)

    if isinstance(data, dict):
        data = data.get("conversations", [])
    if not isinstance(data, list):
        sys.exit("unrecognised export shape: expected a list of conversations")

    os.makedirs(args.outdir, exist_ok=True)
    written = skipped = 0

    for conv in data:
        if not isinstance(conv, dict):
            continue
        title = conv.get("name") or conv.get("title") or "untitled"
        created = (conv.get("created_at") or conv.get("create_time") or "")
        messages = conv.get("chat_messages") or conv.get("messages") or []
        if isinstance(messages, dict):
            messages = list(messages.values())

        body = []
        for m in messages:
            if not isinstance(m, dict):
                continue
            role = m.get("sender") or m.get("role") or "unknown"
            t = text_of(m).strip()
            if t:
                body.append(f"**{role}**\n\n{t}\n")

        joined = "\n".join(body)
        if len(joined.split()) < args.min_words:
            skipped += 1
            continue

        front = (f"---\ntitle: {title}\nsource: chat export\n"
                 f"created: {str(created)[:10]}\n---\n\n# {title}\n\n")
        path = os.path.join(args.outdir, f"{slug(str(title))}.md")
        n = 2
        while os.path.exists(path):
            path = os.path.join(args.outdir, f"{slug(str(title))}-{n}.md")
            n += 1
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(front + joined)
        written += 1

    print(f"wrote {written} files to {args.outdir}, skipped {skipped} short conversations")


if __name__ == "__main__":
    main()
