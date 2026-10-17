---
name: gate-check
description: >-
  Tìm các điểm ra quyết định trong quy trình (pipeline) không cần đến mô hình
  đắt tiền và đề xuất cổng kiểm soát (gate) cho từng điểm: một quy tắc cứng (rule),
  một bộ phân loại cổ điển (classic classifier), hoặc một mô hình nhỏ, kèm định
  tuyến an toàn (fail-closed routing). Sử dụng khi người dùng muốn cắt giảm chi phí
  hoặc độ trễ mô hình, nói rằng mô hình lớn đang phải gánh mọi việc, hoặc muốn có
  một lớp phân loại / định tuyến / lọc đặt trước agent. Bao gồm phân tích cộng với
  khung mã nguồn cơ sở (baseline scaffold) tùy chọn. KHÔNG dùng để kiểm toán bố cục
  ngữ cảnh (context-audit) hoặc xây dựng bộ kiểm thử đánh giá (evals-bootstrap).
---

# Tìm các cổng kiểm soát (Gates)

Lý thuyết: [Những quyết định giá rẻ](https://secondbrainos-vn.pages.dev/#/read/course-3-gate/cheap-decisions)
và [Thực hành Gate](https://secondbrainos-vn.pages.dev/#/read/course-3-gate/gate-practice).
Một agent thực hiện hai loại công việc: viết lách — việc đòi hỏi mô hình lớn, và ra quyết định — đây có phải thư rác không, đưa vào hàng đợi nào, có cần con người can thiệp không — vốn là những câu hỏi đóng mà câu trả lời nằm sẵn trong một tập nhãn bạn đã biết trước.
Cổng kiểm soát (gate) là một lớp ra quyết định chi phí thấp giúp phân loại luồng đầu vào để mô hình đắt tiền chỉ phải xử lý những mục thực sự cần đến khả năng phán đoán sâu.

## Quy trình thực hiện

1. **Lập bản đồ các điểm quyết định.** Đọc các điểm đầu vào (entry points) và prompt của pipeline, sau đó liệt kê mọi quyết định được đưa ra trước hoặc trong một lệnh gọi mô hình: phân loại, định tuyến, lọc, sàng lọc có/không, gán độ ưu tiên, nhận diện ngôn ngữ, "yêu cầu này có thuộc phạm vi của chúng ta không". Bỏ qua phần sinh văn bản — chỉ tập trung vào các quyết định có giới hạn với tập nhãn xác định trước.
2. **Đếm chi phí hiện tại của từng quyết định.** Với mỗi quyết định hiện đang do mô hình lớn đảm nhiệm: số lệnh gọi mỗi ngày (nếu biết), số token mỗi lệnh gọi, và cái giá phải trả nếu trả lời sai. Một quyết định chỉ mang lượng thông tin 1 bit nhưng lại đốt một lệnh gọi mô hình tiên tiến nhất (frontier model) chính là phát hiện quan trọng nhất cần nêu bật.
3. **Đề xuất cổng kiểm soát rẻ nhất có thể đảm đương việc đó**, theo thứ tự chi phí tăng dần:
   - **Quy tắc cứng (rule)** — biểu thức chính quy (regex), danh sách cho phép (allowlist), kiểm tra header: miễn phí, tức thì, nhưng mù trước những tình huống chưa lường trước; luôn là lớp đầu tiên, không bao giờ là lớp cuối cùng.
   - **Bộ phân loại cổ điển (classic classifier)** — hồi quy logistic hoặc tương tự dựa trên các đặc trưng đơn giản, được huấn luyện trên vài trăm mẫu có gắn nhãn: tốn vài mili-giây, chi phí chỉ bằng một phần nhỏ của xu, và là mốc cơ sở (baseline) mà mọi giải pháp cầu kỳ hơn phải vượt qua.
   - **Mô hình nhỏ / Hệ thống 1 (System One model)** — khi đầu vào quá đa dạng đối với các đặc trưng tĩnh nhưng đầu ra vẫn chỉ là một nhãn kèm điểm số độ tự tin (confidence score).
4. **Định tuyến an toàn khi nghi ngờ (fail-closed).** Mọi cổng kiểm soát đều cần một ngưỡng tự tin (confidence threshold), và khi không chắc chắn, luồng xử lý phải đi theo con đường an toàn: không chắc chắn nghĩa là chuyển tiếp lên mô hình lớn (hoặc con người), tuyệt đối không được đoán mò. Hãy nêu rõ lộ trình xử lý khi không chắc chắn của từng cổng.
5. **Đề xuất khung mã nguồn cơ sở (baseline scaffold).** Nếu người dùng muốn tiến hành, hãy tạo bài tập thực hành 30 phút của học phần này cho dữ liệu của họ: một file `label.py` lấy mẫu ~200 ví dụ thực tế để gán nhãn thủ công, và một file `baseline.py` huấn luyện bộ phân loại cổ điển rồi in ra độ chính xác trên tập kiểm thử tách riêng (held-out split). Mọi lời quảng cáo từ nhà cung cấp hay phương án dùng mô hình nhỏ đều phải thắng được con số này trên chính dữ liệu của họ trước khi xứng đáng có mặt trong pipeline.

## Định dạng đầu ra

```
Gate check — <pipeline>
số quyết định tìm thấy: <n>, hiện đang dùng mô hình lớn: <n>

1. <quyết định> — <vị trí trong mã nguồn>
   hiện tại: <ai quyết định, chi phí ước tính>   tập nhãn: <các nhãn>
   cổng đề xuất: <rule | classifier | small model> — <tại sao chọn tầng này>
   khi không chắc chắn -> <lộ trình chuyển tiếp>
   tiết kiệm: <ước tính số lệnh gọi/token được chuyển hướng>
...
```

Xếp hạng theo mức độ tiết kiệm. Nếu một quyết định thực sự cần đến mô hình lớn — câu hỏi mở, không có tập nhãn cố định, chi phí sửa sai thấp — hãy nói rõ như vậy và giữ nguyên; một cổng kiểm soát đoán mò còn tệ hơn là không có cổng nào.
