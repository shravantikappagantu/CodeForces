# efficient solution
t=int(input())
l=[]
for i in range(t):
    n=int(input())
    l.append(n//2)
print(*l,sep='\n')



'''
# exceeds time limit
def gcdfunc(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcdfunc(b,a%b)
t=int(input())
a=[]
for k in range(t):
    n=int(input())
    l=[]
    for i in range(1,n-1):
        for j in range(1,n):
            if(i<j):
                l.append(gcdfunc(i,j))
    ans=max(l)
    a.append(ans)
print(*a,sep='\n')
'''
