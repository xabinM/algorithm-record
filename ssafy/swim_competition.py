from collections import deque

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]
    min_second = [[float('inf')] * N for _ in range(N)]

    A, B = map(int, input().split())
    C, D = map(int, input().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(A, B)])
    min_second[A][B] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    continue
                if graph[nx][ny] == 2:
                    cost = 3
                if graph[nx][ny] == 0:
                    cost = 1

                new_time = min_second[x][y] + cost

                if new_time < min_second[nx][ny]:
                    min_second[nx][ny] = new_time
                    q.append((nx, ny))
    if min_second[C][D] == 0:
        print(-1)
    else:
        print(min_second[C][D])