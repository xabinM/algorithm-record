N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
result = 0

for i in range(N):
    result += A[i] * B.pop(B.index(max(B)))

print(result)