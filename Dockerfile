FROM python:3.10-alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
CMD ["python3", "main.py"]