import math
def encryption(s):
    
    s1,s2="",""
    n1,n2=[],[]
    aditi=0
    for i in range(0,len(s)):
        if(s[i]==" "):
            continue
        else:
            s1=s1+s[i]
    n=len(s1)
    a=math.sqrt(n)
    a1=math.floor(a)
    a2=math.ceil(a)
    if(a1*a2>=n):
        for i in range(0,a1):
            for j in range(0,a2):
                if(aditi==n):
                    break
                else:
                    s2=s2+s1[aditi]
                    aditi+=1
            n1.append(s2)
            s2=""
    elif(a1*a2<n):
        a1=a2
        for i in range(0,a1):
            for j in range(0,a2):
                if(aditi==n):
                    break
                else:
                    s2=s2+s1[aditi]
                    aditi+=1
            n1.append(s2)
            s2=""
    aditi=0
    a=""
    if(len(n1[a1-1])<a2):
        a3=a2-len(n1[a1-1])
        s3=n1[a1-1]
        for i in range(0,a3):
            s3=s3+" "
        n1[a1-1]=s3
    for i in range(0,a2):
        for j in range(0,len(n1)):
            if(n1[j][aditi]==" "):
                break
            else:
                a=a+n1[j][aditi]
        n2.append(a)
        aditi+=1
        a=""
    return n2
            
            
        
            
    
    
    