k,n,w= map(int,input().split())
cost=0
for i in range(1,w+1):
    cost+=(i*k)
    #print(cost)
if cost-n>=0:
    print(cost-n)
else:
    print(0)

