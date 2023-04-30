FROM python:3.10

WORKDIR /app

COPY Pipfile* /app/

RUN pip install pipenv && pipenv install --dev --system --deploy

COPY . /app

RUN alembic upgrade head

EXPOSE 3000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]