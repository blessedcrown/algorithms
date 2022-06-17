import sys
sys.setrecursionlimit(25000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, visited):
    if visited[y][x]:
        return
    visited[y][x] = True
    if arr[y][x] == 0:
        return
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        
        if 0 <= ddx < m and 0 <= ddy < n:
            dfs(ddx, ddy, visited)
    
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    visited = [[False for _ in range(m)] for _ in range(n)]
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    num = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                num += 1
                dfs(j, i, visited)
    print(num)