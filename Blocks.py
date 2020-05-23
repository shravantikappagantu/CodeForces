n=int(input())
s=list(input())
count=0
l=[]
cb=0
cw=0
def swap(char ):
    if char=="W":
        return "B"
    else:
        return "W"
for i in range(len(s)):
    if s[i]=="B":
        cb+=1
    else:
        cw+=1
if (cb%2!=0) and (cw%2!=0):
    print(-1)
elif( cb==0 or cw==0):
    print(0)
else:
    for i in range(len(s)-1):
        #print(s, cb, cw, "-----1")
        if s[i]=="B":
            s[i]=swap(s[i])
            cw+=1
            cb-=1
            s[i+1]=swap(s[i+1])
            l.append(i+1)
            if s[i+1]=="B":
                cb+=1
                cw-=1
            else:
                cw+=1
                cb-=1
        if(cb==0 or cw==0):
            break
    if(cb!=0 and cw!=0):
        for i in range(len(s)-1):
            #print(s, cb, cw, "-----0")
            if s[i]=="W":
                s[i]=swap(s[i])
                cw-=1
                cb+=1
                s[i+1]=swap(s[i+1])
                l.append(i+1)
                if s[i+1]=="B":
                    cb+=1
                    cw-=1
                else:
                    cw+=1
                    cb-=1
            if(cb==0 or cw==0):
                break
    print(len(l))
    print(*l)

"""
#solution
n=int(input())
s=input()
w=s.count("W")
b=n-w
# s=list(s)
if b%2==w%2==1:
	print(-1)
else:
	c=0
	p=0
	ans=[]
	x="W" if w%2==0 else "B"
	for i in range(n):
		if (s[i]==x and p==0) or (s[i]!=x and p==1):
			p=1
			c+=1
			ans.append(i+1)
		else:
			p=0
	print(c)
	print(*ans)
"""
