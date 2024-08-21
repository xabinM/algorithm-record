from collections import deque

def bfs (x, y, color, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_number():
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, graph[i][j], visited)
                count += 1
    return count

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

normal = count_number()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

unnormal = count_number()

print(normal, unnormal)