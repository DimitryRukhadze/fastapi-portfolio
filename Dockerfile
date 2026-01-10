FROM python:3.12-slim as builder

RUN pip install --no-cache-dir poetry
WORKDIR /home/appuser/app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true && poetry install --no-interaction --no-root --only main

COPY . .

FROM python:3.12-slim
RUN useradd -m appuser
WORKDIR /home/appuser/app

COPY --from=builder --chown=appuser:appuser /home/appuser/app/ /home/appuser/app/

ENV PATH="/home/appuser/app/.venv/bin:${PATH}"

USER appuser

EXPOSE 5435

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "5435", "--log-level", "info"]