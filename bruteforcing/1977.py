#https://www.acmicpc.net/problem/1977

m = int(input())
n = int(input())
ans = []
for i in range(101):
    if m <= i**2 <= n:
        ans.append(i**2)
print(sum(ans))
print(min(ans))
    