# Write your code here
import random
from datetime import datetime

random.seed(datetime.now())



account_pin_dict = {}

account_balance_dict = {}

def create_account_with_Luhn_code():

    account_num = '400000' + str(random.randint(0, 10**9-1)).zfill(9)

    account_list = [*account_num]

    for i in range( -1, -len(account_list)-1, -2 ):

        if i % 2 == 1:
            new_digit = int(account_list[i])*2

            if new_digit > 9:
                new_digit -= 9

            account_list[i] = new_digit

    digit_sum = sum( map(int, account_list) ) % 10
    last_digit = 10 - digit_sum

    return account_num + str(last_digit)



def menu():

    choice = -1
    message = ['1. Create an account', '2. Log into account', '0. Exit']

    while choice != 0:

        print('\n'.join(message))
        choice = int(input())

        if choice == 1:

            #account_num = '400000' + str(random.randint(0, 10**10-1)).zfill(10)
            account_num = create_account_with_Luhn_code()
            account_pin = str(random.randint(0, 9999)).zfill(4)

            account_pin_dict[account_num] = account_pin
            account_balance_dict[account_num] = 0

            print()
            print('Your card has been created')
            print('Your card number:')
            print(account_num)

            print('Your card PIN:')
            print(account_pin)

            # new line after account creation
            print()

        elif choice == 2:

            account_num = input('Enter you card number:')
            account_pin = input('Enter your PIN:')

            if (account_num not in account_pin_dict) or (account_pin_dict[account_num] != account_pin):
                print('\nWrong card number or PIN!\n')

            else:
                print('\nYou have successfully logger in!\n')

                msg_log_in = ['1. Balance', '2. Log out', '0. Exit']

                sub_choice = -1
                while sub_choice != 0:

                    print('\n'.join(msg_log_in))

                    sub_choice = int(input())

                    if sub_choice == 1:
                        print()
                        print('Balance: ', account_balance_dict[account_num])
                        print()

                    elif sub_choice == 2:
                        print('\nYou have successfully logged out!\n')
                        sub_choice = 0

                    elif sub_choice == 0:
                        choice = 0
                        break


        if choice == 0:
            print('\nBye!\n')



# ---------------------------------------

menu()
