import sys
def dfs(v, visited, brr):
    if visited[v]:
        return
    visited[v] = True
    for i in brr[v]:
        dfs(i, visited, brr)

def is_intersect(x,y,r,xx,yy,rr):
    if r+rr >= (abs(x-xx)**2 + abs(y-yy)**2)**0.5:
        return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    brr = [[] for _ in range(n)]
    for _ in range(n):
        x, y, r = map(int, sys.stdin.readline().rstrip().split())
        arr.append((x, y, r))
    for i, (x, y, r) in enumerate(arr):
        for j, (xx, yy, rr) in enumerate(arr):
            if is_intersect(x,y,r,xx,yy,rr):
                brr[i].append(j)
    visited = [False for _ in range(n)]

    num = 0
    for i in range(n):
        if not visited[i]:
            num += 1
            dfs(i, visited, brr)
    print(num)