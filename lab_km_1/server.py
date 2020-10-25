import socket
#import os
#from _thread import start_new_thread, enumerate
from random import randrange
import threading

HOST = '127.0.0.1'
PORT = 6543

def form_table():
    table = bytes([0 for i in range(25)])
    return table
    
def form_stat():
    stat = [0, 0, 0]
    return stat

def dead_ship(table, i, j):
    byte_pos = (10*i+j)//4
    from_pos = 2*((10*i+j)%4)
    to_pos = 2*((10*i+j)%4+1)
    bt = format(table[byte_pos], "08b")
    bit2 = format(int("3", 4), "02b")
    bt = bt[:from_pos]+bit2+bt[to_pos:]
    table = table[:byte_pos]+bytes([int(bt, 2)])+table[byte_pos+1:]
    print(table)
    return table

def change_table(table, ships, lives, i, j):
    byte_pos = (10*i+j)//4
    from_pos = 2*((10*i+j)%4)
    to_pos = 2*((10*i+j)%4+1)
    print(byte_pos, table)
    bt = format(table[byte_pos], "08b")
    bit2 = int(bt[from_pos:to_pos], 4)
    if not bit2:
        print(lives)
        if lives[ships[10*i+j]]:
            lives[ships[10*i+j]] -= 1
            if lives[ships[10*i+j]]:
                bit2 = format(int("2", 4), "02b")
            else:
                for c in range(len(ships)):
                    if ships[10*i+j]==ships[c]:
                        print(357)
                        print(c)
                        table = dead_ship(table, c//10, c%10)
                return table, lives
        else:
            bit2 = format(int("1", 4), "02b")
        print("bit2", bit2)
        bt = bt[:from_pos]+bit2+bt[to_pos:]
        print("bt", int(bt, 2)]) )
        table = table[:byte_pos]+bytes([int(bt, 2)])+table[byte_pos+1:]
        print(table)
        return table, lives
    else:
        return "Already", lives

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

def create_ship(blocked, N):
    base = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    positions_set = []
    for i in range(10):
        for j in range(10):
            koef1 = True
            for t in range(N):
                koef1 *= 10*i+(j+t) not in blocked and (j+t) in base
            if koef1:
                positions_set.append(0+10*i+j)
            koef2 = True
            for t in range(N):
                koef2 *= 10*(i+t)+j not in blocked and (i+t) in base
            if koef2:
                positions_set.append(100+10*i+j)
    pos = randrange(len(positions_set))
    ship = positions_set[pos]
    if not positions_set[pos]//100:
        for i in range(((positions_set[pos]%100)//10)-1, ((positions_set[pos]%100)//10)+2):
            for j in range((positions_set[pos]%10)-1, (positions_set[pos]%10)+1+N):
                if i in base and j in base:
                    blocked.append(10*i+j)
    else:
        for i in range(((positions_set[pos]%100)//10)-1, ((positions_set[pos]%100)//10)+1+N):
            for j in range((positions_set[pos]%10)-1, (positions_set[pos]%10)+2):
                if i in base and j in base:
                    blocked.append(10*i+j)
    return blocked, ship

def spawn_ships():
    blocked = []
    ships = [0 for i in range(100)]
    itr = 1
    for item in (4, 3, 3, 2, 2, 2, 1, 1, 1, 1):
        blocked, ship = create_ship(blocked, item)
        if ship<100:
            for g in range(item):
                ships[ship+g] = itr
        else:
            for g in range(item):
                ships[ship%100+10*g] = itr
        itr += 1
    for t1 in range(10):
        for t2 in range(10):
            print(ships[t1*10+t2], end = " ")
        print("")
    return ships

def Who(conn):
    output= bytes([1]) + bytes("Божко Максим, К-23", "utf-8")
    conn.send(output)

def Start_game(conn):
    table = form_table()
    stat = form_stat()
    ships = spawn_ships()
    lives = [0, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    output = bytes([2]) + table
    conn.send(output)
    started = True
    return table, ships, stat, lives

def Shoot(conn, data, table, ships, lives):
    numbers = check_tail(data)
    if numbers=="Error":
        output = bytes([1]) + bytes("incorrect coords. Example: shoot 5b", "utf-8")
        conn.send(output)
    else:
        ans, lives = change_table(table, ships, lives, numbers[0], numbers[1])
        if ans=="Already":
            output = bytes([1]) + bytes("Already attacked", "utf-8")
            conn.send(output)
        else:
            table = ans
            output = bytes([2]) + table
            conn.send(output)
    return table, lives

def In_queue(conn, adr, queue):
    if queue:
        teammate = queue
        conn.send("Success!", "utf-8")
    else:
        teammate = None
        conn.send(bytes([4]) + bytes("Wait for opponent", "utf-8"))
    return adr, teammate

def Exit(conn):
    output = bytes([0]) + bytes("Connection closed", "utf-8")
    conn.send(output)
    conn.close()

def Main(conn, addr):
    global queue
    print("MAIN")
    table = None
    started = False
    
    while True:
        print(addr, queue)
        for thread in threading.enumerate():
            print(thread)
        data = conn.recv(1024).decode("utf-8")
        if data == "Who":
            Who(conn)
        elif data == "Battle":
            queue, teammate = In_queue(conn, addr[1], queue)
        elif data == "Start game":
            if not started:
                table, ships, stat, lives = Start_game(conn)
                started = True
            else:
                conn.send(bytes([1]) + bytes("Already started", "utf-8"))
        elif data[:5] == "Shoot":
            table, lives = Shoot(conn, data[6:], table, ships, lives)
        elif data == "Exit":
            Exit(conn)
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    queue = None
    while True:
        conn, addr = s.accept()
#        start_new_thread(Main, (conn, addr))
        thread_1 = threading.Thread(target = Main, args = (conn, addr, ))
        thread_1.name = "Address"+str(addr[1])
        thread_1.start()

