FROM python:3.9-slim

WORKDIR /app

# Install build dependencies for xgboost
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8001

# Run the API
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "app:app", "--workers", "1", "--timeout", "120"]


