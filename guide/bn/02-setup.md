
# 2. আপনার টুলগুলো সেট আপ করুন

আপনার Git, একটি GitHub অ্যাকাউন্ট, GitHub-এ authenticate করার ব্যবস্থা, একটি কোড এডিটর এবং আপনার বেছে নেওয়া প্রকল্পের প্রোগ্রামিং ভাষার টুলচেইন প্রয়োজন। একবার এগুলো সেট আপ করতে প্রায় এক ঘণ্টা সময় লাগে।

## Git

Git ইনস্টল করুন:

- **macOS:** `xcode-select --install` চালান (এটি Command Line Tools-এর সঙ্গে Git ইনস্টল করে), অথবা [Homebrew](https://brew.sh)-এর মাধ্যমে `brew install git` চালান।
- **Windows:** [Git for Windows](https://git-scm.com/download/win) ইনস্টল করুন। এতে Git Bash অন্তর্ভুক্ত রয়েছে, যা এই নির্দেশিকার কমান্ডগুলো চালানোর জন্য একটি টার্মিনাল।
- **Linux:** আপনার package manager ব্যবহার করুন। উদাহরণস্বরূপ, `sudo apt install git` অথবা `sudo dnf install git` চালান।

Git-কে আপনার পরিচয় জানান। আপনার GitHub অ্যাকাউন্টে যুক্ত একই ইমেইল ঠিকানা ব্যবহার করুন (অথবা নিচে বর্ণিত GitHub-এর ব্যক্তিগত noreply ইমেইল ঠিকানা ব্যবহার করুন), যাতে আপনার commit-গুলো আপনার প্রোফাইলের সঙ্গে যুক্ত হয়।

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### আপনার ইমেইল গোপন রাখুন (ঐচ্ছিক)

GitHub প্রতিটি অ্যাকাউন্টের জন্য `12345678+username@users.noreply.github.com`-এর মতো একটি noreply ইমেইল ঠিকানা দেয়। **Settings → Emails** বিভাগে আপনার ঠিকানাটি খুঁজে নিন, **Keep my email addresses private** চালু করুন এবং `user.email` হিসেবে সেই ঠিকানাটি ব্যবহার করুন। এভাবে করা commit-গুলোও আপনার প্রোফাইলে গণনা হবে।

> **সাধারণ ভুল:** এমন ইমেইল ঠিকানা ব্যবহার করে commit করা, যা আপনার GitHub অ্যাকাউন্টে যুক্ত নেই। সে ক্ষেত্রে commit-গুলো আপনার avatar ছাড়া দেখা যেতে পারে এবং আপনার প্রোফাইলে গণনা নাও হতে পারে। `git config user.email` চালিয়ে ইমেইল ঠিকানাটি দেখুন এবং **Settings → Emails**-এ থাকা ঠিকানার সঙ্গে মিলিয়ে নিন।

## একটি GitHub অ্যাকাউন্ট এবং authentication

1. [github.com](https://github.com)-এ একটি অ্যাকাউন্ট তৈরি করুন। পেশাদার একটি username বেছে নিন, কারণ আপনার প্রতিটি অবদানের সঙ্গে এটি দেখা যাবে।
2. **Settings → Password and authentication** বিভাগে two-factor authentication (2FA) চালু করুন। অনেক প্রতিষ্ঠান এটি বাধ্যতামূলক করে।
3. Git-এর জন্য authentication-এর ব্যবস্থা করুন। সবচেয়ে সহজ উপায় হলো GitHub CLI ব্যবহার করা।

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: see cli.github.com
gh auth login          # choose GitHub.com, HTTPS, and log in with a browser
gh auth setup-git      # lets git push over HTTPS using that login
```

বিকল্পভাবে, [একটি SSH key যোগ করুন](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) এবং `git@github.com:` দিয়ে শুরু হওয়া URL ব্যবহার করে repository clone করুন।

## একটি কোড এডিটর

আপনার সুবিধাজনক যেকোনো এডিটর ব্যবহার করুন। [VS Code](https://code.visualstudio.com) একটি জনপ্রিয় বিকল্প। এতে Git-এর সঙ্গে ভালো সমন্বয় রয়েছে, আর অফিসিয়াল language extension-গুলো কোডের formatting এবং ত্রুটি শনাক্ত করতে সাহায্য করে। JetBrains IDE, Neovim, Zed এবং Emacs-ও ভালো বিকল্প।

Review-এর সময় অপ্রয়োজনীয় মন্তব্য এড়াতে দুটি সেটিংস কাজে আসে:

- **Save করার সময় formatting:** প্রকল্পের formatter ব্যবহার করে save করার সময় কোড স্বয়ংক্রিয়ভাবে format করুন। যেমন Prettier, Black, rustfmt বা gofmt।
- **`.editorconfig` মেনে চলুন:** অনেক প্রকল্পে indentation এবং line ending-এর মতো বিষয় নির্ধারণের জন্য `.editorconfig` ফাইল থাকে। ফাইলটি থাকলে এর নিয়ম অনুসরণ করুন।

## যেসব Git কমান্ড আপনি বাস্তবে ব্যবহার করবেন

| কমান্ড | কাজ |
| --- | --- |
| `git clone URL` | একটি repository-র স্থানীয় কপি তৈরি করে |
| `git status` | কী পরিবর্তন হয়েছে তা দেখায় |
| `git switch -c fix-typo` | নতুন branch তৈরি করে এবং সেটিতে চলে যায় |
| `git add path/to/file` | পরবর্তী commit-এর জন্য পরিবর্তন staging area-তে যোগ করে |
| `git commit -m "message"` | staged পরিবর্তনগুলো সংরক্ষণ করে |
| `git push -u origin fix-typo` | আপনার branch remote repository-তে পাঠায় |
| `git fetch upstream` | মূল প্রকল্পের repository থেকে সর্বশেষ পরিবর্তনের তথ্য আনে |
| `git rebase upstream/main` | upstream-এর পরিবর্তনগুলোর ওপর আপনার commit-গুলো পুনরায় প্রয়োগ করে |
| `git log --oneline -10` | সাম্প্রতিক ১০টি commit সংক্ষেপে দেখায় |
| `git diff` | staging area-তে যোগ না করা পরিবর্তনগুলো দেখায়; staged পরিবর্তন দেখতে `git diff --staged` ব্যবহার করুন |

আপনি আগে কখনো Git ব্যবহার না করে থাকলে, প্রথমে [Learn Git Branching](https://learngitbranching.js.org)-এ ৩০ মিনিট সময় দিন। এটি একটি interactive টিউটোরিয়াল, যেখানে আপনার প্রয়োজনীয় বিষয়গুলো শেখানো হয়।

## প্রোগ্রামিং ভাষার টুলচেইন

আপনার বেছে নেওয়া প্রকল্পের জন্য প্রয়োজনীয় toolchain ইনস্টল করুন এবং প্রকল্পে নির্দিষ্ট করা version ব্যবহার করুন। `.nvmrc`, `.python-version`, `rust-toolchain.toml`, `go.mod` অথবা `.tool-versions`-এর মতো ফাইলে প্রয়োজনীয় version উল্লেখ থাকতে পারে। বিভিন্ন ভাষার জন্য সাধারণ ইনস্টলেশন কমান্ড জানতে [ভাষাভিত্তিক দ্রুত নির্দেশিকা](../languages/README.md) দেখুন।

Version manager ব্যবহার করে এসব সহজে পরিচালনা করা যায়:

- **বিভিন্ন প্রোগ্রামিং ভাষা:** [mise](https://mise.jdx.dev) অথবা [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) অথবা nvm ব্যবহার করুন। pnpm এবং Yarn ব্যবহারের জন্য `corepack enable` চালান।
- **Python:** [uv](https://docs.astral.sh/uv/) ব্যবহার করুন। উদাহরণস্বরূপ, `uv python install 3.12` চালান।
- **Rust:** [rustup](https://rustup.rs) ব্যবহার করুন।
- **Go:** সরকারি ইনস্টলার অথবা আপনার package manager ব্যবহার করুন। `go.mod`-এ নতুন toolchain প্রয়োজন হলে Go নিজেই সেটি ডাউনলোড করে।

## চেকলিস্ট

- [ ] `git --version` কাজ করে এবং `git config user.email`-এ দেখানো ইমেইলটি আমার GitHub অ্যাকাউন্টে যুক্ত কোনো ইমেইলের সঙ্গে মেলে।
- [ ] Two-factor authentication চালু আছে।
- [ ] `gh auth status` (অথবা `ssh -T git@github.com`) দেখায় যে আমি GitHub-এ authenticate করতে পারি।
- [ ] আমার এডিটরে save করার সময় স্বয়ংক্রিয় formatting চালু আছে।

পরবর্তী অধ্যায়: [একটি প্রকল্প বেছে নিন](03-choose-a-project.md)
