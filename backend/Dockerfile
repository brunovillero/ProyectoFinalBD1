# Definimos la imagen base de python
FROM python:3.8

# Definimos el directorio
WORKDIR /app

COPY * /app/

# Copiamos las dependencias al directorio
COPY requirements.txt .

# Instalamos las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el contenido local de la carpeta backend al directorio definido
COPY . .

# Exponemos el puerto 5000
EXPOSE 5000

# Definimos el compando para inicializar la app
CMD ["python", "app.py"]
