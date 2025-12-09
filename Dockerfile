# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo main.py que está dentro de tu carpeta 'app' local
# OJO: Aquí le decimos que busque en 'app/main.py'
COPY app/ .

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
