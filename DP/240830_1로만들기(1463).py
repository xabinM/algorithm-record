N = int(input())

def makeOne(N):
    dp = [0] * (N + 1)
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:  # 2나 3으로 나누어 떨어진다면 나누었을 때 나온 숫자의 연산 횟수에 1을 더한 것과 현재 연산 횟수(1을 더한)를 비교하여 작은 값을 저장
            dp[i] = min(dp[i], dp[i // 2] + 1) # 1을 더하는 이유는 연산을 한 번 더 했기 때문
        if i % 3 == 0:                              
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[N]

print(makeOne(N))