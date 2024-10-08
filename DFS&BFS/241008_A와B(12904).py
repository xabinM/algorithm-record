from collections import deque

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

def bfs(S, T):
    q = deque([T])
    visited = set([T])

    while q:
        cur = q.popleft()

        if cur == S:
            return print(1)

        if len(cur) > len(S):
            if cur[-1] == "A":
                cur = cur[:-1]
                if cur not in visited:
                    visited.add(cur)
                    q.append(cur)
            else:
                cur = ''.join(reversed(cur[:-1]))
                if cur not in visited:
                    visited.add(cur)
                    q.append(cur)            

    return print(0)

S = input()
T = input()

solution(S, T)
bfs(S, T)