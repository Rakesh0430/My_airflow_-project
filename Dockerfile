# Srinivasa Salvapathi Manapaka
FROM python:3.9-slim
COPY requirements.txt /requirements.txt
RUN pip install  --user --upgrade pip  
RUN pip install --no-cache-dir --user -r /requirements.txt
CMD ["python", "./model_training.py"]

