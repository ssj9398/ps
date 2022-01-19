count = int(input())

for i in range(count):
    li = []
    bracket = input()

    for str in bracket:
        if str == "(":                   # 여는괄호 있으면 배열에 추가
            li.append(str)
        elif str == ")":                # 닫는괄호 일때 빈배열이 아니면
            if li:
                li.pop()
            else:
                print("NO")
                break
    else:
        if not li:
            print("YES")
        else:
            print("NO")
