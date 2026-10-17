# Mô hình Wiki vận hành bằng LLM

Đây là mô hình kiến trúc cụ thể mà bộ cẩm nang này triển khai, được Andrej Karpathy công bố dưới dạng một bản gist vào ngày 2026-04-04.

Sự đảo ngược cốt lõi có thể gói gọn trong một câu: thay vì bạn tự tay duy trì các ghi chú và thỉnh thoảng hỏi AI về chúng, AI sẽ là người duy trì hệ thống wiki và bạn là người đọc nó.

## Những nguyên tắc mô hình này quy định

**Tầng wiki là trung tâm.** Nguồn tư liệu thô (`raw/`) chỉ là kho lưu trữ để bạn giữ lại và hiếm khi mở ra. Tầng `wiki/` mới là nơi cả bạn và Agent cùng làm việc trực tiếp, được viết bằng ngôn ngữ mạch lạc, mỗi trang một ý tưởng và liên kết dày đặc với nhau.

**Biên dịch (Compilation), không phải tóm tắt (Summarization).** Mỗi nguồn tài liệu mới đều được tích hợp sâu vào các trang hiện có thay vì chỉ đặt nằm cạnh như một bản tóm tắt rời rạc khác. Một trang viết về một khái niệm sẽ ngày càng sâu sắc và hoàn thiện hơn khi có thêm nhiều nguồn tài liệu mới; chứ không biến thành một danh sách liệt kê xem từng nguồn đã nói những gì.

**Ba thao tác cơ bản.** `Ingest` đưa tư liệu mới vào hệ thống. `Lint` giữ cho cấu trúc luôn chuẩn xác và lành mạnh. `Query` trả lời câu hỏi dựa trên tầng wiki. Mọi tác vụ khác đều chỉ là biến thể xoay quanh ba thao tác này.

## Vì sao mô hình này đứng vững

Bởi vì nó loại bỏ đúng tác vụ duy nhất đã giết chết mọi hệ thống quản lý tri thức trước đây. Việc ngồi liên kết thủ công năm mươi ghi chú với nhau mỗi khi bạn đọc xong một bài báo khoa học thực sự là một công việc nhàm chán mà con người sớm muộn gì cũng ngừng làm — và bất kỳ hệ thống wiki nào cũng sẽ chết yểu khi người bảo trì nó thấm mệt.

Lý do thứ hai là mô hình này không đòi hỏi bất kỳ hạ tầng phức tạp nào. Chỉ cần các file Markdown, hệ thống Wikilink, và một Agent biết đọc ghi file. Không cần cơ sở dữ liệu, không cần duy trì chỉ mục tìm kiếm phức tạp, không phụ thuộc vào dịch vụ bên ngoài nào.

## Ranh giới nơi bản gist dừng lại

Bản gist gốc chỉ mô tả ý định thiết kế chứ không đi vào chi tiết triển khai cụ thể: tích hợp các nguồn tài liệu mới, chạy Lint định kỳ, và coi tầng wiki là trung tâm.

Cơ chế vận hành chi tiết được để mở hoàn toàn, đó là lý do vì sao mỗi bản triển khai thực tế lại có cách làm khác nhau: làm sao để xử lý các thông tin mâu thuẫn khi tích hợp, một trang bắt buộc phải chứa những thành phần gì, khi nào thì chạy Lint, và đối tượng độc giả của wiki là ai. Câu trả lời của cẩm nang này cho những bài toán đó nằm ở chương [Cấu trúc hóa](../04-structuring/README.md) — và đó là những lựa chọn thiết kế có chủ đích của chúng tôi chứ không phải quy định cứng từ bản thân mô hình gốc.

## Những gì cộng đồng xây dựng thêm bên trên

Các phần mở rộng phổ biến nhất là tầng nhật ký cá nhân (journal layer), tầng quản lý dự án (project layer) và hệ thống tự động hóa theo lịch trình. Cẩm nang này đi sâu vào hai phần sau thông qua bài viết [Cấu trúc hai tầng](two-layers.md) và chương [Tác tử (Agents)](../06-agents/README.md).

Mô hình này lan tỏa rất nhanh bởi các thành phần nguyên thủy của nó vô cùng giản dị: bất kỳ ai có một Agent và một thư mục trên máy đều có thể chạy được ngay, và mọi bản triển khai đều là các file Markdown dễ đọc. Hãy xem danh mục [tài nguyên](../../resources/skills.md) để tham khảo những bản triển khai đáng đọc nhất.

## Tiếp theo

[Cấu trúc hai tầng](two-layers.md)
