# शब्दावली

| Term | अर्थ |
| --- | --- |
| **Assignee** | वह व्यक्ति जो किसी issue की जिम्मेदारी लेता है। Assigned issue पर आमतौर पर कोई पहले से काम कर रहा होता है। |
| **Branch** | Commits की एक अलग श्रृंखला। हर बदलाव को अपनी branch में करना चाहिए। |
| **CI (continuous integration)** | Automated checks (tests, linters और builds) जो हर pull request पर चलते हैं। |
| **CLA (Contributor License Agreement)** | एक कानूनी समझौता, जिसे कुछ projects contributions स्वीकार करने से पहले आवश्यक मानते हैं। |
| **Clone** | आपके कंप्यूटर पर repository की एक local copy। |
| **Code owner** | वह व्यक्ति या टीम जिसे कुछ files (`CODEOWNERS`) में बदलाव review करने के लिए अपने-आप अनुरोध भेजा जाता है। |
| **Commit** | बदलावों का एक saved snapshot, जिसके साथ बदलावों का वर्णन करने वाला message होता है। |
| **Conventional Commits** | Commit messages लिखने का एक format, जैसे `fix(parser): handle empty input`। |
| **DCO (Developer Certificate of Origin)** | एक घोषणा जिसे commits में `Signed-off-by:` जोड़कर (`git commit -s`) दिया जाता है। |
| **Default branch** | Repository की मुख्य branch, आमतौर पर `main` या `master`, और कभी-कभी `develop`। |
| **Draft pull request** | ऐसा pull request जिसे अभी review के लिए तैयार नहीं माना गया है। |
| **Fork** | GitHub पर किसी दूसरे व्यक्ति की repository की आपकी अपनी copy। |
| **Force push** | Remote branch के history को बदलना। `git push --force-with-lease` का उपयोग केवल अपनी branches पर करें। |
| **Issue** | Project tracker में bug report, feature request या किसी काम का विवरण। |
| **Linked pull request** | किसी issue से जुड़ा pull request, अक्सर `Fixes #123` जैसे reference के साथ। |
| **Linter** | ऐसा tool जो code में style की समस्याएँ और संभावित bugs जाँचता है। |
| **Maintainer** | वह व्यक्ति जिसे contributions review और merge करने की अनुमति होती है। |
| **Merge conflict** | जब आपकी branch और target branch की एक ही lines में अलग-अलग बदलाव किए गए हों। |
| **Monorepo** | एक repository जिसमें कई packages होते हैं। आमतौर पर केवल उसी package को build और test किया जाता है जिसमें बदलाव किया गया हो। |
| **Pull request (PR)** | अपनी branch के बदलावों को किसी दूसरी branch में merge करने का अनुरोध। GitLab में इसे merge request कहा जाता है। |
| **Rebase** | Branch को update करने के लिए अपने commits को नए commits के ऊपर दोबारा लागू करना। |
| **Regression** | ऐसा bug जिसमें पहले सही काम करने वाली चीज़ काम करना बंद कर देती है। |
| **Repository (repo)** | Project की files और उनका पूरा history। |
| **Reproduction (repro)** | ऐसे न्यूनतम steps या code जिनसे कोई bug भरोसेमंद तरीके से दोबारा सामने आए। |
| **Review** | Pull request पर maintainers की टिप्पणियाँ, approval या बदलाव करने के अनुरोध। |
| **Squash** | कई commits को एक commit में मिलाना, जो अक्सर merge करते समय किया जाता है। |
| **Stale** | ऐसा issue या pull request जिसमें लंबे समय से कोई activity नहीं हुई हो; bots इसे बंद कर सकते हैं। |
| **Triage** | नए issues को व्यवस्थित करना: bug दोबारा जाँचना, labels लगाना और duplicate issues ढूँढना। |
| **Upstream** | वह original repository जिससे आपने fork बनाया है। |
