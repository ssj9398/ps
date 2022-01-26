class test:
    def solution(a, b):
        sum = 0
        for i in range(len(a)):
            for j in range(len(b)):
                if i == j:
                    sum = sum + a[i] * b[j]
        return sum

test = test()
test.solution([1,2,3,4],[-3,-1,0,2])