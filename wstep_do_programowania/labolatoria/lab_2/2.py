# Zad. 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
z = int(input('Podaj z: '))

if x > y and x > z:
    if y >= z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y > x and y > z:
    if x >= z:
        print(y, x, z)
    else:
        print(y, z, x)
elif z > x and z > y:
    if x >= y:
        print(z, x, y)
    elif y >= x:
        print(z, y, x)



