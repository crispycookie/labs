import socket

HOST = '127.0.0.1'
PORT = 65432

def form_table():
    table = [[0 for i in range(10)] for j in range(10)]
    for i in  range(len(table)):
        print(table[i])
    return table

def form_stat():
    stat = [0, 0, 0]
    return stat

def change_table(table, i, j):
    print(i, "i")
    table[i-1][j-1] = 1
    return table
    


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:

            data = conn.recv(1024).decode("utf-8")
            output = {}

            if data == "Who":
                text = "Божко Максим, К-23"
                output["text"] = text
                conn.send(bytes(str(output), "utf-8"))
            elif data == "Start game":
                text = "Started"
                table = form_table()
                stat = form_stat()
                conn.send(bytes("table", "utf-8"))
                conn.send(bytes(str(table), "utf-8"))
            elif data == "shoot":
                print(table, type(table))
                print("***********")
                table = change_table(table, 3, 5)
                print(table)
                conn.send(bytes("table", "utf-8"))
                conn.send(bytes(str(table), "utf-8"))
