class test:
    def solution(n):
        li = []
        for i in range(n):
            if i % 2 == 0:
                li.append('수')
            else:
                li.append('박')
        li = ''.join(li)
        return li

test = test()
test.solution(3)