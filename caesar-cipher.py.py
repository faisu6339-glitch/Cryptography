l = [x for x in range(97,123)]
alphabets = [chr(x) for x in l]
pos_values = [x for x in range(26)]
text = dict(zip(alphabets, pos_values))
value = dict(zip(pos_values, alphabets))

def enc(key, plain):
    char_val = (key+text[plain])%26
    char = value[char_val]
    return char

def dec(key, plain):
    char_val = (text[plain]-key)%26
    char = value[char_val]
    return char

def encrypt():
    key = int(input("enter your key\n"))
    message = input('enter your message to be encrypted')
    m = []
    for i in message:
        c = enc(key, i)
        m.append(c)
    for i in m:
        print(i,end='')

def decrypt():
    key = int(input('enter your key'))
    cipher = input("enter your ciphered text")
    m = []
    for i in cipher:
        c = dec(key, i)
        m.append(c)
    for i in m:
        print(i, end='')

def cipher():
    print("to encrypt press 'E' and to decrypt press 'D'")
    i = input('enter your command\n')
    if i == 'E' or i == 'e':
        encrypt()
    elif i=='D' or i=='d':
        decrypt()

cipher()