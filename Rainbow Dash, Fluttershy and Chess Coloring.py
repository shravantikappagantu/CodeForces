t=int(input())
for test in range(t):
    n=int(input())
    if n==1:
        print(1)
    elif n==2 or n==3:
        print(2)
    else:
        print((n//2) +1)
