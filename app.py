from flask import Flask, request, jsonify
import pandas as pd
import xgboost as xgb
import joblib
import os

app = Flask(__name__)

# Paths to model and encoders
MODEL_PATH = "recall_risk_model_fixed.json"
ENCODERS_PATH = "label_encoders.pkl"

# Load XGBoost model
model = xgb.XGBClassifier(eval_metric="logloss")  # no use_label_encoder
model.load_model(MODEL_PATH)

# Load label encoders
if os.path.exists(ENCODERS_PATH):
    label_encoders = joblib.load(ENCODERS_PATH)
else:
    label_encoders = {}

# Prediction labels
prediction_labels = {0: "Safe", 1: "High Recall Risk"}

@app.route('/')
def home():
    return "Vehicle Recall Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])

        # Encode categorical columns
        for col, le in label_encoders.items():
            if col in df.columns:
                df[col] = df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

        # Ensure all features exist
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0

        df = df[model.feature_names_in_]

        # Predict
        prediction = model.predict(df)[0]
        return jsonify({
            "prediction": int(prediction),
            "label": prediction_labels.get(int(prediction), "Unknown")
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

