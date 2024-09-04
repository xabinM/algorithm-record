def solution(stairs):
    n = len(stairs)
    if n == 1:
        return stairs[0]
    elif n == 2:
        return stairs[0] + stairs[1]
    
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2]) 

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    return dp[-1]

S = int(input())
stairs = [int(input()) for _ in range(S)]
print(solution(stairs))