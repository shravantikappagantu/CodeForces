t=int(input())
for test in range(t):
    n=int(input())
    # s=input()
    l=list(map(int, input().split()))
    ans=['abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']
    for i in l:
        s=''
        s=ans[-1][:i]
        #print(s)
        s+=ans[-1][i+1:]
        #print(s)
        s+=ans[-1][i]
        #print(s)
        ans.append(s)
    #print(ans)
    for ele in ans:
        print(ele)
