from base64 import b64encode
from hashlib import sha256
from hmac import HMAC
from time import time
from urllib.parse import urlsplit
from requests import Session
from requests.auth import AuthBase

class HS256(AuthBase):
    #Base class for authentication

    def __init__(self, api_key: str, secret_key: str, window: int = None):
        self.api_key = api_key
        self.secret_key = secret_key
        self.window = window

    def __call__(self, r):
        url = urlsplit(r.url)
        message = [r.method, url.path]
        if url.query:
            message.append('?')
            message.append(url.query)
        if r.body:
            message.append(r.body)

        timestamp = str(int(time() * 1000))
        window = str(self.window) if self.window else None
        message.append(timestamp)
        if window:
            message.append(window)

        signature = HMAC(key=self.secret_key.encode(),
                         msg=''.join(message).encode(),
                         digestmod=sha256).hexdigest()
        data = [self.api_key, signature, timestamp]
        if window:
            data.append(window)

        base64_encoded = b64encode(':'.join(data).encode()).decode()
        r.headers['Authorization'] = f'HS256 {base64_encoded}'
        return r

# auth = HS256(api_key='apiKey', secret_key='secretKey')
# with Session() as s:
#     response = s.get('https://api.exchange.cryptomkt.com/api/3/spot/balance', auth=auth)
#     print(response.json())
