class test:
    def solution(self,n):
        num = set(range(2, n + 1))

        for i in range(2, n + 1):
            if i in num:
                print(num)
                num -= set(range(2 * i, n + 1, i))

        print(len(num))


test = test()
test.solution(100)