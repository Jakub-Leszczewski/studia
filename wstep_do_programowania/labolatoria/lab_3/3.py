# Zad. 3.
# Mając podana listę ulic w danej dzielnicy i wiedząc, że na każdej ulicy znajduje się 5 bloków
# mieszkalnych, a w każdym z nich jest 10 lokali, wypisz listę wszystkich adresów w dzielnicy.
# Lista ulic w dzielnicy:
# • Jagodowa,
# • Lipowa,
# • Kwiatowa,
# • Kasztanowa,

streets = ['Jagodowa', 'Lipowa', 'Kwiatowa', 'Kasztanowa']

for street in streets:
    for building_number in range(5):
        for flat_number in range(10):
            print(f'{street} {building_number + 1}/{flat_number + 1}')