import ccxt
from func_timeout import func_set_timeout
import func_timeout
from retrying import retry
import requests 
@func_set_timeout(10)

def retry_if_error(exception):
    print("---------------------------")
    return isinstance(exception, func_timeout.exceptions.FunctionTimedOut)

@retry(retry_on_exception=retry_if_error)
def get_percentage_and_price():
    biance = ccxt.binance({
    # 'apiKey': '',
    # 'secret': '',
    'proxies': {

    'https': 'http://127.0.0.1:7890',

    },

    })

    # data = biance.fetch_ohlcv(symbol='DOGE/USDT', limit=limit, since=since_time)
    while True:
        try:
            data_WAVES = biance.fetch_ticker(symbol="WAVES/USDT")
            WAVES_PRIZE =  data_WAVES["last"]
            WAVES_PERCENTAGE = data_WAVES["percentage"]
            return WAVES_PRIZE,WAVES_PERCENTAGE
        
        except requests.exceptions.RequestException as e:
            print("frequently access")
            continue
        except func_timeout.exceptions.FunctionTimedOut as e:
           
            print("timeout")
            continue

if __name__=="__main__":
    price,percentage = get_percentage_and_price()
    print(type(percentage),type(price))
    print(price,percentage)