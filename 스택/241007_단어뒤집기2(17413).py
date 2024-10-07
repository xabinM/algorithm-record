def solution(S):
    temp = []
    result = []
    tagStatus = False

    for i in S:
        if tagStatus:
            if i == ">":
                result.append(''.join(temp))
                temp = []
                result.append(i)
                tagStatus = False
            else:
                temp.append(i)
        else:
            if i == "<":
                result.append(''.join(reversed(temp)))
                temp = []
                result.append(i)
                tagStatus = True
            elif i == " ":
                result.append(''.join(reversed(temp)))
                result.append(i)
                temp = []
            else:
                temp.append(i)
    
    if temp:
        result.append(''.join(reversed(temp)))

    print(''.join(result))

# baekjoon online judge
# <open>tag<close>

S = input().strip()
solution(S)