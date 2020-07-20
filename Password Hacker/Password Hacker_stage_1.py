# write your code here

import socket
from sys import argv
def main():

    if len(argv) == 1:
        print("Parameter list is empty")
        exit()
    elif len(argv) != 4:
        print("Length of parameter list is wrong")
        exit()

    hostname = argv[1]
    port = int(argv[2])
    data = argv[3]

    buffer_size = 1024

    address = (hostname, port)

    with socket.socket() as client_socket:

        client_socket.connect(address)

        # covert from string to byte
        data = data.encode()

        # send data from client to server
        client_socket.send(data)

        # receive data from server to client
        response = client_socket.recv(buffer_size)

        # convert from byte to string
        response = response.decode()

        print(response)

    return



# Entry point of program
if __name__ == '__main__':

    main()
