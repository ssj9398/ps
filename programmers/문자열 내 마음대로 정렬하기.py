class test:
    def solution(self, strings, n):
        li = []
        answer = []
        for i in range(len(strings)):
            strings[i] = strings[i][n] + strings[i]
            li.append(strings[i])
            li.sort()

        for j in range(len(li)):
            answer.append(li[j][1:])
        return answer



test = test()
test.solution(["sun", "bed", "car"],1)