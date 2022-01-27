class test:
    def solution(self,n):
        sum = 0
        for i in str(n):
            sum = sum+int(i)
        return sum


test = test()
test.solution(123)