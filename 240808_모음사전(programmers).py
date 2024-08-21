from itertools import product

def solution(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    words = []
    for length in range(1, 6):
        for i in product(letters, repeat = length):
            words.append(''.join(i))
    
    words.sort()

    return words.index(word) + 1
