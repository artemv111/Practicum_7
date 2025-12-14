n=int(input())
for i in range(1,n):
    if 2**i==n:
        print('верно')
        break
else:
    print('неверно')
