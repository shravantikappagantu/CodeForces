n , a, x, b, y = map(int,input().split())
if a==b:
  print('YES')
else:
  while a!=x and b!=y:
      a+=1
      b-=1
      if b==a+1:
        a=1
      if b==0:
        b=a
      if a==b:
        flag=1
        break
  if flag==1:
    print('YES')
  else:
    print('NO')
