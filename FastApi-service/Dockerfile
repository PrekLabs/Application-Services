# ---------- Build stage ----------
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

# ---------- Runtime stage ----------
FROM python:3.11-slim-bookworm

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app/app app/

RUN apt-get update && \
    apt-get upgrade -y libc6 libc-bin && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
