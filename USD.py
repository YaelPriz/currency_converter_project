from coins import Coins


class USD(Coins):
    def __init__(self, base_currency="USD", conversion_to="ILS", default_rate=3.52):
        super().__init__(base_currency, conversion_to, default_rate)