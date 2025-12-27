FROM python:3.12-slim
WORKDIR /usr/local/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser

COPY --chown=appuser:appuser . .
USER appuser

ENV PATH="/home/appuser/.local/bin:${PATH}"

EXPOSE 5435


CMD ["python", "serve.py"]