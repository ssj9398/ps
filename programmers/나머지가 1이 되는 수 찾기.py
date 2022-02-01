class test:
    def solution(self,n):
        print(n)
        for i in range(2,n):
            if n%i==1:
                print(i)
                return i
                break

test = test()
test.solution(10)