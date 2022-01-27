class test:
    def solution(self,n):
        li=[]
        test = list(str(n)[::-1])
        for i in test:
            li.append(int(i))
        print(li)

test = test()
test.solution(12345)