n1=input()
n2=input()
ans=[]
for i in range(len(n1)):
    if n1[i]==n2[i]:
        ans.append("0")
    else:
        ans.append("1")
ans=''.join(ans)
print(ans)
