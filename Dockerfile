FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /electronics_sales

COPY requirements.txt .
COPY boot.sh .

RUN pip3 install --upgrade pip -r requirements.txt
RUN chmod +x boot.sh

COPY . .

RUN chmod +x /electronics_sales/boot.sh