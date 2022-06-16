#https://www.acmicpc.net/problem/2667
def dfs(x, y, num):
    s = 0
    if arr[x][y] != 1:
        return 0
    arr[x][y] = num
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        
        if 0 <= ddx < n and 0 <= ddy < n:
            s += dfs(ddx, ddy, num)
    return s + 1
            
        
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
section = 1
answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            section += 1
            result = dfs(i, j, section)
            answer.append(result)
print(len(answer))
for i in sorted(answer):
    print(i)
        
        
