s = raw_input()

if (len(s)==1):
    if (s < 'a'):
        print chr(ord(s) + (ord('a')-ord('A')))
        quit()
    else:
        print chr(ord(s) - (ord('a')-ord('A')))
        quit()

w = ""
for i in range(len(s)-1):
    if (s[i+1] < 'a'):
        w = w+chr(ord(s[i+1])+(ord('a')-ord('A')))
    else:
        print s
        quit()
if(s[0] <'a'):
    print chr(ord(s[0]) + (ord('a')-ord('A'))) + w
else:           
	print chr(ord(s[0]) - (ord('a')-ord('A'))) + w
