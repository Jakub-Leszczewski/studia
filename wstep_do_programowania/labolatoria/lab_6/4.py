# Zadanie 4. Utwórz dwie tablice rozmiaru A = (2,3) oraz B = (3,2). Oblicz iloczyn skalarny tych tablic
# (A@B oraz B@A). Następnie zmień rozmiar tablicy B na (3,3). Czy mnożenia się udały? Jeżeli nie, to
# dlaczego?

import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(1, 7).reshape(3, 2)

print(a @ b)
print(b @ a)
print()

b = np.ones((3, 3))

try:
    print(a @ b)
    print(b @ a)
except ValueError as e:
    print(e)
# mnożenie b@a się nie udało, ponieważ liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy

