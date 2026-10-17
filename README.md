# AI Second Brain

Một cơ sở tri thức do AI Agent xây dựng và duy trì cho bạn, nằm trọn trong các file Markdown thuần văn bản mà bạn toàn quyền sở hữu. Mọi thứ bạn đọc, xem và lưu lại đều được chuyển thành các trang wiki có liên kết chặt chẽ, kết nối với toàn bộ tri thức sẵn có, và bạn có thể đặt câu hỏi trực tiếp cho nó.

Repository này là phiên bản đầy đủ của bộ cẩm nang: từ khái niệm cốt lõi, hướng dẫn thiết lập, mẫu Vault khởi đầu, bộ Skills cho Agent, các script tiện ích cho đến danh mục tài nguyên. Hoàn toàn miễn phí, không cần đăng ký, không cần cài đặt thêm bất kỳ thứ gì ngoài Obsidian và một Agent.

**Đọc trên web:** [secondbrainos-vn.pages.dev](https://secondbrainos-vn.pages.dev/) — toàn bộ cẩm nang kèm tính năng tìm kiếm và điều hướng, cùng với [danh sách mọi liên kết đã qua chọn lọc](https://secondbrainos-vn.pages.dev/resources.html) trên một trang có bộ lọc tiện lợi.

Có ba phần nội dung tại đây — hãy chọn lối vào phù hợp với bạn:

- **[Cẩm nang Second Brain](#the-guide)** — lộ trình thực hiện một lần: xây dựng cơ sở tri thức để Agent tự động duy trì cho bạn. Gồm 65 trang tài liệu, một Vault mẫu khởi đầu và 18 Skills.
- **[Khóa học về Agent](#the-agents-course)** — lộ trình đọc theo thứ tự: bảy học phần đi từ một câu lệnh nhắc (prompt) đơn lẻ đến một Agent vận hành thực tế (production), đi kèm [bộ công cụ cài đặt chỉ với hai câu lệnh](plugins/README.md).
- **[Bộ sổ tay chuyên đề](#the-handbooks)** — tài liệu tham khảo độc lập, không cần đọc tuần tự: thực đơn đầy đủ các kỹ thuật, công cụ và bài thực hành xây dựng cho từng tầng kiến trúc. Hãy mở phần tương ứng khi tầng đó bắt đầu gây khó khăn cho bạn.

## Vấn đề hệ thống này giải quyết

Bạn lưu lại rất nhiều thứ với ý định sẽ xem lại sau, nhưng chẳng bao giờ làm thế. Dấu trang (bookmarks), ảnh chụp màn hình, danh sách đọc sau và những trang Notion viết dở cứ thế chất đống mà không tạo ra giá trị tích lũy, bởi việc phân loại và liên kết chúng là công việc nhàm chán mà con người thường bỏ cuộc chỉ sau hai tuần.

Hãy giao công việc đó cho một Agent và hệ thống sẽ luôn sống động. Toàn bộ ý tưởng chỉ gói gọn như vậy.

## Bắt đầu nhanh (Quickstart)

Chỉ mất một buổi tối. Chín bước thực hiện, mỗi bước đều có một trang hướng dẫn chi tiết phía sau.

```bash
# copy the starter vault, skills, commands and agents
git clone https://github.com/lucas10xai/second-brain-os.git
cp -r second-brain-os/vault-template ~/brain

mkdir -p ~/brain/.claude
cp -r second-brain-os/skills   ~/brain/.claude/skills
cp -r second-brain-os/commands ~/brain/.claude/commands
cp -r second-brain-os/agents   ~/brain/.claude/agents
cp -r second-brain-os/scripts  ~/brain/scripts

# the folder READMEs are for reading on GitHub, not for the agent
rm ~/brain/.claude/*/README.md ~/brain/scripts/README.md

cd ~/brain && claude
```

Bản sao thư mục `scripts/` giúp các lệnh `/metrics`, `/health` và `/graph-export` có thể chạy `scripts/vault_stats.py` cùng các công cụ liên quan ngay bên trong Vault. Trên Windows, hãy dùng `python` ở những nơi cẩm nang này ghi `python3`: tên lệnh `python3` thường trỏ tới bản stub của Microsoft Store và không thực thi được gì.

1. [Cài đặt Obsidian](docs/02-setup/obsidian-install-and-vault.md) và mở thư mục `~/brain` bạn vừa sao chép bằng tùy chọn "Open folder as vault"
2. [Thiết lập Claude Code](docs/02-setup/claude-code-setup.md), ngay trong terminal hoặc qua thẻ Code trên ứng dụng máy tính
3. [Kết nối qua MCP](docs/02-setup/mcp-obsidian.md) nếu bạn muốn Agent truy cập được vào Vault từ bất cứ đâu. Tùy chọn này không bắt buộc, có thể bỏ qua trong ngày đầu tiên
4. [Để Agent phỏng vấn tạo file CLAUDE.md](docs/02-setup/claude-md.md) thay vì tự ngồi viết thủ công
5. [Thiết lập cấu trúc hai tầng](docs/02-setup/vault-structure.md): một tầng wiki cho những gì bạn biết, và một tầng dự án (projects) cho những gì bạn đang làm
6. [Giới hạn phạm vi vào một dự án](docs/02-setup/project-scoping.md) khi bạn muốn tập trung hoàn thành một sản phẩm cụ thể
7. Cài đặt [Web Clipper](https://obsidian.md/clipper), lưu một bài viết về `raw/`, sau đó chạy lệnh `/ingest`
8. [Kết nối dữ liệu thời gian thực](docs/02-setup/live-data.md): lịch làm việc, email, tin nhắn trò chuyện
9. [Lên lịch bảo trì tự động](docs/06-agents/scheduled-maintenance.md) để mỗi sáng thức dậy với một Vault đã được tự động sắp xếp gọn gàng

Sau đó, hãy nạp thêm mười nguồn tài liệu nữa trước khi đánh giá hiệu quả. Đồ thị tri thức (Knowledge graph) sẽ chưa mấy thú vị khi chỉ có năm trang, nhưng bạn sẽ khó lòng rời mắt khỏi nó khi đạt mốc năm mươi trang.

Hướng dẫn chi tiết toàn diện: [Thiết lập](docs/02-setup/README.md).

## Cách hệ thống hoạt động

```
   you                    raw/                 agent                 wiki/
 ┌───────┐          ┌──────────────┐      ┌────────────┐      ┌──────────────┐
 │ clip  │  ──────> │ articles     │ ───> │  ingest    │ ───> │ sources/     │
 │ save  │          │ transcripts  │      │  extract   │      │ concepts/    │
 │ dump  │          │ pdfs         │      │  link      │      │ entities/    │
 └───────┘          │ chat exports │      │  lint      │      │ synthesis/   │
                    └──────────────┘      └────────────┘      └──────────────┘
                                                │                     │
                                                │   ask anything      │
                                                └─────────────────────┘
```

Tư liệu thô (`raw/`) là kho lưu trữ mà bạn chẳng bao giờ đọc lại. Tầng `wiki/` mới là thành phẩm chính, được viết bằng ngôn ngữ rõ ràng, mỗi trang một ý tưởng và liên kết dày đặc với nhau. Các nguồn tài liệu mới sẽ cập nhật trực tiếp vào những trang hiện có thay vì chất đống bên cạnh, nhờ đó Vault ngày càng chất lượng hơn khi mở rộng chứ không chỉ phình to về dung lượng.

Nằm cạnh tầng wiki là tầng dự án (project layer): mỗi dự án một thư mục riêng, có file `CLAUDE.md` riêng cùng quy trình `Inputs / Process / Outputs / Feedback`. Tầng wiki lưu giữ những gì bạn biết, còn tầng dự án chứa những gì bạn đang triển khai, và hai tầng này liên tục bồi đắp cho nhau. Bài viết [Cấu trúc hai tầng](docs/01-concepts/two-layers.md) sẽ giải thích vì sao việc tách bạch hai tầng này lại quan trọng hơn bạn nghĩ.

## Có gì trong kho lưu trữ này

| Thư mục | Nội dung lưu trữ |
|---|---|
| [`docs/`](docs/README.md) | Bộ cẩm nang chính. Mười chương, đi từ khái niệm cơ bản đến xử lý sự cố |
| [`docs/course-*/`](docs/course-0-map/README.md) | Khóa học về Agent: bảy học phần, từ câu lệnh nhắc (prompt) đến vận hành thực tế |
| [`docs/track-*/`](docs/track-graph/README.md) | Năm cuốn sổ tay chuyên sâu về kỹ nghệ xây dựng hệ thống: đồ thị, Jev, Harness, Loop, Evals |
| [`vault-template/`](vault-template/) | Mẫu Vault khởi đầu: cấu trúc wiki, quy trình dự án, file `CLAUDE.md` và các mẫu trang |
| [`skills/`](skills/README.md) | 18 Skills cho Agent, mỗi Skill tương ứng với một Workflow trong cẩm nang |
| [`commands/`](commands/README.md) | 72 Slash commands, các điểm kích hoạt theo phạm vi hẹp dẫn vào những Skills trên |
| [`agents/`](agents/README.md) | 6 Subagents, trong đó bốn Subagent được thiết kế ở chế độ chỉ đọc (read-only) |
| [`plugins/`](plugins/README.md) | Các plugin cho Claude Code — bộ công cụ thực hành của khóa học, cài đặt trong hai câu lệnh |
| [`scripts/`](scripts/README.md) | Các script Python không phụ thuộc thư viện ngoài để kiểm tra liên kết, thống kê và xuất đồ thị |
| [`resources/`](resources/README.md) | Công cụ, kho mã nguồn, bài báo khoa học và tài liệu đọc thêm đáng giá |
| [`examples/`](examples/README.md) | Các Vault thực tế và kết quả đầu ra mẫu |

## Cẩm nang hướng dẫn

Mười chương với 77 trang tài liệu, được viết để bạn làm theo từng bước chứ không chỉ đọc lướt qua. Lộ trình đi xuyên suốt từ khái niệm, thiết lập, thu thập, cấu trúc hóa, đồ thị, tự động hóa, truy xuất, xuất bản, cho đến cách khắc phục khi bất kỳ khâu nào gặp sự cố.

| Chương | Nội dung chính |
|---|---|
| [Khái niệm](docs/01-concepts/README.md) | mô hình hoạt động cốt lõi và lý do các hệ thống ghi chú kiểu cũ thất bại |
| [Thiết lập](docs/02-setup/README.md) | Obsidian, Claude Code, `CLAUDE.md`, MCP, dự án, Git |
| [Thu thập dữ liệu (Ingestion)](docs/03-ingestion/README.md) | bài viết web, video, PDF, lịch sử trò chuyện, ghi âm giọng nói, nạp dữ liệu tồn đọng |
| [Cấu trúc hóa](docs/04-structuring/README.md) | các loại trang, quy tắc liên kết, lược đồ chuẩn (schema), xử lý mâu thuẫn |
| [Đồ thị tri thức](docs/05-graphs/README.md) | mục đích của đồ thị, liên kết phân loại, GraphRAG, các chỉ số đo lường |
| [Tác tử (Agents)](docs/06-agents/README.md) | phân vai, lập lịch tự động, Hooks, Guardrails |
| [Truy xuất (Retrieval)](docs/07-retrieval/README.md) | các mẫu câu hỏi truy vấn, công cụ tìm kiếm, ngân sách ngữ cảnh (context budget) |
| [Đầu ra (Outputs)](docs/08-outputs/README.md) | viết bài, lập báo cáo nghiên cứu, xuất bản, học tập chủ động |
| [Bảo trì (Maintenance)](docs/09-maintenance/README.md) | kiểm tra lỗi (Lint), nhịp độ rà soát, Git, quyền riêng tư, mở rộng quy mô |
| [Xử lý sự cố](docs/10-troubleshooting/README.md) | những lỗi phổ biến ai cũng gặp phải và cách khắc phục triệt để |

## Khóa học về Agent

Bảy học phần đi từ một câu lệnh nhắc (prompt) đơn lẻ đến một Agent vận hành thực tế, được xây dựng dựa trên các sách trắng (whitepapers) về Agent của Google và khung kiến trúc năm tầng: những gì Agent nhìn thấy, ai quyết định bước tiếp theo, ai phân loại công việc đầu vào, những công cụ nó có thể chạm tới, và làm sao để biết hệ thống hoạt động đúng. Lý thuyết có trích dẫn nguồn rõ ràng, mỗi học phần đều có một trang thực hành, và khép lại bằng kế hoạch triển khai ngay từ ngày đầu tiên.

| Học phần | Nội dung giảng dạy |
|---|---|
| [0 · Bản đồ tổng quan](docs/course-0-map/README.md) | bản chất của Agent, kiến trúc năm tầng, phân biệt Agent và Workflow |
| [1 · Ngữ cảnh (Context)](docs/course-1-context/README.md) | cơ chế chú ý (attention), Prompt caching, bốn vùng lưu trữ, phiên làm việc và bộ nhớ |
| [2 · Vòng lặp (Loop)](docs/course-2-loop/README.md) | mục tiêu, bộ kiểm tra, quy tắc dừng, ngân sách; mô hình lai trong môi trường thực tế |
| [3 · Cổng phân luồng (The gate)](docs/course-3-gate/README.md) | ưu tiên các quyết định chi phí thấp trước: bộ phân loại, các mô hình Tư duy Nhanh (System One) |
| [4 · Khung kiểm soát (Harness)](docs/course-4-harness/README.md) | cô lập môi trường, hướng dẫn, cảm biến theo dõi, phân quyền truy cập |
| [5 · Đánh giá (Evals)](docs/course-5-evals/README.md) | kiểm tra hành vi trên Traces, thẩm định giám khảo AI, bộ dữ liệu chuẩn (Golden sets) |
| [6 · Vận hành thực tế (Production)](docs/course-6-production/README.md) | cổng kết nối (gateways), truy vết, tối ưu chi phí, bảo mật, kế hoạch ngày đầu tiên |

Khóa học đi kèm bộ công cụ riêng dưới dạng một [plugin cho Claude Code](plugins/README.md) — bao gồm bộ kiểm toán ngữ cảnh, công cụ tạo bài kiểm tra mục tiêu, bộ dò cổng phân luồng, bộ kiểm toán Harness, công cụ khởi tạo Evals và bộ phê bình Loop; mỗi công cụ thực thi đúng bài thực hành của một học phần ngay trên kho mã nguồn của bạn:

```bash
claude plugin marketplace add lucas10xai/second-brain-os
claude plugin install agents-course@second-brain-os
```

## Bộ sổ tay chuyên đề

Toàn bộ phần trên tập trung vào Second Brain. Bộ sổ tay chuyên đề mở rộng sang kỹ nghệ xây dựng hệ thống với Agent nói chung — gồm các chủ đề độc lập, được biên soạn cô đọng có chủ đích: mỗi cuốn dài tám hoặc chín trang, cập nhật đến tháng 9 năm 2026, và luôn kết thúc bằng một bài thực hành xây dựng hoàn chỉnh trong một buổi tối.

| Sổ tay | Nội dung bao quát | Bài thực hành xây dựng |
|---|---|---|
| [Knowledge graphs](docs/track-graph/README.md) | GraphRAG, quy trình trích xuất, kho lưu trữ, dùng Wikilink làm đồ thị | một tầng đồ thị có thể truy vấn trực tiếp trên chính Vault của bạn |
| [Kỹ nghệ Jev](docs/track-jev/README.md) | các mô hình System One: ra quyết định có kiểu dữ liệu kèm độ tin cậy thay vì sinh văn bản | bộ định tuyến kiểm soát bằng ngưỡng tin cậy, sẵn sàng cho Jev khi mở quyền truy cập |
| [Agent harnesses](docs/track-harness/README.md) | vòng lặp Loop, công cụ, Context engineering, MCP, bức tranh toàn cảnh | một bộ Harness hoạt động hoàn chỉnh chỉ trong ~150 dòng mã |
| [Kỹ nghệ Loop](docs/track-loop/README.md) | điều kiện dừng, bộ phê bình (critics), vệ sinh ngữ cảnh, chạy tự động không cần giám sát | một vòng lặp chạy qua đêm có chốt chặn tiến độ (ratchet) và báo cáo sáng hôm sau |
| [Kỹ nghệ Eval](docs/track-evals/README.md) | Golden sets, giám khảo LLM, quỹ đạo hành동 của Agent, cổng kiểm duyệt CI | bộ Eval đầu tiên của bạn, tích hợp thẳng vào quy trình CI |

Đọc trực tuyến trên trang web: [Bộ sổ tay tại secondbrainos-vn.pages.dev](https://secondbrainos-vn.pages.dev/).

## Các quyết định thiết kế cốt lõi

Hệ thống này được thiết kế với quan điểm rất rõ ràng. Dưới đây là ba nguyên tắc quan trọng nhất và lý do đằng sau chúng:

**Chưa liên kết nghĩa là chưa hoàn tất Ingest.** Một trang mới được thêm vào mà không có liên kết nào sẽ trở nên vô hình chỉ sau một tuần. Liên kết tạo nên toàn bộ giá trị của hệ thống, vì vậy việc liên kết phải diễn ra ngay trong cùng một lượt chạy, bằng không quá trình Ingest coi như chưa hoàn thành.

**Mâu thuẫn phải được ghi nhận, tuyệt đối không ghi đè.** Khi một nguồn tài liệu mới bất đồng với nội dung trên một trang hiện có, cả hai quan điểm đều được giữ lại kèm theo ngày tháng và nguồn trích dẫn. Lịch sử về những gì bạn từng tin tưởng và lý do đằng sau đó chính là thứ duy nhất mà Vault của bạn có nhưng các công cụ tìm kiếm thì không.

**Không dùng cơ sở dữ liệu Vector cho đến khi thực sự cần.** Kho tư liệu cá nhân thường có quy mô nhỏ và vốn đã có cấu trúc rõ ràng. Các trang được cấu trúc tốt cộng với hệ thống liên kết có thể trả lời những câu hỏi mà phương pháp so khớp độ tương đồng theo đoạn văn bản (chunk similarity) bó tay, lại không tốn bất kỳ chi phí hạ tầng nào. Bài viết [Khi nào RAG thực sự phát huy tác dụng](docs/07-retrieval/rag-on-top.md) sẽ chỉ rõ ngưỡng quy mô đó.

## Hệ thống này dành cho ai

Bất kỳ ai đọc nhiều nhưng nhớ lại được ít hơn kỳ vọng: các nhà nghiên cứu, kỹ sư, người viết lách, sinh viên, hay những người xem ba tiếng video kỹ thuật mỗi tuần nhưng sau đó không đọng lại được gì.

Hệ thống này không dành cho wiki làm việc nhóm, không phải là công cụ thay thế Notion, và cũng sẽ không thể sắp xếp giúp bạn một Vault mà bạn chẳng bao giờ chịu nạp thêm tư liệu vào.

## Tính khả chuyển (Portability)

Mọi thứ ở đây đều là file Markdown thuần túy, các Wikilink và các file `SKILL.md`. Hệ thống hoạt động mượt mà với Claude Code cũng như bất kỳ Agent nào có khả năng đọc ghi file. Obsidian chỉ đóng vai trò là trình hiển thị đồ thị chứ không phải một sự phụ thuộc bắt buộc. Ngay cả khi bạn từ bỏ mọi công cụ được nhắc đến trong kho lưu trữ này, bạn vẫn giữ nguyên vẹn thư mục của mình cùng toàn bộ tri thức bên trong nó.

## Tài liệu học tập và nền tảng nghiên cứu

Tài liệu gốc khởi nguồn và các công trình nghiên cứu đứng sau những quyết định thiết kế trong cẩm nang này.

| Nguồn tài liệu | Giá trị mang lại |
|---|---|
| **[Bản gist llm-wiki của Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** (4/4/2026) | Mô hình cốt lõi làm nền tảng cho mọi thứ tại đây. Ngắn gọn, được viết như một file ý tưởng để dán thẳng vào Agent hơn là một bản đặc tả kỹ thuật. Hãy đọc tài liệu này trước tiên. |
| **[From Local to Global: GraphRAG](https://arxiv.org/abs/2404.16130)** arXiv:2404.16130 | Giải thích lý do vì sao truy xuất theo đoạn nhỏ (chunk retrieval) thất bại trước các câu hỏi bao quát toàn bộ kho dữ liệu — vốn chính là điều người dùng mong đợi ở một Second Brain. Mã nguồn: [microsoft/graphrag](https://github.com/microsoft/graphrag). |
| **[HippoRAG](https://arxiv.org/abs/2405.14831)** arXiv:2405.14831 | Truy xuất đồ thị kết hợp thuật toán PageRank cá nhân hóa cho các câu hỏi đa bước (multi-hop). Đây là công trình nghiên cứu đã công bố gần giống nhất với cơ chế một Agent lần theo các liên kết mở rộng dần ra ngoài. |
| **[Lost in the Middle](https://arxiv.org/abs/2307.03172)** arXiv:2307.03172, TACL | Bằng chứng thực nghiệm giải thích vì sao bạn không nên dán toàn bộ Vault vào Context window, đồng thời là cơ sở cho các quy tắc về [ngân sách ngữ cảnh](docs/07-retrieval/context-budget.md). |
| **[Ghi chú của Andy Matuschak](https://notes.andymatuschak.org)** | Hệ thống ghi chú xanh mãi (Evergreen notes) được viết công khai. Đây cũng là luận điểm phản biện mạnh mẽ nhất đối với phương pháp của chúng ta: nếu quá trình viết chính là quá trình tư duy, thì việc ủy thác nó cho AI đồng nghĩa với việc bạn không thực sự tư duy. |
| **How to Take Smart Notes** (Ahrens) | Phương pháp Zettelkasten. Nguyên tắc ghi chú nguyên tử (atomic notes) và liên kết dày đặc vẫn giữ nguyên giá trị; chính khối lượng công việc thủ công nặng nề mới là thứ khiến hầu hết mọi người bỏ cuộc. |
| **Building a Second Brain** (Forte) | Nơi khởi nguồn của thuật ngữ Second Brain và phương pháp PARA. Phần lớn cuốn sách bàn về những công việc bảo trì thủ công mà giờ đây một Agent có thể gánh vác hoàn toàn. |

Xem ghi chú đầy đủ tại: [reading.md](resources/reading.md) và [papers.md](resources/papers.md).

## Công cụ và Plugin

Danh sách các plugin Obsidian được xếp hạng theo lượt cài đặt từ thống kê cộng đồng chính thức vào tháng 9 năm 2026. Danh mục đầy đủ nằm trong [plugins.md](resources/plugins.md) và [tools.md](resources/tools.md).

| Mục đích | Lựa chọn khuyên dùng | Lượt cài đặt |
|---|---|---|
| Tích hợp Agent trong trình soạn thảo | [Claudian](https://github.com/yishentu/claudian) | 2.0M |
| Tích hợp Agent trong trình soạn thảo | [Copilot](https://github.com/logancyang/obsidian-copilot) | 1.8M |
| Gợi ý liên kết tự động | [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) | 1.2M |
| Truy cập qua giao thức MCP | [Local REST API with MCP](https://github.com/coddingtonbear/obsidian-local-rest-api) | 712K |
| Truy vấn dữ liệu trên Frontmatter | [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | 4.9M |
| Quản lý biểu mẫu (Templates) | [Templater](https://github.com/SilentVoid13/Templater) | 5.5M |
| Quản lý phiên bản | [Git](https://github.com/Vinzent03/obsidian-git) | 3.1M |
| Di chuyển dữ liệu từ nơi khác vào | [Importer](https://github.com/obsidianmd/obsidian-importer) | 1.6M |
| Tìm liên kết hỏng và trang mồ côi | [Find unlinked files](https://github.com/Vinzent03/find-unlinked-files) | 225K |
| Tạo thẻ ghi nhớ (flashcards) từ ghi chú | [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 592K |
| Bản đồ tư duy có cấu trúc | [ExcaliBrain](https://github.com/zsviczian/excalibrain) | 336K |
| Đồ thị tương tác nâng cao | [Juggl](https://github.com/HEmile/juggl) | 136K |

Các công cụ bên ngoài Obsidian: [Web Clipper](https://obsidian.md/clipper) để thu thập nội dung web, [Claude Code](https://code.claude.com/docs/en/setup) để bảo trì hệ thống, [yt-dlp](https://github.com/yt-dlp/yt-dlp) và [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) để xử lý đa phương tiện và tài liệu quét, [ripgrep](https://github.com/BurntSushi/ripgrep), [NetworkX](https://networkx.org), [Kuzu](https://kuzudb.com) và [Gephi](https://gephi.org) để phân tích đồ thị, cùng với [Quartz](https://github.com/jackyzha0/quartz) để xuất bản thành trang web.

## Bộ Skills và các bản triển khai khác

Kho lưu trữ này cung cấp sẵn **18 Skills, 72 Slash commands, 6 Subagents và 4 scripts**: mỗi Skill đảm nhận một Workflow trong cẩm nang, đi kèm một lệnh gọi cho từng phiên bản giới hạn phạm vi mà bạn thực sự dùng hàng ngày.

Các bản triển khai khác trong cộng đồng, được thống kê theo cùng tiêu chí (một repo cung cấp mười sáu Skills sẽ được tính là mười sáu). Số sao (Stars) lấy từ GitHub API vào tháng 9 năm 2026.

| Kho mã nguồn (Repo) | Số sao (Stars) | Thành phần cung cấp |
|---|---|---|
| [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 14.7K | 16 Skills, 3 Subagents, các cấu hình phân vai dựng sẵn |
| [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 2.2K | 1 Skill bao trọn các khâu ingest, biên dịch, truy vấn, lint |
| [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) | 1.9K | 13 Skills, 4 Subagents, bộ khởi đầu đầy đủ |
| [coleam00/second-brain-starter](https://github.com/coleam00/second-brain-starter) | 768 | 1 Skill thực hiện phỏng vấn người dùng trước khi thiết lập |
| [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain) | 704 | 4 Skills, có bộ cài đặt qua npm |
| [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | nhỏ | 47 lệnh, tương thích với cả ba loại Agent |
| [micuintus/llm-wiki](https://github.com/micuintus/llm-wiki) | nhỏ | 1 Skill, được thiết kế tối giản có chủ đích |

Nơi định nghĩa chuẩn định dạng Skill: [anthropics/skills](https://github.com/anthropics/skills) (20 Skills), [obra/superpowers](https://github.com/obra/superpowers) (14), [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (danh mục hơn 1.000 Skills). Ghi chú chi tiết về từng dự án có tại: [skills.md](resources/skills.md).

## Các kho mã nguồn về Đồ thị, RAG và Bộ nhớ

| Mục đích | Kho mã nguồn (Repo) | Số sao (Stars) |
|---|---|---|
| Xây dựng đồ thị từ bất kỳ thư mục nào | [Graphify](https://github.com/Graphify-Labs/graphify) | 116K |
| Graph RAG hỗ trợ cập nhật tăng dần | [LightRAG](https://github.com/HKUDS/LightRAG) | 39K |
| Bản tham chiếu chuẩn của Graph RAG | [microsoft/graphrag](https://github.com/microsoft/graphrag) | 36K |
| Graph RAG gọn nhẹ, dễ đọc hiểu mã nguồn | [nano-graphrag](https://github.com/gusye1234/nano-graphrag) | 4.0K |
| Truy xuất đa bước (multi-hop) | [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 4.0K |
| Tổng quan hệ sinh thái GraphRAG | [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 2.6K |
| Bộ nhớ dài hạn cho Agent | [mem0](https://github.com/mem0ai/mem0) | 65K |
| Đồ thị tri thức theo thời gian (temporal) | [graphiti](https://github.com/getzep/graphiti) | 31K |
| Bộ nhớ kết hợp đồ thị và Vector | [cognee](https://github.com/topoteretes/cognee) | 31K |
| Danh mục tổng hợp máy chủ MCP | [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 95K |

Các lựa chọn thay thế Obsidian để đặt Vault (từ Logseq đến AFFiNE), cùng với các framework RAG và ứng dụng ghi chú tích hợp sẵn AI được tổng hợp tại: [repositories.md](resources/repositories.md) và [tools.md](resources/tools.md).

## Đóng góp

Mọi chỉnh sửa, bổ sung tài nguyên và ví dụ thực tế đều được hoan nghênh. Hãy đọc [CONTRIBUTING.md](CONTRIBUTING.md) trước tiên: mọi khẳng định mang tính dữ kiện đều cần dẫn nguồn gốc (primary source), và mọi công cụ đưa vào danh sách đều phải có lý do thuyết phục.

## Ghi nhận tác giả (Credit)

Mô hình wiki vận hành bằng LLM (LLM wiki pattern) là ý tưởng của Andrej Karpathy, được công bố dưới dạng một [bản gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) vào ngày 4 tháng 4 năm 2026. Kho lưu trữ này là một bản triển khai cụ thể của mô hình đó, đồng thời bổ sung đầy đủ những phần mà bản gist gốc cố tình để mở.

<!-- TODO before publishing:
     - add the link to the original article
     - screenshots: graph view at 30 days, an example concept page
     - social preview image in Settings -> General -->

Cấp phép theo giấy phép MIT.
