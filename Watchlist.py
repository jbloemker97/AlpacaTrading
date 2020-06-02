import requests, json
from Account import Account

class Watchlist(Account):
    
    def get_watch_lists(self):
        return json.loads(requests.get('{}/v2/watchlists'.format(self.BASE_URL), headers=self.headers).content)

    def get_watch_list_by_id(self, _id):
        return json.loads(requests.get('{}/v2/watchlists/{}'.format(self.BASE_URL, _id), headers=self.headers).content)