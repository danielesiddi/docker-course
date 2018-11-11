FROM ubuntu:latest

ENV FLASK_APP=app.py

RUN apt-get update && apt-get -y install python3 python3-pip 
RUN pip3 install Flask
RUN pip3 install flask-mysql

COPY app.py /app.py

CMD python3 app.py -v

EXPOSE 6000
