def solution(a:str,b:str):
    sum = 0
    if int(a) > int(b):

        for i in range(b, a+1):

            sum = sum + i
    for i in range(a,b+1):
        sum = sum+i
    return sum