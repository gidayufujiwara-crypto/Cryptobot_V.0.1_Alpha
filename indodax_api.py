import requests
import pandas as pd
from datetime import datetime

def fetch_indodax_ohlc(pair='btc_idr', interval_minutes=60, limit=200):
    url = f'https://indodax.com/api/{pair}_ticker'
    resp = requests.get(url).json()
    
    latest_price = float(resp['ticker']['last'])
    timestamp = int(resp['ticker']['server_time'])

    df = pd.DataFrame([{
        'time': datetime.fromtimestamp(timestamp),
        'close': latest_price
    }])

    # Karena Indodax tidak menyediakan full OHLC historical via public API,
    # maka kita akan **simulasikan** dengan hanya close harga terakhir
    return df
