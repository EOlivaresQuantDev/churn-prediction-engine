# 📉 Churn Prediction Engine (Olist E-commerce)

Este proyecto es una solución End-to-End de **Machine Learning** para predecir el abandono de clientes (Churn) en un entorno de E-commerce.

Utiliza datos reales de **Olist (Brasil)** para entrenar un modelo de **Random Forest**, el cual es desplegado como una **API REST** contenerizada en **Docker**.

---

## 🛠️ Tech Stack

* **Lenguaje:** Python 3.9
* **ML Core:** Scikit-Learn, Pandas, Numpy.
* **API:** FastAPI + Uvicorn.
* **Database:** PostgreSQL (Dockerizada).
* **Infrastructure:** Docker & Docker Compose.
* **Data Engineering:** SQL Alchemy + Psycopg2.

---

## 📂 Estructura del Proyecto

```text
churn-project/
├── api/             # Código de la API (FastAPI)
├── data/            # Datos crudos y procesados (Parquet)
├── infra/           # Esquema SQL y configuración
├── model/           # Modelo entrenado (.pkl)
├── notebooks/       # Experimentación (Jupyter)
├── src/             # Scripts de Ingesta (ETL)
├── docker-compose.yml  # Orquestación de servicios
└── Dockerfile          # Imagen de la APIs
