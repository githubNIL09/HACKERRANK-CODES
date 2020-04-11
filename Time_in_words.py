def single_dig(n):
    sd=""
    words=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
    for i in range(1,13):
        if(n==i):
            sd+=words[i-1]
    return sd

def after_ten(n):
    at=""
    i,j=10,0
    words1=["ten","eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen"]
    for i in range(10,20):
        if(n==i):
            at+=words1[j]
            break
        else:
            j+=1
    return at

def tens(n):
    at=""
    i,j=20,0
    words1=["twenty","half"]
    while(i<40):
        if(n==i):
            at+=words1[j]
            break
        else:
            j+=1
            i+=10
    return at

def timeInWords(h, m):
    final=""
    d=0
    if(m>30):
        d=60-m
        if(d==15):
            final+="quarter to "
        else:
            if(d<10):
                if(d>1):
                    final+=single_dig(d)+" minutes to "
                elif(d==1):
                    final+="one minute to "
            if(d>=10 and d<20):
                final+=after_ten(d)+" minutes to "
            elif(d>=20):
                if(d==20):
                    final+=tens(d)+" minutes to "
                elif(d>20 and d<30):
                    r=d%10
                    final+=tens(20)+" "
                    final+=single_dig(r)+" minutes to "
        if(h>=1 and h<12):
            final+=single_dig(h+1)
        elif(h==12):
            final+="one"
    elif(m==0):
        if(h>=1 and h<13):
            final+=single_dig(h)
        final+=" o' clock"
    elif(m<30):
        if(m==15):
            final+="quarter past "
        else:
            if(m<10):
                if(m>1):
                    final+=single_dig(m)+" minutes past "
                elif(m==1):
                    final+="one minute past "
            if(m>=10 and m<20):
                final+=after_ten(m)+" minutes past "
            elif(m>=20):
                if(m==20):
                    final+=tens(m)+" minutes past "
                elif(m>20 and m<30):
                    r=m%10
                    final+=tens(20)+" "
                    final+=single_dig(r)+" minutes past "
        if(h>=1 and h<13):
            final+=single_dig(h)
    elif(m==30):
        final+="half past "
        if(h>=1 and h<13):
            final+=single_dig(h)
    return final
        
        
        
        
    
    

