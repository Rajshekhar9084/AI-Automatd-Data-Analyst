from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_data (
    order_id VARCHAR(50) UNIQUE,
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    segment VARCHAR(50),
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(100),
    product_name VARCHAR(255),
    sales DECIMAL(12,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(12,2),
    month INT,
    year INT,
    profit_margin DECIMAL(10,4),
    shipping_days INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

    conn.commit()
    conn.close()