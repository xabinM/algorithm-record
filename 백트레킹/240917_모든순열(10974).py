def back_track(result, visited, N):
    if len(result) == N:
        return print(" ".join(map(str, result)))

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            back_track(result, visited, N)
            result.pop()
            visited[i] = False


N = int(input())
visited = [False] * (N + 1)
back_track([], visited, N)