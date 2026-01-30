import pandas as pd

data = pd.read_csv('./data/dane.csv', sep=';')
data['Marża'] = (data['Sprzedaż'] - data['Koszt']) / data['Sprzedaż']
data_sorted = data.sort_values(by=['Rok', 'Kraj'], ascending=[True, True])
print(data_sorted)
result = data_sorted[(data_sorted['Kraj'] == 'DE') & (data_sorted['Rok'] >= 2023)][['Sprzedaż', 'Marża']]
print(result)