def backTrack(temp, N):
    global max_value

    if len(temp) == N:
        current_max_value = 0
        for i in range(N - 1):
            current_max_value += abs(temp[i] - temp[i + 1])
        max_value = max(max_value, current_max_value)

    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])

            backTrack(temp, N)

            visited[i] = False
            temp.pop()

N = int(input())
arr = list(map(int, input().split()))
visited = [False] * N
max_value = 0

backTrack([], N)

print(max_value)