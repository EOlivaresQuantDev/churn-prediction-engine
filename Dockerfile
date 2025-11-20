# 1. Imagen base de Python (Ligera y rápida)
FROM python:3.9-slim

# 2. Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requerimientos (si lo tuviéramos) o instalar manual
# Para este demo, instalamos directo para ahorrar pasos
RUN pip install --no-cache-dir pandas scikit-learn joblib fastapi uvicorn pydantic

# 4. Copiar el código del proyecto al contenedor
# Copiamos carpeta por carpeta para mantener orden
COPY ./api /app/api
COPY ./model /app/model

# 5. Exponer el puerto donde vivirá la API
EXPOSE 8000

# 6. Comando para encender el motor cuando inicie el contenedor
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
