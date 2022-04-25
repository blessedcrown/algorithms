#https://www.acmicpc.net/problem/1436

n = int(input())
count = 0
nth = 666
while True:
    if '666' in str(nth):
        count += 1
    if count == n:
        print(nth)
        break
    nth += 1