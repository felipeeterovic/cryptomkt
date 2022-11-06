import requests

def base(url, params = {}):
    '''
    Base method for market_data, only for internal purposes
    '''
    response = requests.get(url, params = params).json()
    if "error" in response:
        print(f"Error: {response['error']['code']}: {response['error']['message']}")
        return None
    else:
        return response

def get_currencie(currency = ""):
    currency.upper()
    currency = currency if currency == "" else f"/{currency}"
    return base(f"https://api.exchange.cryptomkt.com/api/3/public/currency{currency}")


def get_symbol(symbol = ""):
    symbol.upper()
    symbol = symbol if symbol == "" else f"/{symbol}"
    return base(f"https://api.exchange.cryptomkt.com/api/3/public/symbol{symbol}")


def get_ticker(symbol = ""):
    symbol.upper()
    symbol = symbol if symbol == "" else f"/{symbol}"
    return base(f"https://api.exchange.cryptomkt.com/api/3/public/ticker{symbol}")

def get_prices(params):
    return base('https://api.exchange.cryptomkt.com/api/3/public/price/rate', params=params)

def get_prices_history(params):
    return base('https://api.exchange.cryptomkt.com/api/3/public/price/history', params=params)

def get_trades(symbol = "", params = {}):
    symbol.upper()
    symbol = symbol if symbol == "" else f"/{symbol}"
    return base(f"https://api.exchange.cryptomkt.com/api/3/public/trades{symbol}",params)
