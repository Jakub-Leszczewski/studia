import math


def get_valid_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            break
        except:
            print('To nie jest liczba!')

    return value


def calculate_linear_equation(a: float, b: float) -> float | None:
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


def calculate_delta(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def calculate_quadratic_equation(a: float, b: float, c: float) -> tuple[float, float] | tuple[float] | None:
    delta = calculate_delta(a, b, c)

    if delta < 0:
        return None

    if delta == 0:
        x = -b / (2 * a)
        return (x,)

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


def format_quadratic_equation_result(result: tuple[float, float] | tuple[float] | None):
    if type(result) == tuple and len(result) == 1:
        return f'x = {result[0]}'

    if type(result) == tuple and len(result) == 2:
        return f'x1 = {result[0]}, x2 = {result[1]}'

    return 'Brak rozwiązań'


a = get_valid_number('Podaj a: ')
b = get_valid_number('Podaj b: ')
c = get_valid_number('Podaj c: ')

if a == 0:
    x = calculate_linear_equation(b, c)
    print(format_linear_equation_result(x))

result = calculate_quadratic_equation(a, b, c)
print(format_quadratic_equation_result(result))