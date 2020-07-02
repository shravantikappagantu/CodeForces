k2, k3, k5, k6 = map(int, input().split())
a1 = min(k2,k5, k6)
result = a1 * 256
result += min(k2 - a1, k3) * 32
print(result)
