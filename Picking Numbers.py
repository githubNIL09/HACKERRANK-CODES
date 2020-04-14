def pickingNumbers(a):
    a.sort()
    c,max=1,0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if(abs(a[i]-a[j])<2):
                c+=1
        if(c>max):
            max=c
        c=1
    return max

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
print(str(result) + '\n')
