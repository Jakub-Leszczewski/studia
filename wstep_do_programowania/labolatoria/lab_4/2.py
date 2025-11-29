names = ['Jakub', 'Dominik', 'Tomek', 'Piotr']
print('Przed sortowanie', names)

names = sorted(names)
print('Po sortowaniu', names)

names.extend(['Rafał', 'Krzysztof'])
print('Po dodaniu 2 elementów', names)
print('Rezultat pop', names.pop())
print('Lista po pop', names)

names.insert(2, 'Marek')
print('Po wstawieniu elementu w środku', names)

names.reverse()
print('Po odwróceniu', names)

