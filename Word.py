s = input()
cap=low = 0
for i in range(len(s)):
    if 65<=ord(s[i])<=90:
        cap+= 1
    else:
        low+= 1
 
if low >=cap:
    print(s.lower())
else:
    print(s.upper())
