class test:
    def solution(self,numbers):
        answer = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] not in answer:
                    sum = numbers[i] + numbers[j]
                    answer.append(sum)
        answer.sort()
        print(answer)

test = test()
test.solution([5,0,2,7])