arr=list(map(int,input().split(",")))
ls=[]
c=0

for i in range(len(arr)):
    s=0
    a=arr[i]
    for j in range(1,a+1):
        if a%j==0:
            s=s+j
    if s in arr:
        ls.append(a)
        c=c+1
if c==0:
    print("-1")
else:
    ls.sort()
    for i in ls:
        print(i,end=" ")