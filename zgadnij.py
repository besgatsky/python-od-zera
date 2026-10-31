tajna_liczba = 7
liczba = int(input("podaj liczbe: "))
while liczba != tajna_liczba:
    if liczba < tajna_liczba:
        liczba = int(input("za mało, podaj większą "))
    else:
        liczba = int(input("za dużo, podaj mniejszą "))   
print("Trafiłeś!")