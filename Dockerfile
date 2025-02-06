FROM python:3.12.7-slim
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3300"]