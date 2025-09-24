import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib

# Load dataset
df = pd.read_csv("vehicle_data.csv")  # replace with your CSV path

# Features and target
X = df.drop(["Vehicle_ID", "Recall_Flag"], axis=1)
y = df["Recall_Flag"]

# Encode categorical columns
label_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "recall_risk_model_fixed.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("Model and encoders saved successfully.")

