# Zad 1.
# Napisz prosty program, który na podstawie podanej przez Studenta liczby zdobytych punktów,
# poinformuje go o rezultacie egzaminu.
# Każdy Student, który zdobył powyżej 80 punktów zalicza egzamin w terminie 0
# Studenci którzy otrzymali liczbę punków z przedziału 50-80, mogą poprawić jego wynik.
# Studenci, którzy zdobyli poniżej 50 punktów, muszą go poprawić.

points = int(input('Podaj liczbę punktów: '))

if points > 80:
    print('Zaliczyłeś egzamin w terminie 0.')
elif 50 <= points <= 80:
    print('Możesz poprawić wynik egzaminu.')
else:
    print('Musisz poprawić egzamin.')

