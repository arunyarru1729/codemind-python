s=input()
i=j=i1=0
l=len(s)
for i in range(l):
    val=0
    if (s[i]=='#'):
        for j in range(i1,i-2):
            print(chr(ord(s[j])-48+96),end="")
        val=(ord(s[i-2])-48)*10+ord(s[i-1])-48+96
        print(chr(val),end="")
        i1=i+1
    if i==l-1:
        for j in range(i1,l):
            val=ord(s[j])-48+96
            print(chr(val),end="")
        break