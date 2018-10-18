class Date:
    @staticmethod
    def is_date_valid(arg):
        # 1. split으로 list생성, map을 이용해 int함수로 int화시킨 결과값을 동시에 각 변수에 할당.
        # 연도 제외한 달, 일 범위에 대한 boolean check
        year, month, day = map(int, arg.split('-'))
        return 0< month <= 12 and 0 < day <=31


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')



class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 & minute <= 60 & second <= 60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = Time(hour, minute, second)
        return time

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')