def workbook(n, k, arr):
    c,c1,c2=0,0,1
    a,b=[],[]
    for i in range(n):
        for j in range(arr[i]):
            c+=1
            if(c<k+1):
                a.append(j+1)
            else:
                c=1
                b.append(a)
                a=[]
                a.append(j+1)
        if(a==[]):
            continue
        else:
            b.append(a)
            a=[]
            c=0
    for i in range(len(b)):
        for j in range(len(b[i])):
            if(b[i][j]==c2):
                print(b[i][j])
                c1+=1
        c2+=1
    return c1
