import requests


class ILS:
    # This is the ILS coin.
    # It has functions that use to convert user input amount from ILS to USD
    base_currency = "ILS"
    convert_to = "USD"
    default_rate = 0.28

    def get_value(self):
        # returns the latest exchange rate it gets from a REST API.
        # If the API is not available, it returns the default rate
        host_url = 'https://api.frankfurter.app/latest'
        url = f'{host_url}?from={self.base_currency}&to={self.convert_to}'
        try:
            response = requests.get(url)
            rate = response.json()['rates']
            return rate[self.convert_to]
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

