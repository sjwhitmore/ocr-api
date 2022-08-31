FROM python:3.10.6-buster

RUN apt-get update \
  && apt-get -y install ffmpeg libsm6 libxext6 libxrender-dev tesseract-ocr

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "ocr:app"]
