from typing import List

class test:
    def solution(self, numbers: List[int]) -> List[int]:

        answer = []
        print(numbers)

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                print("fdasfdsfas",numbers[i]+numbers[j])
                sum = numbers[i] + numbers[j]
                answer.append(sum)
        print(answer)
        print(list(set(answer)))
        return answer


test = test()
test.solution([2,1,3,4,1])