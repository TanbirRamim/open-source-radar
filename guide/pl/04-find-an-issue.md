# 4. Znajdowanie zadania, które możesz ukończyć

Dobre pierwsze zadanie jest niewielkie, jasno opisane, odtwarzalne i nikt jeszcze nad nim nie pracuje. Ten ostatni punkt to miejsce, w którym większość początkujących traci najwięcej czasu.

## Gdzie szukać

- **[Indeks zgłoszeń](../../issues/README.md) tego repozytorium** oraz [strona internetowa](https://tanbirramim.github.io/open-source-radar/): otwarte zgłoszenia oznaczone etykietami dla nowych osób, już przefiltrowane tak, aby wykluczyć te z przypisaną osobą lub powiązanym otwartym pull requestem.
- **Własny system śledzenia zgłoszeń (issue tracker) projektu**, przefiltrowany według jego etykiet dla nowych osób.
- **Wyszukiwarka GitHuba**, na przykład:

```text
is:issue is:open no:assignee -linked:pr label:"good first issue" language:python
```

`no:assignee` ukrywa przypisane zgłoszenia, a `-linked:pr` ukrywa zgłoszenia, które mają już powiązany pull request. Dodaj `updated:>2026-06-01` (użyj niedawnej daty), aby pominąć nieaktualne zgłoszenia.

## Etykiety, które zobaczysz

| Etykieta | Co zazwyczaj oznacza |
| --- | --- |
| `good first issue`, `first-timers-only`, `beginner`, `E-easy` | Opiekunowie projektu uważają, że nowa osoba sobie z tym poradzi, często z ich pomocą |
| `help wanted`, `PR welcome`, `up-for-grabs` | Opiekunowie projektu chcą, aby ktoś inny się tym zajął; nie zawsze jest to małe zadanie |
| `bug`, `confirmed`, `has: repro` | Prawdziwy błąd; `confirmed` oznacza, że opiekun projektu go odtworzył |
| `needs-triage`, `needs-info`, `question` | Jeszcze niegotowe: problem nie został jeszcze zrozumiany |
| `design`, `rfc`, `discussion`, `blocked` | Niegotowe na pull request; decyzja jest w toku |

Każdy projekt definiuje własne etykiety. Sprawdź opisy etykiet na stronie projektu w zakładce **Issues → Labels**.

## Czy ktoś już nad tym pracuje?

Zanim napiszesz choćby jedną linijkę kodu, sprawdź wszystkie poniższe rzeczy:

1. **Przypisane osoby (Assignees).** Jeśli ktoś jest przypisany, zadanie jest już zajęte.
2. **Powiązane pull requesty.** Sprawdź prawy panel boczny („Development”) oraz oś czasu zgłoszenia pod kątem zdarzeń „linked a pull request” lub „mentioned this issue” z PR-ów. Otwarty PR oznacza, że zadanie jest zajęte; zamknięty, ale niescalony PR może oznaczać, że podejście zostało odrzucone — przeczytaj dlaczego.
3. **Komentarze.** Szukaj wpisów w rodzaju „I'd like to work on this” lub „working on it”. Jeśli zgłoszenie chęci jest niedawne (z ostatnich kilku tygodni) i dana osoba nie zamilkła, wybierz coś innego.
4. **Przeszukaj otwarte pull requesty** pod kątem numeru zgłoszenia lub słów kluczowych z tytułu. Nie każdy PR prawidłowo linkuje powiązane zgłoszenie.

Jeśli deklaracja jest stara, a dana osoba zamilkła, zazwyczaj można uprzejmie zapytać: „Hi @name, are you still working on this? If not, I'd be happy to pick it up.”. Następnie poczekaj kilka dni.

## Czy dasz radę je ukończyć?

Oceń uczciwie swoje możliwości. Dobre pierwsze zadanie dla Ciebie:

- **Ma jasno określone oczekiwane działanie.** Potrafisz w jednym zdaniu powiedzieć, co powinno się dziać zamiast obecnego zachowania.
- **Jest odtwarzalne.** Zgłoszenie zawiera kroki, fragment kodu lub polecenie kończące się błędem. Jeśli nie, odtworzenie problemu jest Twoim pierwszym zadaniem, a opublikowanie instrukcji odtworzenia to już wartościowy wkład.
- **Jest zlokalizowane.** Możesz domyślić się, którego pliku lub funkcji dotyczy. Przeszukaj bazę kodu pod kątem komunikatu błędu lub nazwy funkcji wspomnianej w zgłoszeniu.
- **Nie wymaga decyzji projektowej.** Jeśli opiekunowie projektu nadal dyskutują, *jak* to powinno działać, poczekaj.
- **Działa na Twoim komputerze.** Unikaj błędów występujących wyłącznie na Windowsie, jeśli korzystasz z macOS, błędów GPU bez karty graficznej itd.

## Szybki sposób na oszacowanie rozmiaru zadania

Poświęć 20 do 30 minut, zanim się go podejmiesz:

1. Sklonuj projekt i uruchom raz jego zestaw testów (rozdział 5).
2. Odtwórz błąd albo znajdź w kodzie miejsce dla nowej funkcji.
3. Znajdź istniejący plik z testami dla tego obszaru.

Jeśli udało Ci się przejść przez wszystkie trzy kroki, zadanie ma prawdopodobnie odpowiedni rozmiar. Jeśli po 30 minutach nadal nie wiesz, od czego zacząć, wybierz inne zgłoszenie albo zadaj konkretne pytanie pod zgłoszeniem (rozdział 7).

## Lista kontrolna

- [ ] Brak przypisanej osoby, brak powiązanego otwartego PR-a i brak niedawnej deklaracji w komentarzach.
- [ ] Potrafię opisać oczekiwane działanie w jednym zdaniu.
- [ ] Odtworzyłem/odtworzyłam problem albo dokładnie wiem, gdzie należy wprowadzić zmianę.
- [ ] Opiekunowie projektu nie debatują już nad wyborem podejścia.

Dalej: [Twój pierwszy pull request krok po kroku](../05-first-pull-request.md)
