FROM python:3.6

WORKDIR /app

COPY requirements_api.txt .
RUN pip install --no-cache-dir -r requirements_api.txt

COPY app.py .
COPY models/model.pkl ./models/

EXPOSE 5000

CMD ["python", "app.py"]