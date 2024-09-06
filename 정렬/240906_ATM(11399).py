N = int(input())
P = map(int, input().split())

newP = sorted(P)
A = []
B = []

for i in newP:
    A.append(i)
    B.append(sum(A))

print(sum(B))
