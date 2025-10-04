FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Explicitly copy model files (optional but safe)
COPY recall_risk_model_fixed.json /app/recall_risk_model_fixed.json
COPY label_encoders.pkl /app/label_encoders.pkl

EXPOSE 5000

CMD ["python3", "app.py"]

