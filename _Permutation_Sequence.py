from itertools import permutations
a,b=map(int,input().split())
s=[str(i) for i in range(1,a+1)]
s=''.join(s)
lst=list(permutations(s))
re=lst[b-1]
re=''.join(re)
print(re)