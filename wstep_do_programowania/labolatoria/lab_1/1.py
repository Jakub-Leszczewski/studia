'''
ex. A
'''
print('=' * 10, ' A ', '=' * 10)

sumInt = 1 + 2
print('1. ', sumInt, type(sumInt))

sumFloat = 1 + 4.5
print('2. ', sumFloat, type(sumFloat))

divFloat = 3 / 2
print('3. ', divFloat, type(divFloat))

divInt = 4 / 2
print('4. ', divInt, type(divInt))

divIntFloor = 3 // 2
print('5. ', divIntFloor, type(divIntFloor))

divIntFloorNeg = -3 // 2
print('6. ', divIntFloorNeg, type(divIntFloorNeg))

modInt = 11 % 2
print('7. ', modInt, type(modInt))

powInt = 2 ** 10
print('8. ', powInt, type(powInt))

powFloat = 8 ** (1/3)
print('9. ', powFloat, type(powFloat))

'''
ex. B
'''
print('\n')
print('=' * 10, ' B ', '=' * 10)

print('1. ', 3.0, type(3.0), '->', int(3.0), type(int(3.0)))
print('2. ', 3, type(3), '->', float(3), type(float(3)))
print('3. ', "3", type("3"), '->', float("3"), type(float("3")))
print('4. ', 12.4, type(12.4), '->', str(12.4), type(str(12.4)))
print('5. ', 0, type(0), '->', bool(0), type(bool(0)))
