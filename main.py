# This program converts currency between USD (United States Dollars) and ILS (Israeli Shekel).

import requests
from ILS import ILS
from USD import USD


def get_user_value():
    user_choice = input('Please choose an option (1/2): \n1. Dollars to Shekels \n2. Shekels to Dollars\n')
    if user_choice == '1':
        coin = USD()
    elif user_choice == '2':
        coin = ILS()
    else:
        print('Invalid Choice, please try again\n')
        return
    value_to_convert = float(input('please enter an amount to convert\n'))
    conversion = coin.calculate(value_to_convert)
    print(conversion)
    return user_choice, coin, conversion


def start_over():
    user_choice = input('Do you want to start over? Please choose Y / N\n')
    if user_choice == 'Y':
        return 1
    elif user_choice == 'N':
        return 0


def third_page(name):
    print(f'Hi, {name}')

    if __name__ == '__main__':
        print('PyCharm')


def main():
    print('Welcome to currency converter')
    i = 1
    while i == 1:
        conversion = get_user_value()
        i = start_over()
        print(conversion)

    print('Thanks for using our currency converter')


main()
