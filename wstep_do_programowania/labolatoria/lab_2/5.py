with open("./data/notowania_gieldowe.txt", "r") as plik:
    elements = list(map(lambda x: x.replace('\n', ''), plik.readlines()))

    for element in elements:
        print(element)


with open("./data/notowania_gieldowe.txt", "a") as plik:
    plik.write('\nALR, 113')
    # for i in range(10):
    #     print(f'data {i}', file=plik)