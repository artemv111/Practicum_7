s=[]
for i in range(100,1000):
    if i%17==0:
        s.append(i)
print(*s, len(s))