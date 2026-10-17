# Thực hành xây dựng Gate

Nguyên tắc kỷ luật gói gọn trong một câu: trước khi đánh giá bất kỳ công cụ của nhà cung cấp (vendor) nào, hãy tự gán nhãn vài trăm mẫu dữ liệu thực tế và huấn luyện một bộ phân loại cơ bản. Việc này chỉ mất khoảng ba mươi phút, và đó chính là cột mốc cơ sở (baseline) mà mọi lời quảng cáo phải đánh bại được trên chính dữ liệu của bạn trước khi xứng đáng có một chỗ đứng trong hệ thống.


> Quy trình kiểm toán và xây dựng cột mốc cơ sở này đã được đóng gói thành một `Skill`: hãy cài đặt [plugin của khóa học](../../plugins/README.md) và chạy lệnh `/agents-course:gate-check` trên đường ống dữ liệu của bạn.

## Gán nhãn hai trăm mẫu dữ liệu thực tế

Hãy trích xuất 200 mục dữ liệu gần nhất từ chính luồng dữ liệu mà `Agent` của bạn đang xử lý hàng ngày — tuyệt đối không dùng dữ liệu nhân tạo tự chế, cũng không dùng bộ dữ liệu công khai của người khác. Sử dụng ba nhãn sau:

- `file` — tài liệu tham khảo thuần túy: bản tin định kỳ (newsletters), biên lai, bản tổng hợp tin tức. Đi thẳng vào kho lưu trữ, không cần bất kỳ mô hình nào can thiệp.
- `act` — tạo ra một tác vụ cụ thể rõ ràng: hóa đơn cần thanh toán, biểu mẫu cần ký duyệt, lịch họp cần xác nhận.
- `judge` — đòi hỏi khả năng phán đoán thực sự: một yêu cầu mơ hồ, một lời đề nghị hợp tác, bất cứ thứ gì có rủi ro hoặc hệ quả lớn.

Có ba quy tắc cần tuân thủ trong lúc gán nhãn. Hãy gán nhãn theo đúng bản chất thực tế của mục dữ liệu đó, chứ đừng gán theo những danh mục lý tưởng mà bạn ước ao. Khi phân vân giữa hai nhãn, hãy chọn `judge` — sự ngập ngừng của chính bạn dự báo chính xác sự ngập ngừng của `Gate`. Không tự ý đẻ thêm danh mục nhãn mới giữa chừng; hãy ghi chú các ứng viên nhãn mới ra chỗ khác và hoàn thành trọn vẹn lượt gán nhãn hiện tại. Với tốc độ năm giây cho mỗi mục, toàn bộ việc này chỉ mất khoảng mười lăm phút. Lưu kết quả vào tập tin `labels.csv`:

```csv
text,label
"Weekly digest: ten AI papers you missed",file
"Invoice 2214 attached, due Friday, please confirm receipt",act
"Fwd: any thoughts on this partnership proposal?",judge
```

## Huấn luyện mô hình cơ sở (Baseline)

Cài đặt thư viện một lần duy nhất bằng lệnh `pip install scikit-learn pandas joblib`, sau đó chạy đoạn mã sau:

```python
# train_gate.py
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.read_csv("labels.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.25,
    stratify=df["label"], random_state=42,
)

gate = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
])
gate.fit(X_train, y_train)

print(classification_report(y_test, gate.predict(X_test), digits=3))
joblib.dump(gate, "gate.joblib")
```

## Đo lường rồi mới quyết định

Hãy đọc kỹ chỉ số độ chuẩn xác (precision) và độ phủ (recall) của từng lớp nhãn riêng biệt, chứ đừng chỉ nhìn vào con số độ chính xác tổng thể (headline accuracy). Những con số này chính là cột mốc cơ sở của bạn. Chỉ tới lúc này, câu hỏi lựa chọn nhà cung cấp mới được đặt ra một cách chuẩn xác: liệu có công cụ hào nhoáng nào đánh bại được cột mốc này, trên chính tập dữ liệu này, với cách biệt đủ lớn để biện minh cho một lệnh gọi qua mạng, một hóa đơn chi phí và sự phụ thuộc vào bên thứ ba hay không? Dựa trên các bằng chứng độc lập tính đến hiện tại — xem lại bài [Ứng dụng Gate trong thực tế](gates-in-practice.md) — câu trả lời cho một tác vụ cố định đã có nhãn thường là không.

## Tích hợp bộ phân loại chiến thắng vào hệ thống

```python
# gate.py
import joblib

gate = joblib.load("gate.joblib")
THRESHOLD = 0.85
HANDLED = {"file", "act"}

def route(text: str) -> tuple[str, float]:
    probs = gate.predict_proba([text])[0]
    best = probs.argmax()
    label = gate.classes_[best]
    confidence = float(probs[best])
    if label not in HANDLED or confidence < THRESHOLD:
        return "escalate", confidence
    return label, confidence
```

Mọi trường hợp trả về `"escalate"` đều được chuyển thẳng lên cho mô hình chính xử lý — tuân thủ đúng nguyên tắc đóng an toàn (fail closed). Bộ khung điều hướng hoàn chỉnh, bao gồm cả phần ghi log và luồng chuyển tiếp xuống LLM, nằm trong bài [bộ định tuyến kiểm soát bằng độ tự tin](../track-jev/build-router.md); đường ống `gate.py` này có thể lắp thẳng vào nhánh xử lý nhanh của bộ khung đó mà không cần chỉnh sửa gì thêm.

## Mẹo thực chiến

- Ghi log mọi quyết định kèm theo điểm số độ tự tin của nó, bất kể được xử lý ngay hay bị chuyển giao lên trên. Bản ghi log đó chính là bộ dữ liệu đánh giá (`Evals`) trong tương lai của bạn.
- Huấn luyện lại hàng tuần. Những trường hợp bị chuyển giao (`escalate`) mà mô hình chính đã giải quyết xong chính là nguồn nhãn miễn phí — hãy nối chúng thêm vào tập tin `labels.csv`.
- Giữ lại nhãn `judge` mãi mãi. Một `Gate` không có cửa thoát hiểm là một `Gate` bị ép phải đoán mò.
- Hãy bắt đầu với ngưỡng tự tin ở mức 0,85 và chỉ dịch chuyển ngưỡng này sau khi đã phân dải độ chính xác theo độ tự tin trên tập dữ liệu kiểm thử độc lập (held-out data).

## Tự mình kiểm chứng

1. Chia các dự đoán trên tập kiểm thử độc lập của bạn thành ba dải độ tự tin (0–0,5, 0,5–0,85, 0,85–1,0) và tính độ chính xác cho từng dải. Nếu dải cao nhất chưa đạt mức gần như tuyệt đối, hãy nâng ngưỡng `THRESHOLD` lên.
2. Chạy lại báo cáo ở các mức ngưỡng 0,7, 0,85 và 0,95, đồng thời ghi lại tỷ lệ chuyển giao (escalation rate) so với tỷ lệ lỗi trên luồng nhanh (fast-path error rate) ở từng mức. Hãy chủ động lựa chọn điểm cân bằng phù hợp với bài toán của bạn.
3. Chạy thử nghiệm ngầm (shadow-run) trong một tuần: để `Gate` đưa ra quyết định nhưng mô hình chính vẫn xử lý toàn bộ mọi yêu cầu như cũ. Hãy đếm số lần hai bên bất đồng quan điểm trước khi thực sự trao quyền cho luồng xử lý nhanh.

Khi `Gate` đã đảm nhận việc phân loại luồng dữ liệu đầu vào, mô hình đắt tiền cuối cùng cũng có không gian để làm công việc thực sự của nó — và môi trường làm việc bao quanh nó chính là chủ đề của học phần tiếp theo: [văn phòng làm việc (the office)](../course-4-harness/the-office.md).

Tìm hiểu sâu hơn → [cẩm nang chuyên sâu về kỹ thuật Jev](../track-jev/system-one-models.md): các mô hình `System One`, thế mạnh thực sự của chúng, và cách xây dựng bộ định tuyến kiểm soát bằng độ tự tin.
