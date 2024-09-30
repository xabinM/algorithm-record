def solution(N, K):
    arr = [i for i in range(1, N + 1)]
    answer = []
    idx = 0

    while arr:
        idx = (idx + K - 1) % len(arr)
        answer.append(arr.pop(idx))

    return answer

# 1, 2, 3, 4, 5, 6, 7

N, K = map(int, input().split())
result = solution(N, K)

print("<" + ', '.join(map(str, result)) + ">")