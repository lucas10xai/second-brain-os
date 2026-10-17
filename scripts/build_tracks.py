#!/usr/bin/env python3
"""Sync the course and handbook READMEs with the editorial order below.

COURSE and TRACKS hold each folder's title, blurb and page order. This script
checks every listed page exists, renders it once as a sanity check, and writes
docs/<folder>/README.md so the order on GitHub and on the site agree. The site
reads that order back from the READMEs:

    pip install markdown
    python3 scripts/build_tracks.py
    python3 tools/build_graph_site.py

It used to inject the pages into the old single-file index.html; the graph
page has its own builder now, so index.html is not touched here.
"""
import io, json, os, re, sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# the course: seven modules, three lessons each - theory, mechanics, practice.
# Built on Google's agent whitepapers and the five-layer frame.
COURSE = {
    "course-0-map": {
        "title": "0 · Bản đồ tổng quan",
        "blurb": "Agent là gì, năm tầng kiến trúc bao quanh mô hình, và "
                 "khi nào một quy trình cố định (workflow) vượt trội hơn vòng lặp (loop).",
        "order": ["what-an-agent-is", "five-layers", "agents-or-workflows"],
    },
    "course-1-context": {
        "title": "1 · Ngữ cảnh (Context)",
        "blurb": "Những gì mô hình nhìn thấy: cơ chế chú ý (attention), bộ nhớ đệm (caching), "
                 "bốn vị trí đặt ngữ cảnh, phiên làm việc và bộ nhớ dài hạn.",
        "order": ["how-models-read", "the-four-places", "context-practice"],
    },
    "course-2-loop": {
        "title": "2 · Vòng lặp (Loop)",
        "blurb": "Ai quyết định bước tiếp theo: mục tiêu, bộ kiểm tra (checker), quy tắc dừng, "
                 "ngân sách — và mô hình lai (hybrid) sống sót trong môi trường thực tế.",
        "order": ["loops-vs-workflows", "the-four-parts", "loop-practice"],
    },
    "course-3-gate": {
        "title": "3 · Cổng phân luồng (The Gate)",
        "blurb": "Những quyết định chi phí thấp đặt trước các mô hình đắt tiền: ưu tiên bộ phân loại "
                 "trước, chỉ dùng mô hình System One ở nơi thực sự xứng đáng.",
        "order": ["cheap-decisions", "gates-in-practice", "gate-practice"],
    },
    "course-4-harness": {
        "title": "4 · Khung vận hành (Harness)",
        "blurb": "Không gian làm việc bao quanh mô hình: vùng cô lập, hướng dẫn, cảm biến, "
                 "quyền hạn — được xây dựng từ ngoài vào trong.",
        "order": ["the-office", "the-four-rings", "harness-practice"],
    },
    "course-5-evals": {
        "title": "5 · Đánh giá (Evals)",
        "blurb": "Cùng một bài kiểm tra chạy định kỳ mỗi tháng: kiểm tra hành vi trên vết thực thi (traces), "
                 "kiểm chứng giám khảo AI, và bộ dữ liệu chuẩn (golden set) bao gồm cả các ca lỗi.",
        "order": ["two-kinds-of-checks", "judges-and-golden-sets",
                  "evals-practice"],
    },
    "course-6-production": {
        "title": "6 · Vận hành thực tế (Production)",
        "blurb": "Từ bản thử nghiệm đến triển khai thực tế: gateway, truy vết (tracing), chi phí, bảo mật — "
                 "và kế hoạch ngày đầu tiên xuyên suốt cả năm tầng kiến trúc.",
        "order": ["from-prototype", "operating-agents", "day-one-plan"],
    },
}

# page order inside each track is editorial, not alphabetical
TRACKS = {
    "track-graph": {
        "title": "Đồ thị tri thức (Knowledge graphs)",
        "blurb": "Đồ thị trong vai trò bộ nhớ của Agent: GraphRAG, quy trình trích xuất, "
                 "kho lưu trữ đồ thị — cùng bài thực hành một buổi tối xây dựng tầng đồ thị "
                 "trên chính vault của bạn.",
        "order": ["why-graphs", "graphrag", "building-graphs-with-llms",
                  "graph-stores", "tools",
                  "build-extract", "build-query", "build-use", "resources"],
    },
    "track-jev": {
        "title": "Kỹ thuật Jev (Jev engineering)",
        "module": ("3", "course-3-gate"),
        "blurb": "Cổng phân luồng (Gate) là tầng kiến trúc; Jev là một cách để xây dựng nó. "
                 "Trả về quyết định định kiểu kèm điểm tự tin thay vì sinh văn bản tự do "
                 "— cùng bài thực hành bạn có thể chạy ngay cả trước khi có quyền truy cập Jev.",
        "order": ["system-one-models", "what-jev-is-good-for",
                  "jev-in-an-agent-stack", "getting-started",
                  "build-decision-endpoint", "build-router",
                  "build-swap-in-jev", "resources"],
    },
    "track-harness": {
        "title": "Khung vận hành Agent (Agent harnesses)",
        "module": ("4", "course-4-harness"),
        "blurb": "Cỗ máy bao quanh mô hình: vòng lặp, công cụ, kỹ thuật ngữ cảnh, "
                 "bức tranh toàn cảnh — và tự tay viết một khung vận hành hoàn chỉnh "
                 "chỉ trong một buổi tối với khoảng 150 dòng code.",
        "order": ["what-a-harness-is", "claude-code-as-harness",
                  "context-engineering", "tools-and-mcp",
                  "harness-landscape",
                  "build-the-loop", "build-guardrails", "build-graduate",
                  "resources"],
    },
    "track-loop": {
        "title": "Kỹ thuật vòng lặp (Loop engineering)",
        "module": ("2", "course-2-loop"),
        "blurb": "Hệ thống điều khiển bao quanh Agent: điều kiện dừng, bộ phản biện (critics), "
                 "vệ sinh ngữ cảnh — và một vòng lặp chạy qua đêm bạn có thể hoàn toàn yên tâm "
                 "khi thức dậy vào sáng hôm sau.",
        "order": ["what-loop-engineering-is", "stop-conditions",
                  "critics-and-verification", "context-hygiene", "patterns",
                  "build-goal-test", "build-critic", "build-overnight",
                  "resources"],
    },
    "track-evals": {
        "title": "Kỹ thuật đánh giá (Eval engineering)",
        "module": ("5", "course-5-evals"),
        "blurb": "Đo lường là kỷ luật cốt lõi của sản phẩm AI: bộ dữ liệu chuẩn (golden sets), "
                 "giám khảo không nói dối, quỹ đạo thực thi của Agent — và tự xây dựng "
                 "bộ đánh giá đầu tiên chỉ trong một buổi chiều.",
        "order": ["why-evals", "designing-evals", "llm-as-judge",
                  "agent-evals", "tooling",
                  "build-traces", "build-suite", "build-ci", "resources"],
    },
}

MD = markdown.Markdown(extensions=["fenced_code", "tables"])


def render_page(sec, fname):
    meta = COURSE.get(sec) or TRACKS[sec]
    path = os.path.join(ROOT, "docs", sec, fname + ".md")
    src = io.open(path, encoding="utf-8").read().strip()
    lines = src.split("\n")
    if not lines[0].startswith("# "):
        raise SystemExit(f"{path}: first line must be an H1 title")
    title = lines[0][2:].strip()
    body = "\n".join(lines[1:]).strip()
    MD.reset()
    html = MD.convert(body)
    # relative images resolve against the repo, wherever the page renders
    html = re.sub(r'(<img[^>]+src=")(?!https?:|/|docs/)',
                  lambda m: m.group(1) + f"docs/{sec}/", html)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    headings = re.findall(r"<h2[^>]*>(.*?)</h2>", html)
    links = []
    for href, label in re.findall(r'href="([^"]+\.md)"[^>]*>(.*?)</a>', html):
        to = sec + "/" + href.replace("./", "").replace(".md", "")
        links.append({"to": to, "label": re.sub(r"<[^>]+>", "", label)})
    return {
        "id": f"{sec}/{fname}",
        "path": f"docs/{sec}/{fname}.md",
        "section": sec,
        "section_title": meta["title"],
        "title": title,
        "html": html,
        "headings": headings,
        "words": len(text.split()),
        "text": text[:4000],
        "links": links,
    }


def main():
    D = {"pages": [], "sections": {}, "order": {}}
    build_group(D, COURSE, "course")
    build_group(D, TRACKS, "track")
    print("READMEs synced - now run: python3 tools/build_graph_site.py")


def build_group(D, group, kind):
    cards = []
    for sec, meta in group.items():
        missing = [f for f in meta["order"]
                   if not os.path.exists(os.path.join(ROOT, "docs", sec, f + ".md"))]
        if missing:
            print(f"skip {sec}: missing {', '.join(missing)}")
            continue
        pages = [render_page(sec, f) for f in meta["order"]]
        D["pages"].extend(pages)
        D["sections"][sec] = {"title": meta["title"], "blurb": meta["blurb"],
                              kind: True}
        D["order"][sec] = [p["id"] for p in pages]
        cards.append(
            f'<article><h3><a href="#{pages[0]["id"]}">{meta["title"]}</a></h3>'
            f'<p>{meta["blurb"]}</p>'
            f'<div class="pg">{len(pages)} trang</div></article>')
        # a browsable README per folder, kept in sync with the order
        toc = "\n".join(f"{n}. [{p['title']}]({os.path.basename(p['path'])})"
                        for n, p in enumerate(pages, 1))
        if kind == "course":
            label = ("Một học phần thuộc khóa học bên cạnh [cẩm nang chính](../../README.md)"
                     " — đọc trực tiếp trên trang web hoặc theo thứ tự dưới đây.")
        elif meta.get("module"):
            n, mdir = meta["module"]
            label = (f"Sổ tay chuyên sâu cho [học phần {n}](../{mdir}/README.md) của "
                     "khóa học AI Agent: học phần dạy khái niệm cốt lõi một lần; "
                     "sổ tay này lưu giữ toàn bộ danh mục kỹ thuật, công cụ và "
                     "bài thực hành. Đọc trên trang web hoặc tra cứu bất kỳ bài nào dưới đây.")
        else:
            label = ("Sổ tay chuyên sâu bên cạnh [cẩm nang chính](../../README.md) — "
                     "toàn bộ danh mục kỹ thuật cho một tầng kiến trúc; tra cứu bất kỳ phần nào bạn cần.")
        io.open(os.path.join(ROOT, "docs", sec, "README.md"), "w",
                encoding="utf-8", newline="\n").write(
            f"# {meta['title']}\n\n{meta['blurb']}\n\n{label}\n\n{toc}\n")
        print(f"{sec}: {len(pages)} pages, "
              f"{sum(p['words'] for p in pages)} words")
    return cards


if __name__ == "__main__":
    main()
