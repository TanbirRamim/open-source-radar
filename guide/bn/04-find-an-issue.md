# 4. শেষ করতে পারবেন এমন একটি issue খুঁজুন

একটি ভালো প্রথম issue হলো ছোট, স্পষ্টভাবে বর্ণিত, পুনরায় ঘটানো যায় (reproducible) এবং অন্য কেউ ইতিমধ্যে সেটিতে কাজ করছেন না। শেষ বিষয়টিতেই বেশিরভাগ নতুন অবদানকারী সময় নষ্ট করেন।

## কোথায় খুঁজবেন

- **এই repository-এর [issue index](../../issues/README.md)** এবং [website](https://tanbirramim.github.io/open-source-radar/): নতুনদের জন্য label-যুক্ত open issue, যেখান থেকে assignee থাকা বা linked open pull request থাকা issue-গুলো আগেই বাদ দেওয়া হয়েছে।
- **প্রজেক্টের নিজস্ব issue tracker**, নতুনদের জন্য ব্যবহৃত label দিয়ে filter করে।
- **GitHub search**, উদাহরণস্বরূপ:

```text
is:issue is:open no:assignee -linked:pr label:"good first issue" language:python
```

`no:assignee` assign করা issue-গুলো লুকিয়ে রাখে, আর `-linked:pr` সেই issue-গুলো লুকায় যেগুলোর সঙ্গে ইতিমধ্যে একটি pull request যুক্ত আছে। পুরনো issue বাদ দিতে `updated:>2026-06-01` যোগ করুন (সাম্প্রতিক একটি তারিখ ব্যবহার করুন)।

## যে label-গুলো দেখবেন

| Label | সাধারণত যা বোঝায় |
| --- | --- |
| `good first issue`, `first-timers-only`, `beginner`, `E-easy` | Maintainer-রা মনে করেন একজন নতুন অবদানকারী এটি করতে পারবেন, প্রায়ই তাদের দিকনির্দেশনাসহ |
| `help wanted`, `PR welcome`, `up-for-grabs` | Maintainer-রা চান অন্য কেউ কাজটি করুক; সবসময় ছোট কাজ নয় |
| `bug`, `confirmed`, `has: repro` | একটি সত্যিকারের ত্রুটি; `confirmed` মানে একজন maintainer সমস্যাটি নিজে reproduce করেছেন |
| `needs-triage`, `needs-info`, `question` | এখনো প্রস্তুত নয়: সমস্যাটি এখনো বোঝা যায়নি |
| `design`, `rfc`, `discussion`, `blocked` | Pull request-এর জন্য প্রস্তুত নয়; একটি সিদ্ধান্ত এখনো বাকি |

প্রতিটি প্রজেক্ট নিজের label নিজে ঠিক করে। প্রজেক্টের **Issues → Labels** পেজে label-গুলোর বিবরণ দেখে নিন।

## কেউ কি ইতিমধ্যে এটিতে কাজ করছেন?

কোডের একটি লাইন লেখার আগে নিচের সবগুলো যাচাই করুন:

1. **Assignees.** কেউ assign করা থাকলে issue-টি নেওয়া হয়ে গেছে।
2. **Linked pull requests.** ডান পাশের sidebar ("Development") এবং timeline-এ PR থেকে আসা "linked a pull request" বা "mentioned this issue" ইভেন্টগুলো দেখুন। একটি open PR থাকলে issue-টি নেওয়া হয়ে গেছে; একটি closed এবং merge না হওয়া PR-এর অর্থ হতে পারে যে পদ্ধতিটি গ্রহণ করা হয়নি, তাই কারণটি পড়ে নিন।
3. **Comments.** "I'd like to work on this" বা "working on it" ধরনের মন্তব্য খুঁজুন। দাবিটি সাম্প্রতিক হলে (কয়েক সপ্তাহের মধ্যে) এবং সেই ব্যক্তি এখনো সক্রিয় থাকলে, অন্য কিছু বেছে নিন।
4. **Open pull request-এ খুঁজুন** issue নম্বর বা শিরোনামের কিছু শব্দ দিয়ে। সব PR issue-টিকে ঠিকমতো link করে না।

দাবিটি পুরনো হলে এবং সেই ব্যক্তি আর সাড়া না দিলে, সাধারণত ভদ্রভাবে জিজ্ঞেস করা যায়: "Hi @name, are you still working on this? If not, I'd be happy to pick it up." তারপর কয়েক দিন অপেক্ষা করুন।

## আপনি কি এটি শেষ করতে পারবেন?

সৎভাবে অনুমান করুন। আপনার জন্য একটি ভালো প্রথম issue:

- **প্রত্যাশিত আচরণ স্পষ্ট।** এর বদলে কী হওয়া উচিত, তা আপনি এক বাক্যে বলতে পারেন।
- **Reproduce করা যায়।** Issue-তে ধাপগুলো, একটি code snippet বা ব্যর্থ হওয়া একটি command আছে। না থাকলে, সমস্যাটি reproduce করাই আপনার প্রথম কাজ, আর reproduction পোস্ট করাটাই ইতিমধ্যে একটি অবদান।
- **নির্দিষ্ট জায়গায় সীমিত।** কোন file বা function জড়িত, তা আপনি অনুমান করতে পারেন। Issue-তে উল্লেখ করা error message বা function-এর নাম দিয়ে codebase-এ খুঁজুন।
- **কোনো design সিদ্ধান্তের প্রয়োজন নেই।** Maintainer-রা যদি এখনো আলোচনা করেন যে এটি *কীভাবে* কাজ করবে, তাহলে অপেক্ষা করুন।
- **আপনার কম্পিউটারে চলে।** আপনি macOS ব্যবহার করলে শুধু Windows-এর bug, GPU না থাকলে GPU-সংক্রান্ত bug ইত্যাদি এড়িয়ে চলুন।

## একটি issue-এর আকার দ্রুত যাচাই করার উপায়

কাজটি নেওয়ার আগে ২০ থেকে ৩০ মিনিট সময় দিন:

1. প্রজেক্টটি clone করে এর test suite একবার চালান (অধ্যায় ৫)।
2. Bug-টি reproduce করুন, অথবা feature-টির জন্য কোডের সঠিক জায়গাটি খুঁজে বের করুন।
3. সেই অংশের জন্য বিদ্যমান test file-টি খুঁজুন।

তিনটিই করতে পারলে issue-টি সম্ভবত সঠিক আকারের। ৩০ মিনিট পরেও যদি দিশেহারা থাকেন, অন্য একটি issue চেষ্টা করুন, অথবা issue-তে একটি নির্দিষ্ট প্রশ্ন করুন (অধ্যায় ৭)।

## চেকলিস্ট

- [ ] কোনো assignee নেই, কোনো linked open PR নেই, comment-এ কোনো সাম্প্রতিক দাবি নেই।
- [ ] আমি প্রত্যাশিত আচরণটি এক বাক্যে বলতে পারি।
- [ ] আমি সমস্যাটি reproduce করেছি, অথবা জানি পরিবর্তনটি ঠিক কোথায় হবে।
- [ ] Maintainer-রা পদ্ধতিটি নিয়ে আর বিতর্ক করছেন না।

পরবর্তী: [Your first pull request, step by step](../05-first-pull-request.md)
