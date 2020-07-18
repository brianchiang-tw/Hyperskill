# Write your code here
import sqlite3
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

    if 0 == digit_sum:
        last_digit = 0
    else:
        last_digit = 10 - digit_sum

    return account_num + str(last_digit)



def menu():

    connection, cursor = None, None
    try:
        connection = sqlite3.connect('card.s3db')
        cursor = connection.cursor()

        sql_remove_old_table = 'DROP TABLE IF EXISTS card;'
        cursor.execute(sql_remove_old_table)
        connection.commit()


        sql_create_table = '''CREATE TABLE IF NOT EXISTS card(
id INTEGER,
number TEXT PRIMARY KEY,
pin TEXT,
balance INTEGER DEFAULT 0
)
;
'''
        cursor.execute(sql_create_table)
        connection.commit()
    except Exception as e:
        print(e)


    record_id = -1

    choice = -1
    message = ['1. Create an account', '2. Log into account', '0. Exit']

    while choice != 0:

        print('\n'.join(message))
        choice = int(input())

        if choice == 1:


            account_num_str = create_account_with_Luhn_code()
            account_pin = str(random.randint(0, 9999)).zfill(4)
            record_id += 1

            sql_create_account='INSERT INTO card (id, number, pin, balance) VALUES(?, ?, ?, ?);'
            cursor.execute(sql_create_account, (record_id, account_num_str, account_pin, 0))
            connection.commit()


            print()
            print('Your card has been created')
            print('Your card number:')
            print(account_num_str)

            print('Your card PIN:')
            print(account_pin)

            # new line after account creation
            print()

        elif choice == 2:

            account_num = input('Enter you card number:')
            account_pin = input('Enter your PIN:')

            try:
                sql_read_account = f'SELECT number, pin, balance FROM card WHERE number = {account_num};'
                cursor.execute(sql_read_account)
                account_query = cursor.fetchone()

            except sqlite3.OperationalError as e:
                # SQL error during query
                print('SQL Error')
                print(e)
                continue



            if account_query:
                query_card_number, query_card_pin, query_card_balance = account_query


            if account_query is None or query_card_pin != account_pin:
                # Invalid account number or invalid account PIN
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
                        print('Balance: ', query_card_balance)
                        print()

                    elif sub_choice == 2:
                        print('\nYou have successfully logged out!\n')
                        sub_choice = 0

                    elif sub_choice == 0:
                        choice = 0
                        break

        elif choice == 3:
                # Debug mode for programmer
                sql_read_all = 'SELECT * FROM card;'
                cursor.execute(sql_read_all)
                account_queries = cursor.fetchall()
                for account in account_queries:
                    print(account)

                print()

        if choice == 0:
            print('\nBye!\n')


    # Safely log out from Database
    connection.commit()
    cursor.close()
    connection.close()

# ---------------------------------------

menu()
