class test:
    def solution(self,arr):
        answer = []
        for i in range(len(arr)):
            print(arr[i])
            if not answer:
                answer.append(arr[i])
            elif arr[i]!=answer[len(answer)-1] :
                print("size",len(answer))
                answer.append(arr[i])

        # print('Hello Python')
        print(answer)
        # return answer

test = test()
test.solution([1,1,3,3,0,1,1]	)