FROM python:3.10.0

RUN apt-get update -y && install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]