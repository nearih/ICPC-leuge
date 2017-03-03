import random
s = raw_input().split()

r = float(s[0])/int(s[1])
z = float(s[2])/int(s[3])

num_sim = 20000
v = 0.0
for i in range(num_sim):
    c1 = ((1-r)**i)*((1-z)**i)*r
    v = v+ c1
print v
