import math
s1 = raw_input()
x = []
y = []
for i in range(int(s1)):
	s2 = raw_input().split()
	x.append(int(s2[0]))
	y.append(int(s2[1]))
disx= 0
disy=0
longest = 0
for i in range(len(x)):
	for j in range(len(y)):
		disx = abs(x[i]-x[j])
		disy = abs(y[i]-y[j])
		if(disy>disx):
			disx = disy
		if (disx>longest):
			longest = disx
#longest_dis = math.sqrt(longest)
print longest**2
