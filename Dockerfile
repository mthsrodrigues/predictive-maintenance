FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv \
    && uv sync --frozen --no-dev

COPY src ./src
COPY models ./models

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "predictive_maintenance.api:app", "--host", "0.0.0.0", "--port", "8000"]