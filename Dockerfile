FROM python:3.10.12

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir pytest

CMD ["python3", "-m", "pytest", "-v"]
