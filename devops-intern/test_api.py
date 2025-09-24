import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model and label encoders
model = joblib.load("recall_risk_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.json

        # Fill missing columns with defaults
        input_data = {
            "Make": data.get("Make", "Unknown"),
            "Model": data.get("Model", "Unknown"),
            "Year": data.get("Year", 2020),
            "Engine_Type": data.get("Engine_Type", "Unknown"),
            "Mileage": data.get("Mileage", 0),
            "Previous_Recalls": data.get("Previous_Recalls", 0),
            "Defect_Type": data.get("Defect_Type", "Unknown"),
            "Recall_Year": data.get("Recall_Year", 2025),
            "Recall_Reason": data.get("Recall_Reason", "Unknown"),
            "Risk_Score": data.get("Risk_Score", 0)  # include if used by model
        }

        # Create DataFrame
        df = pd.DataFrame([input_data])

        # Encode categorical columns
        for col in label_encoders.keys():
            if col in df.columns:
                le = label_encoders[col]
                df[col] = df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

        # Predict
        prediction = model.predict(df)

        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("Vehicle Recall Prediction API is running!")
    app.run(debug=True)
