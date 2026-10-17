# Thực hành: Biết khi nào cần nâng cấp

Giờ đây bạn đã tự tay sở hữu khoảng 150 dòng mã thực hiện đầy đủ những gì mà mọi bộ `Harness` đều làm: chạy vòng lặp (`Loop`), thực thi công cụ (`Tool use`), gác cổng (`Gate`), kiểm soát ngân sách ngữ cảnh, và dừng đúng lúc. Quá trình tự xây dựng chính là bài học quý giá nhất. Còn trang này là buổi phỏng vấn tốt nghiệp — chỉ rõ những gì 150 dòng mã đó còn thiếu, những giải pháp dựng sẵn nào trên thị trường lấp đầy từng khoảng trống đó, cùng một quy tắc thẳng thắn để đưa ra quyết định.

Phép so sánh dưới đây lấy [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) làm chuẩn đối chiếu, bởi nó chính là bộ máy bên dưới của `Claude Code` được đóng gói thành thư viện và là lộ trình nâng cấp tự nhiên nhất từ bài thực hành này; các giải pháp thay thế khác đã được khảo sát trong trang [bức tranh toàn cảnh](harness-landscape.md).

## Khoảng trống thứ nhất: Chất lượng nén ngữ cảnh (Compaction)

Hàm kiểm soát ngân sách của bạn thẳng tay cắt bỏ các lượt hội thoại cũ và chỉ để lại một dòng tóm lược sơ sài. Cách làm đó đánh rơi mất các quyết định quan trọng, các đường dẫn tệp tin và những luồng công việc đang làm dở — tức là đánh mất chính những thứ đáng giữ lại nhất. Trong khi đó, Agent SDK kế thừa cơ chế quản lý ngữ cảnh tự động của `Claude Code`: nén ngữ cảnh bằng cách tóm tắt biên bản hội thoại một cách bài bản, bảo toàn ý định xuyên suốt trong khi trút bỏ các kết quả công cụ cồng kềnh, đồng thời cung cấp các `Hooks` để bạn kiểm soát thứ gì được giữ lại. Sự khác biệt giữa một dòng lược trích cắt cụt và một bản tóm tắt chất lượng chính là ranh giới giữa một `Agent` biết tiếp tục công việc đang dang dở và một `Agent` cứ lặp đi lặp lại những gì mình đã làm — bài [Context engineering](context-engineering.md) giải thích rất rõ nguyên nhân tại sao.

## Khoảng trống thứ hai: Thực thi công cụ song song

Các mô hình hiện nay thường xuyên trả về nhiều khối `tool_use` trong cùng một lượt phản hồi. Vòng lặp của bạn đang chạy chúng tuần tự từng cái một, tuy đúng về mặt kết quả nhưng lại chậm — ba câu lệnh mất ba mươi giây mỗi lệnh sẽ tiêu tốn tổng cộng chín mươi giây chờ đợi. Bộ SDK sẽ chạy các lệnh gọi công cụ độc lập một cách đồng thời (concurrently), và còn bổ sung thêm cơ chế `Subagents` cho phiên bản lớn hơn của cùng ý tưởng này: giao phó các nhánh công việc sang một cửa sổ ngữ cảnh mới tinh, và chỉ trả bản báo cáo cuối cùng về cho Agent cha.

## Khoảng trống thứ ba: Đóng hộp an toàn (Sandboxing)

Phần hai đã thẳng thắn thừa nhận rằng cổng gác của nó vẫn còn kẽ hở: phép khớp tiền tố chuỗi dễ dàng để lọt các ký tự đặc biệt của shell (shell metacharacters), và hàm `input()` chỉ có tác dụng khi bạn đang ngồi nhìn chằm chằm vào màn hình. Bộ SDK đóng gói sẵn toàn bộ hệ thống phân quyền được mô tả trong bài [Claude Code trong vai trò một Harness](claude-code-as-harness.md) — từ các quy tắc danh sách cho phép trong cấu hình, các chế độ phân quyền, thực thi câu lệnh trong môi trường hộp cát (sandbox), cho đến các `Hooks` tại bước `PreToolUse` giúp chặn lệnh một cách tất định thay vì dựa vào xác suất. Chính sách an toàn được thực thi cưỡng chế bằng mã nguồn, chứ không phải bằng niềm hy vọng rằng bạn đang ngồi trực bên bàn phím.

## Khoảng trống thứ tư: Khả năng khôi phục phiên (Resume)

Nếu bạn tắt ngang tiến trình Agent của mình khi nó đang làm dở tác vụ, mọi thứ sẽ tan biến sạch sẽ; bởi toàn bộ biên bản hội thoại chỉ nằm trong một danh sách (`list`) trên bộ nhớ tạm của Python. Cơ chế phiên (sessions) của bộ SDK giúp lưu trữ bền vững trạng thái qua từng lượt trao đổi và cho phép bạn khôi phục (resume) hoặc rẽ nhánh (fork) một cuộc hội thoại vào bất kỳ lúc nào sau đó. Kết hợp cùng các tệp bộ nhớ được nạp từ thư mục `.claude/`, Agent bắt đầu mỗi phiên làm việc mới với sự am hiểu sẵn có về dự án thay vì phải mò mẫm khám phá lại từ con số không.

## Quy tắc ra quyết định

Hãy tự viết bộ `Harness` của riêng mình khi có ít nhất một trong các điều kiện sau là đúng: bạn đang trong quá trình học hỏi (đó chính là lý do cuốn sổ tay này tồn tại); bản thân vòng lặp đó chính là sản phẩm cốt lõi của bạn và bạn cần làm chủ từng dòng mã; hoặc tác vụ của bạn đủ hẹp — chỉ có hai hay ba công cụ, phiên chạy ngắn, luôn có con người ngồi giám sát trực tiếp — đến mức 150 dòng mã kia thực sự đã bao quát trọn vẹn nhu cầu. Có rất nhiều công cụ nội bộ hữu ích đang sống khỏe và mang lại giá trị mỗi ngày ở đúng quy mô gọn nhẹ đó.

Ngược lại, hãy chuyển sang áp dụng một bộ `Harness` chuyên nghiệp ngay tại khoảnh khắc bất kỳ điều nào sau đây trở thành sự thật: Agent chạy tự động không có người ngồi canh; nó đọc các nội dung không đáng tin cậy từ bên ngoài (trang web, email, mã nguồn của người khác); phiên làm việc kéo dài đủ lâu khiến chất lượng nén ngữ cảnh quyết định sự thành bại; hoặc bạn bắt gặp chính mình đang cặm cụi tự viết một hệ thống phân quyền phức tạp. Mỗi bài toán kể trên đều tương đương với hàng tháng trời làm công việc kỹ thuật hạ tầng không mấy hào nhoáng mà Anthropic cùng các đội ngũ khác đã làm sẵn và kiểm thử qua vô số kiểu lỗi mà bạn thậm chí còn chưa từng gặp phải. Việc tự xây dựng lại cái bánh xe đó không phải là sự kỹ lưỡng, mà là sự lãng phí đắt đỏ.

Tóm lại một cách chân thành: 150 dòng mã kia chưa bao giờ là đích đến cuối cùng. Chúng chính là lý do giúp bạn từ nay đọc tài liệu của các bộ khung (framework) với tâm thế của người hiểu rõ các lựa chọn thiết kế thay vì nhìn chúng như phép thuật đen — bởi bạn đã từng nhìn thấy vòng lặp (`Loop`) ở trạng thái trần trụi nhất, nên bạn hoàn toàn phân biệt được chiếc áo khoác nào thực sự giữ ấm và chiếc áo nào chỉ để làm cảnh. Hãy chọn lấy một công cụ từ [bức tranh toàn cảnh](harness-landscape.md), đấu nối vào một tác vụ thực tế, và duy trì thói quen đọc kỹ từng biên bản hội thoại.
