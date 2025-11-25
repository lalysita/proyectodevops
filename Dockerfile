FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias directamente para ahorrar pasos
RUN pip install flask pytest

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]