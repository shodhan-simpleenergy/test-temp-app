# ===============================
# Stage 1: Build Stage
# ===============================
FROM python:3.9-slim AS builder
WORKDIR /app

# Copy only requirements first to leverage caching
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Copy source code
COPY . .

# ===============================
# Stage 2: Final Runtime Stage
# ===============================
FROM python:3.9-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]


