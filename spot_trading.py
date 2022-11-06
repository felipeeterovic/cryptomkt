from auth_mkt import HS256

class spot_trader:

    def __init__(self, api_key, api_secret):
        self.at = H256(api_key, api_secret)
