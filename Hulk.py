n=int(input())
s1= "I love"
s2= "I hate"
a=""
for i in range(0,n):
    if(i&1):
        a=a+s1+" "
    else:
        a=a+s2+" "
    if(i!=n-1):
        a+="that "
a+="it"
print(a)
