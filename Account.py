import requests, json

class Account:

    headers = {}
    BASE_URL = ''
    account = {}
    
    def __init__(self, BASE_URL, API_KEY, API_SECRET):
        self.headers['APCA-API-KEY-ID'] = API_KEY
        self.headers['APCA-API-SECRET-KEY'] = API_SECRET
        self.BASE_URL = BASE_URL
        self.set_account()

    def set_account(self):
        self.account = json.loads(requests.get('{}/v2/account'.format(self.BASE_URL), headers=self.headers).content)

    def get_status(self):
        return self.account['status']

    def get_buying_power(self):
        return self.account['buying_power']

    def get_cash(self):
        return self.account['cash']

    def get_portfolio_value(self):
        return self.account['portfolio_value']

    def get_day_trade_count(self):
        return self.account['daytrade_count']

    def get_equity(self):
        return self.account['equity']

    def is_pattern_day_trader(self):
        return self.account['pattern_day_trader']

    def can_trade(self):
        return not self.account['trading_blocked']

    def can_short(self):
        return self.account['shorting_enabled']
