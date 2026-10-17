# Sao lưu và tính khả chuyển

## Đồng bộ (Sync) không phải là sao lưu (Backup)

Đây là thông điệp cốt lõi của cả trang này, và cũng là sai lầm mà hầu như ai cũng mắc phải.

Đồng bộ có tính chất lan truyền. Nếu một tác vụ tự động hóa viết lại hai trăm trang một cách tệ hại, cơ chế đồng bộ sẽ trung thành sao chép sự phá hoại đó sang mọi thiết bị chỉ trong vài giây. Nếu một file bị xóa, nó sẽ bị xóa ở khắp mọi nơi.

Sao lưu nghĩa là một bản sao độc lập không tự động chạy theo những thay đổi đó. Bạn cần ít nhất một bản như vậy, tách rời hoàn toàn khỏi luồng đồng bộ.

## Một cách bố trí thực tế và hiệu quả

**Git remote,** đặt ở chế độ riêng tư, được đẩy lên (push) sau mỗi lượt chạy. Vì có lưu lịch sử phiên bản, nó giải quyết được câu hỏi "cách đây ba tuần trông nó thế nào" — điều mà một bản sao lưu file thông thường không làm được.

**Đồng bộ (Sync)** để làm việc xuyên suốt giữa các máy tính, dùng bất kỳ dịch vụ nào bạn đang quen dùng.

**Một bản lưu trữ định kỳ (periodic archive)** đẩy lên ổ cứng ngoài hoặc một dịch vụ đám mây khác, không kết nối với hai cơ chế trên. Mỗi tháng một lần là đủ.

Ba bản sao, trong đó có một bản "ngây ngô" và cập nhật chậm, là cách bố trí sống sót được qua những sự cố thực sự xảy ra ngoài đời thực.

## Thử khôi phục một lần

Chỉ cần làm một lần thôi. Hãy lấy bản lưu trữ định kỳ đó, khôi phục nó ra một thư mục khác, mở bằng Obsidian và kiểm tra xem các liên kết có hoạt động bình thường không.

Những bản sao lưu chưa từng được kiểm tra luôn hỏng vào đúng thời điểm tồi tệ nhất, và lỗi phổ biến nhất không phải là hỏng dữ liệu (corruption). Lỗi thường gặp là lúc khôi phục mới phát hiện ra bản lưu trữ đã bỏ sót một thư mục, hoặc chụp lại Vault ngay giữa lúc đang đồng bộ dở dang khiến các file ở trạng thái ghi nửa chừng.

## Thứ bạn thực sự cần phòng vệ

Không phải lỗi hỏng ổ cứng — chuyện đó hiếm khi xảy ra và cơ chế đồng bộ đã xử lý được rồi.

Rủi ro thực sự là một tác vụ tự động hóa đã âm thầm làm sai điều gì đó từ ba tuần trước, mà mãi đến hôm nay bạn mới phát hiện ra. Tình huống đó đòi hỏi phải có lịch sử thay đổi, và đó là lý do Git gánh phần lớn trọng trách ở đây chứ không phải các bản sao lưu file đơn thuần.

## Tính khả chuyển (Portability)

Vault thực chất chỉ là các file markdown và Wikilink, nên việc rời bỏ bất kỳ công cụ cụ thể nào cũng không làm mất đi cấu trúc cốt lõi. Tuy nhiên, thỉnh thoảng bạn nên kiểm tra lại vài điểm sau:

**Không có thông tin quan trọng nào nằm bên ngoài các file văn bản.** Dữ liệu đặc thù của plugin, các file canvas, hay các bản xuất cơ sở dữ liệu — tất cả đều tốt khi đóng vai trò bổ trợ, nhưng không thứ nào trong số đó được phép nắm giữ những tri thức không tồn tại ở bất kỳ nơi nào khác.

**Các liên kết vẫn phân giải được khi không có Obsidian.** Script `scripts/link_check.py` giúp xác minh điều này, vì bản thân nó tự phân tích cú pháp Wikilink một cách độc lập.

**Chỉ dẫn dành cho Agent phải nằm ngay trong Vault,** chứ không nằm trong lịch sử trò chuyện hay phần cài đặt của một ứng dụng nào đó. `CLAUDE.md`, các Skills và các lệnh đều phải đi kèm theo thư mục Vault.

## Tiếp theo

[Quyền riêng tư và thông tin nhạy cảm](privacy-and-secrets.md)
