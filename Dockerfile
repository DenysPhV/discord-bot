FROM python:3.12

ENV PYTHONUNBUFFERED True

WORKDIR /bot
COPY . ./

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/bot/main.py"]

