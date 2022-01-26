import datetime


class test:
    def solution(self,a, b):
        print(a,b)
        t = 'MON TUE WED THU FRI SAT SUN'.split()
        return t[datetime.datetime(2016,a,b).weekday()]

test = test()
test.solution(5,24)