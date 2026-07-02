import requests
import json

from db.dataa import create_table,get_connection

create_table()

url = ""
response = requests.get(url)
data = response.json()

conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO api_data (data) VALUES (?)",
    (json.dumps(data),)
)

conn.commit()
conn.close()

print("Data saved successfully")