import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load processed feature dataset
df = pd.read_csv("features.csv")

# Separate features and labels
X = df.drop(columns=['label'])
y = df['label']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the Random Forest model
model = RandomForestClassifier(n_estimators=300, random_state=42)

# Train
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "phishing_model.pkl")
print("Model saved as phishing_model.pkl")