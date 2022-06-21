#https://www.acmicpc.net/problem/2468
import sys
sys.setrecursionlimit(100000)
n = int(input())
arr = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(n)]

answer = []
section = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, rain):
    if visited[x][y]:
        return
    visited[x][y] = True
    if arr[x][y] <= rain:
        return
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if 0 <= ddx < n and 0 <= ddy < n:
            dfs(ddx, ddy, visited, rain)
            
for x in range(0, 101):
    section = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > x:
                section += 1
                dfs(i, j, visited, x)
    answer.append(section)
print(max(answer))
    