# Zad 4. dodatkowe
# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości, za
# każdym razem wskazuje użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości.

number_of_dishes = int(input('Podaj liczbę potraw: '))
number_of_friends = int(input('Podaj liczbę przyjaciół: '))
total_price = 0.0

for i in range(number_of_dishes):
    total_price += float(input(f'Podaj kwotę potrawy nr {i + 1}: '))

price_per_friend = total_price/number_of_friends
print(f'Kwota na gościa to: {price_per_friend:.0f}')