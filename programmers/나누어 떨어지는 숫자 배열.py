class test:
    def solution(arr, divisor):
        li =[]
        for i in arr:
            if i %divisor ==0:
                li.append(i)
        if not li:
            li.append(-1)
        li.sort()
        return li

test = test()
test.solution([3,2,6], 10)