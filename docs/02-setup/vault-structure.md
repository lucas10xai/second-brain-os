# Cấu trúc Vault

Một Vault đảm nhận hai nhiệm vụ hoàn toàn khác nhau, và mỗi nhiệm vụ đòi hỏi một hình thái tổ chức riêng. Việc đặt chung chúng trong cùng một cây thư mục nhưng vẫn giữ cho hai hình thái này tách biệt rạch ròi chính là bí quyết giúp hệ thống trụ vững qua tháng đầu tiên.

**Tầng tri thức (Knowledge layer)** lưu giữ những gì bạn đã đọc và thấu hiểu. Nó phát triển tích lũy mãi mãi và được tổ chức xoay quanh các ý tưởng.

**Tầng dự án (Project layer)** chứa những công việc bạn đang triển khai ngay lúc này. Nó được tổ chức theo quy trình đường ống (pipeline) và phần lớn dữ liệu tại đây sẽ khép lại sứ mệnh ngay khi dự án hoàn thành.

```
brain/
  CLAUDE.md            who you are, how the vault works
  raw/                 source material, never edited after it lands
    assets/
  wiki/                the knowledge layer
    sources/           one page per ingested item
    entities/          people, organisations, products, tools
    concepts/          ideas, methods, frameworks
    synthesis/         comparisons, themes, open questions
    index.md           catalog of every page
    log.md             what the agent did, chronologically
  projects/            the project layer
    youtube-channel/
      CLAUDE.md        this project only
      Inputs/          ideas, briefs, raw material
      Process/         work in progress
      Outputs/         finished work
      Feedback/        results, metrics, what happened
  output/              generated reports and drafts
```

## Lý do phải tách bạch hai tầng

Một đường ống dự án trả lời câu hỏi "tuần này tôi đang làm gì". Một hệ thống wiki trả lời câu hỏi "tôi đang biết gì về chủ đề X". Nếu ép một cấu trúc duy nhất phải gánh cả hai vai trò, bạn sẽ nhận về hoặc là một cơ sở tri thức ngập ngụa những thư mục công việc đã chết, hoặc là các dự án đang chạy bị chôn vùi dưới hàng đống trang khái niệm lý thuyết chẳng ai mở ra xem trong lúc làm việc.

Hai tầng này kết nối với nhau thông qua hệ thống liên kết. Một trang dự án sẽ liên kết tới các trang khái niệm mà nó dựa vào; ngược lại, các trang khái niệm sẽ tích lũy dần các tham chiếu ngược từ những dự án đã ứng dụng chúng trong thực tế. Đó chính là nơi hiệu ứng lãi kép xuất hiện: lần thứ hai bạn bắt tay làm một dự án trong cùng lĩnh vực, tầng tri thức đã chuẩn bị sẵn nền tảng cho bạn rồi.

## Khởi tạo các dự án bằng cách yêu cầu Agent

```
Create a project folder in my vault called youtube-channel. Inside it, create
four folders: Inputs, Process, Outputs, Feedback. Then write a CLAUDE.md inside
that project folder describing what this project is, its one goal, and your
specific role in helping me hit it. Interview me if you need details.
```

Hãy lặp lại thao tác này cho từng mảng công việc của bạn: sản xuất nội dung, tài chính, khách hàng. Mỗi dự án chỉ nên có một mục tiêu cốt lõi duy nhất, được ghi rõ trong file `CLAUDE.md` của riêng dự án đó. Những dự án ôm đồm cùng lúc ba mục tiêu thường tạo ra kết quả nửa vời chẳng phục vụ tốt cho mục tiêu nào cả.

## Các quy tắc giữ cho cấu trúc luôn vận hành tốt

- **Tuyệt đối không chỉnh sửa thư mục `raw/`.** Đây là kho lưu trữ gốc. Nếu một nguồn tài liệu bị lỗi, hãy thay thế bằng file mới rồi chạy Ingest lại, để `raw/` luôn là bản ghi trung thực nhất về những gì bạn thực sự đã lưu.
- **Không lồng thư mục quá sâu.** Những thư mục nằm sâu tới bốn cấp sẽ dần chẳng còn ai mở ra nữa. Đồ thị liên kết mới là công cụ điều hướng chính của bạn, chứ không phải cây thư mục.
- **Mọi thành phẩm do Agent tạo ra để sử dụng bên ngoài đều phải đưa vào `output/` hoặc thư mục `Outputs/` của dự án,** tuyệt đối không vứt rải rác ở thư mục gốc của Vault.

## Tiếp theo

[Giới hạn phạm vi theo dự án (Project scoping)](project-scoping.md)
