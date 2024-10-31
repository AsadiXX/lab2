x = float(input("Podaj lcizbę x: "))
y = float(input("Podaj lcizbę y: "))
z = float(input("Podaj lcizbę z: "))

if x > y:
    x,y=y,x
if y > z:
    x,z=z,x
if y>z:
    y,z=z,y
print(f"Liczbyw kolejności rosnącej: {x}, {y}, {z}")