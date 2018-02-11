# [Crypto 200] Round and Round  
In this challenge, you saw encrypted message and complicated p1 and q1 as parametars.
The goal is obtain two prime numbers, p and q.  
There are several way to get these numbers. Here I explain a way by using binary search. 
<br />
As the FLAG says, I expected binary search, but some guys tought me the other solutions.
Thank you bery much!!
<br />
<br />
So now, let me explain.
At first, how works `(p-1)^i : i = 0, 1, 2, ....` ?  
It shows `1, p-1, 1, p-1, 1, ...`
the sum of group([1, p-1, ...]) come to p, 2p, 3p, ... every twice.  
We can generalize it.  

```
sum_p = p * (z-1)*/2 + 1 where p is prime, z is repeating count and odd

```

In this challenge
```
p1 = p * (q-1)/2 + 1
q1 = q * (p-1)/2 + 1
```


<br />
Problem script is as follofing  

```
p1 = (sum([pow(p-1, i, p) for i in range(q)]))
q1 = (sum([pow(q-1, i, q) for i in range(p)]))
```
