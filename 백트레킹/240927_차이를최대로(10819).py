def backTrack(temp, depth, N):
    global max_value

    if depth == N:
        current_max_value = 0
        for i in range(N - 1):
            current_max_value += abs(temp[i] - temp[i + 1])
        max_value = max(max_value, current_max_value)
        return

    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            temp[depth] = arr[i]

            backTrack(temp, depth + 1, N)

            visited[i] = False

N = int(input())
arr = list(map(int, input().split()))
visited = [False] * N
max_value = 0

backTrack([0] * N, 0, N)

print(max_value)