import pandas as pd
import os
from sqlalchemy import create_engine
import time

# --- CAMBIO: Volvemos a psycopg2 (el driver robusto) en el puerto 5433 ---
# Como ya limpiamos los acentos del archivo, esto funcionara perfecto.
DB_STR = 'postgresql+psycopg2://user_churn:password_churn@localhost:5433/churn_db'
DB_ENGINE = create_engine(DB_STR)

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw')

def ingest_table(file_name, table_name):
    csv_path = os.path.join(RAW_DATA_PATH, file_name)
    
    if not os.path.exists(csv_path):
        print(f"File not found: {file_name}")
        return

    print(f"Reading {file_name}...")
    df = pd.read_csv(csv_path)
    
    # Date conversion
    for col in df.columns:
        if 'date' in col or 'timestamp' in col:
            df[col] = pd.to_datetime(df[col])

    print(f"Inserting {len(df)} rows into {table_name}...")
    
    # Insert to SQL
    df.to_sql(table_name, DB_ENGINE, if_exists='append', index=False, chunksize=10000)
    print("Done.\n")

if __name__ == "__main__":
    print("Starting Data Ingestion with Psycopg2 (Port 5433)...\n")
    
    try:
        ingest_table('olist_customers_dataset.csv', 'customers')
        ingest_table('olist_orders_dataset.csv', 'orders')
        ingest_table('olist_order_items_dataset.csv', 'order_items')
        ingest_table('olist_order_payments_dataset.csv', 'order_payments')
        print("SUCCESS! Database is hydrated.")
        
    except Exception as e:
        print("\nCRITICAL ERROR:")
        print(e)
