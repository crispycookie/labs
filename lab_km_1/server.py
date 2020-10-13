import socket
import os
from _thread import start_new_thread

HOST = '127.0.0.1'
PORT = 65432

def form_table():
    head = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
    table = [[("0" if i else str(j)) for i in range(11)] if j else head for j in range(11)]
    return table

def form_stat():
    stat = [0, 0, 0]
    return stat

def change_table(table, i, j):
    if table[i][j]!="X":
        table[i][j] = "X"
        return table
    else:
        return "Already"

def check_tail(inp):
    try:
        coords1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coords2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
        c1 = int(inp[:len(inp)-1])
        c2 = inp[len(inp)-1]
        if c1 in coords1  and c2 in coords2:
            return c1, coords2.index(c2)+1
        else:
            return "Error"
    except:
        return "Error"

def Who():
    output = {}
    text = "Божко Максим, К-23"
    output["text"] = text
    conn.send(bytes(str(output), "utf-8"))

def Start_game():
    output = {}
    table = form_table()
    stat = form_stat()
    output["table"] = table
    conn.send(bytes(str(output), "utf-8"))
    return table, stat

def Shoot(data, table):
    output = {}
    numbers = check_tail(data)
    if numbers=="Error":
        output["text"] = "incorrect coords. Example: shoot 5b"
        conn.send(bytes(str(output), "utf-8"))
    else:
        ans = change_table(table, numbers[0], numbers[1])
        if ans=="Already":
            output["text"] = "Already attacked"
            conn.send(bytes(str(output), "utf-8"))
        else:
            table = ans
            output["table"] = table
            conn.send(bytes(str(output), "utf-8"))
    return table

def Exit():
    output = {}
    text = "Connection closed"
    output["exit"] = text
    conn.send(bytes(str(output), "utf-8"))
    conn.close()

def Main(conn, addr):
    print("MAIN")
    table = None
    while True:
        print(addr)
        data = conn.recv(1024).decode("utf-8")
        output = {}

        if data == "Who":
            Who()
        elif data == "Start game":
            table, stat = Start_game()
        elif data[:5] == "Shoot":
            table = Shoot(data[6:], table)
        elif data == "Exit":
            Exit()
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        start_new_thread(Main, (conn, addr))



