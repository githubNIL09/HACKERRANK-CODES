n=int(input())
l=list(map(int, input().rstrip().split()))
l.sort()
print(n)
i=0
c=0
while(i<len(l)):
    if(l[i]==0):
        i+=1
    else:
        a=l[i]
        for j in range(i,len(l)):
            l[j]=l[j]-a
            if(l[j]==0):
                continue
            else:
                c+=1
        if(c>0):
            print(c)
        i+=1
    c=0
