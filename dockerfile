FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo 'requirements.txt' dentro del contenedor
COPY requirements.txt .

# Instalar las dependencias de Python que están en 'requirements.txt'
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]

