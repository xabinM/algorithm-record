from collections import deque

t = int(input())

def distanceCheck(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for _ in range(t):

    n = int(input())
    A = []
    for _ in range(n+2):
        A.append(list(map(int, input().split())))

    queue = deque([0])
    visited = [False] * (n + 2)
    visited[0] = True

    while queue:
        cur = queue.popleft()
        curX, curY = A[cur]
        for i in range(n + 2):
            nextX, nextY = A[i]
            if not visited[i] and distanceCheck(curX, curY, nextX, nextY) <= 1000:
                queue.append(i)
                visited[i] = True
    
    if visited[-1]:
        print('happy')
    else:
        print('sad')
        