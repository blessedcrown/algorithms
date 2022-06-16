#https://www.acmicpc.net/problem/2210
def dfs(x, y, num):
    if len(num) == 6:
        if num not in answer:
            answer.append(num)
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]

        if 0<= ddx < 5 and 0 <= ddy < 5:
            dfs(ddx, ddy, num+arr[ddx][ddy])

arr = [list(map(str, input().split())) for _ in range(5)]
answer = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(answer))