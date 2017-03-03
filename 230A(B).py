s = raw_input().split()
st = int(s[0])
dragon = []
for i in range(int(s[1])):
    drag = raw_input().split()
    drag[0] = int(drag[0])
    drag[1] = int(drag[1])
    dragon.append(drag)

q = sorted(dragon)


for i in range(len(dragon)):
    if (st > int(q[i][0])):
        st = st + int(q[i][1])
    else:
        print "NO"
        quit()
print "YES"
