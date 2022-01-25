def solution(absolutes, signs):
    sum = 0
    sum2 = 0
    for i in zip(absolutes, signs):
        if i[1] == False:
            sum = sum + i[0] * -1
        else:
            sum2 = sum2 + i[0]
    return sum + sum2