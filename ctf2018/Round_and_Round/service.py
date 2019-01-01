from Crypto.Util.number import *
from Crypto.Random.random import randint

import gmpy
import key
import binascii

flag = key.FLAG
#print(flag)
FLAG = binascii.hexlify(flag)
#print(FLAG)
FLAG = int(FLAG.decode('utf-8'), 16)
#print(FLAG)

def gen_n(bits=1024):
  p = getStrongPrime(bits)
  q = getStrongPrime(bits)
  return p*q, p, q

def main():
    n, p, q = gen_n()
    e = (1<<16)+1
    enc = pow(FLAG, e, n)
    print("enc =",enc)
#    print(p, q)
#    p = (sum([pow(p-1, i, p) for i in range(q)]))
#    q = (sum([pow(q-1, i, q) for i in range(p)]))

    p1 = (p-1) * (q // 2) + q // 2 + 1 # 配布ファイルはここを
    q1 = (q-1) * (p // 2) + p // 2 + 1 # 消しておくのを忘れない

    print("p =",p1)
    print("q =",q1)

if __name__ == "__main__":
    main()
