import requests

class spot_trader:

    def __init__(self, api_key, api_secret):
        #self.at = H256(api_key, api_secret)
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.session()
        self.session.auth = (self.api_key, self.api_secret)



    def base(self, url):
        response = self.session.get(url).json()
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

    def create_new_order(self, symbol, side, price, quantity):
        order_data = {"symbol": symbol.upper(), "side": side, "quantity": quantity, "price": price}
        response = self.session.post('https://api.exchange.cryptomkt.com/api/3/spot/order/', data = orderData).json()
        if "error" in response:
            print(f"Error: {response['error']['code']}: {response['error']['message']}")
            return None
        return response
