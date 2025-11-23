import joblib
from extract_features import extract_all_features
import pandas as pd

# Load trained model
model = joblib.load("phishing_model.pkl")

# Ask user for URL
user_url = input("Enter a URL to check: ")

# Extract same features as training
features = extract_all_features(user_url)

# Convert dictionary → DataFrame
features_df = pd.DataFrame([features])

# Predict
prediction = model.predict(features_df)[0]

# Print result
if prediction == "phishing":
    print("⚠ This URL is likely PHISHING!")
else:
    print("✅ This URL seems SAFE.")