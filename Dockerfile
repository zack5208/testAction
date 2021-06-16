# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#RUN echo $1
#RUN chmod +x /app.py
#CMD [ "python3", "/app/app.py" ]
run echo $owner

RUN chmod +x /app/app.py
ENTRYPOINT ["/app/app.py"]

#CMD tail -f /dev/null