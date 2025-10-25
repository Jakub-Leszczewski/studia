# Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest
# duża czy mała

letter = input('Podaj literę: ')

if letter.isupper():
    print('Litera jest duża')
else:
    print('Litera jest mała')