# b)
with open('notowania_gieldowe.txt','a') as plik:
    plik.write("\nALR, 113")
with open('notowania_gieldowe.txt','r') as plik:
    for line in plik:
        print(line, end="")