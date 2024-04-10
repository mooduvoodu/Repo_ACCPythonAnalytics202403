import requests
import pandas

def fetch_tickers():
    api_url= f'https://api.polygon.io/v3/reference/tickers?active=true&apiKey=7JbEpLM6e6J0nsQk8BS8kVKKJbFhDAIO'
    tickers = []
    response.status_code = 1

    for i in range(1,200):
        response.status_code = response.status_code + i
        data = response.json()
        tickers.extend(data['results'])
        api_url = data.get('next_url')
    df_tickers = pandas.json_normalize(tickers)
    return df_tickers
print(tickers_df.head(10))
