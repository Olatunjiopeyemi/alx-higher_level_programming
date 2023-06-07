#!/usr/bin/python3
count = 0
for n in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(n - count)), end="")
    count = 32 if count == 0 else 0
