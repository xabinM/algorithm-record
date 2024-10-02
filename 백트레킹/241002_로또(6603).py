def backTrack(temp, T, S):

    if len(temp) == 6:
        print(" ".join(map(str, temp)))
        return
    
    for i in range(T):
        if not visited[i]:
            if len(temp) == 0 or S[i] > temp[-1]:
                visited[i] = True
                temp.append(S[i])
                backTrack(temp, T, S)
                temp.pop()
                visited[i] = False


while True:
    S = list(map(int, input().split()))

    if S[0] == 0:
        break

    T = S.pop(0)

    visited = [False] * T

    backTrack([], T, S)
    print(sep="\n")
