class test:
    def solution(self,n):
        answer = ''

        while n > 0:
            n, re = divmod(n, 3)  # n을 3으로 나눈 몫과 나머지
            print("n","re",n, re)
            answer += str(re)
        print(int(answer,3))
        return int(answer, 3)

test = test()
test.solution(45)