FROM python:3.11-slim

WORKDIR /app

# Install dependencies
# 1. Copy dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly copy model files immediately after dependencies
# This ensures these critical files are copied before general project files
COPY recall_risk_model_fixed.json /app/
COPY label_encoders.pkl /app/

# Copy the remaining project files (app.py, etc.)
COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]

