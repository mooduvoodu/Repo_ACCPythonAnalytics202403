import requests
import pandas as pd
from datetime import datetime as dt, timezone

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
#tickers_df = fetch_tickers(api_key)

# Display the first 10 rows of the DataFrame
#print(tickers_df.head(10))

#tickers_df.to_csv("/workspaces/Repo_ACCPythonAnalytics202403/kclubb/tickers.csv", index=False)

#test aggr load process

ticketlist = ['AAPL','UWMC','DIS','SNOW','WMT']

def fetch_stock_data(tlist,aggrtime,startfromdate,opmode, enddt = dt.now(timezone.utc)):
    #string in 'yyyy-mm-dd' format
    fenddt = enddt.strftime('%Y-%m-%d')
    tickers = tlist
    roundtripcounter = 0
    tickeraggrdatalist = []
  
    match opmode:
        case 'full':
            for t in tlist:
                print(f'working on stock {t}')
                api_url = f'https://api.polygon.io/v2/aggs/ticker/AAPL/range/10/second/{startfromdate}/{fenddt}?adjusted=true&sort=asc&limit=50000&apiKey={api_key}'
                while api_url:
                    roundtripcounter += 1
                    print(f'Round trip #{roundtripcounter}')
                    PGresponse = requests.get(api_url)
                    if PGresponse.status_code != 200:
                        raise ValueError("API request failed. Please check your API key and network connection.")
                    tickeraggrdata = PGresponse.json()
                    tickeraggrdatalist.extend(tickeraggrdata['results'])
                    if tickeraggrdata.get('next_url'):
                        api_url = tickeraggrdata.get('next_url') + f'&apiKey={api_key}'  # Update the URL for the next request
                    else:
                        break

            # Convert the list of tickeraggr to a DataFrame
                df_tickeraggr = pd.json_normalize(tickeraggrdatalist)
                df_tickeraggr.to_csv(f"/workspaces/Repo_ACCPythonAnalytics202403/kclubb/stockhistory/{t}.csv", index=False)

        case 'incremental': #figure out the most recent date for each file and use that as the starting point.
            
                #is there an existing file for that ticker. if there is go get the latest timestamp
                #go get data from the last timestamp and Now
                #merge those 2 together, remove duplicates for overlap day and write back to file.. overite file.
            for t in tlist:
                #Get Most recent time stamp from existing file, assuming the file exists.. error handling for this should be add at some point for missing file
                data = pd.read_csv(f"/workspaces/Repo_ACCPythonAnalytics202403/kclubb/stockhistory/{t}.csv")

                # Convert the epoch time in milliseconds to datetime
                data['date'] = pd.to_datetime(data['t'], unit='ms')
                 # Find the most recent date in the 'date' column
                most_recent_date = dt.date(data['date'].max())
                startfromdate = most_recent_date.strftime('%Y-%m-%d')


                print(f'working on stock {t}')
                api_url = f'https://api.polygon.io/v2/aggs/ticker/AAPL/range/10/second/{startfromdate}/{fenddt}?adjusted=true&sort=asc&limit=50000&apiKey={api_key}'
                while api_url:
                    roundtripcounter += 1
                    print(f'Round trip #{roundtripcounter}')
                    PGresponse = requests.get(api_url)
                    if PGresponse.status_code != 200:
                        raise ValueError("API request failed. Please check your API key and network connection.")
                    tickeraggrdata = PGresponse.json()
                    tickeraggrdatalist.extend(tickeraggrdata['results'])
                    if tickeraggrdata.get('next_url'):
                        api_url = tickeraggrdata.get('next_url') + f'&apiKey={api_key}'  # Update the URL for the next request
                    else:
                        break

            # Convert the list of tickeraggr to a DataFrame
                df_tickeraggr = pd.json_normalize(tickeraggrdatalist)
            # Union the two DataFrames
                union_data = pd.concat([data, df_tickeraggr])
            # Remove duplicates
                unique_data = union_data.drop_duplicates()
            # save the cleaned dataframe back to a CSV
                unique_data.to_csv(f"/workspaces/Repo_ACCPythonAnalytics202403/kclubb/stockhistory/{t}.csv", index=False)

        case _:
            pass

# ACTUAL CALLING CODE
        
api_key = 'dIUMbUHa3jguPZ9WiF5HUgIS4FWhPWlq'
tickeraggr_df = fetch_stock_data(ticketlist,10,'2024-04-01','full')

#try the incremental mode
tickeraggr_df = fetch_stock_data(ticketlist,10,'2024-04-01','incremental')


