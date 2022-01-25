count =  int(input())
max = 0
inputNumber = list(map(int, input().split()))
sum = float(0)
print(inputNumber)
for i in range(count):
    if inputNumber[i]>max:
        max = inputNumber[i]

for i in range(count):
    sum = float(sum) + float(inputNumber[i]/max*100)

res = sum/count
print(res)