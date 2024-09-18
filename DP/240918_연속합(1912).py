n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    dp = [0] * n    # dp[i] 는 i번째 요소까지의 최대합을 기록
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1]) # nums[i] 와 dp[i - 1]에 이어서 더한 값 중 더 큰 값을 선택

    return max(dp)

print(solution(n, nums))