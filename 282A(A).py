s1 = raw_input()
n = 0
for i in range(int(s1)):
	s2 = raw_input()	
	for j in range(3):		
		if (s2[j]=='+'):
			n = n+ 0.5
		elif(s2[j]=='-'):
			n = n - 0.5
print int(n)
