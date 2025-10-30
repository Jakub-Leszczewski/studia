# a)
# Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek.
# Wydrukuj każdą linię do konsoli.
# b)
# Dopisz do pliku notwania_gieldowe.txt, w kolejnej linii dane dotyczące nowej spółki: ALR, 113.
# Wydrukuj każdą linię ponownie do konsoli.

with open("./data/notowania_gieldowe.txt", "r") as plik:
    elements = list(map(lambda x: x.replace('\n', ''), plik.readlines()))

    for element in elements:
        print(element)


with open("./data/notowania_gieldowe.txt", "a") as plik:
    # print('\nALR, 113', file=plik)
    plik.write('\nALR, 113')