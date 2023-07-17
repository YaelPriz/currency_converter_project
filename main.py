# This program converts currency between USD (United States Dollars) and ILS (Israeli Shekel).

from ILS import ILS
from USD import USD


def get_user_value():
    # user value should be 1 or 2.
    # if the user chose an invalid choice:
    # lets them know it's invalid and asks them to choose again
    # repeats until the user's choice is valid
    i = 1
    while i == 1:
        user_choice = input('Please choose an option (1/2): \n1. Dollars to Shekels \n2. Shekels to Dollars\n')
        if user_choice == '1':
            coin = USD()
            i = 0
        elif user_choice == '2':
            coin = ILS()
            i = 0
        else:
            print('Invalid Choice, please try again\n')
    return coin


def save_results(conversion, coin):
    Result.append(conversion)
    Result.append(coin.base_currency + " to " + coin.conversion_to)
    print(f"The conversion result is: {conversion}")


def start_over():
    i = 1
    while i == 1:
        user_input = input('Do you want to start over? Please choose Y / N\n')
        if user_input.lower() == 'y':
            i = 0
            return 1
        elif user_input.lower() == 'n':
            i = 0
            return 0
        else:
            print('Invalid Choice, please try again\n')


def print_results():
    # prints each result in a new line
    for i in range(0, len(Result), 2):
        print(Result[i], Result[i+1])


def main():
    print('Welcome to currency converter')
    i = 1
    while i == 1:
        coin = get_user_value()
        conversion = coin.calculate()
        save_results(conversion, coin)
        i = start_over()

    print('Thanks for using our currency converter')
    print_results()


Result = []
main()


