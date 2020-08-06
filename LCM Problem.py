# Python Program to find the L.C.M. of two input number

def flcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

t=int(input())
for test in range(t):
    l,r = map(int, input().split())
    
    if 2*l<=r:
        print(l,2*l)
    else:
        print("-1 -1")
        
