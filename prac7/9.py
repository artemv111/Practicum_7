n,k,r=map(float,input().split())
for day in range(2,1000):
    pr = n / 100 * k
    n+=pr
    if n>=r:
        print(day)
        break
