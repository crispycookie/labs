import socket

HOST = '127.0.0.1'
PORT = 65432
command_set = ["Who", "Start game", "shoot"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        command = str(input("Enter command:\n"))
        if command in command_set:
            s.sendall(command.encode("utf-8"))
            data = s.recv(1024)
            print(data.decode("utf-8"))
            data = s.recv(1024)
            print(data.decode("utf-8"))