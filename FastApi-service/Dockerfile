# ---------- Build stage ----------
FROM python:3.11-alpine AS builder

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Runtime stage ----------
FROM python:3.11-alpine

WORKDIR /app

# Create non-root user
RUN adduser -D appuser
USER appuser

# Copy only installed packages
COPY --from=builder /install /usr/local

COPY app/ app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
