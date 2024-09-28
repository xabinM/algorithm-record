non_self_num = set()
for i in range(1, 10001):
    temp = [i]
    for j in str(i):
        temp.append(int(j))
    non_self_num.add(sum(temp))


for i in range(1, 10001):
    if i not in non_self_num:
        print(i)