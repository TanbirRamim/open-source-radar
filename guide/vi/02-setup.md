# 2. Thiết lập công cụ

Bạn cần Git, tài khoản GitHub, cách xác thực, trình soạn thảo và bộ công cụ của ngôn ngữ dùng trong dự án. Thiết lập ban đầu thường mất khoảng một giờ.

## Git

Cài đặt Git:

- **macOS:** chạy `xcode-select --install` để cài Git cùng Command Line Tools, hoặc chạy `brew install git` bằng [Homebrew](https://brew.sh).
- **Windows:** cài [Git for Windows](https://git-scm.com/download/win). Bộ cài có Git Bash, một terminal chạy được các lệnh trong hướng dẫn này.
- **Linux:** dùng trình quản lý gói của bản phân phối, chẳng hạn `sudo apt install git` hoặc `sudo dnf install git`.

Cho Git biết danh tính của bạn. Hãy dùng cùng địa chỉ email với tài khoản GitHub (hoặc địa chỉ noreply riêng tư của GitHub, xem bên dưới) để các commit được liên kết với hồ sơ của bạn:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### Giữ email riêng tư (tùy chọn)

GitHub cấp cho mỗi tài khoản một địa chỉ noreply dạng `12345678+username@users.noreply.github.com`. Tìm địa chỉ đó trong **Settings → Emails**, bật **Keep my email addresses private** rồi dùng nó làm `user.email`. Các commit vẫn được tính trên hồ sơ của bạn.

> **Lỗi thường gặp:** commit bằng địa chỉ email chưa được thêm vào tài khoản GitHub. Commit có thể hiện ra mà không có ảnh đại diện và không được tính trên hồ sơ. Chạy `git config user.email` rồi so sánh với địa chỉ trong **Settings → Emails**.

## Tài khoản GitHub và xác thực

1. Tạo tài khoản tại [github.com](https://github.com). Chọn tên người dùng phù hợp trong môi trường chuyên nghiệp vì tên này xuất hiện cùng mỗi đóng góp của bạn.
2. Bật xác thực hai yếu tố trong **Settings → Password and authentication**. Nhiều tổ chức yêu cầu tính năng này.
3. Thiết lập cách để Git xác thực. Cách đơn giản nhất là dùng GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: xem cli.github.com
gh auth login          # chọn GitHub.com, HTTPS và đăng nhập qua trình duyệt
gh auth setup-git      # cho phép git push qua HTTPS bằng phiên đăng nhập đó
```

Bạn cũng có thể [thêm SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) rồi clone bằng URL bắt đầu với `git@github.com:`.

## Trình soạn thảo

Dùng công cụ bạn thấy thoải mái. [VS Code](https://code.visualstudio.com) là lựa chọn phổ biến: tích hợp Git tốt, còn các extension ngôn ngữ chính thức giúp định dạng mã và phát hiện lỗi. JetBrains IDE, Neovim, Zed và Emacs cũng đều dùng được.

Hai thiết lập sau giúp bạn tránh một số góp ý khi review:

- **Tự định dạng khi lưu** bằng formatter của dự án, chẳng hạn Prettier, Black, rustfmt hoặc gofmt.
- **Tuân thủ `.editorconfig`**. Nhiều dự án dùng tệp này để quy định cách thụt lề và kiểu xuống dòng.

## Các lệnh Git bạn sẽ thường dùng

| Lệnh | Tác dụng |
| --- | --- |
| `git clone URL` | Tải một bản sao của repository về máy |
| `git status` | Xem những gì đã thay đổi |
| `git switch -c fix-typo` | Tạo branch mới rồi chuyển sang branch đó |
| `git add path/to/file` | Đưa thay đổi vào staging area để commit tiếp theo ghi nhận |
| `git commit -m "message"` | Lưu các thay đổi đã staging thành một commit |
| `git push -u origin fix-typo` | Đẩy branch của bạn lên remote |
| `git fetch upstream` | Tải thông tin thay đổi mới nhất từ repository gốc |
| `git rebase upstream/main` | Áp dụng lại commit của bạn trên nền `upstream/main` |
| `git log --oneline -10` | Xem tóm tắt 10 commit gần nhất |
| `git diff` | Xem thay đổi chưa staging; dùng `git diff --staged` để xem thay đổi đã staging |

Nếu chưa từng dùng Git, hãy dành 30 phút học qua [Learn Git Branching](https://learngitbranching.js.org). Đây là bài học tương tác, tập trung đúng vào những gì bạn cần.

## Bộ công cụ theo ngôn ngữ

Cài bộ công cụ của ngôn ngữ dự án và dùng đúng phiên bản mà dự án yêu cầu. Tìm thông tin phiên bản trong các tệp như `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod` hoặc `.tool-versions`. [Hướng dẫn nhanh theo ngôn ngữ](../../languages/README.md) liệt kê các lệnh cài đặt thường dùng.

Trình quản lý phiên bản giúp việc này đơn giản hơn:

- **Nhiều ngôn ngữ:** [mise](https://mise.jdx.dev) hoặc [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) hoặc nvm; dùng thêm `corepack enable` để bật pnpm và Yarn.
- **Python:** [uv](https://docs.astral.sh/uv/), chẳng hạn chạy `uv python install 3.12`.
- **Rust:** dùng [rustup](https://rustup.rs).
- **Go:** dùng bộ cài chính thức hoặc trình quản lý gói của bạn. Nếu `go.mod` yêu cầu toolchain mới hơn, Go sẽ tự tải phiên bản đó.

## Checklist

- [ ] `git --version` chạy được và email từ `git config user.email` khớp với một địa chỉ trong tài khoản GitHub của tôi.
- [ ] Tôi đã bật xác thực hai yếu tố.
- [ ] `gh auth status` (hoặc `ssh -T git@github.com`) xác nhận tôi có thể xác thực với GitHub.
- [ ] Trình soạn thảo tự định dạng khi lưu.

Tiếp theo: [Chọn dự án](03-choose-a-project.md)
