# Zadanie 1. Stwórz tablicę 5x5 (wartości od 0 do 24) oraz wyciągnij z niej obramowanie (pierwszy/
# ostatni wiersz i kolumna).

import numpy as np

array = np.arange(25).reshape(5, 5)

print(array)
print()
print(array[0,:5])
print(array[-1,:5])
print(array[:5, 0])
print(array[:5,-1])
