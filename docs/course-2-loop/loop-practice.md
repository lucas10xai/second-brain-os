# Thực hành Loop: lọc trước, lặp ngắn, dự phòng

Mô hình chuẩn trên môi trường `Production` không phải là "cho `Agent` chạy trên mọi thứ". Mà là: lọc trước (filter first), lặp ngắn gọn (loop briefly), và chuyển sang luồng dự phòng (fall back). Bài chia sẻ kỹ thuật của Atlan về `Agent` trực vận hành (on-call agent) của họ đã minh chứng rõ nét cấu trúc này ở quy mô lớn: một bộ lọc tất định không dùng LLM đã chặn trước khoảng 86% trên tổng số khoảng 11.000 cảnh báo trong vòng 30 ngày trước khi tốn bất kỳ một token nào, nhờ đó chỉ có khoảng 14% cảnh báo thực sự đi tới được `Agent`; sau đó `Agent` chỉ suy luận trong khoảng ba chu kỳ, và khi độ tự tin vẫn nằm dưới ngưỡng khoảng 50%, nó sẽ chuyển giao (escalate) sang một `Workflow` dự phòng tất định viết bằng Python thuần. Những cuộc điều tra sự cố trước đây từng mất hơn mười phút và tốn vài đô la nay giảm xuống chỉ còn khoảng hai phút và 0,28 đô la mỗi vụ. Code thông thường chi phí thấp xử lý các trường hợp phổ biến; mô hình xử lý phần phức tạp còn sót lại; và một luồng cố định sẽ đón lõng bất cứ thứ gì mô hình không thể tự khép lại.


> Nửa phần kiểm tra mục tiêu (goal-test) của mô hình này đã được đóng gói thành một `Skill`: hãy cài đặt [plugin của khóa học](../../plugins/README.md) và chạy lệnh `/agents-course:goal-test`; vai trò `Checker` được cung cấp sẵn dưới dạng `Agent` `loop-critic`.

Một lưu ý định hình trước khi vào code: bản triển khai dưới đây mang hình thái phân loại sự cố (triage shape) — lọc trước, lặp ngắn, dự phòng. Hình thái `Production` phổ biến còn lại, nơi một `Loop` bọc bên ngoài một `Agent` lập trình và được dẫn dắt bởi bài kiểm tra mục tiêu, được trình bày chi tiết tại [bài thực hành trong cẩm nang chuyên sâu về Loop](../track-loop/build-goal-test.md); vẫn cùng bốn thành phần cốt lõi, chỉ khác phần thân thực thi.

## Xây dựng hệ thống

Toàn bộ kiến trúc lai (hybrid) này gói gọn trong một tập tin duy nhất. Code dưới đây có thể chạy trực tiếp ngay lập tức; khi triển khai thực tế, bạn chỉ cần thay hàm `model_next_step` bằng lệnh gọi API thật mà không cần sửa đổi luồng điều khiển (control flow).

```python
"""Phân loại cảnh báo lai (Hybrid alert triage): bộ lọc tất định, Loop có giới hạn, và luồng dự phòng cố định."""

MAX_TURNS = 3          # Atlan chạy khoảng ba chu kỳ suy luận trước khi chuyển giao (escalate)
BUDGET_USD = 0.10      # trần chi tiêu tối đa cho mỗi cảnh báo
COST_PER_TURN = 0.02   # thay bằng số liệu chi phí thực tế từ phản hồi API của bạn

ALERTS = [
    {"id": 1, "source": "cron", "message": "nightly backup finished OK"},
    {"id": 2, "source": "api", "message": "TimeoutError in /sync after 30s"},
    {"id": 3, "source": "api", "message": "intermittent 502 from payments"},
]

def prefilter(alert):
    """Tất định, không tốn chi phí. Trả về kết luận ngay, hoặc trả về None để chuyển vào Loop."""
    message = alert["message"].lower()
    if alert["source"] == "cron" or "finished ok" in message:
        return {"cause": "known-benign pattern", "next_step": "close", "via": "filter"}
    return None

def checker(diagnosis):
    """Checker bên ngoài: bản chẩn đoán bắt buộc phải nêu rõ nguyên nhân và bước xử lý tiếp theo cụ thể."""
    return bool(diagnosis.get("cause")) and bool(diagnosis.get("next_step"))

def model_next_step(alert, history):
    """Hàm giả lập (stub) đại diện cho lệnh gọi mô hình. Hãy thay thế bằng lệnh gọi API thực tế tại đây."""
    if "timeout" in alert["message"].lower():
        return {"cause": "client timeout on /sync", "next_step": "raise limit to 60s"}
    return {"cause": "", "next_step": ""}   # hàm giả lập không thể tự xử lý xong trường hợp này

def fallback_workflow(alert):
    """Luồng cố định, không dùng mô hình: luôn tạo ra phương án xử lý an toàn, đáng tin cậy."""
    return {"cause": "unresolved by agent", "next_step": "page on-call with raw alert",
            "via": "fallback"}

def triage(alert):
    verdict = prefilter(alert)
    if verdict is not None:
        return verdict                                   # phần lớn cảnh báo dừng lại ngay tại đây
    history, spent = [], 0.0
    for turn in range(MAX_TURNS):
        diagnosis = model_next_step(alert, history)
        history.append(diagnosis)
        spent += COST_PER_TURN
        if checker(diagnosis):
            diagnosis["via"] = "loop, turn %d" % (turn + 1)
            return diagnosis                             # lối thoát 1: vượt qua Checker
        if len(history) >= 2 and history[-1] == history[-2]:
            break                                        # lối thoát 2: lặp tại chỗ (spinning)
        if spent > BUDGET_USD:
            break                                        # lối thoát 3: vượt ngân sách
    return fallback_workflow(alert)                      # mọi lối thoát khác đều đổ về đây

if __name__ == "__main__":
    for alert in ALERTS:
        print(alert["id"], triage(alert))
```

Cảnh báo số 1 không bao giờ chạm tới mô hình, cảnh báo số 2 được giải quyết xong ngay ở lượt đầu tiên của `Loop`, còn cảnh báo số 3 bị lặp tại chỗ hai lần rồi rơi xuống luồng dự phòng (`fallback_workflow`). Mọi nhánh xử lý đều trả về cùng một cấu trúc dữ liệu đồng nhất, nhờ đó thành phần gọi hàm bên ngoài không cần bận tâm tầng nào đã đưa ra câu trả lời.

## Mẹo thực chiến

- Hãy mở rộng bộ lọc chứ đừng mở rộng `Loop`. Bất kỳ chẩn đoán nào mà `Loop` tạo ra lặp lại tới lần thứ hai đều là ứng cử viên sáng giá để viết thành quy tắc cứng trong hàm `prefilter`.
- Ghi log trường `via` trên mọi kết quả trả về. Tỷ lệ phân bổ giữa `filter`, `loop` và `fallback` chính là chỉ số đo lường sức khỏe hệ thống của bạn; nếu tỷ lệ rơi vào `fallback` tăng lên, nghĩa là `Loop` đang thất bại một cách âm thầm.
- Giữ cho luồng dự phòng (`fallback`) thật đơn giản và nhàm chán. Nhiệm vụ của nó là đưa ra một phương án xử lý an toàn không cần mô hình, chứ không phải là nỗ lực tỏ ra thông minh lần thứ hai.
- Hãy thiết kế `Checker` khắt khe hơn mức bạn cảm thấy lịch sự — bởi đó là chốt chặn duy nhất mà mô hình không thể dùng lời lẽ khéo léo để lách qua. Cách gia cố `Checker` đủ cứng rắn cho một `Agent` lập trình thực thụ được trình bày tại [trang xây dựng bài kiểm tra mục tiêu (goal test)](../track-loop/build-goal-test.md); và toàn bộ danh mục các cơ chế phanh hãm nằm ở bài [các điều kiện dừng (stop conditions)](../track-loop/stop-conditions.md).

## Tự mình kiểm chứng

1. Chạy thử tập tin trên, sau đó đặt `MAX_TURNS = 0` và chạy lại lần nữa. Mọi cảnh báo không được lọc bởi `prefilter` đều phải rơi vào nhánh dự phòng (`fallback`) — nếu chương trình bị văng lỗi (crash), nghĩa là bạn đã bỏ sót một lối thoát nào đó.
2. Sửa hàm `model_next_step` sao cho nó luôn trả về cùng một kết quả sai mãi mãi. Hãy xác nhận rằng điều kiện kiểm tra lặp tại chỗ (`spinning`) sẽ ngắt vòng lặp ngay ở lượt thứ hai chứ không đợi đến lượt thứ ba.
3. Thêm một cảnh báo thứ tư mà bộ lọc của bạn có thể bắt được, rồi ghi log xem toàn bộ lô dữ liệu hiện tại thực hiện bao nhiêu lệnh gọi mô hình. Khi con số lệnh gọi mô hình giảm xuống trong khi độ phủ xử lý vẫn giữ nguyên, bạn đã nắm được toàn bộ bài toán kinh tế của mô hình này — và việc quyết định xem những phán đoán nào thực sự xứng đáng để gọi mô hình sẽ là chủ đề của học phần tiếp theo: [những quyết định chi phí thấp](../course-3-gate/cheap-decisions.md).

Tìm hiểu sâu hơn → [cẩm nang chuyên sâu về kỹ thuật thiết kế Loop](../track-loop/what-loop-engineering-is.md): các điều kiện dừng (`Stop condition`), bộ phê bình (`Critic`), vệ sinh ngữ cảnh, và cách thiết kế một `Loop` chạy xuyên đêm mà bạn có thể hoàn toàn yên tâm vào sáng hôm sau.
