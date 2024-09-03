T = int(input())

def solution(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        dp[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] # dp[i][j - 1]이 아랫층의 현재 호수 전까지의 사람들 수의 합이다.

    return dp[k][n]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(solution(k, n))

# 2 : 1 4 10
# 1 : 1 3 6
# 0 : 1 2 3