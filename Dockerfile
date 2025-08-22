# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el script de Python al contenedor
COPY greetings.py .

# Instalar dependencias si las hay (opcional)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar el script
CMD ["python", "greeting.py"]
