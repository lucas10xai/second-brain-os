# Mở rộng quy mô vượt ngưỡng một nghìn trang

Phần lớn hướng dẫn này giả định một Vault có quy mô từ vài trăm đến vài nghìn trang — đây là ngưỡng mà các Vault cá nhân duy trì trong suốt nhiều năm. Vượt qua ngưỡng đó, một số khía cạnh sẽ bắt đầu chịu áp lực.

## Thứ gì thực sự bị quá tải

**Không phải công cụ tìm kiếm.** Chạy ripgrep trên mười nghìn file markdown vẫn cho kết quả tức thì.

**Không phải Obsidian,** mặc dù chế độ xem đồ thị tổng thể (global graph view) sẽ bắt đầu trở nên rối rắm khó dùng khi chạm ngưỡng khoảng một nghìn nút.

**Kinh tế học truy xuất (Retrieval economy).** Trang chỉ mục trở nên dài đến mức chỉ riêng việc đọc nó đã ngốn một lượng ngữ cảnh đáng kể — đây mới là giới hạn thực sự đầu tiên.

**Sự chú ý của chính bạn.** Một nghìn trang là vượt quá khả năng bao quát trong đầu của một người; đó chính xác là lúc Vault trở nên hữu ích hơn bao giờ hết, nhưng đồng thời cũng là lúc bạn ngừng nhận ra rằng một số phần trong đó đã bắt đầu mục ruỗng.

## Các tầng tóm tắt (Summary layers)

Cách khắc phục bài toán trang chỉ mục quá dài: thêm một tầng trung gian giữa chỉ mục tổng (master index) và các trang chi tiết.

Tạo một trang ngắn cho mỗi mảng chủ đề, liệt kê những gì có trong mảng đó và nội dung chính của từng trang. Agent sẽ đọc chỉ mục tổng, mở đúng chỉ mục chủ đề có liên quan, rồi mới mở các trang chi tiết. Ba lần đọc nhẹ nhàng thay vì một lần đọc đắt đỏ.

Hai cấp độ là đủ. Đến cấp thứ ba nghĩa là tạo ra bản tóm tắt của các bản tóm tắt — chúng sẽ dần trôi dạt khỏi nội dung gốc mà chúng mô tả, và tệ hơn là Agent sẽ đọc chúng thay vì đọc nội dung thật.

## Tách nhỏ Vault

Hãy tách theo lĩnh vực chuyên môn (domain) khi hai mảng thực sự không bổ trợ thông tin cho nhau: chẳng hạn như công việc và một sở thích cá nhân, hoặc hai ngành hoàn toàn không liên quan.

Đừng bao giờ tách theo thời gian hay theo dung lượng. Toàn bộ giá trị của hệ thống nằm ở chỗ tư liệu cũ kết nối được với tư liệu mới, và một Vault bị cắt nhỏ theo dòng thời gian sẽ chặt đứt chính những mối liên kết đáng giá nhất.

Cái giá của việc tách Vault là những kết nối xuyên lĩnh vực sẽ không còn xuất hiện nữa, trong khi đó lại thường là những phát hiện thú vị nhất. Vì vậy, chỉ nên tách khi thực sự muộn và hết cách.

## Lưu trữ lạnh (Archiving)

Chuyển các tư liệu ít dùng ("lạnh") sang một thư mục `archive/` nằm ngoài `wiki/`: chúng vẫn nằm trên ổ đĩa, vẫn tìm kiếm được bằng ripgrep, nhưng không còn chiếm chỗ trong trang chỉ mục hay trên Knowledge graph nữa.

Điểm quan trọng là thao tác này có thể đảo ngược được, bởi việc đánh giá một nội dung là "lạnh" chỉ mang tính phỏng đoán. Một chủ đề bạn đã đưa vào lưu trữ hoàn toàn có thể được đưa trở lại nếu sau này nó bỗng nhiên quan trọng trở lại.

## Cắt tỉa những thứ vốn dĩ chưa từng quan trọng

Những trang khái niệm chỉ có duy nhất một nguồn và không có lấy một liên kết trỏ đến nào sau cả một năm trời thực chất chưa bao giờ là các khái niệm — chúng chỉ là những đoạn văn rời rạc. Xóa bỏ chúng sẽ làm cho mọi thứ còn lại tốt hơn nhờ giảm bớt phần nhiễu mà các câu truy vấn phải đọc lướt qua.

Hãy thực hiện việc này mỗi năm một lần, đừng làm liên tục.

## Ngưỡng trần thực tế

Khi vượt qua ngưỡng mười nghìn trang ở đâu đó, một wiki được biên tập thủ công sẽ không còn là cấu trúc phù hợp cho một cá nhân nữa, bởi không ai có thể biên tập kịp với tốc độ đó, trong khi chính sự biên tập chọn lọc mới là thứ làm nên hiệu quả của hệ thống.

Nếu bạn đã chạm tới ngưỡng đó, hoặc là Vault của bạn đã không còn mang tính cá nhân nữa, hoặc là quy trình Ingest đã chạy tự động không qua phán đoán chọn lọc trong một thời gian quá dài. Trường hợp thứ hai phổ biến hơn rất nhiều, và cách khắc phục nằm ở phía đầu nguồn: hãy kiểm soát lại những gì bạn nạp vào cho nó.

## Tiếp theo

[Xử lý sự cố (Troubleshooting)](../10-troubleshooting/README.md).
