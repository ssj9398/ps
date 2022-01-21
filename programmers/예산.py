class test:
    def solution(d, budget):
        sum=0
        answer=0
        d.sort()
        for i in range(len(d)):
            if d[i]<=budget:
                answer+=1
                budget-=d[i]

        print(answer)

        return answer

test.solution([1,3,2,5,4],9)