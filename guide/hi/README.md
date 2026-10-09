# ओपन सोर्स योगदान गाइड

“मैं योगदान देना चाहता/चाहती हूँ” से लेकर “मेरा Pull Request मर्ज हो गया” तक की एक व्यावहारिक राह। यह गाइड पहली बार योगदान करने वाले लोगों के लिए लिखी गई है और उसके बाद भी सभी के लिए उपयोगी है।

पहली बार इसे क्रम से पढ़ें। प्रत्येक अध्याय के अंत में एक छोटी चेकलिस्ट दी गई है, जिसे आप बाद में दोबारा देख सकते हैं।

[English version](../README.md) · अध्याय 4 से 7 का हिंदी अनुवाद उपलब्ध है; बाकी अध्याय अभी अंग्रेज़ी में हैं।

| # | अध्याय | आप क्या सीखेंगे |
| --- | --- | --- |
| 1 | [योगदान क्यों करें और क्या योगदान माना जाता है](../01-why-contribute.md) (English) | आपको इससे क्या मिलता है और कोड के अलावा योगदान करने के कई तरीके |
| 2 | [अपने टूल सेट अप करें](../02-setup.md) (English) | Git, GitHub अकाउंट, SSH keys, editor और command line की वे बुनियादी बातें जिनका आप वास्तव में उपयोग करेंगे |
| 3 | [एक प्रोजेक्ट चुनें](../03-choose-a-project.md) (English) | एक स्वस्थ और स्वागत करने वाले प्रोजेक्ट को ऐसे प्रोजेक्ट से कैसे पहचानें जो आपको नज़रअंदाज़ कर सकता है |
| 4 | [ऐसा issue खोजें जिसे आप पूरा कर सकें](04-find-an-issue.md) | Labels पढ़ना, यह जाँचना कि किसी और ने पहले से इसे लिया है या नहीं, और काम का आकार समझना |
| 5 | [अपना पहला Pull Request, चरण-दर-चरण](05-first-pull-request.md) | Fork, clone, branch, build, test, commit, push करना और PR खोलना |
| 6 | [शुरू करने से पहले जाँचने वाले नियम](06-rules-before-you-start.md) | Contributing guides, CLAs, DCO sign-off, AI policies और anti-spam bots |
| 7 | [Maintainers से बातचीत करना](07-communication.md) | Issue claim करना, अच्छे सवाल पूछना और ऐसी PR descriptions लिखना जिन्हें लोग review करना चाहें |
| 8 | [Reviews, feedback और rejection](../08-reviews.md) (English) | Change requests, CI failures, चुप्पी और “नहीं” को संभालना |
| 9 | [आगे बढ़ते रहें](../09-keep-going.md) (English) | एक PR से एक अच्छे track record तक: नियमित contributor, reviewer और maintainer बनना |

यह भी उपयोगी है:

- [Glossary](../glossary.md): fork, upstream, rebase, squash, CI, DCO और अन्य शब्दों का एक-लाइन में अर्थ।
- [Language quickstarts](../../languages/README.md): प्रत्येक programming language में प्रोजेक्ट आम तौर पर कैसे build और test किए जाते हैं।
- [Issue index](../../issues/README.md): language और topic के अनुसार sorted खुले और unclaimed issues, जिन्हें अपने-आप refresh किया जाता है।

## संक्षिप्त रूप

1. ऐसा प्रोजेक्ट चुनें जिसे आप इस्तेमाल करते हैं या जिसकी आपको परवाह है और जिसने पिछले महीने बाहरी contributors के Pull Requests मर्ज किए हों।
2. Newcomers के लिए labeled ऐसा issue चुनें जिसे किसी को assign नहीं किया गया है और जिससे कोई linked Pull Request नहीं है।
3. Contributing guide पढ़ें। उसका ठीक-ठीक पालन करें।
4. कुछ भी बदलने से पहले समस्या को reproduce करें।
5. ऐसी सबसे छोटी संभव change करें जो समस्या को ठीक करे, और उसके साथ एक test भी जोड़ें।
6. प्रोजेक्ट के अपने tests, formatter और linter को local रूप से चलाएँ।
7. ऐसा Pull Request खोलें जिसमें बताया गया हो कि समस्या क्या थी, आपने क्या बदला और आपने उसे कैसे check किया।
8. Review का विनम्रता और जल्दी से जवाब दें। इसे दोहराते रहें।
