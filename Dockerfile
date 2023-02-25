FROM python:slim-buster
WORKDIR /flask-docker

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]
