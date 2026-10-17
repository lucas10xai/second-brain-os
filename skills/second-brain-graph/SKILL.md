---
name: second-brain-graph
description: >-
  Phân tích đồ thị liên kết của vault và báo cáo về hình thái cấu trúc của nó:
  tỷ lệ trang mồ côi (orphan rate), bậc liên kết trung bình (average degree),
  các thành phần liên thông (components), điểm nút trung tâm (hubs), cầu nối
  (bridges) và cụm chủ đề (clusters), kèm theo ý nghĩa thực tế của từng con số
  đối với việc truy xuất thông tin. Sử dụng kỹ năng này khi người dùng hỏi về
  sức khỏe hoặc cấu trúc đồ thị, muốn xem các chỉ số, hỏi trang nào được kết nối
  nhiều nhất hay bị cô lập nhất, hoặc hỏi liệu vault có đang bị phân mảnh không.
  KHÔNG dùng để sửa chữa những lỗi phát hiện được — việc đó thuộc về second-brain-lint —
  hoặc để trả lời câu hỏi về mặt nội dung.
---

# Phân tích đồ thị liên kết (Analyse the graph)

Đồ thị liên kết chính là không gian tìm kiếm mà từ đó mọi câu trả lời được rút ra. Hình thái của đồ thị quyết định liệu quá trình truy xuất có chạm tới được tư liệu liên quan chỉ sau vài bước nhảy (hops) hay đi vào ngõ cụt.

## Quy tắc cốt lõi

Báo cáo hình thái đồ thị và ý nghĩa của nó, không bao giờ tự ý sửa chữa bất kỳ thứ gì. Kỹ năng này hoàn toàn chỉ đọc (read-only).

## Quy trình thực hiện

1. **Chạy các script công cụ** thay vì đọc thủ công từng file: chạy `scripts/vault_stats.py` để lấy số lượng và bậc liên kết, `scripts/link_check.py` để tìm trang mồ côi và liên kết gãy, và `scripts/graph_export.py` khi cần phân tích sâu hơn.
2. **Tính toán bốn chỉ số cốt lõi:** tỷ lệ trang mồ côi (`orphan rate`), bậc liên kết trung bình (`average degree`), số thành phần liên thông (`component count`), và tỷ lệ trang cũ bị bỏ quên (`stale-page rate`).
3. **Xác định các điểm nút trung tâm (`hubs`)** (những trang phình quá to nuốt chửng cả đồ thị) và **các cầu nối (`bridges`)** (những trang kết nối các cụm chủ đề vốn tách biệt nhau).
4. **Đặt tên cho các cụm chủ đề (`clusters`).** Đây là những chủ đề mà vault thực sự xoay quanh — thường khác xa so với những gì người dùng tự nghĩ về vault của họ.
5. **Giải thích ý nghĩa của từng con số** đối với khả năng trả lời câu hỏi, chứ không chỉ liệt kê giá trị số học.

## Định dạng đầu ra

```
Pages <n> | links <n> | avg degree <n>
Orphan rate <n>%      (khỏe mạnh khi dưới 5%)
Components <n>        (thành phần chính chiếm <n>%)
Stale concepts <n>%   (chưa cập nhật trên 90 ngày)

Hubs: <các trang có bậc liên kết quá lớn, và có nên tách nhỏ chúng ra không>
Bridges: <các trang nối giữa các cụm, và điều gì sẽ đứt gãy nếu chúng sai>
Clusters: <những chủ đề thực sự trong vault>

Ý nghĩa thực tế: <hai hoặc ba câu nhận định>
```

## Hiệu chuẩn (Calibration)

Không bao giờ báo cáo tổng số trang hay tổng số từ như một tín hiệu về sức khỏe của vault. Cả hai con số đó đều tăng lên bất kể vault đang tốt lên hay tệ đi.

Một lần đo đơn lẻ nói lên rất ít điều. Nếu người dùng đã lưu các con số từ những lần trước, hãy so sánh với chúng; nếu chưa, hãy gợi ý họ ghi nhận lại các con số lần này.
