data = ''
for i in range(8):
    s = raw_input()
    data = data+s

dictb = {'q':9,'r':5,'b':3,'n':3,'p':1,'Q':-9,'R':-5,'B':-3,'N':-3,'P':-1}
lb = ['q','r','b','n','p','Q','R','B','N','P']
p1 = 0
for i in range(len(data)):
    for j in range(len(lb)):
        if (data[i] == lb[j]):
            p1 = p1 + dictb[lb[j]]
            
if (p1 > 0):
    print ("Black")
elif (p1 == 0):
    print ("Draw")
else:
    print ("White")

print (p1)    
print (data)