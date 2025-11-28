# Zad. 1
# Napisz program, który będzie kontrolować zużycie paliwa w samolocie. Przed rozpoczęciem każdej
# jednostki czasu wydrukuj do konsoli informację o pozostałych jednostkach paliwa. Gdy paliwo
# zostanie wyczerpane, wydrukuj do konsoli informacje 'Konie lotu.'.
# Masz do dyspozycji następujące dane.:
# • ilość paliwa w samolocie w litrach
# • ilość paliwa zużywanego na sekundę w litrach
# • czas lotu w sekunadach
# Wartości początkowe:
# • paliwo = 100
# • paliwo_zużyte_na_s = 10
# • czas = 0

paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f'Pozostałe paliwo: {paliwo}')

    czas += 1
    paliwo -= paliwo_zużyte_na_s

print('Koniec lotu.')


