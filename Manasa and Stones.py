t=int(input())
for i in range (t):
    n=int(input())
    a=int(input())
    b=int(input())
    su=0
    first=0
    first=(n-1)*min(a,b)
    print(first,end=' ')
    while(su+first<(n-1)*max(a,b)):
        su+=abs(b-a)
        print(first+su,end=' ')
    print()

