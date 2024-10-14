def check(real, temp):
    strike = 0
    ball = 0

    for i in range(3):
        if real[i] == temp[i]:
            strike += 1
        elif temp[i] in real:
            ball += 1

    return strike, ball   

# 입력 받은 수의 유효성 검사 함수
def is_valid_num(num):
    num_str = str(num)
    # 수가 3개인가? 0이 들어있진 않은가? 세자리 수 중 중복된 수는 없는가?
    if len(num_str) == 3 and '0' not in num_str and len(set(num_str)) == 3:
        return True
    else:
        return False
    
def main():
    N = int(input())
    info = []
    for _ in range(N):
        question = tuple(map(int, input().split())) # 리스트로 받는게 옳은가? 중복된 수를 받으면 에러를 뱉어야되나?
        info.append(question)
    result = 0

    for i in range(123, 988):
        if is_valid_num(i):
            valid = True
            real = str(i)

            for N, S, B in info:
                strike, ball = check(real, str(N))
                if strike != S or ball != B:
                    valid = False
                    break
            if valid:
                result += 1
    
    print(result)

main()
