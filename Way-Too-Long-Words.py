n=int(input())
for i in range(n):
    s=input()
    l=[]
    if len(s)>10:
        l.append(s[0])
        l.append(str(len(s)-2))
        l.append(s[-1])
        l="".join(l)
        print(l)
    else:
        print(s)
