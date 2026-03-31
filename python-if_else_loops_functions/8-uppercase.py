#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:  # kiçik hərflər a-z
            print("{}".format(chr(ord(c) - 32)), end="")  # böyük hərfə çevir
        else:
            print("{}".format(c), end="")  # digər simvolları olduğu kimi çap et
    print()  # yeni sətr
