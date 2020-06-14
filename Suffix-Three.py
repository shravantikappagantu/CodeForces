'''
# Solution using built-in function endswith()
n=int(input())
for i in range(n):
    s=input()
    if s.endswith("po"):
        print("FILIPINO")
    elif s.endswith("desu") or s.endswith("masu"):
        print("JAPANESE")
    else:
        print("KOREAN")

'''
# Alternate solution
n=int(input())
for i in range(n):
    s=input()
    if s[-2:]=="po":
        print("FILIPINO")
    elif s[-4:]=="desu" or s[-4:]=="masu":
        print("JAPANESE")
    else:
        print("KOREAN")
