FROM python:3.8-slim
WORKDIR /app
COPY finnhub_producer.py .
RUN pip install requests kafka-python
CMD ["python", "finnhub_producer.py"]
