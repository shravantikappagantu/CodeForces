n=int(input())
x=y=0
for i in range(n):
    li,ri=map(int,input().split())
    x+=li
    y+=ri
print(min(x,n-x)+min(y,n-y))
