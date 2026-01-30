# Napisz funkcję sum_digits(n), która oblicza sumę cyfr liczby rekurencyjnie. Napisz dokumentacje tej
# funkcji, która opisywać będzie jej działanie.

def sum_digits(n: int):
    return n if n < 10 else n % 10 + sum_digits(n // 10)

# 123 -> 3 + sum_digits(12)
# 12 -> 2 + sum_digits(1)
# 1 -> 1

print(sum_digits(1234))