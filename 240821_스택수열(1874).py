def solution():
    n = int(input())
    sequence = list(int(input()) for _ in range(n))

    stack = []
    anwser = []

    cur = 1

    for i in sequence:
        while cur <= i:
            stack.append(cur)
            anwser.append('+')
            cur += 1
        if stack[-1] == i:
            stack.pop()
            anwser.append('-')
        else:
            print('NO')
            return
    print('\n'.join(anwser))

solution()