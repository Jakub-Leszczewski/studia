# Zad. 4 dodatkowe
# Jesteś menagerem drużyny piłkarskiej i chcesz obliczyć łączny wynik drużyny na podstawie liczby
# strzelonych przez nią bramek i ewentualnie zdobytych dodatkowych punktów. Napisz program,
# który dokona stosownych kalkulacji po wprowadzeniu liczby goli zdobytych przez drużynę.
# Utworzone są dwie zmienne gol i bonus, gdzie gol to liczba całkowita reprezentująca liczbę
# bramek zdobytych przez drużynę, a bonus to liczba całkowita reprezentująca wszelkie możliwe
# punkty bonusowe dla drużyny.
# Następnie użyj instrukcji warunkowej do obliczenia całkowitego wyniku zespołu zgodnie z
# następującymi zasadami:
# - każda zdobyta bramka to 10 punktów,
# - jeśli drużyna zdobędzie więcej niż 5 bramek, zdobywa dodatkowe 5 punktów bonusowych,
# - jeśli drużyna zdobędzie więcej niż 10 bramek, zdobywa dodatkowe 10 punktów bonusowych
# a) Po zdobyciu 5 goli drużyna otrzymuje 5 punktów bonusowych. Jeśli drużyna zdobędzie więcej
# niż 10 goli, to otrzyma za nie 10 punktów bonusowych dodatkowo
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie
# stosowne punkty bonusowe. Wynik wydrukuj do konsoli.
# b) Punkty bonusowe po przekroczeniu 5 i 10 punktów są sumowane, tzn. po przekroczeniu więcej
# niż 10 bramek drużyna zdobywa obydwa bonusy.
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie
# stosowne punkty bonusowe. Wynik wydrukuj do konsoli.

gol_multiplier = 10
five_gol_bonus = 5
ten_gol_bonus = 10
gol = int(input('Zdobyte bramki: '))
total_points = gol * gol_multiplier

if gol > 5:
    total_points += five_gol_bonus
    if gol > 10:
        total_points += ten_gol_bonus

print(f'Punkty drużyny: {total_points}')

# # b
# gol_multiplier = 10
# five_gol_bonus = 5
# ten_gol_bonus = 10
# gol = int(input('Zdobyte bramki: '))
# total_points = gol * gol_multiplier
#
# if gol > 5:
#     total_points += five_gol_bonus
# if gol > 10:
#     total_points += ten_gol_bonus
#
# print(f'Punkty drużyny: {total_points}')




