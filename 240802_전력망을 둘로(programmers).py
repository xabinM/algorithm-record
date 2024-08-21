from collections import deque

def solution(n, wires):
    min_diff = float('inf')

    for i in range(n - 1):
        # 인접 행렬 생성
        graph = makeGraph(n, wires)
        
        # 전선 제거
        graph[wires[i][0]][wires[i][1]] = 0
        graph[wires[i][1]][wires[i][0]] = 0

        # BFS를 통한 서브 그래프 크기 계산
        visited = [0] * (n + 1)
        q = deque([1])
        visited[1] = 1

        cnt = 1
        while q:
            x = q.popleft()

            for j in range(1, n + 1):
                if graph[x][j] == 1 and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
                    cnt += 1

        # 두 서브 그래프의 크기 차이 계산 및 최소값 갱신
        diff = abs(n - cnt - cnt)
        if diff < min_diff:
            min_diff = diff

    return min_diff


def makeGraph(n, wires):
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in wires:
        graph[a][b] = 1
        graph[b][a] = 1
    return graph


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))# 3
print(solution(4, [[1,2],[2,3],[3,4]]))# 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))# 1