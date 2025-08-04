FROM python:3.13-alpine AS builder
WORKDIR /build
COPY requirements.txt .
RUN python -m venv .venv \
    && .venv/bin/pip install --no-cache-dir -U pip setuptools \
    && .venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.13-alpine
WORKDIR /app
RUN adduser -D appuser
COPY --from=builder /build/.venv/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY app .
USER appuser
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000
CMD ["sh", "-c", "python -m uvicorn main:app --host 0.0.0.0 --port $PORT"]
EXPOSE 8000