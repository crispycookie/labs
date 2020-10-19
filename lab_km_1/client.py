import socket

HOST = '127.0.0.1'
PORT = 65432
command_set = ["Who", "Start game", "Exit"]

def print_table(data):
    table = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
    for s in data:
        s = format(s, "08b")
        for i in range(4):
            table.append(int(s[2*i:2*i+2], 2))
    for j in range(11):
        print(str(j)+" "*(2-len(str(j))), end = " ")
        for k in range(10):
            print(table[10*j+k], end=" ")
        print("")

def print_text(data):
    print(data.decode("utf-8"))

def print_data(head, data):
    if head == 1: #text
        print_text(data)
    elif head == 2: #table
        print_table(data)
    elif head == 3: #stat
        pass
    return closed

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    closed = False

    while not closed:
        command = str(input("Enter command:\n"))
        if command in command_set or command[0:6] == "Shoot ":
            s.send(command.encode("utf-8"))
            data = s.recv(1024)
            if data[0]:
                print_data(data[0], data[1:])
            else:
                print(data[1:].decode("utf-8"))
                closed = True
    s.close()
