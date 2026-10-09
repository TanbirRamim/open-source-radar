# 6. शुरू करने से पहले जाँचने वाले नियम

हर project में contributions के लिए कुछ नियम होते हैं। कुछ केवल conventions होते हैं; जबकि दूसरे यह तय करते हैं कि आपका Pull Request merge किया जा सकता है या नहीं, या वह अपने-आप बंद हो जाएगा। Code लिखने से **पहले** इन नियमों को जाँचें।

[English version](../06-rules-before-you-start.md)

[Issue index](../../issues/README.md) प्रत्येक project के लिए अपने-आप detect किए गए hints दिखाता है। ये केवल hints हैं, guarantees नहीं: हमेशा project की अपनी files पढ़ें।

| Index में Note | इसका मतलब |
| --- | --- |
| ⚠️ AI restricted | Project की contribution files में AI-generated contributions पर प्रतिबंध या कड़े restrictions दिखाई देते हैं |
| 🤖 disclose AI use | Project आपसे AI assistance का खुलासा करने के लिए कहता है |
| 📄 AI policy | Project की AI policy है; उसे पढ़ें |
| ✍️ CLA | संभवतः आपको Contributor License Agreement पर हस्ताक्षर करने होंगे |
| 🔏 DCO | Commits में संभवतः `Signed-off-by` line की आवश्यकता होगी |

## नियम कहाँ होते हैं

इन सभी जगहों को देखें, केवल README को नहीं:

- `CONTRIBUTING.md` (root, `.github/` या `docs/` में)
- `.github/PULL_REQUEST_TEMPLATE.md` और issue templates
- `CODE_OF_CONDUCT.md`
- `AI_POLICY.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.claude/`, `.cursor/rules`
- `DEVELOPMENT.md`, `docs/development/` या project की website पर contributing page
- `.github/workflows/` (ऐसी automation जो Pull Requests को label, check या close करती है)

## Contributor License Agreements (CLA)

CLA एक कानूनी agreement है जो project (या उसके पीछे की company) को आपके contribution का उपयोग करने के अधिकार देता है। Company-backed कई projects में इसकी आवश्यकता होती है।

- आम तौर पर आपका पहला Pull Request खोलने पर एक bot link के साथ comment करता है। आप एक बार online sign करते हैं और यह उस project या organization में आपके future contributions को भी cover करता है।
- कुछ CLAs organization-wide account से जुड़े होते हैं, जैसे Linux Foundation का EasyCLA (जिसका उपयोग कई CNCF projects करते हैं) या Google का CLA।
- **जिस पर sign कर रहे हैं उसे पढ़ें।** अगर आप किसी employer की ओर से contribution कर रहे हैं, तो आपके employer को corporate CLA पर sign करने की आवश्यकता हो सकती है।

## Developer Certificate of Origin (DCO)

DCO, CLA का एक सरल alternative है: आप certify करते हैं कि आपके पास code submit करने का अधिकार है। आप हर commit में एक sign-off line जोड़कर ऐसा करते हैं:

```bash
git commit -s -m "fix: handle empty username"
# adds: Signed-off-by: Your Name <you@example.com>
```

DCO bot Pull Request में हर commit को check करता है। अगर आप भूल गए हों, तो इसे इस तरह ठीक करें:

```bash
git rebase --signoff upstream/main
git push --force-with-lease
```

Sign-off में दिया गया name और email आपके commit author से match होना चाहिए।

## AI-assisted contributions

Maintainers ने low-quality, AI-generated Pull Requests की संख्या में वृद्धि देखी है और कई projects में अब इसके लिए स्पष्ट rules हैं। ये rules काफी अलग-अलग हो सकते हैं:

- **सामान्य standards के साथ allowed।** आप हर line के लिए responsible हैं और उसे explain करने में सक्षम होना चाहिए।
- **Disclosure के साथ allowed।** आपको PR description में बताना होगा कि आपने कौन-सा tool इस्तेमाल किया और किस काम के लिए, या commits में `Assisted-by:` जैसा trailer जोड़ना होगा।
- **केवल human-written communication।** AI code में मदद कर सकता है, लेकिन issue comments और PR descriptions आपको स्वयं लिखनी होंगी।
- **Restricted या banned।** कुछ projects AI-generated code या documentation स्वीकार नहीं करते, या AI agents को Pull Requests खोलने की अनुमति नहीं देते।

Policy चाहे जो भी हो, ये बातें हर जगह लागू होती हैं:

- आपको अपने submit किए गए हर change को समझना और उसका बचाव करने में सक्षम होना चाहिए।
- बिना स्वयं review किए किसी tool को अपने नाम से Pull Requests खोलने या comments post करने न दें।
- जब project में disclosure rules हों, तो उनका ठीक-ठीक पालन करें। जहाँ disclosure आवश्यक हो वहाँ AI के उपयोग को छिपाना project से ban होने का तेज़ तरीका हो सकता है।

## Anti-spam और first-time-contributor automation

Spam के कारण कुछ projects ऐसे workflows चलाते हैं जो Pull Requests को अपने-आप close या label कर देते हैं। वास्तविक projects में देखे जाने वाले rules में शामिल हैं:

- ऐसे accounts से Pull Requests बंद करना जिन्होंने कम समय में कई असंबंधित repositories में PR खोले हों
- ऐसे authors के PRs बंद करना जिनके Pull Requests हाल ही में कहीं और reject हुए हों
- AI tools के नाम वाली branches से PRs बंद करना (उदाहरण के लिए `claude/...` या `codex/...`)
- PR स्वीकार करने से पहले linked issue या `help wanted` जैसा issue label आवश्यक होना
- भरा हुआ PR template आवश्यक होना, जिसमें हर checkbox का उत्तर दिया गया हो
- First-time contributors के लिए maintainer की approval मिलने तक CI को रोकना (यह सामान्य और harmless है)

`.github/workflows/` में `close-spam`, `first-interaction` या `pr-checks` जैसे नाम वाली files देखें ताकि पता चल सके कि इनमें से कौन-से rules लागू होते हैं। व्यावहारिक सलाह: एक ही सप्ताह में दर्जनों repositories में Pull Requests खोलने के बजाय कुछ projects में लगातार योगदान करें।

## कानूनी statements और licensing

कुछ projects आपसे Pull Request में कोई statement शामिल करने के लिए कहते हैं, जैसे कि आपने code स्वयं लिखा है और उसे project की terms के तहत license करते हैं। केवल वही statements करें जो सच हों। Contribution submit करने पर आम तौर पर आप उसे project के license के तहत license करते हैं, इसलिए जाँच लें कि वह license आपके लिए (और अगर relevant हो तो आपके employer के लिए) स्वीकार्य है।

## Checklist

- [ ] मैंने contributing guide, PR template और किसी भी AI policy या agent instructions को पढ़ लिया है।
- [ ] मुझे पता है कि CLA या DCO sign-off की आवश्यकता है या नहीं।
- [ ] मुझे project की commit message और PR title conventions पता हैं।
- [ ] मैंने `.github/workflows/` में ऐसी automation की जाँच कर ली है जो मेरा PR close कर सकती है।
- [ ] अगर AI ने मेरी मदद की है, तो मुझे पता है कि मुझे इसका खुलासा करना है या नहीं और कैसे करना है।

अगला: [Maintainers से बातचीत करना](07-communication.md)
