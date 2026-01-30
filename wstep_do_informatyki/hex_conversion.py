hex_map = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def hex_conversion(number):
    hex_list = []
    current_number = number
    while True:
        hex_list.append(current_number % 16)
        current_number //= 16
        if current_number == 0:
            break



    return hex_list[::-1]

def serialize_hex(hex_arr):
    new_arr = []

    for hex_num in hex_arr:
        new_arr.append(f'{hex_map.get(hex_num, hex_num)}')

    return ''.join(new_arr)

if __name__ == "__main__":
    number = int(input("Podaj liczbę całkowitą: "))
    hex_arr = hex_conversion(number)
    print(serialize_hex(hex_arr))




