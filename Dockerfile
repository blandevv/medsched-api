FROM python:3.14-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.1.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/opt/poetry/bin:$PATH"

RUN groupadd --gid 1001 appgroup && \
    useradd --uid 1001 \
            --gid appgroup \
            --shell /bin/bash \
            --create-home \
            appuser && \
    apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://install.python-poetry.org | \
    POETRY_VERSION=$POETRY_VERSION python3 -

WORKDIR /app

FROM base AS dependencies

COPY pyproject.toml poetry.lock ./

RUN poetry install \
    --without dev \
    --no-interaction \
    --no-ansi

FROM dependencies AS production

COPY --chown=appuser:appgroup src/ ./src/

USER appuser

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM dependencies AS development

RUN poetry install \
    --no-interaction \
    --no-ansi

COPY --chown=appuser:appgroup src/ ./src/

USER appuser

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
