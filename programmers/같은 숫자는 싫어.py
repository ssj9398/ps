class test:
    def solution(self,arr):
        answer = []
        for i in range(len(arr)-1):
            print(arr[i])
            if arr[i] == arr[i+1]:
                answer.append(arr[i])
        # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        # print('Hello Python')
        print(answer)
        # return answer

test = test()
test.solution([4,4,4,3,3])