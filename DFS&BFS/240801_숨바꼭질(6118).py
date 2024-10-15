from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


queue = deque([1])
visited[1] = 1
cnt = 0

while queue:
    v = queue.popleft()
    cnt += 1

    for i in graph[v]:
        if not visited[i]:
            visited[i] = visited[v] + 1
            queue.append(i)


hideRoom = visited.index(max(visited))
maxDistance = max(visited)
maxDistanceCount = visited.count(maxDistance)

print(hideRoom, maxDistance - 1, maxDistanceCount)
