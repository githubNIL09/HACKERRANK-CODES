def kaprekarNumber(n):
    str1=""
    m=n*n
    a=str(n*n)
    b=str(n)
    a1=len(a)
    b1=len(b)
    if(a1==2*b1 or a1==2*b1-1):
        y=0
        while(y<b1):
            r=m%10
            str1=str(r)+str1
            m=m//10
            y+=1
    k=int(str1)+m
    if(k==n):
        return True
    else:
        return False