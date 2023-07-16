import requests


class Coins:
    def __init__(self, base_currency, conversion_to, default_rate):
        exchangerates_url = 'https://api.engxchaerate-api.com/v4/latest'
        api_key = '298a6cfe9f41e386201b17c1'
        self.base_currency = base_currency
        self.conversion_to = conversion_to
        self.default_rate = default_rate
        self.url = f'{exchangerates_url}?access_key={api_key}&base={base_currency}'

    def get_value(self):
        try:
            response = requests.get(self.url)
            data = response.json()
            rates = data['rates']
            return rates[self.conversion_to]
        except Exception:
            print('Could not get rate from API. using default rate')
            return self.default_rate

    def calculate(self, user_input):
        return user_input * self.get_value()
