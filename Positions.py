import requests, json
from Account import Account

class Positions(Account):

    def __init__(self):
        super().__init__();

    def get_positions(self, symbol=None):
        if symbol:
            url = '{}/v2/postiions/{}'.format(self.BASE_URL, symbol)
        else:
            url = '{}/v2/positions'.format(self.BASE_URL)
        
        return json.loads(requests.get(url, headers=self.headers).content)

    def close_position(self, symbol=None):
        if symbol:
            url = '{}/v2/positions/{}'.format(self.BASE_URL, symbol)
        else:
            url = '{}/v2/positions'.format(self.BASE_URL)

        return requests.delete(url).status_code