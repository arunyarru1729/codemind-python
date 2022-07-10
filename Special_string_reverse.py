s=input()
spc=[]
ar=''
spci=[]
for i in range(len(s)):
    if s[i] in "1234567890'!@#$%^&*()_+=-'""][}{:<>?,./'":
        spc.append(s[i])
        spci.append(i)
    else:
        ar+=s[i]
ar=''.join(ar)
ar=ar.strip()
ar=ar[::-1]
ar=list(ar)
j=0
for i in spci:
    ar.insert(i,spc[j])
    j+=1
ar=''.join(ar)
ar=ar.strip()
print(ar)