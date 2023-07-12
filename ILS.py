from coins import Coins


class ILS(Coins):
    def __init__(self, base_currency="USD", conversion_to="ILS", default_rate=0.28):
        super().__init__(base_currency, conversion_to, default_rate)