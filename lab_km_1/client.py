import socket
import json

HOST = '127.0.0.1'
PORT = 6543
command_set = ["Who", "Start game", "shoot"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        command = str(input("Enter command:\n"))
        if command in command_set or command[0:6] == "shoot ":
            s.sendall(command.encode("utf-8"))
            inp = s.recv(1024).decode("utf-8")
            inp = inp.replace("\'", "\"")
            data = json.loads(inp)
            for key in data:
                if key == "text":
                    print (data[key])
                elif key == "table":
                    for line in data[key]:
                        print(line)
                    
            
            