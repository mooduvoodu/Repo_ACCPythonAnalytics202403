import pandas as pd
import requests

def fetch_tickers(apikey):
    url = 'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&limit=100&apiKey=' + apikey
    tickers = []

    response = requests.get(url)
    data = response.json()
    tickers.extend(data['results'])

    url = data.get('next_url')

    print(url)

    return pd.json_normalize(tickers)

apikey = 'eLg5ahqp8wVsMqzJ7g4smd6Dq7hYCbgJ'
tickers_df = fetch_tickers(apikey)

print(tickers_df.head(10))

#next Url Not working