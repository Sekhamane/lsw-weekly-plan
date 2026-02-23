FROM python:3.13-slim

WORKDIR /app

# Copy backend requirements and install
COPY backend/requirements.txt backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend code
COPY backend/ backend/

# Copy frontend (if already built)
COPY frontend/build/ frontend/build/ 2>/dev/null || true

# Expose port
EXPOSE 8000

# Run backend
CMD ["python", "-m", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
