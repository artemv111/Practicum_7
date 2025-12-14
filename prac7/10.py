ch=0
t=None
while True:
    n=float(input())
    if n==0:
        break
    if t is not None and n<t:
        ch+=1
    t=n
print(ch)


