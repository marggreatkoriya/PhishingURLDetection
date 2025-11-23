import pandas as pd

# Load your existing dataset
df = pd.read_csv("dataset.csv")

print("Dataset loaded successfully!")
print(df.head())
print("\nTotal rows:", len(df))
print("Columns:", df.columns)