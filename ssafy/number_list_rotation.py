T = int(input())

for t in range(1, T + 1):
    N = int(input())

    graph = [list(map(str, input().split())) for _ in range(N)]

    print("#{}".format(t))

    result90 = []
    result180 = []
    result270 = []
    for i in range(N):
        temp90 = ""
        temp180 = ""
        temp270 = ""
        for j in range(1, N + 1):
            temp90 += graph[N - j][i]
            temp180 += graph[N - (i + 1)][N - j]
            temp270 += graph[j - 1][N - (i + 1)]
        result90.append(temp90)
        result180.append(temp180)
        result270.append(temp270)

    for k in range(N):
        print(result90[k], result180[k], result270[k])