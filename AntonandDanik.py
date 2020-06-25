n=int(input())
a=list(input())
for i in range(n):
    if a.count("A")==a.count("D"):
        print("Friendship")
        break
    elif a.count("A")>a.count("D"):
        print("Anton")
        break
    else:
        print("Danik")
        break
