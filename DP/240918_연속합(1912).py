n = int(input())
nums = list(map(int, input().split()))
max = 0

def solution(n, nums):
    dp = [0] * n