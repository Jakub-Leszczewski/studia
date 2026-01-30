# Zadanie 2. Dla macierzy losowej 6×4 (N(0,1)) znajdź: średnią każdej kolumny, indeksy min/max w
# każdej kolumnie.

import numpy as np

rng = np.random.default_rng(10)
matrix = rng.normal(0,1,(6, 4))

print(matrix)
print()
print(matrix.mean(axis=0))
print(np.argmax(matrix, axis=0))
print(np.argmin(matrix, axis=0))
