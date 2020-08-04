t=int(input())
for i in range(t):
    a,b,c=map(int, input().split())
    if a < c:
        print(1 )
    else:
        print(-1, end=" ")
    if c < a * b:
        print(b)
    else:
        print(-1)
