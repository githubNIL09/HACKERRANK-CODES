def timeConversion(s):
    a=len(s)
    a1=s[a-2]
    a2=''
    if(a1=='P'):
        for i in range(0,2):
            a2+=s[i]
        if(a2=='12'):
            for i in range(2,a-2):
                a2+=s[i]
        elif(a2>='01' and a2<='11'):
            a2=str((int(a2)+12))
            for i in range(2,a-2):
                a2+=s[i]
    elif(a1=='A'):
        for i in range(0,2):
            a2+=s[i]
        if(a2=='12'):
            a2='00'
            for i in range(2,a-2):
                a2+=s[i]
        else:
            a2=''
            for i in range(0,a-2):
                a2+=s[i]
    return a2

s = input()
result = timeConversion(s)
print(result)

