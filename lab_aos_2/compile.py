from funcs import *

command_set = []
with open("commands.py", "r") as commands:
    for line in commands:
        command_set.append(line[:len(line)-1])
i = 1
for cmd in command_set:

    smth = input("next1:")
    NAME, ARG0, ARG1, C, T = write(cmd, i)
    print("NAME", NAME[2:10], NAME[10:18], NAME[18:26], "(" + str(int(NAME, 2)) + ")") 
    print("ARG0", ARG0[2:10], ARG0[10:18], ARG0[18:26], "(" + str(int(ARG0, 2)) + ")")
    print("ARG1", ARG1[2:10], ARG1[10:18], ARG1[18:26], "(" + str(int(ARG1, 2)) + ")")
    print("C   ", C[2:10], C[10:18], C[18:26], "(" + str(int(C, 2)) + ")")
    print("T   ", T[2:10], T[10:18], T[18:26], "(" + str(int(T, 2)) + ")")
    print("RO  ", R0[2:10], R0[10:18], R0[18:26], "(" + str(int(R0, 2)) + ")") 
    print("R1  ", R1[2:10], R1[10:18], R1[18:26], "(" + str(int(R1, 2)) + ")")
    print("R2  ", R2[2:10], R2[10:18], R2[18:26], "(" + str(int(R2, 2)) + ")")
    print("R3  ", R3[2:10], R3[10:18], R3[18:26], "(" + str(int(R3, 2)) + ")")

    smth = input("next2:")
    R0, R1, R2, R3, T = do(NAME)
    print("NAME", NAME[2:10], NAME[10:18], NAME[18:26], "(" + str(int(NAME, 2)) + ")") 
    print("ARG0", ARG0[2:10], ARG0[10:18], ARG0[18:26], "(" + str(int(ARG0, 2)) + ")")
    print("ARG1", ARG1[2:10], ARG1[10:18], ARG1[18:26], "(" + str(int(ARG1, 2)) + ")")
    print("C   ", C[2:10], C[10:18], C[18:26], "(" + str(int(C, 2)) + ")")
    print("T   ", T[2:10], T[10:18], T[18:26], "(" + str(int(T, 2)) + ")")
    print("RO  ", R0[2:10], R0[10:18], R0[18:26], "(" + str(int(R0, 2)) + ")") 
    print("R1  ", R1[2:10], R1[10:18], R1[18:26], "(" + str(int(R1, 2)) + ")")
    print("R2  ", R2[2:10], R2[10:18], R2[18:26], "(" + str(int(R2, 2)) + ")")
    print("R3  ", R3[2:10], R3[10:18], R3[18:26], "(" + str(int(R3, 2)) + ")")
    i+=1
#    do(NAME, ARG0, ARG1)

