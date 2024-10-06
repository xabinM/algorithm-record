def solution(N):
    for i in range(1, N + 1):
        print(' ' * (N - i) + '*' * i + '*' * (i - 1))

N = int(input())
solution(N)