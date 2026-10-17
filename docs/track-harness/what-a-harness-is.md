# Harness là gì

Một Harness (khung vận hành) là toàn bộ những gì bao quanh mô hình để biến việc dự đoán văn bản thành công việc hoàn thành thực tế: vòng lặp (Loop), các công cụ (Tool use), các câu lệnh nhắc (prompts), hệ thống phân quyền và đường ống kết nối hạ tầng. Mô hình đưa ra quyết định; còn Harness thực thi, quan sát và nạp kết quả quay trở lại. Cùng một mô hình, nhưng đặt trong hai Harness khác nhau sẽ tạo ra hai Agent khác biệt một trời một vực.

## Vòng lặp (The loop)

Nằm ở phần lõi là một vòng lặp `while`. Gửi cuộc hội thoại tới mô hình. Nếu phản hồi trả về có chứa các lệnh gọi công cụ (tool calls), hãy chạy chúng, nối kết quả vào lịch sử hội thoại, rồi lặp lại vòng nữa. Nếu phản hồi chỉ chứa văn bản thuần túy, hãy dừng lại và hiển thị cho người dùng. Toàn bộ bí quyết chỉ có vậy — bài viết [How to build an agent](https://ampcode.com/notes/how-to-build-an-agent) của Thorsten Ball thực hiện trọn vẹn cơ chế này trong chưa đầy 400 dòng mã Go. Mọi nội dung còn lại trong cuốn sổ tay này đều là sự tinh chỉnh và hoàn thiện thêm cho vòng lặp đó.

## Lược đồ công cụ (Tool schemas)

Công cụ là các lược đồ JSON mà mô hình đọc vào: một cái tên, một đoạn mô tả, cùng các tham số có định kiểu. Đoạn mô tả thực chất là một câu lệnh nhắc (prompt) ngụy trang — mô hình chọn công cụ bằng cách đọc đoạn mô tả đó, nên mô tả mơ hồ sẽ sinh ra hành vi mơ hồ. Độ mịn (granularity), cách đặt tên và nội dung thông báo lỗi quan trọng hơn nhiều so với giao thức truyền tải bên dưới. Chủ đề này được trình bày bài bản trong bài [công cụ (Tools) và MCP](tools-and-mcp.md).

## Câu lệnh nhắc hệ thống (System prompt)

Những chỉ dẫn thường trực: Agent này là ai, nó nên cư xử như thế nào, môi trường xung quanh nó trông ra sao. Các Harness trong môi trường thực tế (production) thường đi kèm những câu lệnh nhắc hệ thống dài hàng nghìn từ — quy định văn phong riêng, quy tắc an toàn, quy ước sử dụng công cụ. Đây chính là nơi biến "một con chatbot đơn thuần" thành "một Agent có khả năng phán đoán".

## Hệ thống phân quyền (Permissions)

Một Agent có khả năng chạy lệnh `rm -rf` bắt buộc phải có một cổng gác (Gate). Các Harness xếp chồng nhiều lớp bảo vệ gồm danh sách cho phép (allowlists), lời nhắc phê duyệt trên từng công cụ, môi trường hộp cát (sandboxes) và các chế độ chỉ-đọc (read-only) nằm chắn giữa ý định của mô hình và hệ thống máy móc thực tế. Hệ thống phân quyền chính là thứ cho phép bạn yên tâm để một Agent tự chạy mà không cần ngồi canh; nếu thiếu nó, chính bạn phải làm cái Harness đó.

## Quản lý cửa sổ ngữ cảnh

Cửa sổ ngữ cảnh là hữu hạn và chất lượng suy luận đã bắt đầu suy giảm từ trước khi nó đầy tràn. Harness là bên quyết định thứ gì được phép đi vào cửa sổ đó: những tệp tin nào, bao nhiêu dung lượng đầu ra từ công cụ, khi nào cần tóm tắt các lượt hội thoại cũ, và thông tin gì được lưu giữ bền vững qua nhiều phiên làm việc trong các tệp bộ nhớ. Đây chính là bộ môn [Context engineering](context-engineering.md) (kỹ thuật ngữ cảnh), và là nơi những Harness tốt chứng minh giá trị xứng đáng với chi phí của mình.

## Tại sao Harness lại quan trọng ngang ngửa với mô hình

Các bài kiểm chuẩn (benchmarks) xuyên suốt năm 2026 liên tục cho thấy cùng một sự thật: chính Harness làm dịch chuyển các con số điểm số. Thử nghiệm nội bộ của Databricks phát hiện ra rằng Harness tối giản của `pi` đã đánh bại những bộ khung nặng nề hơn về tỷ lệ hoàn thành tác vụ trong khi chỉ tiêu tốn một phần ba lượng ngữ cảnh trên mỗi lượt — vẫn cùng những mô hình đó, chỉ khác bộ máy vận hành bên ngoài. Một Harness gửi đi ngữ cảnh phình to vừa đốt tiền vừa làm suy giảm khả năng suy luận; ngược lại, một Harness biết phục hồi tốt sau các lệnh gọi công cụ thất bại sẽ hoàn tất được những tác vụ mà các hệ thống khác phải bỏ cuộc. Các phòng thí nghiệm mô hình hiện nay đều tinh chỉnh Harness khớp chặt với mô hình của họ (OpenAI gọi thiết kế của mình là "in-distribution" — nằm trong phân phối huấn luyện), điều đó cho thấy họ coi Harness là một phần máu thịt của sản phẩm chứ không chỉ là lớp vỏ đóng gói bên ngoài.

## Phần còn lại của cấu trúc giải phẫu

Những Harness trưởng thành sẽ bổ sung thêm `Hooks` (các kịch bản tất định gắn vào sự kiện vòng đời), `Subagents` (các cửa sổ ngữ cảnh mới tinh dành riêng cho công việc được ủy quyền), và `skills` (các chỉ dẫn chỉ được nạp khi có nhu cầu). [Claude Code](claude-code-as-harness.md) là bản cài đặt tham chiếu tiêu biểu cho tất cả những thành phần này; còn trang [bức tranh toàn cảnh](harness-landscape.md) sẽ khảo sát các giải pháp thay thế khác trên thị trường.

Chỉ cần nắm vững cấu trúc giải phẫu này một lần, mọi bộ khung (framework) đều trở nên dễ đọc hiểu: tất cả chúng đều là cùng một vòng lặp (Loop) nhưng khoác lên mình những chiếc áo khác nhau mà thôi.
