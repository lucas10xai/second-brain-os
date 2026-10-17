---
name: second-brain-chat-import
description: >-
  Sàng lọc lịch sử trò chuyện đã xuất ra (exported chat history) thành ba nhóm:
  đáng nạp vào wiki, chỉ lưu trữ, và xóa bỏ — bắt đầu bằng một bước rà soát quyền
  riêng tư trước tiên. Sử dụng kỹ năng này khi người dùng đã xuất lịch sử trò chuyện
  Claude hoặc ChatGPT của họ, yêu cầu nhập các cuộc hội thoại cũ, hoặc hỏi xem trong
  kho lưu trữ chat của họ có gì đáng giữ lại. KHÔNG dùng để nạp một cuộc trò chuyện
  đơn lẻ được dán trực tiếp, hoặc bất kỳ tài liệu nào mà người dùng chưa chủ động
  yêu cầu đưa vào vault.
---

# Nhập lịch sử trò chuyện (Import chat history)

Lịch sử trò chuyện là nguồn tư liệu bị đánh giá thấp nhất mà một người sở hữu, đồng thời cũng là nguồn nhạy cảm nhất. Nó ghi lại quá trình lập luận chứ không chỉ các dữ kiện khô khan, nhưng nó cũng lưu giữ cả những điều mà chủ sở hữu không hề muốn xuất hiện trong một file được đồng bộ, commit lên git và sao lưu khắp nơi.

## Quy tắc cốt lõi

Rà soát quyền riêng tư trước khi sàng lọc, sàng lọc trước khi nạp (ingest). Không bao giờ nạp nguyên khối toàn bộ một bản xuất lịch sử trò chuyện mà chưa qua chọn lọc.

## Quy trình thực hiện

1. **Chuyển đổi định dạng** bằng script `scripts/chat_export_to_md.py` để tách mỗi cuộc hội thoại thành một file riêng, đồng thời lọc bỏ các cuộc trao đổi quá ngắn.
2. **Rà soát quyền riêng tư (Privacy pass).** Liệt kê các cuộc hội thoại có chạm đến sức khỏe, tài chính, thông tin cá nhân của người khác, hoặc công việc bảo mật. Người dùng là người ra quyết định; bạn không được tự ý xóa bất kỳ thứ gì.
3. **Sàng lọc phần còn lại** thành ba nhóm: đáng nạp vào wiki (`worth ingesting` — nơi người dùng đã tháo gỡ được một vấn đề, đưa ra một quyết định, hoặc nhận được một lời giải thích thực sự thấu đáo), đáng lưu trữ trong `raw/` (`archive only`), và đề xuất xóa (`delete`).
4. **Báo cáo danh sách phân loại.** Chưa di chuyển hay chỉnh sửa bất kỳ file nào ở bước này.
5. **Khi được phê duyệt, tiến hành nạp (ingest)** nhóm đầu tiên với chỉ dẫn cốt lõi rằng đây là tư duy của chính người dùng: hãy xây dựng các trang xoay quanh vấn đề họ đang tìm lời giải và kết luận họ rút ra, chứ không phải xoay quanh các đoạn giải thích chung chung của trợ lý AI.

## Định dạng đầu ra

```
Converted: <n> cuộc hội thoại (đã bỏ qua <n> cuộc quá ngắn)

Privacy review needed: <n>
  <tiêu đề> - <lý do cần xem xét>

Worth ingesting: <n>
  <tiêu đề> - <vấn đề đã được tháo gỡ>

Archive only: <n>
Delete suggested: <n>
```

## Hiệu chuẩn (Calibration)

Hãy kỳ vọng khoảng chín trên mười cuộc hội thoại chỉ là những lần tra cứu vặt rồi bỏ. Một đợt sàng lọc mà khuyến nghị nạp hầu hết bản xuất dữ liệu tức là chưa hề lọc gì cả.

Ghi rõ ngày tháng trên mọi trang. Một quan điểm từ hai năm trước không phải là niềm tin hiện tại, và vault bắt buộc phải phân biệt được hai điều đó.
