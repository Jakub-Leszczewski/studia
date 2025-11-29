# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
# alfabetycznej, a następnie wypisz te litery, których to zdanie nie zawiera.

alphabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
text = input('Podaj zdanie: ')
text_letters = set(text.lower())
sorted_text_letters = [letter for letter in sorted(text_letters) if letter.strip()]
print(sorted_text_letters)

not_used_letters = []
for letter in alphabet:
    if letter not in text_letters:
        not_used_letters.append(letter)

print(not_used_letters)
