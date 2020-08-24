t=int(input())
for test in range(t):
    n,k = map(int, input().split())
    '''if n==k:
        print(0)
    el'''
    if k>n:
        print(k-n)
    else:
        if (n-k)%2!=0:
            print(1)
        else:
            print(0)
