def solution(N, times, prices):
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        # 상담을 안하고 있을 때
        dp[i] = max(dp[i], dp[i - 1])

        if i + times[i] <= N + 1: # ????? 왜 일까 N + 1
            dp[i + times[i] - 1] = max(dp[i - 1] + prices[i], dp[i + times[i] - 1])

    return dp[N]

N = int(input())
times = [0]
prices = [0]
for i in range(N):
    T, P = map(int, input().split())
    times.append(T)
    prices.append(P)

print(solution(N, times, prices))