import pandas as pd
import requests as rq 
pip install polygon-api-client
from polygon import RESTClient

client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("BDRYmUV3NU29r6y734HcvipzFA6GQMzt") # api_key is used

def fetch_tickets = requests.get('https://api.polygon.io/v3/reference/tickers?type=CS&market=stocks&active=true&limit=100&apiKey=BDRYmUV3NU29r6y734HcvipzFA6GQMzt')

print(fetch_tickets.text)
