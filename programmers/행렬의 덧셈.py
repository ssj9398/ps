class test:
    def solution(self,arr1, arr2):
        answer = []

        for i in range(len(arr1)):
            arr_sum = []
            for j in range(len(arr2[0])):
                arr_sum.append(arr1[i][j]+arr2[i][j])
            answer.append(arr_sum)
        print(answer)
test = test()
test.solution([[1,2],[2,3]],[[3,4],[5,6]])