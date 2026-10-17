# Lộ trình nội dung (Roadmap)

Toàn bộ các chương đã được biên soạn xong. Trang này đóng vai trò là bản đồ tổng quan về nội dung của từng bài viết, đồng thời là nơi để đề xuất thêm các chủ đề mới.

Mọi Pull Request đóng góp vào đề cương đều được hoan nghênh. Hãy đọc [CONTRIBUTING.md](../CONTRIBUTING.md) trước tiên: mọi khẳng định mang tính dữ kiện đều phải có nguồn dẫn chứng gốc.

---

## Khái niệm (hoàn thành)

Vì sao một cơ sở tri thức do LLM duy trì lại vượt trội hơn hẳn những hệ thống ghi chú bạn từng bỏ dở, và bản chất thực sự của mô hình này là gì.

- [x] **Second Brain thực chất là gì**
  - Định nghĩa cốt lõi trong khuôn khổ tài liệu này: một không gian lưu trữ cục bộ, thuần văn bản mà Agent của bạn có thể đọc và ghi trực tiếp
  - Những gì không phải là Second Brain: một bản Notion bóng bẩy hơn, hay một chatbot đính kèm đống file PDF của bạn
  - Ba nhiệm vụ chính: thu thập, kết nối và trả lời
  - Hiệu ứng lãi kép tri thức và lý do nó chỉ thực sự xuất hiện sau khoảng ~50 nguồn tài liệu
- [x] **Nghịch lý "lưu để đọc sau"**
  - Vì sao bạn liên tục lưu lại những thứ mình chẳng bao giờ mở ra xem lại
  - Chi phí truy xuất so với chi phí thu thập
  - Điểm gãy của dấu trang (bookmarks), ứng dụng đọc sau và ảnh chụp màn hình
  - Mọi thứ thay đổi ra sao khi có một tác nhân khác làm thay việc phân loại và sắp xếp
- [x] **Mô hình Wiki vận hành bằng LLM (LLM wiki pattern)**
  - Bản gist llm-wiki của Karpathy (công bố ngày 4/4/2026) và những gì nó quy định
  - Biên dịch thay vì tóm tắt: tầng `wiki/` là chính yếu, nguồn tư liệu thô (`raw/`) chỉ là kho lưu trữ
  - Ba thao tác cốt lõi: Ingest (nạp dữ liệu), Lint (kiểm tra lỗi), Query (truy vấn)
  - Ranh giới nơi bản gist dừng lại và việc triển khai thực tế bắt đầu
- [x] **Vì sao chọn Markdown và văn bản thuần túy**
  - Agent đọc và ghi file trực tiếp hiệu quả hơn nhiều so với việc gọi qua API
  - Tính khả chuyển: không bị khóa chặt vào nền tảng (vendor lock-in), không cần bước xuất dữ liệu, thân thiện với Git
  - Wikilink như một định dạng đồ thị bền vững trước mọi sự thay đổi công cụ
  - Giới hạn của văn bản thuần túy và thời điểm cần bổ sung cơ sở dữ liệu
- [x] **Zettelkasten, PARA và ghi chú xanh mãi (Evergreen notes)**
  - Điểm đúng đắn của từng hệ thống và gánh nặng mà chúng đòi hỏi ở người dùng
  - Vì sao gánh nặng bảo trì chính là thủ phạm giết chết mọi hệ thống ghi chú
  - Những nguyên tắc nào từ các phương pháp cũ vẫn còn nguyên giá trị áp dụng
  - Những phần việc nào LLM gánh vác giúp bạn và những gì nó không thể làm thay
- [x] **Wiki so với RAG**
  - Vì sao một kho tư liệu cá nhân hiếm khi cần đến cơ sở dữ liệu Vector
  - Chất lượng truy xuất: các trang có cấu trúc rõ ràng đối đầu với so khớp độ tương đồng theo đoạn nhỏ (chunk similarity)
  - So sánh về chi phí, độ trễ và khả năng gỡ lỗi (debuggability)
  - Khi nào RAG thực sự xứng đáng có mặt trong hệ thống
- [x] **Thế nào là một hệ thống vận hành tốt**
  - Các tiêu chí đánh giá thành công cụ thể cho một Vault đang hoạt động
  - Các chỉ báo sức khỏe: tỷ lệ trang mồ côi (orphan rate), mật độ liên kết (link density), độ tươi mới của trang
  - Các dấu hiệu suy thoái cần phát hiện sớm
  - Lộ trình thực tế trong tháng đầu tiên sử dụng

## Thiết lập (hoàn thành)

Đi từ con số không đến một Vault được Agent tự động duy trì, chỉ trong một buổi tối.

- [x] **Obsidian và Vault đầu tiên của bạn**
  - Cài đặt và khởi tạo một Vault cục bộ trên máy
  - Vì sao bản chất của Vault chỉ đơn giản là một thư mục
  - Những thiết lập đáng thay đổi ngay trong ngày đầu tiên
  - Các lưu ý về ứng dụng di động và đồng bộ hóa
- [x] **Cấu trúc Vault**
  - Các thư mục `raw/`, `wiki/`, `output/` và những gì thuộc về từng nơi
  - Các thư mục phân theo loại trang: `sources`, `entities`, `concepts`, `synthesis`
  - Hai file `index.md` và `log.md` đóng vai trò bề mặt điều khiển của Agent
  - Những cấu trúc cần tránh và lý do cây thư mục phân cấp quá sâu lại xung đột với đồ thị
- [x] **Chạy Claude Code bên trong Vault**
  - Cài đặt và khởi động Claude Code ngay trong thư mục Vault
  - Thiết lập quyền hạn (permissions) và những thao tác nào nên cấp phép
  - Lần chạy đầu tiên: hướng dẫn Agent nhận diện cấu trúc thư mục
  - Phân biệt phiên làm việc tương tác trực tiếp và các lượt chạy tự động theo lịch
- [x] **Viết file CLAUDE.md của bạn**
  - Những gì cần đưa vào file chỉ dẫn và những gì nên loại bỏ
  - Hợp đồng định dạng trang (page contracts): khuôn mẫu chuẩn cho từng loại trang
  - Các quy tắc liên kết mà Agent bắt buộc phải tuân thủ trong mọi lần chạy
  - Tinh chỉnh và hoàn thiện `CLAUDE.md` khi Vault phát triển lớn dần
- [x] **Những plugin đáng cài đặt**
  - Web Clipper
  - Dataview và những lợi ích thực sự nó mang lại
  - Templater
  - Những plugin dễ gây xung đột với các file do Agent quản lý
- [x] **Giao thức MCP cho Obsidian**
  - Khi nào bạn cần đến MCP và khi nào chỉ thao tác trực tiếp trên file là đủ
  - Kết hợp plugin Local REST API với lệnh `claude mcp add`
  - Những khả năng MCP mở khóa: làm việc ngay cả khi Obsidian đang đóng
  - Lưu ý bảo mật đối với máy chủ chạy cục bộ
- [x] **Git, đồng bộ hóa và sao lưu**
  - Vì sao một Vault lại là một kho lưu trữ Git lý tưởng
  - Những gì nên đưa vào commit và những gì cần loại trừ (ignore)
  - Các phương án đồng bộ hóa giữa nhiều thiết bị
  - Khôi phục lại trạng thái cũ sau một lượt chạy lỗi của Agent

## Thu thập dữ liệu - Ingestion (hoàn thành)

Đưa mọi thứ bạn đọc, xem và viết vào thư mục `raw/` với ít lực cản nhất có thể.

- [x] **Bài viết trên web**
  - Thiết lập Obsidian Web Clipper và cấu hình biểu mẫu (templates)
  - Lưu bài viết về `raw/` với cấu trúc Frontmatter đồng nhất
  - Xử lý tường thu phí (paywalls), bản tin (newsletters) và các trang web động
  - Nên lưu những gì và nên bỏ qua những gì
- [x] **YouTube và podcast**
  - Trích xuất bản gỡ băng (Transcripts) một cách đáng tin cậy
  - Dấu mốc thời gian (timestamps) và lý do cần giữ chúng lại
  - Video thời lượng dài: chia nhỏ trước khi đưa vào Ingest
  - Các nguồn chỉ có âm thanh và các phương án chuyển giọng nói thành văn bản
- [x] **PDF, bài báo khoa học và sách**
  - Trích xuất văn bản giữ nguyên được cấu trúc tài liệu
  - Tài liệu bản quét (scan) và nhận diện ký tự quang học (OCR)
  - Đồng bộ các đoạn tô sáng (highlights) từ máy đọc sách điện tử
  - Xử lý các bài báo khoa học có nhiều biểu đồ và bảng biểu
- [x] **Lịch sử trò chuyện AI (Chat exports)**
  - Xuất lịch sử trò chuyện từ Claude và ChatGPT
  - Chuyển đổi file xuất JSON thành từng file Markdown cho mỗi cuộc hội thoại
  - Lọc bỏ nhiễu: chọn lọc những cuộc trò chuyện thực sự đáng để Ingest
  - Bước rà soát quyền riêng tư trước khi đưa bất kỳ dữ liệu nào vào Vault
- [x] **Ghi chú giọng nói và cuộc họp**
  - Thu âm nhanh trên thiết bị di động
  - Quy trình chuyển đổi âm thanh thành văn bản
  - Biến nội dung cuộc họp thành các quyết định cụ thể và các trang thực thể (entities)
  - Giữ các bản ghi âm cá nhân tách biệt khỏi những Vault dùng chung
- [x] **Bản tin (Newsletters) và email**
  - Tạo một địa chỉ email chuyên dụng cho việc thu thập nội dung
  - Tự động chuyển tiếp (forward) thẳng vào thư mục `raw/`
  - Khử trùng lặp cho các bản tin định kỳ
  - Khi nào không nên đưa email vào hệ thống
- [x] **Nạp bù dữ liệu tồn đọng nhiều năm (Bulk backfill)**
  - Sắp xếp thứ tự nạp dữ liệu để các trang tạo trước không bị ghi đè mất thông tin
  - Chia lô xử lý (batching): bao nhiêu nguồn tài liệu mỗi lượt chạy là hợp lý
  - Kiểm soát chi phí khi nhập khối lượng dữ liệu lớn
  - Tạo điểm lưu trạng thái (checkpoints) và tiếp tục lại khi bị gián đoạn

## Cấu trúc hóa (hoàn thành)

Những quy tắc quyết định liệu Vault của bạn sẽ trở thành một đồ thị tri thức hay một bãi rác dữ liệu.

- [x] **Mỗi trang một ý tưởng**
  - Ý nghĩa thực tế của tính nguyên tử (atomic) trong ghi chú
  - Tách một nguồn tài liệu thành nhiều trang khái niệm riêng biệt
  - Độ dài hợp lý của một trang wiki
  - Khi nào nên gộp trang thay vì tách nhỏ
- [x] **Bốn loại trang cốt lõi**
  - Nguồn tư liệu (Sources): mỗi mục dữ liệu được Ingest tương ứng với một trang
  - Thực thể (Entities): con người, tổ chức, sản phẩm, công cụ
  - Khái niệm (Concepts): ý tưởng, khung tư duy (frameworks), phương pháp
  - Tổng hợp (Synthesis): so sánh đối chiếu, chủ đề xuyên suốt, các câu hỏi mở
- [x] **Quy tắc liên kết**
  - Đặt liên kết ngay ở lần nhắc đến đầu tiên đối với mọi loại trang
  - Số lượng liên kết tối thiểu và tối đa trên mỗi trang
  - Liên kết mang tính khẳng định mệnh đề, không phải để trang trí
  - Ngăn chặn các trang nút giao (hub pages) nuốt chửng toàn bộ đồ thị
- [x] **Lược đồ Frontmatter (Frontmatter schema)**
  - Các trường thông tin bắt buộc cho từng loại trang
  - Ngày tháng, đường dẫn nguồn (URL), mức độ tin cậy
  - Thẻ phân loại (Tags): duy trì một bộ từ vựng kiểm soát nhỏ gọn
  - Giữ cho lược đồ luôn ổn định khi Vault mở rộng quy mô
- [x] **Đặt tên và định danh thay thế (Aliases)**
  - Tiêu đề chuẩn hóa (canonical titles) và tầm quan trọng của chúng đối với Wikilink
  - Dùng Aliases cho các từ viết tắt và tên gọi thay thế
  - Phân biệt rõ hai khái niệm trùng tên nhưng khác bản chất
  - Đổi tên trang mà không làm gãy các liên kết hiện có
- [x] **Khử trùng lặp và gộp trang**
  - Phát hiện các trang gần như trùng lặp nhau
  - Quy trình gộp trang bảo toàn nguyên vẹn các liên kết ngược (Backlinks)
  - Tạo trang chuyển hướng (redirect stubs)
  - Lên lịch chạy khử trùng lặp định kỳ thay vì xử lý trực tiếp ngay lúc nạp
- [x] **Xử lý mâu thuẫn và thông tin thay thế**
  - Khi hai nguồn tài liệu bất đồng: trang wiki nên trình bày như thế nào
  - Đánh dấu các nhận định đã lỗi thời thay vì xóa bỏ hoàn toàn
  - Các trường ghi nhận độ tin cậy và nguồn gốc xuất xứ (provenance)
  - Vì sao việc âm thầm ghi đè dữ liệu lại là kiểu lỗi tệ hại nhất
- [x] **Hai file index.md và log.md**
  - File chỉ mục (`index.md`) đóng vai trò danh mục điều hướng chứ không phải bãi chứa
  - Những thông tin Agent bắt buộc phải ghi vào nhật ký (`log.md`)
  - Sử dụng nhật ký để kiểm toán và khôi phục trạng thái (rollback)
  - Ngăn không cho cả hai file này phình to vô hạn

## Đồ thị tri thức - Graphs (hoàn thành)

Phần mà hầu hết các tài liệu hướng dẫn Second Brain đều bỏ qua: đồ thị thực sự dùng để làm gì và làm sao để bắt nó phục vụ công việc của bạn.

- [x] **Kiến thức cơ bản về đồ thị cho cơ sở tri thức**
  - Đỉnh (nodes), cạnh (edges), hướng và trọng số được giải thích dễ hiểu
  - Vì sao cơ sở tri thức bản chất đã là một đồ thị dù bạn có chủ đích thiết kế hay không
  - Mật độ, hệ số phân cụm, độ dài đường đi và ý nghĩa thực tế của chúng
  - Các hình thái đồ thị lỗi cần tránh: hình sao, chuỗi dài và các ốc đảo cô lập
- [x] **Cách đọc chế độ xem đồ thị (Graph view) trong Obsidian**
  - Đồ thị cục bộ (local graph) so với đồ thị toàn cục (global graph)
  - Các bộ lọc và nhóm màu giúp đồ thị thực sự hữu ích
  - Nhận diện nhanh các trang mồ côi và các trang nút giao quá tải liên kết
  - Vì sao một đồ thị trông đẹp mắt chưa chắc đã là một đồ thị khỏe mạnh
- [x] **Liên kết có phân loại (Typed links)**
  - Wikilink không phân loại sẽ dần đánh mất ý nghĩa khi quy mô lớn lên
  - Bộ từ vựng quan hệ tối giản: củng cố (`supports`), mâu thuẫn (`contradicts`), mở rộng (`extends`), thuộc về (`part-of`)
  - Mã hóa loại quan hệ trong Frontmatter hoặc ngay trong dòng văn bản (inline)
  - Truy vấn dữ liệu dựa theo loại quan hệ
- [x] **Đồ thị so với Embeddings**
  - Thế mạnh thực sự của từng phương pháp truy xuất
  - Vì sao phép đo độ tương đồng lại bỏ sót khả năng suy luận bắc cầu qua nhiều nguồn
  - Các mô hình kết hợp (hybrid setups)
  - So sánh chi phí vận hành và công sức bảo trì
- [x] **GraphRAG và vị trí phù hợp của nó**
  - Tóm gọn ý tưởng cốt lõi trong một trang
  - Trích xuất thực thể và quan hệ từ chính Vault của bạn
  - Phát hiện cộng đồng (community detection) và các tầng tóm tắt
  - Liệu một Vault cá nhân có đủ lớn để cần đến GraphRAG hay không
- [x] **Xuất dữ liệu đồ thị**
  - Phân tích cú pháp Wikilink thành danh sách cạnh (edge list)
  - Nạp dữ liệu vào Kuzu, Neo4j hoặc NetworkX
  - Trực quan hóa đồ thị bên ngoài Obsidian
  - Giữ cho bản xuất dữ liệu luôn đồng bộ với Vault
- [x] **Các chỉ số đồ thị đáng theo dõi**
  - Tỷ lệ trang mồ côi (orphan rate)
  - Bậc liên kết trung bình (average degree) và ngưỡng giá trị khỏe mạnh
  - Các cụm liên kết (clusters) như bằng chứng phản ánh mối quan tâm thực sự của bạn
  - Theo dõi sự biến đổi của các chỉ số theo thời gian

## Tác tử - Agents (hoàn thành)

Biến một thiết lập thủ công một lần thành một hệ thống có khả năng tự duy trì chính nó.

- [x] **Phân vai cho Agent**
  - Bộ nạp dữ liệu (ingestor), bộ liên kết (linker), bộ rà soát (reviewer), bộ nghiên cứu (researcher)
  - Nguyên tắc mỗi Agent một nhiệm vụ chuyên biệt và lý do đằng sau
  - Cơ chế bàn giao công việc (handoffs) giữa các Agent
  - Những vai trò không đáng để tự động hóa
- [x] **Lập lịch tự động (Scheduling)**
  - Nhịp độ chạy cho từng tác vụ: mỗi giờ, mỗi ngày, mỗi tuần
  - Các tác vụ lập lịch sẵn, cron và các phương án chạy trên CI
  - Kết quả đầu ra chuẩn mà mỗi lượt chạy cần tạo ra
  - Phát hiện các lỗi ngầm không báo động (silent failures)
- [x] **Subagents và xử lý song song**
  - Khi nào nên phân nhánh tác vụ cho nhiều Subagents chạy đồng thời
  - Cô lập ngữ cảnh (context isolation) giữa các Subagents
  - Hợp nhất các chỉnh sửa song song mà không gây xung đột dữ liệu
  - Chi phí phải trả cho việc xử lý song song
- [x] **Cơ chế Hooks**
  - Tự động kích hoạt khi có thay đổi file trong thư mục `raw/`
  - Kiểm tra hợp lệ trước khi ghi file (pre-write validation)
  - Chạy Lint tự động sau mỗi lượt thực thi
  - Giữ cho các Hooks luôn chạy nhanh và gọn nhẹ
- [x] **Skills và Slash commands**
  - Dùng Skills cho các hành vi lặp lại, dùng Slash commands cho các tác vụ lặp lại
  - Nơi lưu trữ chuẩn để bất kỳ Agent nào cũng có thể sử dụng được
  - Quản lý phiên bản bộ Skills song hành cùng với Vault
  - Kiểm thử một Skill trước khi tin tưởng giao Vault cho nó thao tác
- [x] **Hàng rào bảo vệ (Guardrails)**
  - Tuyệt đối không để Agent xóa nội dung mà không ghi lại vào nhật ký
  - Giới hạn phạm vi ghi (write scopes): những thư mục nào là vùng cấm
  - Chế độ chạy thử không ghi thật (dry-run mode)
  - Rà soát kết quả của Agent thông qua bảng so sánh thay đổi của Git (git diffs)

## Truy xuất - Retrieval (hoàn thành)

Cách đặt câu hỏi cho Vault của bạn và nhận lại những câu trả lời thực sự đáng tin cậy.

- [x] **Đặt câu hỏi cho Vault**
  - Những cấu trúc câu hỏi mang lại hiệu quả cao
  - Neo chặt câu trả lời vào các trang wiki và nguồn tư liệu gốc
  - Yêu cầu trích dẫn trực tiếp từ chính Vault của bạn
  - Cách xử lý khi câu trả lời không có sẵn trong kho tri thức
- [x] **Các mẫu truy vấn phổ biến**
  - Tôi đang biết những gì về chủ đề X
  - Điều gì kết nối giữa X và Y
  - Tôi đã thay đổi quan điểm về vấn đề gì theo thời gian
  - Còn thiếu mảnh ghép nào trong sự hiểu biết của tôi về X
- [x] **Công cụ tìm kiếm**
  - Sử dụng `ripgrep` làm công cụ mặc định
  - Truy vấn bằng Dataview
  - Các phương án đánh chỉ mục toàn văn (full-text index)
  - Khi nào tốc độ tìm kiếm trở nên chậm đến mức cần can thiệp
- [x] **Bổ sung RAG khi thực sự cần thiết**
  - Ngưỡng quy mô dữ liệu mà tại đó RAG bắt đầu mang lại lợi ích
  - Cách chia nhỏ (chunking) một hệ thống wiki vốn đã được chia theo từng trang
  - Giữ cho chỉ mục tìm kiếm luôn được cập nhật mới
  - Mô hình lai (Hybrid): dùng đồ thị cho cấu trúc, dùng Vector cho độ phủ truy xuất (recall)
- [x] **Ngân sách ngữ cảnh (Context budget)**
  - Vì sao bạn không nên dán toàn bộ Vault vào khung trò chuyện
  - Tiết lộ thông tin lũy tiến (progressive disclosure): đọc chỉ mục trước, mở trang chi tiết sau
  - Các tầng tóm tắt phân cấp
  - Đo lường chính xác những gì Agent thực sự đã đọc

## Đầu ra - Outputs (hoàn thành)

Vault chỉ thực sự chứng minh được giá trị khi bạn tạo ra được các thành phẩm cụ thể từ nó.

- [x] **Viết lách từ Vault**
  - Lập dàn ý bài viết từ các trang khái niệm
  - Giữ nguyên các trích dẫn trỏ về nguồn tư liệu của chính bạn
  - Giữ vững giọng văn cá nhân: dựa trên ghi chú của bạn chứ không phải giọng văn rập khuôn của mô hình AI
  - Vòng lặp đưa bài viết đã xuất bản quay trở lại làm giàu cho Vault
- [x] **Báo cáo nghiên cứu**
  - Xác định phạm vi câu hỏi nghiên cứu dựa trên các trang hiện có
  - Lấp đầy các khoảng trống kiến thức bằng những đợt Ingest mới
  - Cấu trúc báo cáo vững chắc vượt qua được các vòng phản biện
  - Lưu trữ các báo cáo đầu ra để chúng tiếp tục trở thành nguồn tư liệu mới
- [x] **Xuất bản và trích xuất**
  - Các công cụ tạo trang web tĩnh (static site) cho một wiki công khai
  - Quyết định phần nội dung nào cần giữ riêng tư
  - Xuất dữ liệu sang định dạng HTML và PDF
  - Quản lý chung cả nội dung công khai lẫn riêng tư trong cùng một Vault
- [x] **Học tập từ chính Vault của bạn**
  - Tự động sinh câu hỏi ôn tập từ các trang khái niệm
  - Áp dụng lặp lại ngắt quãng (spaced repetition) ngay trên ghi chú của bạn
  - Phát hiện những nội dung bạn đã lưu lại nhưng chưa thực sự hiểu rõ
  - Đo lường mức độ tiếp thu kiến thức thay vì chỉ đếm số lượng thu thập

## Bảo trì - Maintenance (hoàn thành)

Những thói quen và công cụ giữ cho hệ thống luôn sống động sau khi cảm giác hào hứng ban đầu qua đi.

- [x] **Kiểm tra lỗi cho Vault (Linting)**
  - Phát hiện liên kết hỏng, trang mồ côi và các trang sơ khai bỏ trống (empty stubs)
  - Các lỗi vi phạm lược đồ chuẩn (schema violations)
  - Tự động hóa quy trình chạy Lint
  - Cách đọc và xử lý một báo cáo Lint
- [x] **Nhịp độ rà soát định kỳ**
  - Buổi rà soát hàng tuần chỉ tốn đúng mười phút
  - Rà soát cấu trúc tổng thể hàng tháng
  - Quyết định nội dung nào cần cắt tỉa và nội dung nào nên đưa vào lưu trữ lạnh
  - Các bản báo cáo rà soát do Agent chuẩn bị sẵn cho bạn
- [x] **Quản lý phiên bản (Versioning)**
  - Độ chi tiết của từng bản commit đối với các lượt chạy của Agent
  - Cách đọc bảng so sánh thay đổi (diffs) của các trang do AI tạo ra
  - Hoàn tác (revert) một lượt Ingest bị lỗi
  - Tạo nhánh (branching) riêng cho các thử nghiệm mới
- [x] **Sao lưu và tính khả chuyển**
  - Duy trì các bản sao cục bộ, trên đám mây và ngoại tuyến (offline)
  - Kiểm thử quy trình khôi phục dữ liệu
  - Chuyển đổi sang trình soạn thảo hoặc Agent khác
  - Tránh xa các định dạng độc quyền giam cầm dữ liệu của bạn
- [x] **Quyền riêng tư**
  - Xác định rõ những thông tin nào tuyệt đối không bao giờ được đưa vào Vault
  - Biên tập ẩn thông tin nhạy cảm (redaction) trước khi Ingest
  - Sử dụng các mô hình chạy cục bộ (local models) cho tư liệu nhạy cảm
  - Chia sẻ một phần Vault một cách an toàn
- [x] **Mở rộng quy mô vượt mốc một nghìn trang**
  - Những điểm mà phương pháp văn bản thuần túy bắt đầu bộc lộ sự quá tải
  - Tách nhỏ Vault theo từng lĩnh vực chuyên môn (domain)
  - Xây dựng các tầng tóm tắt và hệ thống chỉ mục phân cấp
  - Tinh chỉnh tối ưu hiệu năng

## Xử lý sự cố - Troubleshooting (hoàn thành)

Các tình huống lỗi cụ thể trong thực tế, đi kèm cách khắc phục triệt để.

- [x] **Những thất bại kinh điển ai cũng gặp phải**
  - Vault bị đình trệ và bỏ xó sau hai tuần đầu tiên
  - Các trang bị biến thành bản tóm tắt của những bản tóm tắt
  - Agent tự ý viết đè lên những nội dung bạn dày công biên soạn thủ công
  - Chất lượng Ingest suy giảm dần khi Vault phình to
- [x] **Agent viết ra nội dung rác**
  - Chẩn đoán nguyên nhân nằm ở file `CLAUDE.md` hay do chất lượng nguồn tài liệu đầu vào
  - Siết chặt lại các hợp đồng định dạng trang (page contracts)
  - Bổ sung các ví dụ mẫu cụ thể thay vì chỉ viết thêm quy tắc trừu tượng
  - Khôi phục lại bản cũ và chạy lại quy trình
- [x] **Liên kết hỏng và các trang mồ côi**
  - Vì sao việc đổi tên file lại làm gãy hệ thống Wikilink
  - Sửa lỗi hàng loạt một cách an toàn
  - Ngăn chặn sự hình thành trang mồ côi ngay tại thời điểm Ingest
  - Kiểm toán lại toàn bộ hệ thống sau một đợt nhập dữ liệu lớn
- [x] **Vault trở nên quá lớn**
  - Các triệu chứng nhận biết
  - Lựa chọn giữa việc tách nhỏ Vault hay tạo tầng tóm tắt
  - Đưa các tư liệu ít dùng vào kho lưu trữ lạnh (archiving)
  - Tái cấu trúc lại file chỉ mục (`index.md`)
- [x] **Câu hỏi thường gặp (FAQ)**
  - Tôi có thực sự cần dùng MCP hay không
  - Hệ thống này có hoạt động với các Agent khác ngoài Claude Code không
  - Chi phí vận hành thực tế là bao nhiêu
  - Tôi có thể sử dụng mô hình AI chạy cục bộ (local model) được không

---

[Quay lại cẩm nang hướng dẫn](README.md)
