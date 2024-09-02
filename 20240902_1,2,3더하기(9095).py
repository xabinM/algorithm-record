T = int(input())
def plusOneTwoThree(N):
    dp = [0] * 11
    dp[1], dp[2], dp[3] = 1, 2, 4

    if N < 4:
        return dp[N]
    
    for i in range(4, N + 1):
        # dp[i - 1] : 전 단계의 모든 가짓수에 1을 더하는 경우
        # dp[i - 2] : 전전 단계의 모든 가짓수에 2를 더하는 경우
        # dp[i - 3] : 전전전 단계의 모든 가짓수에 3을 더하는 경우
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[N]

for _ in range(T):
    N = int(input())
    print(plusOneTwoThree(N))