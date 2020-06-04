s=input()
l=[]
i=0
while i<len(s):
    l.append(s[i])
    i+=2
l.sort()
l="+".join(l)
print(l)
