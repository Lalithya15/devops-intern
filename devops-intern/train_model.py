import pandas as pd
import xgboost as xgb
import joblib
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("vehicle_data.csv")

# Features and target
X = df.drop("Recall_Flag", axis=1)
y = df["Recall_Flag"]

# Encode categorical columns
label_encoders = {}
for col in X.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Train XGBoost model
model = xgb.XGBClassifier(eval_metric="logloss")  # no use_label_encoder
model.fit(X, y)

# Save model in JSON format
model.get_booster().save_model("recall_risk_model_fixed.json")

# Save label encoders
joblib.dump(label_encoders, "label_encoders.pkl")

print("Model and encoders saved!")

