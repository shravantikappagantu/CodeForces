t=int(input())
for test in range(t):
    n=int(input())
    s=input()
    count=0
    bal=0
    for i in range(n):
        if s[i]=="(":
            bal+=1
        else:
            bal-=1
            if bal<0:
                bal=0
                count+=1
    print(count)
