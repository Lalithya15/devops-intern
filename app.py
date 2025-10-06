from flask import Flask, request, jsonify
import pandas as pd
import xgboost as xgb
import joblib
import os
import warnings
import logging
from sklearn.preprocessing import LabelEncoder

# Ignore XGBoost UserWarnings
warnings.filterwarnings("ignore", category=UserWarning, module='xgboost')

# Configure logging
logging.basicConfig(
    filename='api.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

app = Flask(__name__)

# Paths to model and encoders
MODEL_PATH = "recall_risk_model_fixed.json"
ENCODERS_PATH = "label_encoders.pkl"

# Load XGBoost model
model = xgb.XGBClassifier(eval_metric="logloss")  # no use_label_encoder needed
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

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logging.info(f"Received request: {data}")  # Log input

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
        response = {
            "prediction": int(prediction),
            "label": prediction_labels.get(int(prediction), "Unknown")
        }

        logging.info(f"Response: {response}")  # Log output
        return jsonify(response)

    except Exception as e:
        logging.error(f"Error: {str(e)}")  # Log errors
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Run with 1 worker and higher timeout in Docker CMD instead of here
    app.run(debug=False,host='0.0.0.0', port=5000)

