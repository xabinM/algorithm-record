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

