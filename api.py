import requests
import pandas as pd

api_key = "658d6f96e99059.57993945"
ticker = "AAPL.US"

url = f'https://eodhd.com/api/eod/{ticker}?api_token={api_key}&fmt=json'

data = requests.get(url, verify = False).json()

df = pd.DataFrame(data)

print(df)