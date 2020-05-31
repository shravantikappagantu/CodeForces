n=input()
while(True):
    n = str(int(n)+1)
    if(len(set(n))==4):
        flag=1
        break
print(n)
