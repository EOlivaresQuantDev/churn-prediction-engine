-- 1. Tabla de Clientes (Unificamos customer_id y unique_id)
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) PRIMARY KEY, -- ID de la orden
    customer_unique_id VARCHAR(50),      -- ID real del cliente (churn target)
    customer_zip_code_prefix VARCHAR(10),
    customer_city VARCHAR(100),
    customer_state VARCHAR(5)
);

-- 2. Tabla de Órdenes (El corazón del Churn)
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),            -- Link a la tabla customers
    order_status VARCHAR(20),
    order_purchase_timestamp TIMESTAMP, -- ¡Clave para calcular recencia!
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

-- 3. Tabla de Items (Detalle de qué compraron)
CREATE TABLE IF NOT EXISTS order_items (
    order_id VARCHAR(50),
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date TIMESTAMP,
    price FLOAT,
    freight_value FLOAT
);

-- 4. Tabla de Pagos (Para calcular valor monetario - Monetary)
CREATE TABLE IF NOT EXISTS order_payments (
    order_id VARCHAR(50),
    payment_sequential INT,
    payment_type VARCHAR(20),
    payment_installments INT,
    payment_value FLOAT
);

-- Crear índices para que las consultas sean rápidas como el rayo ⚡
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_timestamp ON orders(order_purchase_timestamp);
CREATE INDEX idx_customers_unique ON customers(customer_unique_id);
