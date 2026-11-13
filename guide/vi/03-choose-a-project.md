# 3. Chọn dự án

Dự án còn quan trọng hơn cả issue. Một dự án thân thiện và hoạt động tích cực thường review pull request của bạn trong vài ngày. Ngược lại, một dự án không còn hoạt động hoặc đang quá tải có thể chẳng bao giờ xem qua, dù đóng góp của bạn tốt đến đâu.

[Bản tiếng Anh](../03-choose-a-project.md)

## Bắt đầu từ thứ bạn đang dùng

Dự án đầu tiên phù hợp nhất thường là dự án bạn đã dùng: một thư viện trong code của mình, công cụ bạn chạy hằng ngày hoặc ứng dụng bạn yêu thích. Bạn hiểu dự án cần hoạt động ra sao, có thể kiểm thử thay đổi trong thực tế và quan tâm đến kết quả.

Nếu chưa nghĩ ra dự án nào, hãy duyệt [danh sách issue](../../issues/README.md) theo ngôn ngữ bạn biết rõ nhất và xem dự án nào thường xuất hiện.

## Dấu hiệu của một dự án lành mạnh và cởi mở

Hãy kiểm tra các mục này trên trang repository. Dành năm phút ở đây có thể giúp bạn tránh phải chờ đợi nhiều tuần.

| Điều cần kiểm tra | Xem ở đâu | Dấu hiệu tốt |
| --- | --- | --- |
| Hoạt động gần đây | Tab Commits, ngày “last commit” | Có commit trong vài tuần gần đây |
| Đóng góp bên ngoài được merge | **Pull requests → Closed**, lọc `is:merged` rồi xem tác giả | Trong tháng qua có pull request của người không phải maintainer được merge |
| Tốc độ review | Mở một vài PR gần đây của contributor bên ngoài đã được merge | Có phản hồi đầu tiên trong vài ngày, không phải vài tháng |
| Hướng dẫn đóng góp | `CONTRIBUTING.md` ở thư mục gốc, `.github/` hoặc `docs/` | Có hướng dẫn thiết lập và kiểm thử |
| Nhãn dành cho người mới | Issues, lọc `good first issue` hoặc `help wanted` | Có dùng nhãn và có người nhận các issue được gắn nhãn |
| Cách trao đổi | Đọc vài luồng trao đổi trên issue | Maintainer kiên nhẫn và góp ý cụ thể, kể cả khi từ chối |
| Quy tắc ứng xử | `CODE_OF_CONDUCT.md` | Có tệp này |
| CI | Các check trên PR gần đây | Test tự động chạy khi có pull request |

Tìm nhanh các PR đã được merge từ contributor bên ngoài trong bất kỳ repository nào (thay `OWNER/REPO`):

```text
https://github.com/OWNER/REPO/pulls?q=is:pr+is:merged+-author:app/dependabot+sort:updated-desc
```

Hãy xem tên tác giả: nếu mọi PR được merge gần đây đều đến từ cùng một hoặc hai người, có thể dự án chưa ưu tiên đóng góp từ bên ngoài.

## Dấu hiệu cần thận trọng

- **Hàng trăm pull request đang mở nhưng chưa được review.** PR của bạn có thể phải xếp hàng chờ.
- **Hướng dẫn đóng góp nói dự án không nhận pull request**, hoặc chỉ nhận những PR gắn với issue có nhãn cụ thể. Một số dự án phổ biến áp dụng quy định này; hãy tôn trọng nó.
- **Mỗi issue gần đây đều đã có vài pull request cạnh tranh.** Dự án phổ biến thường nhận PR tự phát chỉ sau vài giờ kể từ khi có bug. Bạn vẫn có thể đóng góp, nhưng hãy chọn việc ít cạnh tranh hơn như tài liệu, test hoặc bug cũ đã được xác nhận, hay tìm dự án nhỏ hơn.
- **Maintainer yêu cầu mọi người ngừng mở pull request sơ sài.** Hãy đọc các luồng trao đổi đó để biết chính xác điều gì cần tránh.
- **Không có commit nào trong nhiều tháng.** Có thể dự án đã hoàn tất hoặc bị bỏ dở.

## Dự án lớn hay nhỏ?

| | Dự án lớn, nổi tiếng | Dự án nhỏ hơn, hoạt động tích cực |
| --- | --- | --- |
| Cạnh tranh với issue dễ | Rất cao | Thấp |
| Tốc độ review | Thay đổi nhiều, đôi khi rất chậm với contributor bên ngoài | Thường nhanh và có trao đổi trực tiếp |
| Quy trình | Chặt chẽ: template, CLA, CI nghiêm ngặt | Gọn nhẹ hơn |
| Cố vấn | Đôi khi có chương trình bài bản | Có thể trao đổi trực tiếp với maintainer |
| Dấu ấn trên hồ sơ | Tên tuổi dễ nhận biết | Có giá trị nếu bạn đóng góp thường xuyên |

Một chiến lược phù hợp là bắt đầu với một hoặc hai đóng góp ở dự án nhỏ, hoạt động tích cực để nhận phản hồi sớm; sau đó dùng kinh nghiệm đó để tham gia các dự án lớn hơn.

## Checklist

- [ ] Trong tháng qua, dự án có commit mới.
- [ ] Gần đây dự án đã merge pull request của contributor bên ngoài.
- [ ] Tôi đã đọc hướng dẫn đóng góp của dự án.
- [ ] Tôi có thể build và chạy dự án trên máy mình (chương 5 sẽ hướng dẫn).

Tiếp theo: [Tìm issue bạn có thể hoàn thành](../04-find-an-issue.md) (English)
