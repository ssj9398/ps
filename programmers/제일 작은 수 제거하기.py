class test:
    def solution(self,arr):
        arr.remove(min(arr))
        if len(arr) == 0:
            return [-1]
        print(arr)
        return arr

test = test()
test.solution([4,3,2,1])