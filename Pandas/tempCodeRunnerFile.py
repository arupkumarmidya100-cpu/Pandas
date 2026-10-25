
import pandas as pd

df = pd.read_excel("CodeVoyage_finalist.xlsx", header=7)

print(df.to_string())