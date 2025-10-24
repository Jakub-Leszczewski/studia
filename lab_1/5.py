def get_valid_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            break
        except:
            print('To nie jest liczba!')

    return value


a = get_valid_number('Podaj bok a: ')
b = get_valid_number('Podaj bok b: ')

perimeter = 2 * (a + b)
area = a * b

print(f'Pole: {perimeter}')
print(f'Obwod: {area}')
