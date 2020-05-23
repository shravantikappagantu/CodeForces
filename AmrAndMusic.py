nk=list(map(int,input().split()))
days=list(map(int,input().split()))
ind=[]
for i in range(len(days)):
    ind.append(days[i])
    
s=0

if (sum(days))<=(nk[1]):
    print(nk[0])
    for i in range(1,nk[0]+1):
        print(i, end=" ")
    
elif sum(days)>nk[1]:
    while(sum(days)>nk[1]):
        days.remove(int(max(days)))
    print(len(days))
    for i in range(len(days)):
        if days[i] in ind:
            print(ind.index(days[i])+1, end=" ")
            ind[ind.index(days[i])] = -1
#print(ind, end ="\n")
#print(days)
