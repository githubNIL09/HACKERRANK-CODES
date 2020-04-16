def biggerIsGreateer(w):
    n=len(w)
    a=[]
    str=""
    i,temp=n-1,0
    for i in range(0,n):
        a.append(w[i])
    while(i>0 and w[i-1]>=w[i]):
        i-=1
    if i==0:
        print("no answer")
    else:
        j=n-1
        while(j>0 and w[j]<=w[i-1]):
            j-=1
        temp=a[i-1]
        a[i-1]=a[j]
        a[j]=temp
        j=n-1
        while i<j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            i+=1
            j-=1
        for i in range(0,n):
            str+=a[i]
    return str
    
    
        
        
    
    
