import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Make": "Toyota",
    "Model": "Corolla",
    "Engine_Type": "Petrol",
    "Defect_Type": "Brake",
    "Recall_Reason": "Safety"
}

response = requests.post(url, json=data)
print(response.json())
