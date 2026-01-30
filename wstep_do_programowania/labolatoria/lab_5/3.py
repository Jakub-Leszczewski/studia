# Napisz funkcję, która zwraca listę tylko z liczbami parzystymi. Funkcja przyjmuje dowolną ilość
# argumentów. Wykorzystaj funkcję filter oraz lambda.

def filter_even_numbers(*numbers: int) :
    return list(filter(lambda x: x % 2 == 0, numbers))

print(filter_even_numbers(1, 2, 3, 4, 5))