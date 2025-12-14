n=int(input())
s=[]
for i in range(1,n):
    if i**3<n:
        s.append(i**3)
    else:
        break
print(*s)
