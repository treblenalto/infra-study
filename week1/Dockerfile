FROM python:3.12-slim

WORKDIR /app

COPY ./main.py /app
COPY ./pyproject.toml /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8050
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8050"]