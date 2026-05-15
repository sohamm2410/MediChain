import pandas as pd

df = pd.read_csv("datasets/clinical_notes.csv")

print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nDisease Categories:")
print(df["disease"].unique())