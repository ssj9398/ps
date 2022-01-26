def solution(x, n):
    print(x, n)
    li = []
    for i in range(1, n + 1):
        print(x * i)
        li.append(x * i)
    return li