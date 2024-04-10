
### Solution Code:

```python
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

    # Convert the list of tickers to a DataFrame
    df_tickers = pd.json_normalize(tickers)
    return df_tickers

# Use your API key here
api_key = 'dIUMbUHa3jguPZ9WiF5HUgIS4FWhPWlq'
tickers_df = fetch_tickers(api_key)

# Display the first 10 rows of the DataFrame
print(tickers_df.head(10))

tickers_df.to_csv("tickers.csv", index=False)
```

#### Note:
Replace `'dIUMbUHa3jguPZ9WiF5HUgIS4FWhPWlq'` with your actual API key to execute the solution code. This exercise will help you understand how to work with APIs, handle pagination, and manipulate JSON data using Pandas.
