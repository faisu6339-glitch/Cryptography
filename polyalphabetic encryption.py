'''
This encryption is based on Polyalphabetic Encryption. This program only works for uppercase letters.
'''

import pandas as pd

# key generator of given length
def keygen(length):
    from random import randint as ri
    key = []
    for i in range(length):
        key.append(chr(ri(65,90)))
    return ''.join(key)

# tabula
tabula = {chr(x):[chr(x) for x in list(range(x,91))+list(range(65,x))] for x in range(65,91)}

key = "LOCKL"
message = "HELLO"

# binding


