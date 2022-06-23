import sys
sys.setrecursionlimit(150000)
def input():
    return sys.stdin.readline().rstrip() 
n, a, b = map(int, input().split())
if a > b:
    a, b = b, a
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    x, y, z = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def dfs(cur, target, visited):
    if cur == target:
        return 0
    if visited[cur]:
        return -1
    visited[cur] = True
    for i in arr[cur]:
        if not visited[i]:
            dist = dfs(i, target, visited)
            if dist >= 0:
                return dist + 1
    return -1
if a == b:
    print(0)
else:
    result = dfs(a, b, visited)
    print(result - 1)
    