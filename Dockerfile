FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install python-dotenv
COPY app.py .
CMD ["python", "app.py"]
