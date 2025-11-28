# Zad. 9
# Napisz programy, które:
# • Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# • Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany
# wiek.
# • Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# • Wczyta łańcuch i wyświetli go pięć razy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa
# łańcuchy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę

imię = input('Podaj imię: ')
print(f'Witaj {imię}')

wiek = input('Podaj wiek: ')
print(f'Twój wiek to: {wiek}')

nazwisko = input('Podaj nazwisko: ')
print(f'{imię[0].upper()}{nazwisko[0].upper()}')

tekst = input('Podaj teskt: ')
for i in range(5):
    print(tekst)

tekst1 = input('Podaj tekst1: ')
tekst2 = input('Podaj tekst2: ')
tekst3 = tekst1 + tekst2
print(tekst3)

tekst4 = input('Podaj tekst4: ')
tekst5 = input('Podaj tekst5: ')
tekst6 = tekst4 + tekst5
tekst6 = tekst6[0: len(tekst6)//2]

print(tekst6)

