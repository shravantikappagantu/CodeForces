import math
l=list(map(int, input().split()))
 
dist = math.sqrt(math.pow(l[4] - l[2], 2) + math.pow(l[3] - l[1], 2))
ans = math.ceil(dist / l[0]/ 2)
//print(dist)
//print(dist / l[0]/ 2)
print(ans)
