import sys

inputStr = sys.stdin.readline()
print(inputStr)

# 0또는 1로 바꾼 횟수
count0 = 0
count1 = 0

if inputStr[0] == '1':
    count0 +=1
else:
    count1+=1

for i in range(len(inputStr)-1):
    if inputStr[i] != inputStr[i+1]:
        if inputStr[i+1] =='1':
            count0+=1
        else:
            count1+=1

res = min(count0,count1)
print(res)