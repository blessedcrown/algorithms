import sys
sys.setrecursionlimit(15000)
n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, visited):
    if visited[x][y] or arr[x][y] == 0:
        return 0
    visited[x][y] = True
    temp = 0
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if 0 <= ddx < n and 0 <= ddy < m:
            r = dfs(ddx, ddy, visited)
            temp += r
    return temp + 1
    
answer = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            answer.append(dfs(i, j, visited))
print(max(answer))
    