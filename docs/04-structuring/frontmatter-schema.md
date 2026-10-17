# Lược đồ Frontmatter

`Frontmatter` là thứ giúp `Vault` có thể được truy vấn bằng những cách khác ngoài tìm kiếm văn bản thuần túy. Việc viết nó hầu như không tốn công sức, và đó chính là dữ liệu để Dataview, các script và bản thân `Agent` sử dụng nhằm tìm kiếm thông tin theo cấu trúc.

## Lược đồ chuẩn

```yaml
---
title: Canonical name
type: source | entity | concept | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases: [other names this is known by]
tags: [two or three]
---
```

Các trang nguồn (source pages) bổ sung thêm:

```yaml
url: https://...
author:
published: YYYY-MM-DD
```

Các trang thực thể (entity pages) bổ sung thêm `kind: person | org | product | tool`.

## Lý do tồn tại của từng trường

`type` điều khiển mọi truy vấn cấu trúc và mọi bước kiểm tra `Lint`. Không có nó, bạn không thể hỏi mình đang có bao nhiêu khái niệm, hay tìm ra những trang nguồn chưa được gắn với bất kỳ khái niệm nào.

`updated` là thứ giúp việc rà soát (review) trở nên khả thi. Những trang khái niệm cũ kỹ, lỗi thời là nguyên nhân chính khiến một `Vault` bị mục rữa, và bạn không thể tìm ra chúng nếu không có ngày cập nhật.

`aliases` là thứ giúp các `Wikilink` phân giải chính xác khi cùng một thứ có tới ba tên gọi khác nhau. Xem thêm [Đặt tên và Aliases](naming-and-aliases.md).

`url` trên một trang nguồn là ranh giới phân biệt giữa một trích dẫn có căn cứ và một lời tuyên bố suông. Một trang nguồn không có `url` là không thể kiểm chứng.

## Thẻ phân loại (Tags)

Hai hoặc ba thẻ mỗi trang, lấy từ một bộ từ vựng kiểm soát nhỏ mà bạn thực sự duy trì.

Thẻ phân loại thường thất bại theo một cách rất cụ thể: bộ từ vựng phình to cho đến khi trở nên vô nghĩa. Năm mươi thẻ mà mỗi thẻ chỉ dùng đúng một lần còn tệ hơn là không dùng thẻ nào, bởi chúng tạo ra ảo tưởng về một hệ thống phân loại (taxonomy) nhưng thực tế chẳng giải quyết được việc gì.

Hãy giữ danh sách thẻ trong `CLAUDE.md` và chỉ dẫn `Agent` chỉ sử dụng các thẻ hiện có hoặc đề xuất rõ ràng một thẻ mới thay vì âm thầm tự bịa ra thẻ mới.

Thư mục và liên kết đã gánh vác phần tải trọng cấu trúc. Thẻ chỉ dành cho những tính chất cắt ngang (cross-cutting qualities) không thuộc về cả hai thứ kia: `unverified`, `to-revisit`, `disputed`.

## Các trường trống

Hãy bỏ qua một trường thay vì điền vào đó bằng sự phỏng đoán. Việc vắng mặt trường `published` có nghĩa là không rõ ngày xuất bản — điều mà `Agent` có thể trả lời một cách trung thực. Một ngày tháng phỏng đoán sẽ biến thành một "sự thật" nằm chễm chệ trong một trang khái niệm ba tuần sau đó.

## Giữ lược đồ ổn định

Thêm một trường mới vào lược đồ đồng nghĩa với việc hoặc phải cập nhật bổ sung (backfill) cho toàn bộ các trang cũ, hoặc phải sống chung với một `Vault` pha tạp mà các truy vấn sẽ bỏ sót mất một nửa số trang cũ.

Hãy quyết định lược đồ từ sớm, giữ nó gọn nhẹ và hiếm khi thay đổi. Khi bạn thực sự cần thay đổi, hãy chạy một lượt backfill trên toàn bộ `Vault` trong một lần duy nhất thay vì để thay đổi đó chỉ áp dụng cho các trang mới.

## Tiếp theo

[Đặt tên và Aliases](naming-and-aliases.md)
