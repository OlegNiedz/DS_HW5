import pandas as pd

# Przykładowy DataFrame
data = {
    "Kolumna1": ["10", "20", "30"],
    "Kolumna2": ["40", "50", "60"],
    "Kolumna3": ["70", "80", "90"],
}

df = pd.DataFrame(data)

# Zamiana wszystkich kolumn na numeryczne
df = df.apply(pd.to_numeric, errors="coerce")

# Wyświetlenie DataFrame po zmianie
print(df)
