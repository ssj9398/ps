inputNumber = input()

Len = len(inputNumber)

sumA = 0
sumB = 0
for i in range(Len//2):
    sumA += int(inputNumber[i])

for j in range(Len//2,Len):
    sumB +=int(inputNumber[j])

print(sumA, sumB)

if sumA == sumB:
    print("LUCKY")
else:
    print("READY")

