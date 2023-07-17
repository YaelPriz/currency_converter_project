# This program converts currency between USD (United States Dollars) and ILS (Israeli Shekel).

import os
import platform
import subprocess
from ils import ILS
from usd import USD
from result import Result

results = []
file_name = 'results.txt'


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
    # saves the result as a Result class in the results list
    result = Result(conversion, coin.base_currency + " to " + coin.convert_to)
    results.append(result)
    print(f"The conversion result is: {conversion}")


def start_over():
    # gets user value about start over
    # user value should be Y or N (case-insensitive).
    # return 1 if start over was chosen and 0 if it was chosen not to start over
    # if the user chose an invalid choice:
    # lets them know it's invalid and asks them to choose again
    # repeats until the user's choice is valid
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


def print_and_save():
    # Gets the project directory
    # Creates the file path by joining the project directory and the filename
    # using a for loop to write to the file and print each result in a new line

    current_file_path = os.path.abspath(__file__)
    project_directory = os.path.dirname(current_file_path)
    file_path = os.path.join(project_directory, file_name)

    try:
        with open(file_path, 'w') as file:
            for result in results:
                file.write(f"result: {result.result}, conversion flow: {result.conversion_flow}\n")
                print(result.result, result.conversion_flow)
    except IOError as e:
        print(f"Error writing to the file: {str(e)}")

    return file_path


def open_file(file_path):
    # opens the results file (using the correct function for each operating system)
    try:
        if platform.system() == 'Windows':  # Windows
            os.startfile(file_path)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', file_path))
        else:  # Linux
            subprocess.call(('xdg-open', file_path))
    except IOError:
        print(f"Failed to open {file_path}")


def main():
    print('Welcome to currency converter')
    i = 1
    while i == 1:
        coin = get_user_value()
        conversion = coin.calculate()
        save_results(conversion, coin)
        i = start_over()

    print('Thanks for using our currency converter')
    file_path = print_and_save()
    open_file(file_path)


main()


