import requests
import pandas as pd

response = requests.get(
    "https://api.mockaroo.com/api/491b7240?count=1000&key=ffae8640"
)

with open("SALES_DATA.csv", "w", encoding="utf-8") as f:
        f.write(response.text)

df = pd.read_csv("SALES_DATA.csv")
print(df.head())