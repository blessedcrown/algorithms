import sys
n, a, b = map(int, sys.stdin.readline().rstrip().split())
if a > b:
    a, b = b, a
arr = []
if a == b:
    print(0)
    exit()
for _ in range(n-1):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    arr.append(z)

print(sum(arr[a-1:b-1])-max(arr[a-1:b-1]))
    