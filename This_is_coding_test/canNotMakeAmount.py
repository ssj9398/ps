import sys

number = sys.stdin.readline()
print(number)

numberList =  list(map(int,input().split()))

print(numberList)

numberList.sort()

minAmount =1

for i in numberList:
    if minAmount < i:
        break
    minAmount+=i

print(minAmount)