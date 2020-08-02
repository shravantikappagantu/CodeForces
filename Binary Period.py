t=int(input())
for i in range(t):
    t=input()
    
    one=t.count('1')
    zero=t.count('0')
 
    if(zero>0 and one>0):
        if(zero>=one):
            print('01'*len(t))
        else:
            print('10'*len(t))
    else:
        print(t)
