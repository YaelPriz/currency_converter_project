import requests


class USD:
    base_currency = "USD"
    conversion_to = "ILS"
    default_rate = 3.52

    def get_value(self):
        exchangerates_url = 'https://api.engxchaerate-api.com/v4/latest'
        api_key = '298a6cfe9f41e386201b17c1'
        url = f'{exchangerates_url}?access_key={api_key}&base={self.base_currency}'
        try:
            response = requests.get(url)
            data = response.json()
            rates = data['rates']
            return rates[self.conversion_to]
        except Exception:
            print(f"Could not get rate from API. using default rate - {self.default_rate}")
            return self.default_rate

    def calculate(self):
        # gets user value (float).
        # if the user inserted an invalid value:
        # lets them know it's invalid and asks them to insert again
        # repeats until the user's value is valid
        # then calculate the conversion (multiply user input by the coin rate)
        i = 1
        while i == 1:
            try:
                value_to_convert = float(input('please enter an amount to convert\n'))
                i = 0
            except ValueError:
                print('Invalid Value, please try again\n')
        conversion = value_to_convert * self.get_value()
        return conversion
