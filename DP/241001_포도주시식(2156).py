def solution(n, vin):
    if n == 1:
        return vin[0]
    elif n == 2:
        return vin[0] + vin[1]

    dp = [0] * n
    dp[0] = vin[0]
    dp[1] = vin[0] + vin[1]
    dp[2] = max(vin[0] + vin[2], vin[1] + vin[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + vin[i], dp[i - 3] + vin[i - 1] + vin[i], dp[i - 1])

        print(dp)
    return dp[n - 1]

n = int(input())
vin = [int(input()) for _ in range(n)]

print(solution(n, vin))