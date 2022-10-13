FROM python:3.7-alpine

RUN pip install art

COPY ./main.py /app/main.py

CMD /app/main.py