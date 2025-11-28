# Zad. 2.
# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych
# przecinkiem tak jak pokazano poniżej.
# Pamiętaj, że liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne:
# jedynkę i samą siebie.
# W rozwiązaniu użyj pętli while oraz instrukcji break
# Oczekiwany wynik:
# 2,3,5,7,11,13,17,19,23,29

def is_prime(n):
    divider_count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divider_count += 1

        if divider_count > 2:
            break

    return divider_count == 2


numbers = []
current_number = 0

while len(numbers) < 10:
    if is_prime(current_number):
        numbers.append(current_number)

    current_number += 1

print(numbers)