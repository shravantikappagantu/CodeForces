def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
s=input()
t=input()
if reverse(s)==t:
    print("YES")
else:
    print("NO")
