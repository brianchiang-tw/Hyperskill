# write your code here

import socket
from sys import argv
from itertools import product
from string import ascii_lowercase, digits
from time import sleep


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

    with socket.socket() as client_socket:

        client_socket.connect(address)

        test_counter = 0
        exit_flag = False

        with open('.\passwords.txt','r') as f:

            for line in f:

                line = line.strip()

                if exit_flag:
                    break

                # get all permutation with uppercase and lowercase of alphabetic letters
                all_permutation = permute_letters(line)

                for pwd_trial in all_permutation:

                    if not exit_flag and test_counter < 10 ** 6:

                        # generate attack data by dictionary
                        attack_data = pwd_trial

                        #sleep(0.00001)

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
                            print(f'exit flag {exit_flag}')
                            print(f'test count {test_counter}')
                            print(e)


                        test_counter += 1



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
