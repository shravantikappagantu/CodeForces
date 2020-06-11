#Nearly Lucky Number

n=input()
c=0
for i in range(len(n)):
    if n[i]=="4" or n[i]=="7":
        c+=1
if c==4 or c==7:
    print("YES")
else:
    print("NO")
