FROM python:3.10-slim

WORKDIR /cron

COPY . /cron

ENV PYTHONPATH=$PWD/cron

RUN pip install -r requirements.txt

EXPOSE 8080

# CMD ["python", "cron.py"]
CMD [ "tail", "-f", "/dev/null" ] # for tests
