def cutTheSticks(arr):
    arr.sort()
    n=len(arr)
    c1=n
    c=[]
    c.append(n)
    for i in range(0,n-1):
        if(arr[i]<=0):
            continue
        elif(i==n-2 and arr[i]==arr[i+1]):
            continue
        else:
            c1-=1
            for j in range(i+1,n):
                if(arr[i]==arr[j]):
                    c1-=1
                    arr[j]=arr[j]-arr[i]
                else:
                    arr[j]=arr[j]-arr[i]
        c.append(c1)
    return c


n = int(input())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
for i in range(0,len(result)):
    if(result[i]==0):
        break
    else:
        print(result[i])
