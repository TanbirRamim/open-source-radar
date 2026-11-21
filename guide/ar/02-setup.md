# 2. إعداد أدواتك

ستحتاج إلى Git، وحساب على GitHub، وطريقة للمصادقة، ومحرر نصوص، وأدوات التطوير الخاصة بلغة المشروع الذي تختاره. يستغرق إعداد هذه الأدوات مرة واحدة حوالي ساعة.

## Git

ثبّت Git:

- **macOS:** استخدم `xcode-select --install` (لتثبيت Git مع أدوات سطر الأوامر)، أو `brew install git` باستخدام [Homebrew](https://brew.sh).
- **Windows:** استخدم [Git for Windows](https://git-scm.com/download/win). يتضمن Git Bash، وهي واجهة طرفية يمكنها تشغيل الأوامر الواردة في هذا الدليل.
- **Linux:** استخدم مدير الحزم الخاص بتوزيعتك، على سبيل المثال `sudo apt install git` أو `sudo dnf install git`.

أخبر Git بهويتك. استخدم البريد الإلكتروني نفسه المرتبط بحساب GitHub الخاص بك (أو عنوان noreply الخاص بـ GitHub، الموضح أدناه) حتى تُربط عمليات الإيداع (commits) بملفك الشخصي:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### الحفاظ على خصوصية بريدك الإلكتروني (اختياري)

يوفر GitHub لكل حساب عنوان بريد إلكتروني خاصًا من نوع noreply، مثل `12345678+username@users.noreply.github.com`. اعثر على عنوانك ضمن **Settings → Emails**، وفعّل خيار **Keep my email addresses private**، ثم استخدم ذلك العنوان في إعداد `user.email`. ستظل عمليات الإيداع تُحتسب ضمن مساهماتك في ملفك الشخصي.

> **خطأ شائع:** إجراء عملية إيداع باستخدام بريد إلكتروني غير مضاف إلى حساب GitHub الخاص بك. قد تظهر عمليات الإيداع دون صورتك الشخصية، ولن تُحتسب ضمن مساهماتك في ملفك الشخصي. تحقق باستخدام `git config user.email` وقارن النتيجة بعنوان بريدك في **Settings → Emails**.

## حساب GitHub والمصادقة

1. أنشئ حسابًا على [github.com](https://github.com). اختر اسم مستخدم احترافيًا؛ لأنه سيظهر مع كل مساهمة تقدمها.
2. فعّل المصادقة الثنائية من خلال **Settings → Password and authentication**. تشترطها العديد من المؤسسات.
3. أعدّ طريقة تسمح لـ Git بالمصادقة. أسهل طريقة هي استخدام GitHub CLI:

```bash
# macOS: brew install gh   Windows: winget install GitHub.cli   Linux: see cli.github.com
gh auth login          # choose GitHub.com, HTTPS, and log in with a browser
gh auth setup-git      # lets git push over HTTPS using that login
```

بدلًا من ذلك، يمكنك [إضافة مفتاح SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) واستنساخ المستودعات باستخدام عناوين `git@github.com:`.

## محرر النصوص

استخدم المحرر الذي تشعر بالراحة عند العمل به. يُعد [VS Code](https://code.visualstudio.com) خيارًا شائعًا؛ إذ يوفر تكاملًا جيدًا مع Git، كما توفر إضافات اللغات الرسمية تنسيقًا للكود واكتشافًا للأخطاء. وتُعد JetBrains IDEs وNeovim وZed وEmacs خيارات مناسبة أيضًا.

هناك إعدادان يساعدانك على تجنب ملاحظات المراجعة:

- **Format on save:** فعّل تنسيق الملفات عند الحفظ باستخدام أداة التنسيق الخاصة بالمشروع، مثل Prettier أو Black أو rustfmt أو gofmt وغيرها.
- **Respect `.editorconfig`:** احترم إعدادات ملف `.editorconfig`. تتضمن العديد من المشاريع هذا الملف لتحديد المسافات البادئة ونهايات الأسطر.

## أوامر Git التي ستستخدمها فعليًا

| الأمر                         | وظيفته                                                                 |
| ----------------------------- | ---------------------------------------------------------------------- |
| `git clone URL`               | تنزيل مستودع                                                           |
| `git status`                  | معرفة التغييرات                                                        |
| `git switch -c fix-typo`      | إنشاء فرع جديد والانتقال إليه                                          |
| `git add path/to/file`        | تجهيز تغيير لإضافته إلى عملية الإيداع التالية                          |
| `git commit -m "message"`     | تسجيل التغييرات التي تم تجهيزها                                        |
| `git push -u origin fix-typo` | رفع فرعك إلى المستودع البعيد                                           |
| `git fetch upstream`          | تنزيل أحدث التغييرات من المشروع الأصلي                                 |
| `git rebase upstream/main`    | إعادة تطبيق عمليات الإيداع الخاصة بك فوق تلك التغييرات                 |
| `git log --oneline -10`       | عرض آخر عمليات الإيداع                                                 |
| `git diff`                    | عرض التغييرات غير المجهزة (`git diff --staged` لعرض التغييرات المجهزة) |

إذا لم تستخدم Git من قبل، خصص 30 دقيقة للتعلم من [Learn Git Branching](https://learngitbranching.js.org). فهو موقع تفاعلي يغطي بالضبط ما تحتاج إليه.

## أدوات تطوير اللغات البرمجية

ثبّت أدوات التطوير الخاصة بالمشروع الذي تختاره، مع استخدام الإصدار الذي يطلبه المشروع. ابحث عن ملفات مثل `.nvmrc` و`.python-version` و`rust-toolchain.toml` و`go.mod` و`.tool-versions`. تعرض [الأدلة السريعة للغات البرمجية](../languages/README.md) الأوامر المعتادة لكل لغة.

تجعل أدوات إدارة الإصدارات هذه العملية أسهل:

- **عدة لغات:** [mise](https://mise.jdx.dev) أو [asdf](https://asdf-vm.com)
- **Node.js:** [fnm](https://github.com/Schniz/fnm) أو nvm، بالإضافة إلى `corepack enable` لاستخدام pnpm وYarn.
- **Python:** [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`)
- **Rust:** [rustup](https://rustup.rs)
- **Go:** استخدم أداة التثبيت الرسمية أو مدير الحزم الخاص بك؛ إذ يستطيع Go تنزيل إصدارات أحدث من أدوات التطوير تلقائيًا عندما يطلب ملف `go.mod` ذلك.

## قائمة التحقق

- [ ] يعمل الأمر `git --version`، ويتطابق البريد الإلكتروني في `git config user.email` مع أحد عناوين البريد الإلكتروني المرتبطة بحساب GitHub الخاص بي.
- [ ] تم تفعيل المصادقة الثنائية.
- [ ] يُظهر الأمر `gh auth status` (أو `ssh -T git@github.com`) أنني أستطيع المصادقة.
- [ ] يقوم محرر النصوص بتنسيق الملفات عند الحفظ.

التالي: [اختيار مشروع](03-choose-a-project.md)
