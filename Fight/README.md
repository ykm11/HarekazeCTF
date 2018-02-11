# [Crypto 100] Fight  
This problem requires [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function).
Without the theory, it will take too long time to calculate seed-value.  
As you make out `gen_seed()` means Euler's totient function, all you have to do is calculate, or search on this [site](https://www.wolframalpha.com/input/?i=totient+function+of+4529255040439033800342855653030016000)  
<br />
You can get seed-value easily by means of [sageMath script](https://github.com/ykm11/HarekazeCTF2018/blob/master/Fight/get_seed.sage)  

```get_seed.sage
s = 4529255040439033800342855653030016000
seed = 1
for p, e in factor(s):
  seed *= pow(p, e) - pow(p, e-1)
print(seed)
```

<br />
<br />
Finally, we know seed-value.  
Let's get the FLAG.  

```solver.py(partialy)
enc = base64.b64decode(b"7XDZk9F4ZI5WpcFOL/z6X6W9zDQuiA47sVJfaZxm1nNI")
random.seed(str(seed).rstrip("0"))
key = bytes([random.randint(0,255) for _ in enc])

flag = xor(enc, key)
print(flag)
```

Here is [solver script](https://github.com/ykm11/HarekazeCTF2018/blob/master/Fight/solver.py)  

Flag is `HarekazeCTF{3ul3rrrrrrrrr_t0000000t1nt!!!!!}`  
<br />  
<br />  
By the way, the problem name, Fight, is derived from Phi.  
Did you know?  
