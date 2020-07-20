t=int(input())
for i in range(t):
    s=input()
    if min(s.count('0'), s.count('1')) % 2 == 1:
        print('DA' )
    else:
        print('NET')
