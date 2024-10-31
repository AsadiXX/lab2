litera = input("Wprowadź literę: ")
#Sprawdzenie czy wprowadzony zank jest literą
if litera.isalpha() and len(litera) == 1:
    #Sprawdzenie czy litera jest wielka
    if litera.isupper():
        print(f"Litera {litera} jest dużą literą")
    #Sprawdzenie czy litera jest mała
    elif litera.islower():
        print(f"Litera {litera} jest małą literą")
else:
    print("Wprowadzony znak nie jest pojedynczą literą")