s = 4529255040439033800342855653030016000
seed = 1
for p, e in factor(s):
    seed *= pow(p, e) - pow(p, e-1)

print(seed)
