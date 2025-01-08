T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())

    S = list(map(int, input().split()))

    min_high = 0

    for i in range(len(S)):

