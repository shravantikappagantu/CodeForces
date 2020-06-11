n,m=map(int,input().split())
flag=True
for i in range(n+1, m):
    for j in range(2, i//2+2):
        if i%j == 0:
            break
        if j == i//2+1:
            flag = False
if flag:
    for j in range(2, m//2+1):
        if m%j == 0:
            flag = False
            break
if flag:
    print('YES')
else:
    print('NO')



'''
n, m = map(int, input().split())
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
a = "NO"
while True:
    n += 1
    if n in p:
        if n == m:
            a = "YES"
            break
        else:
            break
    if n > m:
        break
print(a)

'''

"""
# Alternate Solution

def isprime(n):
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True
 
def next_prime(n):
  i = n + 1
  while True:
    if isprime(i):
      return i
    i += 1
 
n, m = map(int, input().split())
if next_prime(n) == m:
  print('YES')
else:
  print('NO')

  """
