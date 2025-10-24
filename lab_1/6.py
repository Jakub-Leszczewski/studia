# import random
#
# def get_valid_boolean(prompt: str) -> bool:
#     while True:
#         value = input(prompt)
#
#         if value.lower() in ['yes', 'y']:
#             value = True
#             break
#
#         elif value.lower() in ['no', 'n']:
#             value = False
#             break
#         else:
#             print('Nieprawidłowa wartość! Wpisz y/n')
#
#     return value
#
#
# def get_valid_number(prompt: str) -> float:
#     while True:
#         try:
#             value = float(input(prompt))
#             break
#         except:
#             print('To nie jest liczba!')
#
#     return value
#
#
# is_random = get_valid_boolean('Czy dystans jest losowy? (y/n): ')
#
# distance = (
#     random.randint(1, 1000) if is_random
#     else get_valid_number('Podaj pokonany dystans(km): ')
# )
# fuel_consumption = get_valid_number('Podaj średnie spalanie(l/100km): ')
# gas_price = 6.5
#
# total_fuel_consumption = distance / 100 * fuel_consumption
# total_cost = total_fuel_consumption * gas_price
#
# print('\n')
# print('=' * 10)
#
# print(f'Dystans: {distance} km')
# print(f'Średnie spalanie: {fuel_consumption} l/100km')
# print(f'Koszt paliwa: {gas_price} PLN/l')
#
# print('\n')
#
# print(f'Zużycie paliwa: {fuel_consumption:.2f} l')
# print(f'Szacowane koszty: {total_cost:.2f} PLN')

import random

def get_valid_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            break
        except:
            print('To nie jest liczba!')

    return value


distance = random.randint(1, 1000)
fuel_consumption = get_valid_number('Podaj średnie spalanie(l/100km): ')
gas_price = 6.5

total_fuel_consumption = distance / 100 * fuel_consumption
total_cost = total_fuel_consumption * gas_price

print('\n')
print('=' * 10)

print(f'Dystans: {distance} km')
print(f'Średnie spalanie: {fuel_consumption} l/100km')
print(f'Koszt paliwa: {gas_price} PLN/l')

print('\n')

print(f'Zużycie paliwa: {fuel_consumption:.2f} l')
print(f'Szacowane koszty: {total_cost:.2f} PLN')