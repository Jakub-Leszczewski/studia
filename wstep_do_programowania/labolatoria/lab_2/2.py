# Zad. 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia
# wbudowanych funkcji

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
z = int(input('Podaj z: '))

def bubble_sort(array: list[float]):
    new_array = array.copy()
    is_changed = True

    while is_changed:
        is_changed = False

        for j in range(len(new_array) - 1):
            if new_array[j] > new_array[j + 1]:
                new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]
                is_changed = True

    return new_array


print(bubble_sort([x, y, z]))


# if x < y and x < z:
#     if y <= z:
#         print(x, y, z)
#     else:
#         print(x, z, y)
# elif y < x and y < z:
#     if x <= z:
#         print(y, x, z)
#     else:
#         print(y, z, x)
# elif z < x and z < y:
#     if x <= y:
#         print(z, x, y)
#     elif y <= x:
#         print(z, y, x)



