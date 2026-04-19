FROM python:3.11-slim

WORKDIR /app

COPY analyze.py .
COPY queries.sql .

RUN pip install pandas matplotlib seaborn

CMD ["python", "analyze.py"]
