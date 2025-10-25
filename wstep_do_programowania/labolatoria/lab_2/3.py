# Zad. 3
# Zmienna Nazwa
# _pliku przechowującej jego nazwę.
# Sprawdź, czy plik o podanej nazwie jest z rozszerzeniem '.xlsx'.
# Nazwa_pliku= 'Raport_maj.xlsx'
# Wydrukuj do konsoli 'Tak' jeśli to prawda, przeciwnie 'Nie'.
# Podpowiedz:
# Skorzystaj z metody endswith (jest to metodą wbudowaną dla obiektów typu str w Pythonie),
# sprawdza ona, czy ciąg znaków (Nazwa_pliku) kończy się podanym sufiksem (w tym przypadku
# '.xlsx').

Nazwa_pliku = 'Raport_maj.xlsx'

if Nazwa_pliku.endswith('.xlsx'):
    print('Tak')
else:
    print('Nie')