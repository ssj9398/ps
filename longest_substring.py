string = input()                                         # 문자열을 입력 받는다.
replace = ''.join(filter(str.isalnum,string))            # 특수문자를 제거해준다.
replace_list = list(map(str,replace))                    # 리스트로 만들어준다.

li=[]
length = 0
for v in replace_list:
    if v not in li:                     # li에 중복이 아닌 것을 체크한다.
        li.append(v)                    # li에 추가를 해준다.
        if length< len(li):             # li의 길이가 현재기록 되어있는 length보다 크면
            length = len(li)            # length에 값을 넣어준다.
    elif v in li:
        li=[]
        li.append(v)                    # li에 추가를 해준다.
        if length < len(li):            # li의 길이가 현재기록 되어있는 length보다 크면
            length = len(li)            # length에 값을 넣어준다.

print(length)



'''
    if v not in li:                  # li리스트에 집어넣는데 있으면 끝
        li.append(v)

        print("li",v,li)
        if v in li:
            continue

    else:
        if v not in li2:
            li2.append(v)
            print("li2", v, li2)
            if len(li)<len(li2):

                li=[]

if len(li)<len(li2):
    count = len(li2)
else:
    count = len(li)
print(li,li2)
print(count)
'''