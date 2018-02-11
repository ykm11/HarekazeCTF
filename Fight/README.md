# [Crypto 100] Fight  
This problem requires Euler's totient(phi) function.  
Without the theory, it will take too long time to calculate seed-value.  
Here is [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function) .

As you make out `gen\_seed()` means Euler's totient function, all you have to do is calculate, or search on this [site](https://www.wolframalpha.com/input/?i=totient+function+of+4529255040439033800342855653030016000)  
<br />
You can get seed-value easily by means of [sageMath script](https://github.com/ykm11/HarekazeCTF2018/blob/master/Fight/get_seed.sage)  
<br />
<br />
Finally, we know seed-value.  
Let's get the FLAG.  
Here is [solver script](https://github.com/ykm11/HarekazeCTF2018/blob/master/Fight/solver.py)
