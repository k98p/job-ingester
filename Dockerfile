# ---- Base image ----
FROM docker.io/library/python:3.11-slim

# ---- System settings ----
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---- Install Python deps ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy service contents ----
COPY . app/
RUN echo "==== Contents of /app ====" && ls -la /app

# ---- Cloud Run listens on 8080 ----
EXPOSE 8080

# Set the correct WORKDIR
WORKDIR ./app

# ---- Start FastAPI ----
CMD ["gunicorn", "main:app", \
     "-k", "uvicorn.workers.UvicornWorker", \
     "-w", "1", \
     "--bind", "0.0.0.0:8080"]
