def solution(progresses, speeds):
    answer = []
    count = 0

    # progresses가 값이 있을때
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            print("if:",count)


        if count > 0:
            print(count)
            answer.append(count)
            count = 0

    return answer