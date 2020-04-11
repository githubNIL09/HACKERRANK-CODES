a=input()
c=1
n=len(a)
i=0
if n==1:
    print((1,int(a)))
elif n > 1:
    while(i!=n-1):
        if(i==n-2):
            if(a[i]==a[i+1]):
                c+=1
                print((c,int(a[i])),end=" ")
            else:
                print((c,int(a[n-2])),end=" ")
                print((1,int(a[n-1])),end=" ")
        elif(a[i]==a[i+1]):
            c+=1
        elif(a[i]!=a[i+1]):
            print((c,int(a[i])),end=" ")
            c=1
        i+=1
    