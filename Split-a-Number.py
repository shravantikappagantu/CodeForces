l=int(input())
n=input()
#print(n[l//2])
if n[l//2 +1]=="0":
    a=int(n[0:(l//2)])
    b=int(n[(l//2):])
    print(a+b)
else:
    
