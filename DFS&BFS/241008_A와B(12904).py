def solution(S, T):

    while len(T) > len(S):
        if T[-1] == "A":
            T = T[:-1]
        elif T[-1] == "B":
            T = T[:-1]
            T = ''.join(reversed(T))

    if T == S:
        print(1)
    else:
        print(0)

S = input()
T = input()

solution(S, T)