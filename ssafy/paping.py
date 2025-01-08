T = int(input())

for t in range(1,T + 1):
    N = int(input())

    paping = []

    for i in range(N):
        temp = []
        for j in input():
            temp.append(j)
        paping.append(temp)

    for i in paping:
        print(i)


        (1,1) (2, 0) (3, 0) (2, 2) (3, 3) (1, 3)

        (1, 1)
        (2, 0)
        (3, 0)
        (2, 2)
        (3, 3)

        (4, 3) (0, 1), (0, 3), (1, 0), (1, 1), (1, 3), (1, 4), (2, 0)