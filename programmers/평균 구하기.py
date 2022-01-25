class test:
    def solution(self,arr):
        sum = 0
        print(arr)
        for i in range(len(arr)):
            print(arr[i])
            sum = sum + arr[i]
        sum = sum/len(arr)
        print(sum)

test = test()
test.solution([1,2,3,4])