#https://www.acmicpc.net/problem/1074
n, r, c = map(int, input().split())
ans = 0

def z(n, r, c):
    global ans
    if n == 1:
        if r % 2 == 0:
            ans += r+c
        else:
            ans += r+c+1
        return
    #2X2가 아닌이상 매번 배열을 4등분하여 해당 인덱스가 1,2,3,4 분면중
    #어디에 해당되는지 확인. 그후 index도 같이 줄여준다
    line = 2**(n-1)
    #4사분면
    if r >= line and c >= line:
        ans += line**2 * 3
        r -= line
        c -= line
    #3사분면
    elif r>= line and c < line:
        ans += line**2 * 2
        r -= line
    #2사분면
    elif r < line and c>= line:
        ans += line**2
        c -= line
    z(n-1, r, c)
z(n, r, c)
print(ans)