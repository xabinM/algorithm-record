def solution(N, chapters):
    dp = [0] * (N + 1)

    for days, pages in chapters:
        for i in range(N, days - 1, -1):
            dp[i] = max(dp[i], dp[i - days] + pages)
            # print("dp[{}] : ".format(i), dp[i])
    return dp[N]

N, M = map(int, input().split())
chapters = [list(map(int, input().split())) for _ in range(M)]

print(solution(N, chapters))