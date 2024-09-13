# 버블, 삽입, 선택, 병합(머지), 퀵, 힙

N = int(input())
arr = []

for i in str(N):
    arr.append(int(i))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): # n - i - 1은 이미 정렬된 마지막 부분을 제외하기 위함
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insert_sort1(arr): # 틀린 버전
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

def insert_sort2(arr): # 올바른 버전
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        temp = i
        for j in range(i + 1, n): # 최소값 찾기
            if arr[j] < arr[temp]:
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]
    return arr

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    sorted_arr = []
    l, h = 0, 0

    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            sorted_arr.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[h])
            h += 1

    if l < len(left):
        sorted_arr.extend(left[l:])
    if h < len(right):
        sorted_arr.extend(right[h:])
    
    return sorted_arr

# print(''.join(map(str, merge_sort(arr))))

# 1427 3947
# 14 27 39 47
# 1 4 2 7 3 9 4 7
# 14 27 39 47
# 1247 3479
# 1234779
