import pandas as pd
import numpy as np

# --- Twój kod generujący dane ---
rng = np.random.default_rng(42)
dates = pd.date_range("2024-01-01", periods=120, freq="D")
kraj = rng.choice(["PL", "DE", "US"], size=len(dates))
sprzedaz = rng.integers(50, 250, size=len(dates))
koszt = sprzedaz * rng.uniform(0.4, 0.8, size=len(dates))
produkt = rng.choice(["A", "B", "C"], size=len(dates))
df = pd.DataFrame({
"Data": dates,
"Kraj": kraj,
"Produkt": produkt,
"Sprzedaż": sprzedaz,
"Koszt": np.round(koszt, 2),
"Waluta": "PLN"
})

df.head()

df['Marża'] = np.where(df['Sprzedaż'] == 0, 0, (df['Sprzedaż'] - df['Koszt']) / df['Sprzedaż'])
df['Rok'] = df['Data'].dt.year

print(df[(df['Kraj'] == 'PL') & (df['Produkt'] == 'A')])
print('\n', '='*10, '\n')
print(df.groupby('Kraj')['Sprzedaż'].sum().sort_values(ascending=False))
print('\n', '='*10, '\n')
print(df.groupby('Kraj', group_keys=False).apply(lambda g: g.nlargest(20, 'Marża')))