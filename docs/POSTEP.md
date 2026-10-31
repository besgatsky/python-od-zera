# Postęp

## Aktualny etap
Etap 1: zaliczony (bramka przeszła)
Następny: Etap 2 (funkcje, listy, słowniki, start projektu: lista zadań), jeszcze nie rozpoczęty

## Zrobione
Etap 0:
- Profil w PLAN.md uzupełniony: Windows, 3 godziny tygodniowo
- Python 3.15.2, VS Code z rozszerzeniem Python, Git 2.56.0
- Repo sklonowane poza OneDrive na obu komputerach, imię i e-mail w Git tylko dla tego repo (bez --global)
- hello.py, README.md, pierwsze commity i push
- Obieg dwóch komputerów sprawdzony (commit i push na jednym, pull na drugim)

Etap 1 (każde ćwiczenie w osobnym pliku, z commitem):
- zmienne.py: tworzenie i nadpisywanie zmiennych, print z kilkoma argumentami
- typy.py: str, int, float, bool, type(), różnica między 5 + 5 a "5" + "5"
- wejscie.py: input(), zamiana typu przez int(), obliczanie wieku z roku urodzenia
- warunki.py: if / elif / else, testy graniczne (17, 18, 64, 65)
- petle.py: pętla for z range, tabliczka mnożenia, wcięcie jako zapis tego, co należy do pętli
- zgadnij.py: pętla while, gra w zgadywanie liczby

## Poznane pojęcia
- Zmienna: nazwa, pod którą Python pamięta wartość; = to "włóż do pudełka", nie "równa się"
- Python czyta kod od góry do dołu, nowa wartość zmiennej działa od miejsca przypisania
- Typy: str, int, float, bool; liczby różnych typów można mieszać, tekstu z liczbą nie (TypeError)
- input() zawsze zwraca str; do liczenia trzeba int() lub float()
- Czytanie błędu (Traceback): linijka z komunikatem bywa dalej niż faktyczna przyczyna
- Komentarz #: pisze się dlaczego, nie co; musi opisywać kod, który faktycznie stoi w pliku
- Warunki: if / elif / else, dwukropek i wcięcie; porównania <, >, <=, >=, ==, !=
- Kolejność warunków ma znaczenie: Python zatrzymuje się na pierwszym spełnionym; układamy od najbardziej szczegółowego do najogólniejszego
- if / elif / else nie jest pętlą (pomija pozostałe gałęzie i idzie dalej)
- for i in range(...): liczenie od zera, górna granica nie wchodzi do wyniku
- while: powtarza, dopóki warunek jest prawdziwy; w środku musi się zmieniać to, co warunek sprawdza
- Nieskończona pętla: warunek zostaje prawdziwy; zatrzymanie programu: Ctrl+C
- Wcięcie w Pythonie to zapis przynależności do bloku, nie ozdoba
- Dobre nazwy zmiennych mówią, co jest w środku (rok_urodzenia, a nie wiek_wprowadz); jeden język w nazwach (polski)

## Otwarte pytania
- Czy laptop jest używany także do pracy zawodowej na tym samym koncie Windows? (od tego zależy, czy ustawienia Gita muszą zostać tylko lokalne dla repo)

## Backlog (pytania i pomysły na później)
- Dlaczego Git i OneDrive się gryzą; czym jest ukryty folder .git
- Konflikty przy pracy na 2 komputerach (etap 3)
- fetch vs pull, dokładniej (etap 3)
- Ścieżki względne zamiast bezwzględnych w kodzie (etap 4)
- Obsługa złego wejścia (litera zamiast liczby, ValueError), try/except (etap 4)
- Dokładniejsze liczenie wieku (czy urodziny już były w tym roku), dziś uproszczone: 2026 - rok
- Formatowanie kodu (spacje wokół operatorów) przejmie ruff (etap 7)
- Uproszczenie podwójnego input() w zgadnij.py, może po poznaniu funkcji (etap 2)

## Proponowane zmiany planu
- Brak. Etapy w PLAN.md zostają bez zmian.

## Decyzje
- Źródło prawdy: docs/ w repo. Aktualizacje wklejam ręcznie po każdym etapie.
- Repo lokalne trzymam poza OneDrive: C:\Users\<nazwa>\python-od-zera
- Praca na 2 komputerach: zaczynam od git pull, kończę git push
- Imię i e-mail w Git ustawiam bez --global, tylko dla tego repo
- Przed commitem zawsze: Ctrl+S, git add, git status, git commit -m "opis co zmieniłem", git push
- Nazwy zmiennych w jednym języku (polskim), komentarze tłumaczą "dlaczego"
