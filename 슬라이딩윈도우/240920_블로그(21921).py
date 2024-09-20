def solution(N, X, visitor):
    visitor_forX = [sum(visitor[:X])]

    for i in range(N - X):
        visitor_forX.append(visitor_forX[i] - visitor[i] + visitor[i + X])

    if max(visitor_forX) == 0:
        return print("SAD")
    else:
        return print(max(visitor_forX), visitor_forX.count(max(visitor_forX)), sep="\n")

N, X = map(int, input().split())
visitor = list(map(int, input().split()))
solution(N, X, visitor)