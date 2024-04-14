import requests
import pandas as pd
import datetime

def fetch_stock_data():
    api_url = f'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/hour/2024-04-01/2024-04-01?adjusted=true&sort=asc&limit=500&apiKey=7JbEpLM6e6J0nsQk8BS8kVKKJbFhDAIO'
    stock= []
    roundtripcounter = 0

    while api_url:
        roundtripcounter += 1
        print(f'Round trip #{roundtripcounter}')
        PGresponse = requests.get(api_url)
        if PGresponse.status_code != 200:
            raise ValueError("API request failed. Please check your API key and network connection.")
        stockdata = PGresponse.json()
        stock.extend(stockdata['results'])
        if stockdata.get('next_url'):
            api_url = stockdata.get('next_url') + f'&apiKey={7JbEpLM6e6J0nsQk8BS8kVKKJbFhDAIO}'  # Update the URL for the next request
        else:
            break
    # Convert the list of stocks to a DataFrame
    df_stockdata = pd.json_normalize(stock)
    return df_stockdata

stock_df=fetch_stock_data()
stock_df.to_csv('/workspaces/Repo_ACCPythonAnalytics202403/Dey/SecondFile.py"stockdata.csv"', index=False)
