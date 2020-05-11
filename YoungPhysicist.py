n=int(input())
p=[]
for i in range (0,n):
    l=list(map(int,input().split()))
    p.append(l)
    #del l[:]
    l=[]
    #l.clear()
    #print(p)
#l.clear()
#print(p)
for  i in range(0,3):
    s=0
    flag=0
    for j in range(0,len(p)):
        s+=p[j][i]
    if(s!=0):
        flag=1
        break
if(flag==0):
    print("YES")
else:
    print("NO")
