# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Cache breaker
ARG BUILD_DATE
RUN echo "Build started on: ${BUILD_DATE}"

# Copy model files
COPY recall_risk_model_fixed.json .
COPY label_encoders.pkl .

# Copy rest of project files
COPY . .

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python3", "-u", "app.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

