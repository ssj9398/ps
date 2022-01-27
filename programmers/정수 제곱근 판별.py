class test:
    def solution(self,n):
        sqrt = n ** (1 / 2)
        print(sqrt)
        if sqrt % 1 == 0:
            print(sqrt)
            return (sqrt + 1) ** 2
        return -1
test = test()
test.solution(121)