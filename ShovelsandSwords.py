import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    m=min(a,b,(a+b)/3)
    print(math.floor(m))
