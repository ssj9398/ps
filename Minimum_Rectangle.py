
def solution(sizes):
    small = []
    big = []
    for i in sizes:
        if i[0] < i[1]:
            big.append(i[1])
            small.append(i[0])
        else:
            big.append(i[0])
            small.append(i[1])

    return max(small) * max(big)