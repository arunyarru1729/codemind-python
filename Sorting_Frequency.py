a=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if i not in d.keys() :
        d[i]=1
    else:
        d[i]+=1
l=[]
c=0
for i in d:
    if d[i]>1:
        c+=1
for j in range(c):
    m=ele=0
    for i in d:
        if d[i]>m:
            m=d[i]
            ele=i
    l.append(ele)
    d[ele]=0
another=[]
for i in d:
    if d[i]>0:
        another.append(i)
another.sort()
for i in another:
    l.append(i)
print(*l)