T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        longer = A
        shorter = B
    else:
        longer = B
        shorter = A

    max_value = 0

    for i in range(len(longer) - len(shorter) + 1):
        sum = 0
        for j in range(len(shorter)):
            sum += shorter[j] * longer[j + i]

        max_value = max(max_value, sum)

    print("#{}".format(t), max_value)