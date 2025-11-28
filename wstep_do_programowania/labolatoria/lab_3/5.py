# Zad. 5
# Napisz kod, który generuje listę liczb zmniejszających się o 4, zaczynając od 80 i kończąc w 0.

numbers = []
for i in range(80, -1, -4):
    numbers.append(i)

print(numbers)