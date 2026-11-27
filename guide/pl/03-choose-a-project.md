# 3. Wybór projektu

Projekt jest ważniejszy niż samo zadanie. Przyjazny, aktywny projekt zrecenzuje Twój pull request w ciągu kilku dni. Nieaktywny projekt lub przeciążony zespół może nigdy na niego nie spojrzeć, niezależnie od tego, jak dobry jest.

## Zacznij od tego, czego używasz

Najlepszy pierwszy projekt to taki, którego już używasz: biblioteka wykorzystywana w Twoim kodzie, narzędzie, z którego korzystasz na co dzień, albo aplikacja, którą lubisz. Wiesz, jak powinien działać, możesz naprawdę przetestować swoją zmianę i zależy Ci na jej rezultacie.

Jeśli nic nie przychodzi Ci do głowy, przejrzyj [indeks zgłoszeń](../../issues/README.md) według języka programowania, który znasz najlepiej, i sprawdź, które projekty regularnie się w nim pojawiają.

## Oznaki zdrowego i przyjaznego projektu

Sprawdź te rzeczy na stronie repozytorium. Pięć minut poświęconych na to teraz może oszczędzić Ci tygodni czekania.

| Co sprawdzić | Gdzie szukać | Dobry znak |
| --- | --- | --- |
| Ostatnia aktywność | Karta Commits, data „last commit” | Commity z ostatnich kilku tygodni |
| Scalanie wkładu osób spoza zespołu opiekunów | **Pull requests → Closed**, filtr `is:merged` i autorzy | W ostatnim miesiącu scalono pull requesty od osób, które nie są opiekunami projektu |
| Szybkość recenzji | Otwórz kilka niedawno scalonych PR-ów od osób spoza zespołu opiekunów | Pierwsza odpowiedź pojawia się w ciągu dni, a nie miesięcy |
| Instrukcja współtworzenia | Plik `CONTRIBUTING.md` w katalogu głównym, `.github/` lub `docs/` | Istnieje i opisuje konfigurację oraz testowanie |
| Etykiety dla nowych osób | Zgłoszenia, filtr `good first issue` lub `help wanted` | Etykiety są używane, a oznaczone nimi zgłoszenia są podejmowane |
| Ton rozmów | Przeczytaj kilka wątków zgłoszeń | Opiekunowie projektu są cierpliwi i konkretni, nawet gdy odmawiają |
| Kodeks postępowania | `CODE_OF_CONDUCT.md` | Plik istnieje |
| CI | Kontrole w niedawnych PR-ach | Testy uruchamiają się automatycznie przy pull requestach |

Szybkie wyszukiwanie scalonych PR-ów od osób spoza zespołu opiekunów dla dowolnego repozytorium (zastąp `OWNER/REPO`):

```text
https://github.com/OWNER/REPO/pulls?q=is:pr+is:merged+-author:app/dependabot+sort:updated-desc
```

Spójrz na autorów: jeśli wszystkie scalone PR-y pochodzą od tych samych dwóch osób, wkład z zewnątrz może nie być priorytetem projektu.

## Sygnały ostrzegawcze

- **Setki nieprzejrzanych, otwartych pull requestów.** Twój dołączy do kolejki.
- **Instrukcja współtworzenia mówi, że projekt nie przyjmuje pull requestów** albo przyjmuje je tylko dla zgłoszeń z określoną etykietą. Niektóre popularne projekty działają w ten sposób. Uszanuj te zasady.
- **Do każdego niedawnego zgłoszenia jest już kilka konkurencyjnych pull requestów.** W popularnych projektach PR-y od osób, które tylko przelotnie trafiły na projekt, mogą pojawić się w ciągu kilku godzin od zgłoszenia błędu. Nadal możesz tam wnieść wkład, ale wybierz mniej oblegane zadanie (dokumentację, testy, starsze potwierdzone błędy) albo mniejszy projekt.
- **Opiekunowie projektu proszą, żeby nie otwierać PR-ów o niskiej jakości.** Przeczytaj te wątki: dowiesz się z nich dokładnie, czego unikać.
- **Brak commitów od miesięcy.** Projekt może być ukończony albo porzucony.

## Duży czy mały projekt?

| Czynnik | Duży, znany projekt | Mniejszy, aktywny projekt |
| --- | --- | --- |
| Konkurencja o łatwe zadania | Bardzo duża | Niewielka |
| Szybkość recenzji | Różna, często wolna dla osób spoza zespołu | Często szybka i bezpośrednia |
| Proces | Formalny: szablony, umowy CLA, rygorystyczne CI | Lżejszy |
| Mentoring | Czasem dostępne są zorganizowane programy | Bezpośredni kontakt z opiekunem projektu |
| Rozpoznawalność na profilu | Silna dzięki znanej nazwie | Silna, jeśli zostaniesz stałym współtwórcą |

Dobra strategia: pierwsze jedno lub dwa wkłady wnieś w mniejszym, aktywnym projekcie, gdzie szybko otrzymasz informację zwrotną. Potem wykorzystaj zdobyte doświadczenie w większych projektach.

## Lista kontrolna

- [ ] W projekcie były commity w ostatnim miesiącu.
- [ ] Ostatnio scalano w nim pull requesty od osób spoza zespołu opiekunów.
- [ ] Projekt ma instrukcję współtworzenia i przeczytałem/przeczytałam ją.
- [ ] Potrafię zbudować i uruchomić projekt na swoim komputerze (omawia to rozdział 5).

Dalej: [Znajdowanie zadania, które możesz ukończyć](04-find-an-issue.md)
