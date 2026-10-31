# Postęp

## Aktualny etap
Etap 0: zaliczony (bramka przeszła)
Następny: Etap 1 (podstawy: zmienne, typy, warunki, pętle), jeszcze nie rozpoczęty

## Zrobione
- Uzupełniony profil w PLAN.md: Windows, 3 godziny tygodniowo
- Zainstalowany Python 3.15.2 (z opcją "Add python.exe to PATH")
- Zainstalowany VS Code z rozszerzeniem Python (Microsoft)
- Zainstalowany Git 2.56.0 (domyślny edytor: VS Code, backend HTTPS: Windows Secure Channel)
- Repo sklonowane lokalnie (poza OneDrive) na obu komputerach
- Imię i e-mail w Git ustawione tylko dla tego repo (bez --global)
- Pierwszy program: hello.py (wypisuje kilka linijek przez print)
- Pierwsze commity z kodem i README, wysłane na GitHuba
- Obieg między dwoma komputerami sprawdzony: commit i push na jednym, pull na drugim
- README.md napisany własnymi słowami

## Poznane pojęcia
- PATH: lista folderów, w których Windows szuka programów po nazwie
- print(): wbudowana funkcja wypisująca tekst na ekranie
- Plik .py: kod w Pythonie, uruchamiany przez `python nazwa.py`
- Markdown (.md): tekst z prostym formatowaniem (# nagłówek, bloki kodu)
- Git a GitHub: Git działa lokalnie, GitHub to wspólne miejsce w internecie
- Cykl pracy: git add (do paczki) -> git commit -m "opis" (zatwierdzenie lokalne) -> git push (wysłanie na GitHuba)
- git status: pokazuje, co jest zmienione, w paczce i niewysłane
- Stany pliku: untracked, modified, staged ("Changes to be committed")
- Commit zapisuje to, co jest na dysku, nie to, co widać w oknie edytora (trzeba zapisać Ctrl+S)
- "no changes added to commit": zapomniane git add (albo niezapisany plik)
- git clone: pobranie całego repo z GitHuba
- git pull: pobranie i wciągnięcie zmian z GitHuba; git fetch tylko sprawdza, co nowego
- Zasada pracy na 2 komputerach: zaczynam od pulla, kończę pushem
- Dobry opis commita mówi, co zmieniłem (nie "poprawki")
- Git i OneDrive nie współpracują dobrze, repo trzymamy poza OneDrive

## Otwarte pytania
- Czy laptop jest używany także do pracy zawodowej na tym samym koncie Windows? (od tego zależy, czy ustawienia Gita muszą zostać tylko lokalne dla repo)

## Backlog (pytania i pomysły na później)
- Dlaczego Git i OneDrive się gryzą; czym jest ukryty folder .git
- Konflikty przy pracy na 2 komputerach (etap 3)
- fetch vs pull, dokładniej (etap 3)
- Ścieżki względne zamiast bezwzględnych w kodzie (etap 4)

## Proponowane zmiany planu
- Brak. Etapy w PLAN.md zostają bez zmian (profil w PLAN.md już uzupełniony).

## Decyzje
- Źródło prawdy: docs/ w repo. Aktualizacje wklejam ręcznie po każdym etapie.
- Repo lokalne trzymam poza OneDrive: C:\Users\<nazwa>\python-od-zera
- Praca na 2 komputerach: zaczynam od git pull, kończę git push
- Imię i e-mail w Git ustawiam bez --global, tylko dla tego repo
