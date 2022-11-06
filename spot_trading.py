import requests

class spot_trader:

    def __init__(self, api_key, api_secret):
        #self.at = H256(api_key, api_secret)
        self.api_key = api_key
        self.api_secret = api_secret

    def base(self, url):
        session = requests.session()
        session.auth = (self.api_key, self.api_secret)
        response = session.get(url).json()
        if "error" in response:
            print(f"Error: {response['error']['code']}: {response['error']['message']}")
            return None
        return response


    def get_spot_trading_balance(self, currency = ""):
        currency = currency.upper()
        currency = currency if currency == "" else f"/{currency}"
        return self.base(f"https://api.exchange.cryptomkt.com/api/3/spot/balance{currency}")

    def get_order(self, client_order_id = ""):
        client_order_id = client_order_id if client_order_id = "" else f"/{client_order_id}"
        return self.base(f"https://api.exchange.cryptomkt.com/api/3/spot/order{client_order_id}")
