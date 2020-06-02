from Account import Account

class Risk(Account):
    
    def __init__(self, position_size=0.20, max_risk_per_trade=0.01):
        super().__init__()
        self.max_risk_per_trade = max_risk_per_trade
        self.position_size = position_size

    def get_share_size(self, price):
        equity = self.get_equity()
        position_dollar_amount = float(equity) * self.position_size
        share_size = position_dollar_amount / price

        return int(share_size)

    def get_stop_loss(self, price):
        return price - (float(price) * self.max_risk_per_trade)

    def get_target(self, price):
        return price + (float(price) * (self.max_risk_per_trade * 3))

    def total_shutdown(self):
        pass

    
    