n=int(input())
l=list(map(int, input().split()))

dp=[[0]*3 for i in range(n+1)]
print(dp)
l.insert(0,0)
print(l)
for i in range(1,n+1):
    if l[i] in [1,3]:
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])+1
    if l[i] in [2,3]:
        dp[i][2]=max(dp[i-1][1],dp[i-1][0])+1
 
    dp[i][0]=max(dp[i-1])
    
 
print(n-max(dp[n]))
