l=list(map(int,input().split()))
li=[]
m1=min(l)
m2=max(l)
li.append(m1)
li.append((m2-m1)//2)
print(*li)
