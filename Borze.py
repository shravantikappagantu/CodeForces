# Borze- Codeforces

s=input()
ans=[]
i=0
while i<len(s):
    if s[i]==".":
        ans.append("0")
    elif s[i]=="-" and s[i+1]==".":
        ans.append("1")
        i+=1
    elif s[i]=="-" and s[i+1]=="-":
        ans.append("2")
        i+=1
    i+=1
ans= ''.join(ans)
print(ans)
