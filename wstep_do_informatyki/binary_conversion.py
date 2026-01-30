def binary_conversion(number):
    binary_list = []
    current_number = number
    while True:
        binary_list.append(current_number % 2)
        current_number //= 2
        if current_number == 0:
            break

    return binary_list[::-1]

if __name__ == "__main__":
    number = int(input("Podaj liczbę całkowitą: "))
    print(binary_conversion(number))