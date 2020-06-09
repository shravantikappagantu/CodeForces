n=int(input())
scores=list(map(int,input().split()))

hs=ls=scores[0]
hcount=lcount=0
for i in range(len(scores)):
    if scores[i]>hs:
        hs=scores[i]
        hcount+=1
    elif scores[i]<ls:
        ls=scores[i]
        lcount+=1
print(hcount+lcount)
