s=input()
ar=[]
f=1
for i in range(len(s)):
    if s[i] in '({[':
        ar.append(s[i])
        f=1
    else:
        if len(ar)>0:
            if ar[-1]=='(' and s[i]==')':
                ar.pop()
            elif ar[-1]=='{' and s[i]=='}':
                ar.pop()
            elif ar[-1]=='[' and s[i]==']':
                ar.pop()
            else:
                print(i+1)
                f=0
                break
        else:
            print(i+1)
            f=0
            break
if f==1:
    if len(ar)==0:
        print(0)
    else:
        print(len(s)+1)