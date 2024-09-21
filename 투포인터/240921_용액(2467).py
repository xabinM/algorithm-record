def solution(N, liquid):
    left = 0
    right = N - 1
    min_sum = float('inf')
    result_left = 0
    result_right = 0

    while left < right:
        current_sum = liquid[left] + liquid[right]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result_left = left
            result_right = right

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return print(liquid[result_left], liquid[result_right])

N = int(input())
liquid = list(map(int, input().split()))
solution(N, liquid)