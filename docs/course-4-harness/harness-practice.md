# Thực hành xây dựng Harness

Lý thuyết đã xong; giờ là lúc gia cố một `Agent` thực tế. Ví dụ thực hành dưới đây là một `Agent` lập trình làm việc trên một ứng dụng web sử dụng cơ sở dữ liệu Postgres và chạy thông qua Claude Code, nhưng mọi bước thực hiện đều có thể chuyển đổi tương đương sang bất kỳ `Harness` nào — bao gồm cả vòng lặp dài bảy mươi dòng code trong bài [xây dựng Loop](../track-harness/build-the-loop.md). Hãy triển khai lần lượt từng vòng đai theo đúng thứ tự.


> Nửa phần kiểm toán (audit) của buổi thực hành này đã được đóng gói thành một `Skill`: hãy cài đặt [plugin của khóa học](../../plugins/README.md) và chạy lệnh `/agents-course:harness-audit` trước khi bắt tay vào gia cố thủ công.

Một lưu ý định hình trước khi vào các bước: buổi thực hành này tập trung vào việc gia cố một `Agent` mà bạn đang vận hành sẵn. Còn việc tự tay chế tạo toàn bộ cỗ máy từ con số không — vòng lặp bảy mươi dòng code cùng các rào chắn bảo vệ (`Guardrails`) của nó — nằm ở [bài thực hành trong cẩm nang chuyên sâu về Harness](../track-harness/build-the-loop.md).

## Bước một: Dựng tường chắn (Containment)

Trước khi viết dòng prompt đầu tiên, hãy quyết định những gì `Agent` không được phép chạm tới. Hãy cấp cho nó một git worktree riêng biệt thay vì thư mục làm việc chính của bạn, cùng một tài khoản cơ sở dữ liệu chỉ có quyền đọc (read-only):

```bash
git worktree add ../agent-workspace -b agent/task-one
```

```sql
CREATE USER agent_ro WITH PASSWORD 'rotate-me';
GRANT CONNECT ON DATABASE app TO agent_ro;
GRANT USAGE ON SCHEMA public TO agent_ro;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO agent_ro;
```

Nếu `Agent` cần cài đặt các gói thư viện hoặc gọi API bên ngoài, hãy cho nó chạy bên trong một container có danh sách mạng được phép truy cập (allowlist — chỉ mở cho kho lưu trữ gói thư viện và API của mô hình, ngoài ra chặn toàn bộ). Bài kiểm tra cho bước này rất đơn giản: hãy tưởng tượng ra phiên làm việc tồi tệ nhất có thể xảy ra và kiểm tra xem bán kính thiệt hại (blast radius) có phải chỉ dừng lại ở một thư mục worktree bị xóa bỏ hay không.

## Bước hai: Viết tài liệu hướng dẫn (Guides)

Đặt một tập tin `AGENTS.md` (hoặc `CLAUDE.md`) duy nhất ngay tại thư mục gốc của kho mã nguồn, đủ ngắn gọn để được đọc trọn vẹn trong mọi phiên làm việc:

```markdown
- App code in src/, tests in tests/, run everything from the repo root.
- `make check` must pass before you call any task done.
- Never hand-edit files in migrations/ — generate them with `make migration`.
- Your database user is read-only. Ask before proposing any schema change.
```

Mỗi dòng đều nêu một quy tắc cụ thể mà `Agent` có thể hành động theo ngay. Không triết lý sáo rỗng, không kể lể lịch sử.

## Bước ba: Lắp đặt cảm biến (Sensors)

Hãy gom toàn bộ các bước kiểm tra tất định (deterministic checks) vào chung một lệnh duy nhất, sau đó cấu hình để `Harness` tự động chạy lệnh đó sau mỗi lần chỉnh sửa tập tin, thay vì hy vọng mô hình sẽ tự nhớ mà chạy:

```make
check:
	ruff check .
	mypy src
	pytest -q
```

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "make check" }
        ]
      }
    ]
  }
}
```

Mọi lỗi phát sinh sẽ xuất hiện ngay lập tức trong bản ghi hội thoại (transcript), ngay khi sai sót vừa mới diễn ra ở thao tác chỉnh sửa liền trước.

## Bước bốn: Cắt giảm quyền hạn (Permissions)

Áp dụng nguyên tắc đặc quyền tối thiểu (least privilege), và chỉ yêu cầu phê duyệt thủ công đối với những thao tác không thể đảo ngược:

```json
{
  "permissions": {
    "allow": ["Read", "Grep", "Glob", "Bash(make check)", "Bash(git diff:*)", "Bash(git status)"],
    "ask": ["Bash(git commit:*)", "Bash(git push:*)"],
    "deny": ["WebFetch", "Bash(rm:*)"]
  }
}
```

Con người có xu hướng bấm đồng ý gần như mọi hộp thoại xin phép mà họ nhìn thấy, vì vậy một danh sách hỏi xin phép (`ask`) thật ngắn gọn là thứ duy nhất thực sự được người dùng đọc kỹ. Nếu bạn thấy ngày nào mình cũng bấm phê duyệt một thao tác nào đó theo phản xạ mà không cần suy nghĩ, hãy chuyển nó sang danh sách cho phép sẵn (`allow`) — hoặc tốt hơn nữa, hãy thiết kế để thao tác đó không thể gây hại và loại bỏ luôn hộp thoại hỏi.

## Bước năm: Bổ sung một Hook cưỡng chế

Hãy chọn ra một quy tắc trong `AGENTS.md` mà nếu bị vi phạm sẽ gây hậu quả nặng nề nhất, và dùng `Hook` để cưỡng chế thực thi nó:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | grep -q 'migrations/' && { echo 'Blocked: generate migrations with make migration' >&2; exit 2; } || exit 0"
          }
        ]
      }
    ]
  }
}
```

Một `Hook` duy nhất được chọn lọc kỹ lưỡng sẽ hiệu quả hơn hẳn mười `Hook` kêu báo động liên hồi.

## Rà soát định kỳ hàng quý

Mỗi mảnh ghép trong `Harness` là một khoản đặt cược rằng mô hình chưa thể tự làm được việc gì đó, và những khoản cược này sẽ hết hạn theo thời gian — Anthropic từng xóa sổ nguyên một thành phần khung đỡ (cơ chế làm mới `Context` để chống lỗi kết thúc sớm) ngay sau một đợt nâng cấp mô hình khiến thành phần đó trở nên thừa thãi. Vì vậy, hãy đặt lịch hẹn định kỳ hàng quý. Đối với từng `Hook`, từng dòng hướng dẫn và từng quyền hạn bị cấm, hãy viết ra câu "thành phần này tồn tại vì mô hình không thể làm được X", sau đó đem kiểm thử khả năng X ngay trên thế hệ mô hình hiện tại. Hãy mạnh dạn xóa bỏ những gì không còn tạo ra giá trị; một `Harness` chỉ biết phình to thêm theo thời gian là một hệ thống đang cố bù đắp cho những điểm yếu của một mô hình đã thuộc về quá khứ.

## Mẹo thực chiến

- Chỉ thêm quy tắc mới vào `AGENTS.md` sau khi `Agent` làm sai cùng một việc tới lần thứ hai. Những quy tắc viết ra do suy đoán trước thường nhanh chóng trở nên lỗi thời.
- Ghi log lại mọi lần `Hook` kích hoạt chặn lệnh. Một `Hook` không bao giờ phải kích hoạt là ứng cử viên hàng đầu để xóa bỏ trong đợt rà soát định kỳ.
- Phần mô tả công cụ (`Tool use` descriptions) cũng chính là tài liệu hướng dẫn — hãy đọc kỹ bài [công cụ và MCP](../track-harness/tools-and-mcp.md) trước khi thêm bất kỳ công cụ mới nào.

## Tự mình kiểm chứng

1. Chạy cùng một tác vụ trong hai phiên làm việc mới tinh: một lần có tập tin `AGENTS.md` và một lần không có. Hãy so sánh hai bản ghi lịch sử thực thi (transcripts).
2. Đếm tổng số hộp thoại xin cấp quyền xuất hiện trong một ngày làm việc và số lần bạn đã bấm chấp thuận. Tự tính tỷ lệ bấm đồng ý của chính bạn.
3. Tắt thử một thành phần trong `Harness`, chạy lại tác vụ mà thành phần đó vốn được sinh ra để bảo vệ, và quan sát xem chất lượng thực tế có bị suy giảm hay không.

Tiếp theo: các cảm biến kiểm tra chất lượng xứng đáng có riêng một học phần độc lập — [hai loại kiểm tra](../course-5-evals/two-kinds-of-checks.md).

Tìm hiểu sâu hơn → [cẩm nang chuyên sâu về Harness cho Agent](../track-harness/what-a-harness-is.md): giải phẫu chi tiết bộ máy bên trong, bức tranh toàn cảnh các công cụ hiện có, và cách tự viết một `Harness` hoàn chỉnh chỉ trong khoảng 150 dòng code.
