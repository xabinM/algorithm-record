T = int(input())

for _ in range(T):
    string = input()
    result = 0
    depth = 0
    for i in string:
        if i == 'O':
            depth += 1
            result += depth
        else:
            depth = 0
    print(result)