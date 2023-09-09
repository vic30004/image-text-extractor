FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
