# ax+b = 0 /-b
# ax = -b / :a
# x = -b / a
import math


def get_valid_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            break
        except:
            print('To nie jest liczba!')

    return value


def calculate_linear_equation(a: float, b: float):
    if a != 0:
        return -b / a

    if b == 0:
        return math.inf

    return None


def format_linear_equation_result(result: float | None) -> str:
    if result is not None and result != math.inf:
        return f'x = {result}'

    if type(result) == float and result == math.inf:
        return 'Nieskończenie wiele rozwiązań.'

    return 'Równanie sprzeczne.'

a = get_valid_number('Podaj a: ')
b = get_valid_number('Podaj b: ')
result = calculate_linear_equation(a, b)

print(format_linear_equation_result(result))