from registres import *

def name_parser(in_name, arg):
    if in_name=="ins":
        return format(int(arg[1:]), "#014b")+format(0, "012b")
    elif in_name=="add":
        return format(int(arg[1:], 2), "#014b")+format(1, "012b")

def arg0_parser(in_arg):
    for reg in ["R0", "R1", "R2", "R3"]:
        if in_arg==reg:
            return eval(reg)

def arg1_parser(in_arg):
    if in_arg.isdigit():
        return bin(int(in_arg))
    else:
         return arg0_parser(in_arg)

def calc_add(ARG0, ARG1):
    setter = "0b"
    ARG0 = format(int(ARG0, 2), "#026b")
    ARG1 = format(int(ARG1, 2), "#026b")
    num = int(ARG1[17:25], 2)
    for i in range(0, 24, 8):
        setter += "0000000" + str((num+int(ARG0[18-i:26-i], 2))%2)
    return setter

def write(cmd, i):
    global NAME, ARG0, ARG1, C, T
    ARG0 = arg0_parser(cmd[cmd.index("(")+1:cmd.index(", ")])
    NAME = name_parser(cmd[:cmd.index("(")], cmd[cmd.index("(")+1:cmd.index(", ")])
    ARG1 = arg1_parser(cmd[cmd.index(", ")+2:cmd.index(")")])
    C = bin(i)
    T = bin(1)
    return format(int(NAME, 2), "#026b"), format(int(ARG0, 2), "#026b"), format(int(ARG1, 2), "#026b"), format(int(C, 2), "#026b"), format(int(T, 2), "#026b")

def do(NAME):
    global R0, R1, R2, R3, ARG0, ARG1
    T = bin(2)
    if int("0b"+NAME[14:], 2)==0: #ins
        if int(NAME[:14], 2)==0:
            R0 = ARG1
        elif int(NAME[:14], 2)==1:
            R1 = ARG1
        elif int(NAME[:14], 2)==2:
            R2 = ARG1
        elif int(NAME[:14], 2)==3:
            R3 = ARG1
    elif int("0b"+NAME[14:], 2)==1: #add
        setter = calc_add(ARG0, ARG1)
        if int(NAME[:14], 2)==0:
            R0 = setter
        if int(NAME[:14], 2)==1:
            R1 = setter
        if int(NAME[:14], 2)==2:
            R2 = setter
        if int(NAME[:14], 2)==3:
            R3 = setter
    return format(int(R0, 2), "#026b"), format(int(R1, 2), "#026b"), format(int(R2, 2), "#026b"), format(int(R3, 2), "#026b"), format(int(T, 2), "#026b")
