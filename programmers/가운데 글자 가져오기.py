def solution(inputStr):
    a = int(len(inputStr) / 2)  # inputStr
    if len(inputStr) % 2 == 0:
        return inputStr[a - 1:a + 1]
    else:
        return inputStr[a:a + 1]