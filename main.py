# This program converts currency between USD (United States Dollars) and ILS (Israeli Shekel).

import requests
from ILS import ILS
from USD import USD


def get_user_value():
    # gets user value.
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


def convert(coin):
    # gets user value (float).
    # if the user inserted an invalid value:
    # lets them know it's invalid and asks them to insert again
    # repeats until the user's value is
    # then calculate the conversion and saves it to list
    i = 1
    while i == 1:
        try:
            value_to_convert = float(input('please enter an amount to convert\n'))
            i = 0
        except ValueError:
            print('Invalid Value, please try again\n')
    conversion = coin.calculate(value_to_convert)
    save_results(conversion, coin)


def save_results(conversion, coin):
    Result.append(conversion)
    if coin.base_currency == "USD":
        Result.append('USD to ILS')
    elif coin.base_currency == "ILS":
        Result.append('ILS to USD')
    print(conversion)




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
        convert(coin)
        i = start_over()
        print(Result[len(Result)])

    print('Thanks for using our currency converter')
    print_results


Result = []
main()


