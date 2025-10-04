FROM python:3.11-slim

WORKDIR /app

# Install dependencies
# 1. Copy dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Cache Breaker Added ---
# Force Docker to re-evaluate the following steps
ARG BUILD_DATE
RUN echo "Build started on: ${BUILD_DATE}" 

# Explicitly copy model files immediately after dependencies
# This ensures these critical files are copied before general project files
COPY recall_risk_model_fixed.json /app/
COPY label_encoders.pkl /app/

# Copy the remaining project files (app.py, etc.)
COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]

