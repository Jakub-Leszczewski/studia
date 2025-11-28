# Zad. 8
# Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
# • Zerowym
# • Ostatnim
# • Co drugi, zaczynając od zerowego
# • Co trzeci zaczynając od pierwszego
# • Od dziesiątego do ostatniego
# • Wyświetl od końca do początku

tekst ="Python jest super"
print(tekst[0])
print(tekst[-1])
print(tekst[::2])
print(tekst[1::3])
print(tekst[10:len(tekst)])
print(tekst[::-1])