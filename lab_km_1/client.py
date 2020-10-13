import socket
import json

HOST = '127.0.0.1'
PORT = 65432
command_set = ["Who", "Start game", "Exit"]

def receive_data(inp):
    inp = inp.replace("\'", "\"")
    data = json.loads(inp)
    return data

def print_data(data, closed):
    for key in data:
        if key == "text":
            print (data[key])
        elif key == "table":
            for line in data[key]:
                print(line)
        elif key == "exit":
            print(data[key])
            closed = True
    return closed

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    closed = False

    while not closed:
        command = str(input("Enter command:\n"))
        if command in command_set or command[0:6] == "Shoot ":
            s.send(command.encode("utf-8"))
            data = receive_data(s.recv(1024).decode("utf-8"))
            closed = print_data(data, closed)
    s.close()
            
                    
                    
                    
            
            