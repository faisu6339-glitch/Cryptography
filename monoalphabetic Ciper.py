Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
alphabets = [chr(x) for x in range(97,123)]
alphabets
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import random as r
key = alphabets.copy()
key
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r.shuffle(key)
key
['w', 'k', 'v', 't', 'x', 'o', 'z', 'f', 'j', 's', 'c', 'y', 'i', 'a', 'u', 'q', 'e', 'b', 'm', 'n', 'p', 'l', 'd', 'r', 'g', 'h']
def keygen():
    key = [chr(x) for x in range(97,123)]
    r.shuffle(key)
    return key

keygen()
['y', 'h', 'z', 'j', 'p', 'i', 'g', 'w', 'b', 'e', 'c', 'r', 'v', 'n', 'd', 't', 'q', 'f', 'o', 'x', 'l', 'k', 'm', 'a', 'u', 's']
keygen()
['g', 'v', 'z', 'r', 'd', 'x', 'h', 'm', 'w', 'i', 'o', 'l', 'f', 'p', 'e', 'u', 'b', 'n', 'c', 'q', 'y', 'k', 'a', 'j', 's', 't']
alphabets
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = dict(zip(alphabets,keygen()))
code
{'a': 'y', 'b': 'n', 'c': 'a', 'd': 'o', 'e': 'v', 'f': 'f', 'g': 'q', 'h': 'e', 'i': 'x', 'j': 'd', 'k': 's', 'l': 'k', 'm': 'g', 'n': 'r', 'o': 'h', 'p': 'i', 'q': 'l', 'r': 'z', 's': 'w', 't': 't', 'u': 'u', 'v': 'p', 'w': 'j', 'x': 'm', 'y': 'c', 'z': 'b'}
code
{'a': 'y', 'b': 'n', 'c': 'a', 'd': 'o', 'e': 'v', 'f': 'f', 'g': 'q', 'h': 'e', 'i': 'x', 'j': 'd', 'k': 's', 'l': 'k', 'm': 'g', 'n': 'r', 'o': 'h', 'p': 'i', 'q': 'l', 'r': 'z', 's': 'w', 't': 't', 'u': 'u', 'v': 'p', 'w': 'j', 'x': 'm', 'y': 'c', 'z': 'b'}
def enc(code):
    message = input('enter your message')
...     cipher = []
...     for i in message:
...         cipher.append(code[i])
... 
...     
>>> def enc(code):
...     message = input('enter your message')
...     cipher = []
...     for i in message:
...         cipher.append(code[i])
...     return ''.join(cipher)
... 
>>> enc(code)
enter your messagehello
'evkkh'
>>> 
>>> code.values()
dict_values(['y', 'n', 'a', 'o', 'v', 'f', 'q', 'e', 'x', 'd', 's', 'k', 'g', 'r', 'h', 'i', 'l', 'z', 'w', 't', 'u', 'p', 'j', 'm', 'c', 'b'])
>>> decode = list(code.values())
>>> decode
['y', 'n', 'a', 'o', 'v', 'f', 'q', 'e', 'x', 'd', 's', 'k', 'g', 'r', 'h', 'i', 'l', 'z', 'w', 't', 'u', 'p', 'j', 'm', 'c', 'b']
>>> decode = dict(zip(decode,alphabets))
>>> decode
{'y': 'a', 'n': 'b', 'a': 'c', 'o': 'd', 'v': 'e', 'f': 'f', 'q': 'g', 'e': 'h', 'x': 'i', 'd': 'j', 's': 'k', 'k': 'l', 'g': 'm', 'r': 'n', 'h': 'o', 'i': 'p', 'l': 'q', 'z': 'r', 'w': 's', 't': 't', 'u': 'u', 'p': 'v', 'j': 'w', 'm': 'x', 'c': 'y', 'b': 'z'}
>>> def dec(key):
...     cipher = input('enter your cipher text.')
...     decrypt = []
...     for i in cipher:
...         decrypt.append(key[i])
...     return ''.join(decrypt)
... 
>>> dec(decode)
enter your cipher text.evkkh
'hello'
