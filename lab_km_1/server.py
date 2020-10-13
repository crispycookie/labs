import socket

HOST = '127.0.0.1'
PORT = 6543

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
#    try:
    if True:
        coords1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coords2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
        c1 = int(inp[:len(inp)-1])
        c2 = inp[len(inp)-1]
        if c1 in coords1  and c2 in coords2:
            return c1, coords2.index(c2)+1
        else:
            return "Error"
            



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
                table = form_table()
                stat = form_stat()
                output["table"] = table
                conn.send(bytes(str(output), "utf-8"))
            elif data[:5] == "shoot":
                numbers = check_tail(data[6:])
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
