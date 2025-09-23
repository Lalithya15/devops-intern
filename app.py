from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoders
model = joblib.load("recall_risk_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Define mapping for prediction labels
prediction_labels = {0: "Safe", 1: "High Recall Risk"}

@app.route('/')
def home():
    return "Vehicle Recall Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Encode categorical columns
        for col in label_encoders.keys():
            if col in df.columns:
                le = label_encoders[col]
                df[col] = df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

        # Ensure all expected columns exist
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0  # placeholder for missing columns

        # Reorder columns
        df = df[model.feature_names_in_]

        # Make prediction
        prediction = model.predict(df)[0]
        response = {
            "prediction": int(prediction),
            "label": prediction_labels.get(int(prediction), "Unknown")
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
