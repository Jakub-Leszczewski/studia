# Zad. 7 dodatkowe
# A)
# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy liczbę
# punktów dla każdego studenta.
# Napisz program, który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while.
# Zastosuj instrukcje continue w programie tak, aby po podaniu liczby punktów spoza przedziału 0 –
# 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu.
# B)
# Następnie zmień pętlę na nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ
# działanie pętli przy użyciu instrukcji break.
# Obie wersje zadnia proszę zamieścić w sprawozdaniu.

# students_count = int(input('Podaj liczbę studentów: '))
# total_points = 0
#
# i = 0
# while i < students_count:
#     points = int(input(f'Podaj punkty dla studenta nr {i + 1}: '))
#
#     if points < 0 or points > 100:
#         continue
#
#     total_points += points
#     i += 1
#
# avg_points = total_points / students_count
# print(f'Średnia liczba punktów w grupie: {avg_points}')


students_count = int(input('Podaj liczbę studentów: '))
total_points = 0

i = 0
while True:
    if i == students_count:
        break

    points = int(input(f'Podaj punkty dla studenta nr {i + 1}: '))

    if points < 0 or points > 100:
        continue

    total_points += points
    i += 1

avg_points = total_points / students_count
print(f'Średnia liczba punktów w grupie: {avg_points}')

