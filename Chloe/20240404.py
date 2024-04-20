import requests
import pandas as pd

def fetch_tickers(api_key):
    api_url = f'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&limit=500&apiKey={api_key}'
    tickers = []
    roundtripcounter = 0

    while api_url:
        roundtripcounter += 1
        print(f'Round trip #{roundtripcounter}')
        PGresponse = requests.get(api_url)
        if PGresponse.status_code != 200:
            raise ValueError("API request failed. Please check your API key and network connection.")
        tickerdata = PGresponse.json()
        tickers.extend(tickerdata['results'])
        if tickerdata.get('next_url'):
            api_url = tickerdata.get('next_url') + f'&apiKey={api_key}'  # Update the URL for the next request
        else:
            break
    df_tickers = pd.json_normalize(tickers)
    return df_tickers

api_key = 'BDRYmUV3NU29r6y734HcvipzFA6GQMzt'
tickers_df = fetch_tickers(api_key)

print(tickers_df.head(10))

tickers_df.to_csv("tickers.csv", index=False)
