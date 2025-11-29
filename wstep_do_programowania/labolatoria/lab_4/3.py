print('\n === a ===')
imię = input('Podaj imię: ')
print(f'Witaj {imię}')

print('\n === b ===')
wiek = input('Podaj wiek: ')
print(f'Twój wiek to: {wiek}')

print('\n === c ===')
nazwisko = input('Podaj nazwisko: ')
print(f'{imię[0].upper()}{nazwisko[0].upper()}')

print('\n === d ===')
tekst = input('Podaj teskt: ')
for i in range(5):
    print(tekst)

print('\n === e ===')
tekst1 = input('Podaj tekst1: ')
tekst2 = input('Podaj tekst2: ')
tekst3 = tekst1 + tekst2
print(tekst3)

print('\n === f ===')
tekst4 = input('Podaj tekst4: ')
tekst5 = input('Podaj tekst5: ')
tekst6 = tekst4 + tekst5
tekst6 = tekst6[:len(tekst6)//2]

print(tekst6)