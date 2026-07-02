import pandas as pd
from datetime import datetime
from pathlib import Path
from db.dataa import get_connection

conn = get_connection()

query = """
SELECT *
FROM api_data
WHERE created_at >= datetime('now', '-1 day')
"""

df = pd.read_sql_query(query, conn)

if not df.empty:

    today = datetime.now()

    folder = (
        Path("data")
        / "raw"
        / today.strftime("%Y")
        / today.strftime("%m")
        / today.strftime("%d")
    )

    # Create folders if they don't exist
    folder.mkdir(parents=True, exist_ok=True)

    # Complete CSV path
    csv_path = folder / "api_data.csv"

    # Save CSV
    df.to_csv(csv_path, index=False)

    print(f"Created: {csv_path}")

else:
    print("No records found.")

conn.close()