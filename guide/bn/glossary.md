# শব্দকোষ

| Term | অর্থ |
| --- | --- |
| **Assignee** | যে ব্যক্তি একটি issue-এর দায়িত্ব নিয়েছেন। কোনো issue কাউকে assign করা থাকলে সাধারণত ধরে নেওয়া হয় যে সেটিতে কেউ ইতিমধ্যে কাজ করছেন। |
| **Branch** | Commit-এর একটি আলাদা ধারা। প্রতিটি পরিবর্তন তার নিজস্ব branch-এ করা উচিত। |
| **CI (continuous integration)** | স্বয়ংক্রিয় পরীক্ষা (tests, linters এবং builds), যা প্রতিটি pull request-এ চলে। |
| **CLA (Contributor License Agreement)** | একটি আইনি চুক্তি, যা কিছু প্রজেক্ট অবদান গ্রহণ করার আগে সই করতে বলে। |
| **Clone** | আপনার কম্পিউটারে থাকা একটি repository-র local কপি। |
| **Code owner** | যে ব্যক্তি বা দলকে নির্দিষ্ট কিছু ফাইলে (`CODEOWNERS`) পরিবর্তন হলে স্বয়ংক্রিয়ভাবে review করতে অনুরোধ করা হয়। |
| **Commit** | পরিবর্তনগুলোর একটি সংরক্ষিত snapshot, সঙ্গে একটি message যা পরিবর্তনগুলো বর্ণনা করে। |
| **Conventional Commits** | Commit message লেখার একটি নির্দিষ্ট format, যেমন `fix(parser): handle empty input`। |
| **DCO (Developer Certificate of Origin)** | একটি ঘোষণা, যা commit-এ `Signed-off-by:` যোগ করে (`git commit -s`) দেওয়া হয়। |
| **Default branch** | একটি repository-র প্রধান branch, সাধারণত `main` বা `master`, কখনও কখনও `develop`। |
| **Draft pull request** | এমন একটি pull request, যা এখনও review-এর জন্য প্রস্তুত নয় বলে চিহ্নিত করা হয়েছে। |
| **Fork** | GitHub-এ অন্য কারও repository-র আপনার নিজস্ব কপি। |
| **Force push** | Remote branch-এর history বদলে দেওয়া। `git push --force-with-lease` শুধু নিজের branch-এ ব্যবহার করুন। |
| **Issue** | একটি প্রজেক্টের tracker-এ থাকা bug report, feature request বা কোনো কাজের বিবরণ। |
| **Linked pull request** | কোনো issue-এর সঙ্গে যুক্ত একটি pull request, প্রায়ই `Fixes #123`-এর মতো reference দিয়ে। |
| **Linter** | এমন একটি টুল, যা কোডে style-এর সমস্যা এবং সম্ভাব্য bug খুঁজে বের করে। |
| **Maintainer** | এমন একজন ব্যক্তি, যার অন্যদের অবদান review এবং merge করার অনুমতি আছে। |
| **Merge conflict** | যখন আপনার branch এবং target branch একই লাইনে ভিন্নভাবে পরিবর্তন করেছে। |
| **Monorepo** | একটি repository, যার ভেতরে অনেকগুলো package থাকে। সাধারণত আপনি যে package পরিবর্তন করেছেন, শুধু সেটিই build এবং test করেন। |
| **Pull request (PR)** | আপনার branch-এর পরিবর্তনগুলো অন্য একটি repository-র branch-এ merge করার অনুরোধ। GitLab-এ একে merge request বলা হয়। |
| **Rebase** | একটি branch আপডেট করার জন্য আপনার commit-গুলোকে নতুন commit-গুলোর ওপরে আবার প্রয়োগ করা। |
| **Regression** | এমন একটি bug, যেখানে আগে ঠিকভাবে কাজ করা কোনো কিছু আর কাজ করছে না। |
| **Repository (repo)** | একটি প্রজেক্টের ফাইলগুলো এবং তাদের সম্পূর্ণ history। |
| **Reproduction (repro)** | ন্যূনতম কিছু ধাপ বা কোড, যা দিয়ে একটি bug নির্ভরযোগ্যভাবে আবার ঘটানো যায়। |
| **Review** | একটি pull request-এ maintainer-দের মন্তব্য, approval বা পরিবর্তনের অনুরোধ। |
| **Squash** | কয়েকটি commit একত্র করে একটি commit বানানো, যা প্রায়ই merge করার সময় করা হয়। |
| **Stale** | এমন একটি issue বা pull request, যাতে দীর্ঘ সময় ধরে কোনো activity নেই; bot এটি বন্ধ করে দিতে পারে। |
| **Triage** | নতুন issue গোছানো: bug আবার ঘটিয়ে দেখা, label লাগানো এবং duplicate খুঁজে বের করা। |
| **Upstream** | যে মূল repository থেকে আপনি fork করেছেন। |
