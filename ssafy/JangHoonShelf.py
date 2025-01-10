T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    # DP 배열의 크기는 키의 최대 합까지만 필요
    max_sum = sum(S)
    dp = [False] * (max_sum + 1)
    dp[0] = True  # 초기값: 아무 것도 선택하지 않았을 때 합은 0

    # DP 갱신
    for height in S:
        for cur_sum in range(max_sum, height - 1, -1):
            if dp[cur_sum - height]:
                dp[cur_sum] = True
    # # B 이상에서 가장 작은 합 찾기
    result = float('inf')
    for i in range(B, max_sum + 1):
        if dp[i]:
            result = i
            break

    print(f"#{t} {result - B}")
