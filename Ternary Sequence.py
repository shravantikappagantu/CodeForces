t=int(input())
for test in range(t):
    x0,x1,x2=map(int,input().split())
    y0,y1,y2=map(int,input().split())
    s=0
    m = min(x0,y2)
    x0-=m
    y2-=m

    m = min(x1,y0)
    x1-=m
    y0-=m

    m = min(x2,y1)
    x2-=m
    y1-=m

    s+=2*m
    s-=2* min(x1,y2)

    print(s)
