import joblib

# Load the label encoders
label_encoders = joblib.load("label_encoders.pkl")

# Print all available keys
print("Columns stored in label_encoders:", list(label_encoders.keys()))
