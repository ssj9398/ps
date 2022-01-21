
## 보석과 돌
## 문자열 두개를 입력받아 첫번째 문자열에 포함된 문자를 기준으로 두번째 문자열에 얼마나 포함되는지 찾기


inputStringA = input()                                      # 첫번째 문자열 받기
print(inputStringA)
removeCh = ''.join(filter(str.isalnum, inputStringA))       # 특수문자제거
print("removeCh"+ removeCh)
inputStringAList = list(set(removeCh))                      # J를 배열로 만듬

inputStringB = input()                                      # 두번째 문자열 받기
count = 0                                                   # 갯수 초기화


print("listJ = ", inputStringAList, "S = ", inputStringB)
for i in range(len(inputStringAList)):                      # inputStringA의 문자 갯수만큼 반복문을 돌린다.
    for j in range(len(inputStringB)):                      # inputStringB의 문자 갯수만큼 반복문을 돌린다.
        if inputStringAList[i] == inputStringB[j]:          # 첫번째 문자열의 문자와 두번째 문자열의 문자가 같아 질때
            count += 1                                      # 갯수를 하나씩 더해준다.
print(count)