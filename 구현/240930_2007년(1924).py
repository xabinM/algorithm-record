def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
def solution(year, month, day):
    all_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        all_month[2] = 29

    total_days = 0
    for i in range(1, month):
        total_days += all_month[i]
    total_days += day

    if total_days % 7 == 1:
        print("MON")
    elif total_days % 7 == 2:
        print("TUE")
    elif total_days % 7 == 3:
        print("WED")
    elif total_days % 7 == 4:
        print("THU")
    elif total_days % 7 == 5:
        print("FRI")
    elif total_days % 7 == 6:
        print("SAT")
    elif total_days % 7 == 0:
        print("SUN")

x, y = map(int, input().split())
year = 2007

solution(year, x, y)