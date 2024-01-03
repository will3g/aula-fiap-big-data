FROM python:3.10-slim

WORKDIR /cron

COPY . /cron

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "cron.py"]
