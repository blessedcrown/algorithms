import sys
sys.setrecursionlimit(15000)
n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
visitedw = [[False]*n for _ in range(m)]
visitedb = [[False]*n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, c):
    if visited[x][y]:
        return 0
    visited[x][y] = True
    if arr[x][y] != c:
        return 0
    temp = 0
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if 0 <= ddx < m and 0 <= ddy < n:
            r = dfs(ddx, ddy, visited, c)
            temp += r
    return temp + 1

w =[]
b =[]
for i in range(m):
    for j in range(n):
        if not visitedw[i][j] and arr[i][j] == 'W':
            w.append(dfs(i,j,visitedw, 'W')**2)
        if not visitedb[i][j] and arr[i][j] == 'B':
            b.append(dfs(i,j,visitedb, 'B')**2)
print(sum(w), sum(b))
    