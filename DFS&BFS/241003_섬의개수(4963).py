import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y, earth, w, h):
    earth[x][y] = 0 # 방문 처리

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and earth[nx][ny]:
            dfs(nx, ny, earth, w, h)

def solution(earth, w, h):
    result = 0

    for i in range(h):
        for j in range(w):
            if earth[i][j] == 1: # 아직 방문 안하면 1 이후 방문 할때 0으로 바꿀거임
                dfs(i, j, earth, w, h)
                result += 1

    return result

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    earth = [list(map(int, input().split())) for _ in range(h)]

    print(solution(earth, w, h))