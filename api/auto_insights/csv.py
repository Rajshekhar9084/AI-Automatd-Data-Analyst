import pandas as pd
from datetime import datetime
from db.dataa import get_connection

conn = get_connection()

query = """
SELECT *
FROM api_data
WHERE created_at >= NOW() - INTERVAL 1 DAY
"""

df = pd.read_sql_query(query, conn)

if not df.empty:
    filename = f"api_data_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)
    print(f"Created: {filename}")
else:
    print("No records found.")

conn.close()  