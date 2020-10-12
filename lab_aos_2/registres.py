from random import randint

NAME = bin(randint(0, 2**24-1))
ARG0 = bin(randint(0, 2**24-1))
ARG1 = bin(randint(0, 2**24-1))
C = bin(randint(0, 2**24-1))
T = bin(randint(0, 2**24-1))
R0 = format(int(bin(randint(0, 2**24-1)), 2), "#026b")
R1 = format(int(bin(randint(0, 2**24-1)), 2), "#026b")
R2 = format(int(bin(randint(0, 2**24-1)), 2), "#026b")
R3 = format(int(bin(randint(0, 2**24-1)), 2), "#026b")