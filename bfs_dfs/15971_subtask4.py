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
    arr[x].append((y, z))
    arr[y].append((x, z))

def dfs(cur, target, visited):
    if cur == target:
        return []
    if visited[cur]:
        return None
    visited[cur] = True
    
    for i, d in arr[cur]:
        if not visited[i]:
            answer = dfs(i, target, visited)
            if answer is None:
                continue
            answer.append(d)
            return answer
    return None
if a == b:
    print(0)
else:
    result = dfs(a, b, visited)
    print(sum(result)-max(result))