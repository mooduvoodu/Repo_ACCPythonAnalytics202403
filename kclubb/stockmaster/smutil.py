import requests
import pandas as pd
import datetime as dt

class polygonutil:
    def __init__(self,sp,ak) -> None:
        self.storagepath = sp
        self.apikey = ak

    
    def fetch_tickers(self) -> pd.DataFrame:
        api_url = f'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&limit=500&apiKey={self.apikey}'
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
                api_url = tickerdata.get('next_url') + f'&apiKey={self.api_key}'  # Update the URL for the next request
            else:
                break

        # Convert the list of tickers to a DataFrame
        df_tickers = pd.json_normalize(tickers)
        return df_tickers


    def fetch_stock_data(self,tlist,aggrtime,startfromdate,opmode):
        pass