from coins import Coins


class ILS(Coins):
    def __init__(self, base_currency="ILS", conversion_to="USD", default_rate=0.28):
        super().__init__(base_currency, conversion_to, default_rate)