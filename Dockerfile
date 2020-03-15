FROM python:3.8-alpine


WORKDIR /home/zpmerch

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]