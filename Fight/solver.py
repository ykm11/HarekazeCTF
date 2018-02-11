import base64
import random


def xor(msg, key):
    return bytes([ch1^ch2 for ch1, ch2 in zip(msg, key)])

enc = base64.b64decode(b"7XDZk9F4ZI5WpcFOfej3Dbau3yc1kxUgqmRCPMkzgyYFGjsRJF9aMaLHyDU=")
seed = 765753154007029226621575888896000000
random.seed(str(seed).rstrip("0"))
key = bytes([random.randint(0,255) for _ in enc])

flag = xor(enc, key)
print(flag)
