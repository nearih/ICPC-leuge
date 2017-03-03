s1 = raw_input()
s2 = raw_input()

k = ['q','w','e','r','t','y','u','i','o','p','[',']','\\','a','s','d','f','g','h','j','k','l',';','\,','z','x','c','v','b','n','m',',','.','/']
if (s1 == 'R'):
	l = -1
else:
	l = 1
word = ''
for i in s2:
	word = word + k[k.index(i)+l]
print word
