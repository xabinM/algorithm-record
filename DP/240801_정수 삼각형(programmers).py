def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:  # 맨 왼쪽
                triangle[i][j] += triangle[i-1][j]
            elif j == i:   # 맨 오른쪽
                triangle[i][j] += triangle[i-1][j-1]
            else: # 중간
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[-1])
    return answer
