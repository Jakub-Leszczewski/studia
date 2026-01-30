# Napisz funkcję, która oblicza pierwiastki funkcji kwadratowej. Funkcja przyjmuje argumenty a,b,c,
# które są współczynnikami funkcji kwadratowej. Dla a=0, napisz wyjątek, gdy funkcja nie jest
# kwadratowa. Skorzystaj z biblioteki math. Napisz dokumentację tej funkcji, kiedy jest co obliczane itp.
import math

def quadratic_equation(a: float, b: float, c: float) -> tuple[float, float | None]:
    '''
        Funkcja oblicza pierwiastki kwadratowe funkcji kwadratowej o współczynnikach a, b, c.
        Zwraca pierwszy lub pierwszy i drugi pierwiastek funkcji w formie krotki. Jeśli funkcja
        ma tylko jeden pierwiastek, to druga wartość krotki to None.

        Parametry:
        a (float): Współczynnik a funkcji. Nie może być równy 0.
        b (float): Współczynnik b funkcji
        c (float): Współczynnik c funkcji
    '''

    if a == 0:
        raise ValueError('a nie może być równe 0')

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        raise ValueError('Funkcja nie jest kwadratowa!')

    if delta == 0:
        return -b / (2 * a), None

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2


print(quadratic_equation(2, 10, 0))
print(quadratic_equation(1, 0, 0))
print(quadratic_equation(1, 0, 1))