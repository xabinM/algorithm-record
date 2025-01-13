T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    max_sum = sum(S)
    dp = [False] * (max_sum + 1)

    dp[0] = True

    for height in S:
        for cur_sum in range(max_sum, height - 1, -1):
            if dp[cur_sum - height]:
                dp[cur_sum] = True

    for i in range(B, max_sum + 1):
        if dp[i]:
            result = i
            break

    print("#{}".format(t), result - B)
