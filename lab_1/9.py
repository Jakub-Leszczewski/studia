def get_valid_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            break
        except:
            print('To nie jest liczba!')

    return value


def get_valid_option() -> int:
    while True:
        try:
            value = int(input('Wybierz operację (1-6): '))

            if value not in range(1, 7):
                raise ValueError

            break
        except:
            print('To nie jest prawidłowa liczba!')

    return value


while True:
    print('\n' * 100)
    print('=' * 20)
    print('Kalkulator')
    print('=' * 20)
    print('1. Dodawanie')
    print('2. Odejmowanie')
    print('3. Mnożenie')
    print('4. Dzielenie')
    print('5. Potęgowanie')
    print('6. Zamknij program')
    print('=' * 20)

    choice = get_valid_option()
    print('=' * 20)

    if choice == 6:
        break

    a = get_valid_number('Podaj liczbę a: ')
    b = get_valid_number('Podaj liczbę b: ')

    if choice == 1:
        print(f'{a} + {b} = {a + b}')
    elif choice == 2:
        print(f'{a} - {b} = {a - b}')
    elif choice == 3:
        print(f'{a} * {b} = {a * b}')
    elif choice == 4:
        if b == 0:
            print('Nie można dzielić przez zero!')
        else:
            print(f'{a} / {b} = {a / b}')
    elif choice == 5:
        print(f'{a}^{b} = {a ** b}')

    print('=' * 20)
    input('Naciśnij dowolny przycisk aby zresetować kalkulator...')


