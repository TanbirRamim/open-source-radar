# 4. Tìm một issue mà bạn có thể hoàn thành

Một issue tốt dành cho người mới bắt đầu thường có phạm vi nhỏ, mô tả rõ ràng, có thể tái hiện được và chưa có người khác đang thực hiện. Điểm cuối cùng này là nơi khiến nhiều người mới mất thời gian nhất.

## Nơi tìm kiếm

- **[Danh sách issue của repository này](../../issues/README.md)** và [website](https://tanbirramim.github.io/open-source-radar/): các issue được gắn nhãn dành cho người mới bắt đầu đã được lọc để loại trừ những issue có người được giao hoặc có pull request đang mở được liên kết.
- **Issue tracker của chính dự án**, được lọc theo các nhãn dành cho người mới.
- **Tìm kiếm trên GitHub**, ví dụ:

```text
is:issue is:open no:assignee -linked:pr label:"good first issue" language:python
```

`no:assignee` ẩn các issue đã được giao cho người khác và `-linked:pr` ẩn các issue đã có pull request được liên kết. Thêm `updated:>2026-06-01` (sử dụng một ngày gần đây) để bỏ qua những issue đã lâu không được cập nhật.

## Các nhãn bạn sẽ gặp

| Nhãn | Ý nghĩa thông thường |
| --- | --- |
| `good first issue`, `first-timers-only`, `beginner`, `E-easy` | Người quản lý dự án cho rằng người mới có thể thực hiện, thường có hướng dẫn |
| `help wanted`, `PR welcome`, `up-for-grabs` | Người quản lý dự án muốn người khác tham gia; nhưng không phải lúc nào cũng là công việc nhỏ |
| `bug`, `confirmed`, `has: repro` | Một lỗi thực sự; `confirmed` có nghĩa là người quản lý dự án đã tái hiện được lỗi |
| `needs-triage`, `needs-info`, `question` | Chưa sẵn sàng: vấn đề vẫn chưa được hiểu rõ |
| `design`, `rfc`, `discussion`, `blocked` | Chưa sẵn sàng để tạo pull request vì vẫn đang chờ quyết định |

Mỗi dự án có thể định nghĩa các nhãn riêng. Hãy kiểm tra mô tả nhãn trên trang **Issues → Labels** của dự án.

## Có ai đang thực hiện issue này chưa?

Trước khi viết bất kỳ dòng mã nào, hãy kiểm tra tất cả những điều sau:

1. **Người được giao (Assignees).** Nếu đã có người được giao, issue đó đã có người thực hiện.
2. **Các pull request được liên kết (Linked pull requests).** Kiểm tra thanh bên phải ("Development") và dòng thời gian để tìm các sự kiện như "linked a pull request" hoặc "mentioned this issue" từ các pull request. Một PR đang mở có nghĩa là issue đã có người thực hiện; một PR đã đóng nhưng chưa được hợp nhất có thể cho thấy phương pháp đó đã bị từ chối, vì vậy hãy đọc lý do.
3. **Bình luận (Comments).** Tìm những bình luận như "I'd like to work on this" hoặc "working on it". Nếu người nhận issue đã xác nhận gần đây (khoảng vài tuần) và vẫn đang hoạt động, hãy chọn một issue khác.
4. **Tìm kiếm các pull request đang mở.** Tìm theo số issue hoặc các từ khóa trong tiêu đề. Không phải PR nào cũng liên kết issue một cách chính xác.

Nếu một lời nhận issue đã lâu và người đó không còn hoạt động, bạn thường có thể lịch sự hỏi:

"Chào @name, bạn vẫn đang thực hiện issue này chứ? Nếu không, tôi rất sẵn lòng tiếp nhận nó."

Sau đó hãy chờ vài ngày.

## Bạn có thể hoàn thành issue này không?

Hãy đánh giá một cách trung thực. Một issue tốt dành cho người mới bắt đầu nên:

- **Có hành vi mong đợi rõ ràng.** Bạn có thể diễn đạt trong một câu về điều gì nên xảy ra thay vì hành vi hiện tại.
- **Có thể tái hiện được.** Issue có các bước thực hiện, một đoạn mã hoặc một lệnh bị lỗi. Nếu không có, việc tái hiện lỗi sẽ là nhiệm vụ đầu tiên của bạn và đăng kết quả tái hiện cũng đã là một đóng góp.
- **Có phạm vi cục bộ.** Bạn có thể dự đoán tệp hoặc hàm nào liên quan. Hãy tìm kiếm trong mã nguồn thông báo lỗi hoặc tên hàm được đề cập trong issue.
- **Không cần quyết định về thiết kế.** Nếu người quản lý dự án vẫn đang thảo luận về *cách* hoạt động của tính năng, hãy chờ.
- **Có thể chạy trên máy của bạn.** Tránh các lỗi chỉ xảy ra trên Windows nếu bạn dùng macOS, các lỗi GPU nếu không có GPU, v.v.

## Cách nhanh chóng đánh giá độ phức tạp của một issue

Dành 20 đến 30 phút trước khi quyết định thực hiện:

1. Clone dự án và chạy bộ kiểm thử một lần (chương 5).
2. Tái hiện lỗi hoặc tìm vị trí trong mã nguồn cần triển khai tính năng.
3. Tìm tệp kiểm thử hiện có cho khu vực đó.

Nếu bạn hoàn thành cả ba bước, issue đó có thể có phạm vi phù hợp. Nếu sau 30 phút bạn vẫn chưa hiểu rõ, hãy thử một issue khác hoặc đặt một câu hỏi cụ thể trong issue (chương 7).

## Danh sách kiểm tra

- [ ] Không có người được giao, không có PR đang mở được liên kết và không có lời nhận issue gần đây.
- [ ] Tôi có thể diễn đạt hành vi mong đợi trong một câu.
- [ ] Tôi đã tái hiện được vấn đề hoặc biết chính xác vị trí cần thay đổi.
- [ ] Người quản lý dự án không còn đang tranh luận về phương pháp thực hiện.

Tiếp theo: [Pull request đầu tiên của bạn, từng bước một](../05-first-pull-request.md) (English)
