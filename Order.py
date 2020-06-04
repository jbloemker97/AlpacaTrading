import requests, json
from Account import Account

class Order(Account):
    
    def __init__(self):
        super().__init__()

    def get_orders(self, order_id=None):
        if order_id:
            url = '{}/v2/orders/{}'.format(self.BASE_URL, order_id)
        else:
            url = '{}/v2/orders'.format(self.BASE_URL)

        return json.loads(requests.get(url, headers=self.headers).content)

    def cancel_orders(self, order_id=None):
        if order_id:
            url = '{}/v2/orders/{}'.format(self.BASE_URL, order_id)
        else: 
            url = '{}/v2/orders'.format(self.BASE_URL)

        return requests.delete(url, headers=self.headers).status_code

    def order(self, **kwargs):
        if 'symbol' in kwargs and 'qty' in kwargs and 'side' in kwargs and 'limit_price' in kwargs:
            url = '{}/v2/orders'.format(self.BASE_URL)
            order = {
                'symbol': kwargs['symbol'],
                'qty': kwargs['qty'],
                'side': kwargs['side'],
                'type': 'limit',
                'limit_price': kwargs['limit_price'],
                'time_in_force': 'day',
            }

            if 'take_profit' in kwargs:
                order['take_profit'] = {
                    'limit_price': kwargs['take_profit']
                }
            
            if 'stop_loss' in kwargs:
                order['stop_loss'] = {
                    'stop_price': kwargs['stop_loss']['stop_price'],
                    'stop_limit': kwargs['stop_loss']['limit_price']
                }
            
            if 'order_class' in kwargs:
                order['order_class'] = kwargs['order_class']

            return requests.post(url, json=order, headers=self.headers).json()

        return False