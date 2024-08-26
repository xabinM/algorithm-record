n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
result = set()
visited = [False] * n

def backtrace(depth, selected):
    if depth == k:
        result.add(''.join(selected))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            selected.append(cards[i])
            backtrace(depth + 1, selected)
            selected.pop()
            visited[i] = False

backtrace(0, [])
print(len(result))

# 1 2 12 1