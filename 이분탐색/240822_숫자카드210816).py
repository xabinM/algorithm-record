import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# 딕셔너리 - 통과
cards.sort()

dic = {}

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in nums:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')

# 이진탐색 - 시간 초과
sequence = sorted(nums)
result = [0] * M

for i in range(N):
    left, right = 0, M - 1
    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == cards[i]:
            result[nums.index(sequence[mid])] += 1
            break
        elif sequence[mid] < cards[i]:
            left = mid + 1
        else:
            right = mid - 1

for i in result:
    print(i, end=' ')