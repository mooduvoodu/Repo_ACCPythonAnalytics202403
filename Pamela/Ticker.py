import requests 
import pandas as pd
def fetch_tickers(api_key):
    api_url = f'https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&limit=500&apiKey={api_key}'
    tickers = []
    response.status_code = 1

    while response.status_code <200 :
        response.status= response.status+1
        response = requests.get(api_url)
        tickerdata =response.json()
        tickers.extend =(tickerdata['results'])
    if tickerdata.get('next url'):
         api_url = tickerdata.get('next_url') + f'&apiKey={api_key}'  # Update the URL for the next request
    else:
        break 
      
    # Convert the list of tickers to a DataFrame
    df_tickers = pd.json_normalize(tickers)
    return df_tickers
   

# Use your API key here
api_key = 'mGY_jfBBhxriPIExHNoKE_biRpfXAKVU'
tickers_df = fetch_tickers(api_key)

# Display the first 10 rows of the DataFrame
print(tickers_df.head(10))

tickers_df.to_csv("tickers.csv", index=False)

