# Utwórz listę: Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21], przetestuj działanie wszystkich
# zaprezentowanych operacji na listach, a ich wynik wyświetl w konsoli.

Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print('\n==== Pierwszy element ====')
print(Moja_lista[0])

print('\n==== Ostatni element ====')
print(Moja_lista[-1])

print('\n==== Długość listy ====')
print(len(Moja_lista))

print('\n==== Maksymalny element ====')
print(max(Moja_lista))

print('\n==== Minimalny element ====')
print(min(Moja_lista))

print('\n=== Suma wszystkich elementów ====')
print(sum(Moja_lista))

print('\n==== Lista posortowana ====')
print(sorted(Moja_lista))


print('\n==== Dodawanie na końcu listy ====')
print('Przed', Moja_lista)
Moja_lista.append(6)
print('Po', Moja_lista)

print('\nDodawanie w środku elementu ====')
print('Przed', Moja_lista)
Moja_lista.insert(3, 100)
print('Po', Moja_lista)

print('\n==== Usuwanie ostatniego elementu ====')
print('Przed', Moja_lista)
print(Moja_lista.pop())
print('Po', Moja_lista)

print('\n==== Odwrotna lista ====')
print('Przed', Moja_lista)
Moja_lista.reverse()
print('Po', Moja_lista)

print('\n=== Dodawanie listy ====')
Moja_lista_2 = [1,2,3]
new_list = Moja_lista + Moja_lista_2
print('Lista 1', Moja_lista)
print('Lista 2', Moja_lista_2)
print('Nowa lista', new_list)

print('=== Mnożenie listy ====')
print('Lista', Moja_lista)
new_list_2 = Moja_lista * 3
print('Lista * 3', new_list_2)

print('==== Wycinanie elementów z listy ====')
print('Pierwotna lista: ', Moja_lista)
print('5 pierwszych elementów: ', Moja_lista[:5])
print('Pobieranie od 3 elementu włącznie: ', Moja_lista[2:])
print('Pobieranie od 2 włącznie do 7 elementu, co drugi:', Moja_lista[1:7:2])
print('Lista od końca: ', Moja_lista[::-1])