imie = input("Jak masz na imie? ")
rok_urodzenia = int(input("w którym roku się urodziłeś? "))  # input() zwraca tekst, więc zamieniam na liczbę, żeby móc odejmować
wiek = 2026 - rok_urodzenia
print(imie,"masz",wiek,"lat")