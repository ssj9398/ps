class test:
    def solution(self,n):
        ls = list(str(n))
        ls.sort(reverse=True)
        ls = int(''.join(ls))
        return ls


test = test()
test.solution(118372)