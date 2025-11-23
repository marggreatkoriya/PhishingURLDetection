import pandas as pd
from extract_features import extract_all_features

# Load dataset
df = pd.read_csv("dataset.csv")

# Extract features for every URL
rows = []
for index, row in df.iterrows():
    url = row["URL"]
    label = row["label"]

    features = extract_all_features(url)
    features["label"] = label
    rows.append(features)

# Create final DataFrame
final_df = pd.DataFrame(rows)

# Save output
final_df.to_csv("features.csv", index=False)

print("features.csv created successfully!")