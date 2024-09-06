n = int(input())

def solution(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print(solution(n) % 10007)

# 1

# 1 1
# 2

# 1 1 1
# 1 2
# 2 1

# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2

# 1 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 2 1 1
# 2 1 1 1
# 1 2 2
# 2 1 2
# 2 2 1
