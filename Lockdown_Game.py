n=int(input())
a=[]
for i in range(1,n+1):
    a.append(i)
r=input()
s=0
c=0
#print(r,n)
while (len(a)!=1):
    
    #print(r[s],a[c])
    if r[s]=='y':
        a.pop(c)
        s+=1
    else:
        s+=1
        c+=1
    if (s>len(r)-1):
        s=0
    if (c>len(a)-1):
        c=0
print(*a)