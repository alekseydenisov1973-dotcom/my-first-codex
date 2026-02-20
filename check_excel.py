import pandas as pd

path = "rbc500_500_kompaniy_rf (1).xlsx"
df = pd.read_excel(path)

print("OK. Rows:", len(df), "Cols:", len(df.columns))
print("Columns:", list(df.columns))
print(df.head(3))
