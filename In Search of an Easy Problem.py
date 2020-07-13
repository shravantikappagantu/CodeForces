n=int(input())
l=list(map(int, input().split()))
flag=1
for i in range(n):
    if l[i]==1:
        flag=0
if flag==0:
    print("HARD")
else:
    print("EASY")
