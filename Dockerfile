FROM python:3.12-alpine
WORKDIR /bot
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY .. .

CMD ["python", "/bot/main.py"]

