#!/usr/bin/env python3
alphabet = ""

for i in range(97, 123):
    letter = chr(i)
    if letter != "e" and letter != "q":
        alphabet += letter

print("{}".format(alphabet))
