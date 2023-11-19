FROM python:3.10.5-alpine3.16
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python -u etl.py --port=6001 --host=0.0.0.0