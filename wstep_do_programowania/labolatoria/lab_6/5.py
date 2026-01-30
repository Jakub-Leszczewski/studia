# Zadanie 1. Wczytaj plik CSV. Dodaj kolumnę marża = (sprzedaż - koszt) / sprzedaż. Posortuj po rok i po
# kraj rosnąco.

import pandas as pd

data = pd.read_csv('./data/dane.csv', sep=';')
data['Marża'] = (data['Sprzedaż'] - data['Koszt']) / data['Sprzedaż']
data_sorted = data.sort_values(by=['Rok', 'Kraj'], ascending=[True, True])

print(data_sorted.head())