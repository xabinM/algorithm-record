sentence = input().strip()
cur = 1
index = 0

while index < len(sentence):
    cur_str = str(cur)
    cur += 1
    for i in cur_str:
        if index < len(sentence) and i == sentence[index]:
            index += 1


print(cur - 1)