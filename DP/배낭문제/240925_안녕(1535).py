def solution(N, hp, happy):
    dp = [0] * 101

    for i in range(N):
        for j in range(100, hp[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - hp[i]] + happy[i])
            # print("dp[{}] : ".format(j), dp[j])

    return dp[99]

N = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

print(solution(N, hp, happy))

# 3
# 1 21 79
# 20 30 25
