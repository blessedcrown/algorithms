#https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(2500)
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(v, visited):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i, visited)
    return

num = 0
for i in range(1, n+1):
    if not visited[i]:
        num += 1
        dfs(i, visited)
        
print(num)