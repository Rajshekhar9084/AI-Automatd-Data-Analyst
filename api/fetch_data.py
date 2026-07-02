import requests

from db.dataa import create_table, get_connection

# Ensure database and table exist
create_table()

# API URL (add later)
url = ""

# Fetch data
response = requests.get(url)
data = response.json()

# Database connection
conn = get_connection()
cursor = conn.cursor()

# Insert all API records
cursor.executemany(
    """
    INSERT INTO api_data (
        order_id,
        order_date,
        ship_date,
        ship_mode,
        customer_id,
        customer_name,
        segment,
        country,
        city,
        state,
        region,
        product_id,
        category,
        product_name,
        sales,
        quantity,
        discount,
        profit,
        month,
        year,
        profit_margin,
        shipping_days
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    [
        (
            record["order_id"],
            record["order_date"],
            record["ship_date"],
            record["ship_mode"],
            record["customer_id"],
            record["customer_name"],
            record["segment"],
            record["country"],
            record["city"],
            record["state"],
            record["region"],
            record["product_id"],
            record["category"],
            record["product_name"],
            record["sales"],
            record["quantity"],
            record["discount"],
            record["profit"],
            record["month"],
            record["year"],
            record["profit_margin"],
            record["shipping_days"]
        )
        for record in data
    ]
)

conn.commit()
conn.close()

print("Data saved successfully.")