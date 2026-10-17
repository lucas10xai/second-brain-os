# Cơ bản về đồ thị cho cơ sở tri thức

`Vault` của bạn vốn dĩ đã là một đồ thị dù bạn có chủ đích thiết kế hay không. Các trang là các đỉnh (nodes), các `Wikilink` là các cạnh (edges). Mọi quyết định về cấu trúc ở chương trước thực chất đều là quyết định về hình thái mà đồ thị đó sẽ mang.

Chỉ cần bốn thuật ngữ là đủ để tư duy về nó. Chương này bàn về chính đồ thị bên trong `Vault` của bạn — các `Wikilink`, hình thái và độ lành mạnh của đồ thị. Còn đồ thị đóng vai trò như bộ nhớ tổng quát của một `Agent` (`GraphRAG`, trích xuất thực thể, kho lưu trữ đồ thị) nằm ở [cẩm nang chuyên sâu về Knowledge graph](../track-graph/why-graphs.md).

**Bậc (Degree)** là số lượng liên kết mà một trang có. Bậc vào (in-degree) là số liên kết trỏ tới nó, bậc ra (out-degree) là số liên kết từ nó trỏ ra ngoài. Một trang có bậc vào bằng không sẽ không thể tiếp cận được bằng cách lần theo các liên kết — đó chính là lý do khiến các trang mồ côi (orphans) trở thành một vấn đề thực sự chứ không chỉ là chuyện thẩm mỹ.

**Độ dài đường đi (Path length)** là số bước nhảy (hops) ngăn cách giữa hai trang. Đây là chỉ số quan trọng nhất đối với việc trả lời câu hỏi: `Agent` khi lần theo các liên kết từ một trang xuất phát chỉ có thể vươn tới những gì cách đó vài bước nhảy trước khi cạn ngân sách `Context window`. Hai ý tưởng có liên quan nhưng cách nhau tới tám bước nhảy sẽ không bao giờ được kết nối với nhau trong một câu trả lời.

**Hệ số phân cụm (Clustering)** đo lường mức độ các trang láng giềng của một trang liên kết chéo với nhau. Độ phân cụm cao đồng nghĩa với một vùng chủ đề thực thụ. Độ phân cụm thấp nhưng bậc (degree) lại cao thường là dấu hiệu của một trang thu thập những thứ rời rạc không liên quan đến nhau.

**Thành phần liên thông (Components)** là các ốc đảo bị cô lập với nhau. Một `Vault` bị chia làm năm thành phần liên thông thực chất là năm `Vault` riêng biệt, và không có thông tin nào ở vùng này có thể bổ trợ cho một câu trả lời ở vùng kia.

## Những hình thái đồ thị sai lệch

**Hình ngôi sao (The star).** Mọi thứ chỉ liên kết tới hai hoặc ba trang trung tâm (hub pages) và không liên kết với bất kỳ thứ gì khác. Độ dài đường đi giữa hai trang lá bất kỳ rất ngắn, nhưng chỉ vì đi qua trang trung tâm, nên đồ thị không cho bạn biết thêm điều gì ngoài việc "tất cả những thứ này đều nằm trong `Vault` của tôi". Nguyên nhân thường là do thói quen liên kết tới các khái niệm quá rộng thay vì các khái niệm cụ thể.

**Hình chuỗi xích (The chain).** Các trang nguồn liên kết tới khái niệm mà chúng giới thiệu, nhưng không có liên kết ngang nào giữa các khái niệm. Tình trạng này rất phổ biến sau một đợt nhập dữ liệu hàng loạt (bulk import) chạy mà không kiểm tra đối chiếu với các trang hiện có. `Vault` cứ phình to ra nhưng không bao giờ kết nối lại với nhau.

**Các ốc đảo (Islands).** Các cụm chủ đề riêng biệt hoàn toàn không có cầu nối. Đôi khi điều này là hợp lý: ghi chú nấu ăn và ghi chú cơ sở dữ liệu của bạn thực sự chẳng có gì liên quan đến nhau. Nhưng thường thì không phải vậy: hai cụm bàn về những thứ liên quan nhưng lại được xây dựng bằng hai bộ từ vựng khác nhau và không bao giờ được nối lại vì thiếu `Aliases`.

## Một đồ thị lành mạnh trông như thế nào

Dày đặc bên trong từng chủ đề, thưa hơn nhưng vẫn có kết nối giữa các chủ đề với nhau. Hầu hết các trang đều có thể đi tới hầu hết các trang khác trong vòng ba hoặc bốn bước nhảy. Có các trang trung tâm (hubs) nhưng chúng không thống trị toàn bộ đồ thị. Có một số lượng nhỏ các trang cầu nối (bridge pages) kết nối các cụm lại với nhau — đây thường là những trang giá trị nhất của bạn, bởi chúng nắm giữ những mối liên hệ mà bạn không thể nào rút ra được nếu chỉ đọc từ một tài liệu nguồn đơn lẻ.

## Tại sao những điều này lại quan trọng

Khi bạn hỏi `Vault` một điều gì đó, `Agent` sẽ bắt đầu tại các trang khớp với câu hỏi và lần theo các liên kết tỏa ra xung quanh. Đồ thị chính là không gian tìm kiếm (search space). Một đồ thị có hình thái tốt giúp quá trình duyệt đồ thị chạm tới các tài liệu liên quan chỉ sau vài bước nhảy; còn một đồ thị có hình thái tệ sẽ khiến nó hoặc chẳng chạm tới thứ gì, hoặc chạm tới tất cả mọi thứ một cách vô nghĩa.

Đó là toàn bộ lý lẽ đứng sau các quy tắc liên kết. Chúng không phải là sự gọn gàng sạch sẽ hình thức, mà là yếu tố quyết định liệu cơ chế truy xuất có hoạt động được hay không.

## Tiếp theo

[Cách đọc Graph View trong Obsidian](obsidian-graph-view.md)
