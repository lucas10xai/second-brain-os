# Vì sao chọn Markdown và văn bản thuần túy

Định dạng lưu trữ thoạt nhìn tưởng như chỉ là một chi tiết nhỏ, nhưng thực chất nó quyết định liệu toàn bộ hệ thống có vận hành được hay không.

## Agent xử lý file tốt hơn nhiều so với gọi API

Một Agent khi đọc một thư mục sẽ phát huy được đúng sở trường mạnh nhất của nó: đọc văn bản và ghi văn bản. Không cần học lược đồ phức tạp của bên thứ ba, không cần gọi API sao cho đúng cú pháp, và không gặp phải tình trạng dở khóc dở cười khi một yêu cầu mạng chỉ thành công một nửa.

Sự tin cậy đó tích lũy qua hàng nghìn thao tác liên tiếp. Một quy trình ghi trực tiếp ra các file Markdown nếu có lỗi sẽ hiển thị rõ ràng ngay trên bảng so sánh thay đổi (diff); trong khi một quy trình ghi dữ liệu qua API thường gặp những lỗi ngầm mà mãi về sau bạn mới phát hiện ra.

## Tính khả chuyển không phải là chuyện lý thuyết suông

Mọi công cụ ghi chú từng được cộng đồng tin dùng trước đây đều rơi vào một trong ba kết cục: đóng cửa dịch vụ, thay đổi chính sách giá, hoặc cố tình làm cho tính năng xuất dữ liệu trở nên rắc rối để giữ chân người dùng.

Các file văn bản thuần túy xóa sổ hoàn toàn nỗi lo đó. Vault của bạn có thể mở bằng bất kỳ trình soạn thảo văn bản nào, đồng bộ qua bất kỳ công cụ lưu trữ nào, và làm việc mượt mà với bất kỳ Agent nào biết đọc file. Dù bạn có đổi mô hình AI, đổi trình soạn thảo hay đổi cả hệ điều hành thì Vault vẫn hoàn toàn nguyên vẹn — bởi ngay từ đầu nó đã chẳng bị nhốt bên trong bất kỳ ứng dụng nào.

Yếu tố này đặc biệt sống còn đối với một Second Brain, vì cơ sở tri thức tích lũy giá trị qua hàng chục năm. Một định dạng giam cầm dữ liệu của bạn sớm muộn gì cũng sẽ khiến bạn mất trắng toàn bộ công sức tích lũy đó.

## Wikilink trong vai trò định dạng đồ thị

Cú pháp `[[Tên trang]]` là một quy ước chỉ tốn đúng hai cặp ký tự nhưng lại tạo ra một đồ thị thực thụ, có thể đọc hiểu tự nhiên như văn bản thường, và sống sót qua mọi công cụ dù công cụ đó có hỗ trợ Wikilink hay không — bởi trong trường hợp xấu nhất, nó vẫn chỉ là những từ ngữ nằm ngay ngắn trong một câu văn.

Bạn có thể phân tích cú pháp của nó dễ dàng bằng một biểu thức chính quy (regex), và đó chính xác là cách mà `scripts/graph_export.py` hoạt động. Hãy thử làm điều tương tự với định dạng tham chiếu khối (block reference) độc quyền của các ứng dụng đóng xem sao.

## Tương thích hoàn hảo với Git

So sánh thay đổi trên văn bản (text diffs) — chỉ riêng đặc tính duy nhất này đã đủ giúp việc cho phép một Agent chạy tự động không cần giám sát trở nên an toàn: mọi chỉnh sửa do Agent tạo ra đều có thể kiểm tra lại, hoàn tác dễ dàng, và truy vết chính xác về từng lượt chạy cụ thể.

Các định dạng nhị phân và các ứng dụng lưu trữ bằng cơ sở dữ liệu đóng không thể mang lại cơ chế tương đương. Với chúng, bạn chỉ có hai lựa chọn cực đoan: hoặc nhắm mắt tin tưởng hoàn toàn vào tiến trình tự động hóa, hoặc không dám tự động hóa chút nào.

## Những giới hạn cần biết

Văn bản thuần túy thực sự bộc lộ điểm yếu ở một vài khía cạnh, và việc cố tình phớt lờ những giới hạn này chính là lý do khiến nhiều người rơi vào cảnh vỡ mộng.

**Truy vấn có cấu trúc ở quy mô lớn.** Plugin Dataview giải quyết được rất nhiều nhu cầu, nhưng khi vượt qua ngưỡng vài nghìn trang, các câu hỏi truy vấn quan hệ phức tạp sẽ cần đến một cơ sở dữ liệu thực thụ. Khi đó, hãy xuất dữ liệu đồ thị ra ngoài để truy vấn thay vì từ bỏ định dạng Markdown; xem chi tiết tại bài [Xuất dữ liệu đồ thị](../05-graphs/exporting-your-graph.md).

**Đa phương tiện (Rich media).** Hình ảnh phải nằm tách biệt bên cạnh văn bản dưới dạng các file rời chứ không gói gọn bên trong cùng một file. Sơ đồ và biểu đồ cũng đều là các tệp đính kèm.

**Chỉnh sửa đồng thời (Concurrent editing).** Hai Agent cùng ghi vào một file tại một thời điểm sẽ gây ra xung đột y hệt như cách các file văn bản xung đột với nhau — nghĩa là rất tệ.

Tuy nhiên, không có hạn chế nào trong số trên lấn át được lợi thế về tính khả chuyển đối với một Vault cá nhân. Điều quan trọng là bạn cần nắm rõ tất cả những giới hạn này trước khi thực sự chạm trán với chúng.

## Tiếp theo

[Zettelkasten, PARA và ghi chú xanh mãi](pkm-lineage.md)
