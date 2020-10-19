import socket
import os
from _thread import start_new_thread

HOST = '127.0.0.1'
PORT = 65432

def form_table():
    table = bytes([0 for i in range(25)])
    return table
    
def form_stat():
    stat = [0, 0, 0]
    return stat

def change_table(table, i, j):
    byte_pos = (10*i+j)//4
    from_pos = 2*((10*i+j)%4)
    to_pos = 2*((10*i+j)%4+1)
    bt = format(table[byte_pos], "08b")
    bit2 = int(bt[from_pos:to_pos], 4)
    if not bit2:
        bit2 = format(int("1", 4), "02b")
        bt = bt[:from_pos]+bit2+bt[to_pos:]
        table = table[:byte_pos]+bytes([int(bt, 2)])+table[byte_pos:]
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
            return c1-1, coords2.index(c2)
        else:
            return "Error"
    except:
        return "Error"

def Who(conn):
    output= bytes([1]) + bytes("Божко Максим, К-23", "utf-8")
    conn.send(output)

def Start_game(conn):
    table = form_table()
    stat = form_stat()
    output = bytes([2]) + table
    conn.send(output)
    started = True
    return table, stat

def Shoot(conn, data, table):
    numbers = check_tail(data)
    if numbers=="Error":
        output = bytes([1]) + bytes("incorrect coords. Example: shoot 5b", "utf-8")
        conn.send(output)
    else:
        ans = change_table(table, numbers[0], numbers[1])
        if ans=="Already":
            output = bytes([1]) + bytes("Already attacked", "utf-8")
            conn.send(output)
        else:
            table = ans
            output = bytes([2]) + table
            conn.send(output)
    return table

def Exit(conn):
    output = bytes([0]) + bytes("Connection closed", "utf-8")
    conn.send(output)
    conn.close()

def Main(conn, addr):
    print("MAIN")
    table = None
    started = False
    while True:
        print(addr)
        data = conn.recv(1024).decode("utf-8")
        if data == "Who":
            Who(conn)
        elif data == "Start game":
            if not_started:
                table, stat = Start_game(conn)
            else:
                conn.send(bytes([1]) + bytes("Already started", "utf-8"))
        elif data[:5] == "Shoot":
            table = Shoot(conn, data[6:], table)
        elif data == "Exit":
            Exit(conn)
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        start_new_thread(Main, (conn, addr))
