liczba_punktow = float(input("Podaj liczbę punktów zdobytych z egzaminu: "))
if liczba_punktow >= 80:
    print("Egzamin zaliczony w terminie 0")
elif liczba_punktow < 80 and liczba_punktow >= 50:
    print("Egzamin zaliczony, lecz można poprawić wynik")
else:
    print("Egzamin niezaliczony")