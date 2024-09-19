def solution(N, RGB):
    dp = [[0] * 3 for _ in range(N)]

    # 첫번째 집은 그대로 저장
    for i in range(3):
        dp[0][i] = RGB[0][i]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1] + RGB[i][0], dp[i - 1][2] + RGB[i][0])
        dp[i][1] = min(dp[i - 1][0] + RGB[i][1], dp[i - 1][2] + RGB[i][1])
        dp[i][2] = min(dp[i - 1][0] + RGB[i][2], dp[i - 1][1] + RGB[i][2])

    return min(dp[N - 1])

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, RGB))
