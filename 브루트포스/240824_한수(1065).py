N = int(input())
result = 0

for i in range(1, N+1):
    A = list(map(int, str(i)))
    if len(A) < 3:
        result += 1
    if len(A) >= 3:
        if A[0] - A[1] == A[1] - A[2]:
            result += 1
print(result)

# def is_hansu(N):
#     if N < 100:
#         return 1
#     pocket = list(map(int, str(N)))
#     if pocket[0] - pocket[1] == pocket[1] - pocket[2]:
#         return 1
#     else:
#         return 0

# def count_hansu(N):
#     count = 0
#     for i in range(1, N+1):
#         count += is_hansu(i)
#     return count

# N = int(input())

# print(count_hansu(N))

