import sys
sys.setrecursionlimit(100000)
n = int(input())
arr = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(v, prev=''):  
    for i in arr[v]:
        if i != prev:
            answer[i] = v
            dfs(i, v)
    return 

dfs(1)
for i in answer[2:]:
    print(i)