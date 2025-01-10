def backtrace(limit, cur_sum):
    global result

    if cur_sum >= result:
        return

    if limit <= cur_sum:
        result = min(result, cur_sum)
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtrace(limit, cur_sum + S[i])
            visited[i] = False

T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    S.sort(reverse=True)

    visited = [False] * N
    result = float('inf')

    backtrace(B, 0)

    print("#{}".format(t), result - B)

